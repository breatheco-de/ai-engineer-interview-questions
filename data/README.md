# The data

Five tables, three layers. Every number in [the report](../REPORT.md) comes from one of them, and
every one of them can be opened in the browser — GitHub renders a CSV as a sortable, searchable
table, so you do not need to download anything to check a claim.

```
questions.csv            2,354 rows   one row = one time a question was written down
      │
      │  Phase 1: drop non-questions, merge identical wordings
      ▼
unified_questions.csv    1,988 rows   one row = one question, with its sources attached
      │
      │  Phase 2: classify priority, task, layer, failure mode
      ▼
unified_labeled.csv      1,988 rows   the same rows, plus labels and confidences
      │
      │  count firm labels, split by source type
      ▼
rollups/*.csv                         the eight tables the figures are drawn from
```

| File | Rows | What it is |
|---|---|---|
| [`questions.csv`](questions.csv) | 2,354 | The lab notebook. Untouched since ingestion. One row is one instance, not one interview. |
| [`unified_questions.csv`](unified_questions.csv) | 1,988 | One row per question. Sources, companies, named terms. No labels yet. |
| [`unified_labeled.csv`](unified_labeled.csv) | 1,988 | The same rows with the classifier's priority, task, layer and failure mode, each with a confidence. **Start here.** |
| [`canonical_questions.csv`](canonical_questions.csv) | 2,044 | Superseded. An earlier grouping that glued different prompts together. Kept for the audit trail; not used by any finding. |
| [`rollups/`](rollups/) | 8 files | The aggregates behind the figures. Each carries its own `figure_title` warning you what it does not mean. |
| [`schema/jev_questions.json`](schema/jev_questions.json) | — | The earlier classifier schema. The live criteria are in [PHASE2.md](../docs/PHASE2.md). |

## Read this before you read a column

**One row is not one interview.** `questions.csv` counts the times a question was written down,
and one blog post can write down twelve. Nothing in this repository supports "X% of interviews ask
this."

**A company name is usually a tag.** 1,309 of the 1,326 company rows are a name a bank author
attached to a question. Seventeen were stated by the person who sat the interview. Never read
`company` without reading `company_attribution`, and never read `companies_bank_tag` as evidence
that the company asked anything.

**A label is only firm above 0.6.** `primary_use`, `task_use`, `layer_use` and `failure_use` are
`firm` or `review`. Every count in the report uses `firm` rows only. The `review` rows are still in
the file, on purpose — you can disagree with the bar and recount.

## `unified_labeled.csv`

The table most questions should be asked of.

| Column | Values | Meaning |
|---|---|---|
| `unified_id` | `UQ-0001`… | Stable id for one question. Cited throughout the catalog and the docs. |
| `question_text` | free text | The normalized wording. |
| `validity` | `candidate`, `compiled report`, `study bank`, `mixed` | How well-attested the question is. `candidate` means at least one first-hand instance and no other source type. |
| `source_types` | pipe-separated | Every source type this question appears in. |
| `n_instances` | integer | How many rows of `questions.csv` collapsed into this one. |
| `n_candidate`, `n_compiled_report`, `n_study_bank` | integer | Instances of each type. Filtering `n_candidate > 0` gives the 45 questions someone reported from a room. |
| `instance_ids` | pipe-separated | The `instance_id` values in `questions.csv` this row was built from. This is the join key back to the notebook. |
| `source_authors` | pipe-separated | Who wrote it down. |
| `companies_stated` | pipe-separated | Employers named by the candidate who sat the interview. Usually empty. |
| `companies_bank_tag` | pipe-separated | Company names a bank attached. Not evidence. |
| `company_pairs` | `Name:attribution` | The two columns above, zipped, so the attribution travels with the name. |
| `named_concepts`, `named_tools` | pipe-separated, closed list | Terms the question text actually says. Blank when it names none. |
| `merge_kind`, `n_wordings` | `exact`/`near`, integer | How the instances were merged, and how many distinct wordings collapsed. |
| `primary_priority` | one of 18, or `unclear` | What the question is testing. |
| `primary_confidence` | 0–1 | The classifier's confidence. |
| `primary_use` | `firm`, `review` | `firm` when confidence ≥ 0.6 and the choice is not `unclear`. |
| `task_verb` | `explain`, `design`, `implement`, `diagnose`, `defend`, `evaluate` | What the candidate has to do. `explain` means define or compare. |
| `task_confidence`, `task_use` | | Same rule. |
| `required_priority`, `required_confidence`, `required_use` | | A second priority the question also leans on, asked in a separate call and forbidden from repeating the primary. 264 firm, 568 firmly `none`. The links cycle, so this is not a skill tree. |
| `layer`, `layer_confidence`, `layer_use` | `model`, `retrieval`, `serving`, `agent_runtime`, `data_plane`, `control_plane`, `security`, `evals`, `product`, `none` | Where in a system the question lives. |
| `failure_mode`, `failure_confidence`, `failure_use` | `hallucination`, `latency_or_cost`, `prompt_injection`, `stale_index`, `cross_tenant`, `rate_limit`, `double_write`, `bad_chunking`, `no_eval`, `none` | The named failure the question probes. `none` on most rows: the question does not name a failure, which is not the same as the failure being impossible. |
| `mixed_source` | `no`, `two_types` | `two_types` on the 3 questions whose exact wording appears in both a compiled report and a study bank. No question is `all_three`. |
| `jev_model` | string | The classifier build that produced the labels. |

`unified_questions.csv` is the same table without the label columns.

## `questions.csv`

The notebook. Useful when you want the source URL, the round, or the raw per-instance coding.

| Column group | Columns | Notes |
|---|---|---|
| Identity | `instance_id`, `canonical_id`, `question_text`, `question_variant_notes` | `canonical_id` is the superseded grouping. Join on `instance_id`. |
| Provenance | `evidence_tier`, `reported_or_representative`, `source_kind`, `source_url`, `source_author`, `source_date`, `verification_status`, `confidence` | `evidence_tier` is `1_first_hand` (47 rows), `2_sourced_bank` (753), or `2b_topic_map` (1,554). An empty `source_url` is a reject; no current row has one. |
| Employer | `company`, `company_attribution`, `role_title`, `level_guess`, `round`, `geo_or_site` | `company_attribution` is `stated_by_candidate` or `bank_tag`. `level_guess` is filled on 32 rows and blank on every bank row. |
| Hand coding | `skill_primary`, `skill_secondary`, `technology`, `system_layer`, `failure_mode`, `seniority_signal` | Set by hand on first-hand rows; keyword heuristics (`coded_by=landed_parser`, `pallavi_parser`) elsewhere. Superseded by the classifier columns in `unified_labeled.csv`. |
| Bookkeeping | `in_mock`, `in_student_kit`, `include_in_paper`, `coded_by`, `coded_at`, `notes`, `jev_*`, `review_status` | The `jev_*` columns here are empty. Labeling happened on the unified table, not on instances. |

## `rollups/`

Each file's first column is a `figure_title` that states what the table refuses to claim. Keep it
when you quote the table.

| File | What it counts |
|---|---|
| [`rollup_priority.csv`](rollups/rollup_priority.csv) | Firm priorities, split by source type, plus the review rows left out. |
| [`rollup_task.csv`](rollups/rollup_task.csv) | Firm task verbs, split by source type. |
| [`rollup_concepts.csv`](rollups/rollup_concepts.csv) | Closed-list concept names found in the question text. |
| [`rollup_tools.csv`](rollups/rollup_tools.csv) | Closed-list tool names found in the question text. |
| [`rollup_company_priority.csv`](rollups/rollup_company_priority.csv) | Priorities inside each company's tag pile. 47 tags. |
| [`rollup_company_questions.csv`](rollups/rollup_company_questions.csv) | The top ten tagged questions per company. |
| [`sitting_portfolio.csv`](rollups/sitting_portfolio.csv) | The 7 candidate questions that ask about a project the person owned. |
| [`sitting_level.csv`](rollups/sitting_level.csv) | 22 senior, 10 mid, 13 unstated, from first-hand instances only. |

## Loading it

No install needed to browse: click any CSV above and GitHub renders it.

```python
import pandas as pd

q = pd.read_csv("data/unified_labeled.csv")

# The 45 questions someone actually reported from a room
sittings = q[q.n_candidate > 0]

# Firm priorities, the way the report counts them
firm = q[q.primary_use == "firm"]
firm.primary_priority.value_counts()

# A question's provenance, back to the source URL
notebook = pd.read_csv("data/questions.csv")
ids = q.loc[q.unified_id == "UQ-0660", "instance_ids"].iat[0].split("|")
notebook[notebook.instance_id.isin(ids)][["source_author", "source_url", "evidence_tier"]]
```

```sql
-- duckdb, straight off the working copy
SELECT primary_priority, count(*) AS firm
FROM 'data/unified_labeled.csv'
WHERE primary_use = 'firm'
GROUP BY 1 ORDER BY 2 DESC;
```

Pipe-separated cells (`instance_ids`, `companies_bank_tag`, `named_concepts`) split on `|`. They are
never quoted lists, and a blank cell means none, not unknown.

## Integrity

[`scripts/validate_data.py`](../scripts/validate_data.py) checks the row counts, the id formats, the
allowed values of every coded column, and that the numbers quoted in the report still match the
tables. It runs on every push and pull request
([workflow](../.github/workflows/validate-data.yml)). If you change a CSV, run it locally first:

```bash
python3 scripts/validate_data.py
python3 scripts/build_catalog.py   # regenerate catalog/ from the new data
```
