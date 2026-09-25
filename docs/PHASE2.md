# Phase 2 — priorities and tasks

Date: 2026-09-24. Input: [unified_questions.csv](../data/unified_questions.csv) (1,988 questions). That file was not rewritten.

## Result

[unified_labeled.csv](../data/unified_labeled.csv). Every question has a Jev priority and a Jev task. A label is **firm** only when the choice is not `unclear` and confidence is at least 0.6. Otherwise `primary_use` or `task_use` is `review`, and that row is left out of the rollup counts.

| | Firm | Review |
|---|---|---|
| Priority | 1,519 | 469 |
| Task | 1,673 | 315 |

Model: `typesafe/jev-1.13-20260917`, through OpenRouter Decisions. State was the question text only. Jev did not see the company or the source.

## The list, edited before the call

The sixteen-skill hypothesis had no home for fine-tuning or for classic ML, and the five task verbs had no home for “what is X.” Those were added. No node came back empty.

Priorities: project defense, coding, tokens and attention, context and sampling, embeddings, chunking, hybrid search, ANN indexes, grounding, evals, data plane, API and limits, serving and cost, agent reliability, injection and gates, fine-tuning, classic ML, system design.

Tasks: design, diagnose, implement, evaluate, defend, explain.

`explain` means define, compare, or derive. It is not design.

## Required priority

A first pass asked for the required priority in the same call as the primary. Those answers were discarded. The questions in one call cannot see each other, so Jev could not avoid repeating the primary, and the confidence was mostly under 0.6.

A second call, only on the 1,519 firm priorities, was given the primary and forbidden to pick it. 264 questions have a second priority at confidence ≥ 0.6. 568 are firm `none` (the question stands on the primary). The rest stay blank.

## Other columns

- `layer` and `failure_mode` are on every row, with the same 0.6 rule. Failure is `none` on most rows. That means the question does not probe a named failure, not that the failure cannot happen.
- `mixed_source` is `two_types` on 3 questions (compiled report and study bank, same wording). It is `all_three` on none. No candidate sentence matched a bank sentence.

## Rollups

Each count below is firm labels only. A mixed question is counted once in each source type it has. The three source columns can add up to more than the firm total. They are not probabilities.

| Priority | Firm | Candidate | Compiled report | Study bank |
|---|---|---|---|---|
| system design | 267 | 8 | 68 | 192 |
| evals | 216 | 2 | 40 | 174 |
| serving and cost | 181 | 1 | 22 | 158 |
| fine-tuning | 137 | 0 | 18 | 119 |
| agent reliability | 134 | 11 | 24 | 99 |
| classic ML | 113 | 1 | 28 | 85 |
| coding | 100 | 1 | 52 | 47 |
| tokens and attention | 94 | 1 | 14 | 79 |
| injection and gates | 47 | 1 | 9 | 37 |
| project defense | 44 | 7 | 16 | 21 |
| context and sampling | 32 | 2 | 3 | 27 |
| grounding | 32 | 1 | 6 | 25 |
| API and limits | 28 | 1 | 10 | 17 |
| hybrid search | 25 | 1 | 6 | 18 |
| data plane | 22 | 0 | 1 | 21 |
| embeddings | 21 | 1 | 4 | 16 |
| chunking | 14 | 2 | 1 | 11 |
| ANN indexes | 12 | 3 | 1 | 8 |

| Task | Firm | Of which candidate |
|---|---|---|
| explain | 922 | 27 |
| design | 463 | 5 |
| implement | 143 | 0 |
| diagnose | 72 | 2 |
| defend | 47 | 3 |
| evaluate | 26 | 0 |

Files:

- [rollup_priority.csv](../data/rollups/rollup_priority.csv)
- [rollup_task.csv](../data/rollups/rollup_task.csv)
- [rollup_concepts.csv](../data/rollups/rollup_concepts.csv) and [rollup_tools.csv](../data/rollups/rollup_tools.csv), from the Phase 1 closed lists, split by source type
- [rollup_company_questions.csv](../data/rollups/rollup_company_questions.csv), top 10 questions per company tag
- [rollup_company_priority.csv](../data/rollups/rollup_company_priority.csv)

The company files are titled as tags. They are not the probability a company asks the question.

## Sittings only

[sitting_portfolio.csv](../data/rollups/sitting_portfolio.csv): 7 candidate questions whose priority is project defense or whose task is defend.

[sitting_level.csv](../data/rollups/sitting_level.csv): 45 first-hand instances still in the unified table. 22 senior, 10 mid, 13 with no level on the source. The banks are not in this file.

## Audit

Checked against the candidate rows, which we can read:

| Question | Jev | Verdict |
|---|---|---|
| Draw HNSW vs IVF | ANN indexes, explain, confidence 1.0 and 0.96 | Pass |
| What's the last GenAI project you have worked on? | project defense, defend | Pass |
| How do you prevent prompt injection? | injection and gates | Pass |
| Temperature 0 should be deterministic, but two runs differ | context and sampling | Pass |
| What evaluation metrics do you use for RAG? | evals | Pass |
| Explain a project you owned end to end | priority project defense (firm); task explain at 0.52 | Priority pass. Task stays in review, so it is not counted as defend |
| Answer one or two scenario questions (prompts not stated) | unclear at 0.92 | Pass. There is no prompt to classify |
| Explain SAGA and two-phase commit | system design | Weak. It is a distributed-systems concept, not a system design. Left as Jev returned it |
