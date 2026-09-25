# Findings study — plan (not a prep package)

Date: 2026-09-24. Freeze: no more scraping until this plan is finished.

## Claim we are trying to earn

Public 2026 sources, once unified and labeled, show which **priorities** an AI Engineer is tested on: what they must be able to decide, not a list of tools.

Credibility comes from: source honesty, one question counted once, and findings written as priorities with evidence under them. It does not come from row count.

Out of scope until findings exist: student kit, 60-minute mock comparison, answer formulas, “how to study this week.”

## Audience of the published piece

A hiring manager, a curriculum lead, or a senior engineer who wants to know what this role is being selected for. A candidate may read it. It is not written as a coach.

## Published artifact (Phase 5)

A findings report covering: source mix, priorities, task verbs, project defense, named concepts and tools, sitting-vs-bank contrast, mixed-source core, absences, and company **tags** (never probabilities). The lab notebook (`questions.csv`) stays in the repo and is cited, not handed out as the product.

Limits that stay true in every phase: 1,309 of 1,326 company rows are `bank_tag`; 17 are stated by a candidate; first-hand named employers here are Sopra Steria, Deloitte, NetApp; `level_guess` exists on 32 rows (22 senior, 10 mid). No P(asked at company). No junior/mid/senior chart of the whole corpus. No raw word cloud.

## Phases

### Phase 1 — Unify the questions

One row per question. Sources listed under it. Validity label: candidate | compiled report | study bank | mixed.

Also in this phase, because later cuts need it on the same row:

- Keep every company name, with `company_attribution` (`stated_by_candidate` vs `bank_tag`). Do not drop tags. Do not promote them.
- Extract **named concepts** and **named tools** from the question text into closed lists (BM25, HNSW, MRR, prefill/decode, LangGraph, MCP, …). Empty when the text does not name one.
- Drop junk headings (“How to use this file”) and split false merges.

Stop when: a unified table exists, ten random rows survive an audit, and concept/tool cells are either a closed-list value or blank.

**Status (2026-09-24): done.** Table: [unified_questions.csv](../data/unified_questions.csv). Notes and the ten-row audit: [PHASE1.md](PHASE1.md). Lab notebook `questions.csv` was not rewritten.

### Phase 2 — Name priorities, tasks, and the other cuts

On that unified table only:

- One **primary priority** from the sixteen-skill hypothesis (edit the list if a node is empty). Up to two required priorities.
- One **task verb**: design | diagnose | implement | evaluate | defend.
- **Layer** and **failure mode** when the question implies them.
- Flag **mixed-source** (sitting + compiled + bank).
- Build four rollups, each **split by source type**:
  1. Priority coverage
  2. Task-verb coverage
  3. Named concepts / named tools
  4. Company-tag lists: top questions and top priorities **tagged** to each company
- Sitting-only slice for **project defense / portfolio** and for **level** (22 senior, 10 mid, banks silent).

Stop when: every unified question has a priority and a task verb, the four rollups exist, and the company rollup is titled as tags, not as interviews.

**Status (2026-09-24): done.** Labeled table: [unified_labeled.csv](../data/unified_labeled.csv). Notes: [PHASE2.md](PHASE2.md). Firm labels only enter the rollups. `fine_tuning`, `classic_ml`, and the task `explain` were added before the call.

### Phase 3 — Write findings

From those rollups only. Each finding is one sentence a reader can disagree with, then the sources, then the limit. The report must hit all of these, in this order:

1. Most wanted **priorities** (stacked by source type)
2. Most wanted **tasks**
3. Whether the **portfolio** is tested (sittings first)
4. **Named concepts** and **named tools** in this corpus
5. What **candidate sittings** emphasize that **study banks** inflate or skip
6. The **mixed-source core**
7. **Absences** (leases as a named prompt, swarm-as-default, …)
8. **Company tags**: “what coaches attach to OpenAI / Anthropic / …,” with the bank-tag sentence on every such finding
9. **Level**: only the 32 coded rows, plus “the banks almost never mark junior / mid / senior”

No combined “percent of interviews.” No P(asked at X).

Stop when those nine findings exist and each has a validity line.

**Status (2026-09-24): done.** [FINDINGS.md](FINDINGS.md). Counts are firm labels only, split by source type. No combined probability.

### Phase 4 — Pictures that serve those findings

Only after Phase 3. One picture per finding that needs one:

- Priority tree
- Priority coverage stacked by source type
- Task-verb bars stacked by source type
- Named-concept and named-tool bars
- Sitting-vs-bank contrast
- Optional company-tag small multiples, title: “Tags in study banks,” never “What X asks”

Stop when: hiding study-bank rows does not make a picture lie, and every company figure still reads as a tag list.

**Status (2026-09-24): done.** [FIGURES.md](FIGURES.md). Seven figures in [figures/](../figures/). No skill tree: the measured links cycle. Company figure is titled as tags.

### Phase 5 — Methods note + publish

How the register was built, the trust-first rule, Shamim cited as Shamim, why company figures are tags. Then the findings report.

Stop when: a reader can see where a claim came from without opening the 2,354-row file.

**Status (2026-09-24): done.** Published report: [REPORT.md](../REPORT.md). Methods, the nine findings, and the refusal to draw a skill tree or a company probability are in that file.
