#!/usr/bin/env python3
"""Check that the tables in data/ still say what the report says they say.

This is the guard on the whole repository. It re-derives the headline numbers from
the CSVs instead of trusting the prose, so a row added or a label changed shows up
as a failing check rather than as a report that quietly stopped being true.

    python3 scripts/validate_data.py

Exit code 0 when every check passes, 1 otherwise.
"""

import csv
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

PRIORITIES = {
    "system_design", "evals", "serving_cost", "fine_tuning", "agent_reliability",
    "classic_ml", "coding", "tokens_attention", "injection_gates", "project_defense",
    "context_sampling", "grounding", "api_control", "hybrid_search", "data_plane",
    "embeddings", "chunking", "ann_indexes", "unclear",
}
TASKS = {"explain", "design", "implement", "diagnose", "defend", "evaluate", "unclear"}
VALIDITY = {"candidate", "compiled report", "study bank", "mixed"}
USE = {"firm", "review"}
ATTRIBUTION = {"stated_by_candidate", "bank_tag", "none", ""}
TIERS = {"1_first_hand", "2_sourced_bank", "2b_topic_map"}

failures = []
checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        failures.append(message)


def read(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main():
    labeled = read("unified_labeled.csv")
    unified = read("unified_questions.csv")
    notebook = read("questions.csv")

    # --- shape -------------------------------------------------------------
    check(len(notebook) == 2354, f"questions.csv should have 2,354 rows, has {len(notebook)}")
    check(len(unified) == 1988, f"unified_questions.csv should have 1,988 rows, has {len(unified)}")
    check(len(labeled) == 1988, f"unified_labeled.csv should have 1,988 rows, has {len(labeled)}")
    check({r["unified_id"] for r in unified} == {r["unified_id"] for r in labeled},
          "unified_questions.csv and unified_labeled.csv do not cover the same questions")

    ids = [r["unified_id"] for r in labeled]
    check(len(set(ids)) == len(ids), "duplicate unified_id in unified_labeled.csv")
    bad = [i for i in ids if not re.fullmatch(r"UQ-\d{4}", i)]
    check(not bad, f"malformed unified_id: {bad[:5]}")

    inst_ids = {r["instance_id"] for r in notebook}
    check(len(inst_ids) == len(notebook), "duplicate instance_id in questions.csv")

    # --- every question keeps its provenance -------------------------------
    orphans, empty_text = [], []
    for r in labeled:
        for iid in r["instance_ids"].split("|"):
            if iid and iid not in inst_ids:
                orphans.append((r["unified_id"], iid))
        if not r["question_text"].strip():
            empty_text.append(r["unified_id"])
    check(not orphans, f"instance_ids with no row in questions.csv: {orphans[:5]}")
    check(not empty_text, f"questions with empty text: {empty_text[:5]}")

    no_url = [r["instance_id"] for r in notebook if not r["source_url"].strip()]
    check(not no_url, f"instances with no source_url: {no_url[:5]}")

    # --- coded columns stay inside their vocabularies ----------------------
    for col, allowed in (("primary_priority", PRIORITIES), ("task_verb", TASKS),
                         ("validity", VALIDITY), ("primary_use", USE), ("task_use", USE)):
        bad = sorted({r[col] for r in labeled} - allowed)
        check(not bad, f"unexpected {col} values: {bad}")

    bad = sorted({r["company_attribution"] for r in notebook} - ATTRIBUTION)
    check(not bad, f"unexpected company_attribution values: {bad}")
    bad = sorted({r["evidence_tier"] for r in notebook} - TIERS)
    check(not bad, f"unexpected evidence_tier values: {bad}")

    # --- the 0.6 bar is actually the bar -----------------------------------
    choice_column = {"primary": "primary_priority", "task": "task_verb",
                     "layer": "layer", "failure": "failure_mode"}
    for prefix, column in choice_column.items():
        wrong = []
        for r in labeled:
            use, conf, choice = r[f"{prefix}_use"], r[f"{prefix}_confidence"], r[column]
            if not conf:
                continue
            firm_by_rule = float(conf) >= 0.6 and choice != "unclear"
            if firm_by_rule != (use == "firm"):
                wrong.append(r["unified_id"])
        check(not wrong, f"{prefix}_use disagrees with the 0.6 rule on {len(wrong)} rows: {wrong[:5]}")

    # --- a company name never loses its attribution ------------------------
    stated_rows = [r for r in notebook if r["company_attribution"] == "stated_by_candidate"]
    check(len(stated_rows) == 17,
          f"17 company rows should be stated by a candidate, found {len(stated_rows)}")
    tagged_rows = [r for r in notebook if r["company_attribution"] == "bank_tag"]
    check(len(tagged_rows) == 1309,
          f"1,309 company rows should be bank tags, found {len(tagged_rows)}")
    named = sorted({r["company"] for r in stated_rows})
    check(named == ["Deloitte", "NetApp", "Sopra Steria"],
          f"the employers a candidate named should be Deloitte, NetApp, Sopra Steria; found {named}")
    check(not [r for r in notebook if r["company"] and r["company_attribution"] == "none"],
          "a company name is present with no attribution")

    # --- the headline counts in REPORT.md ----------------------------------
    validity = Counter(r["validity"] for r in labeled)
    for name, expected in (("candidate", 45), ("compiled report", 433),
                           ("study bank", 1507), ("mixed", 3)):
        check(validity[name] == expected,
              f"validity={name} should be {expected}, is {validity[name]}")

    firm = [r for r in labeled if r["primary_use"] == "firm"]
    check(len(firm) == 1519, f"1,519 firm priorities expected, found {len(firm)}")
    check(len([r for r in labeled if r["task_use"] == "firm"]) == 1673,
          "1,673 firm tasks expected")

    counts = Counter(r["primary_priority"] for r in firm)
    for priority, expected in (("system_design", 267), ("evals", 216), ("serving_cost", 181),
                               ("fine_tuning", 137), ("agent_reliability", 134),
                               ("project_defense", 44), ("ann_indexes", 12)):
        check(counts[priority] == expected,
              f"firm {priority} should be {expected}, is {counts[priority]}")

    cand = [r for r in labeled if int(r["n_candidate"]) > 0]
    check(len(cand) == 45, f"45 questions should have a first-hand instance, found {len(cand)}")
    cand_firm = Counter(r["primary_priority"] for r in cand if r["primary_use"] == "firm")
    check(sum(cand_firm.values()) == 44, "44 candidate questions should have a firm priority")
    check(cand_firm["fine_tuning"] == 0,
          "fine-tuning should have no candidate question; the report's central contrast depends on it")
    check(cand_firm["data_plane"] == 0, "the data plane should have no candidate question")
    check(cand_firm["agent_reliability"] == 11, "agent reliability should be 11 candidate questions")

    # --- the absences the report claims ------------------------------------
    blob = " ".join(r["question_text"].lower() for r in labeled)
    for word in ("lease", "swarm", "backpressure"):
        hits = len(re.findall(rf"\b{word}\b", blob))
        check(hits == 0, f"the report says '{word}' never appears; it appears {hits} times")
    check(len(re.findall(r"\bidempotenc", blob)) == 1,
          "the report says idempotency appears exactly once")

    # --- rollups agree with the table they summarize -----------------------
    for row in read("rollups/rollup_priority.csv"):
        p = row["priority"]
        check(counts[p] == int(row["n_firm_questions"]),
              f"rollup_priority disagrees on {p}: {row['n_firm_questions']} vs {counts[p]}")
    tasks = Counter(r["task_verb"] for r in labeled if r["task_use"] == "firm")
    for row in read("rollups/rollup_task.csv"):
        t = row["task_verb"]
        check(tasks[t] == int(row["n_firm_questions"]),
              f"rollup_task disagrees on {t}: {row['n_firm_questions']} vs {tasks[t]}")
    for name in os.listdir(os.path.join(DATA, "rollups")):
        rows = read(f"rollups/{name}")
        if name.startswith("rollup_"):
            check(rows and "figure_title" in rows[0],
                  f"{name} lost its figure_title, the column that states what it refuses to claim")

    # --- figures and schema are where the docs point -----------------------
    for fig in ("priority-by-source", "task-by-source", "sitting-vs-bank", "concepts",
                "tools", "company-tags", "required-links"):
        check(os.path.exists(os.path.join(ROOT, "figures", f"{fig}.png")),
              f"figures/{fig}.png is missing but the docs link to it")
    with open(os.path.join(DATA, "schema", "jev_questions.json"), encoding="utf-8") as fh:
        json.load(fh)

    # --- internal markdown links resolve -----------------------------------
    broken = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding="utf-8") as fh:
                body = fh.read()
            for link in re.findall(r"\]\(([^)\s]+)\)", body):
                if link.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                target = os.path.normpath(os.path.join(dirpath, link.split("#")[0]))
                if not target.startswith(ROOT):
                    # ../../issues/new and friends: GitHub resolves these against
                    # the repository root, not the filesystem.
                    continue
                if not os.path.exists(target):
                    broken.append(f"{os.path.relpath(path, ROOT)} → {link}")
    check(not broken, f"broken relative links: {broken[:8]}")

    print(f"{checks - len(failures)}/{checks} checks passed")
    for message in failures:
        print(f"  FAIL  {message}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
