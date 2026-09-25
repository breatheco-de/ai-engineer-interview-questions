# How the register was built

These are the working notes, in the order they were written. Each phase was frozen before the next
one began, and each one records the audits — including the ones that came back weak.

Read them if you want to know whether to trust [the report](../REPORT.md). They are not a study
guide and they were never written as one.

| | Note | What it settles |
|---|---|---|
| **Plan** | [RESEARCH-PLAN.md](RESEARCH-PLAN.md) | What claim the study was trying to earn, what was out of scope, and the stop condition for each phase. Written before the results existed. |
| **0** | [ingestion.md](ingestion.md) | What one row means, the trust-first inclusion rule, how each source was graded, and the fourteen first-hand sittings by id. |
| **1** | [PHASE1.md](PHASE1.md) | 2,354 instances → 1,988 questions. What was dropped, what was merged, what was deliberately *not* merged, and a ten-row hand audit. |
| **2** | [PHASE2.md](PHASE2.md) | The labels: eighteen priorities, six task verbs, layer and failure mode. Why the first attempt at a second priority was discarded. The 0.6 bar. An audit against the candidate rows, including one verdict of "weak". |
| **3** | [FINDINGS.md](FINDINGS.md) | Nine findings. Each is one sentence you can disagree with, then its sources, then its limit. |
| **4** | [FIGURES.md](FIGURES.md) | Seven figures, each with what it claims and what it refuses. Why there is no skill tree. |
| **5** | [REPORT.md](../REPORT.md) | The published report. |

## The three decisions that shaped everything

**Trust-first, not trust-only.** A question was not dropped for coming from a compilation. It was
labeled as one, and every count in the report is broken out by source. This is why the register can
show the disagreement between rooms and banks instead of averaging it away.

**The classifier was blinded.** It saw the question text and nothing else — not the company, not
the source, not the other questions in the batch. It could not label a question "agent reliability"
because Anthropic's name sat next to it on the page.

**A label counts only above 0.6.** 1,519 priorities clear the bar and 469 do not. The 469 are still
in [`data/unified_labeled.csv`](../data/unified_labeled.csv) with their confidences, so you can move
the bar and recount. Each catalog page lists its own review rows in a collapsed block.

## Where the numbers live

Every count quoted in these notes can be re-derived from
[`data/unified_labeled.csv`](../data/unified_labeled.csv) and the
[rollups](../data/rollups/). [`scripts/validate_data.py`](../scripts/validate_data.py) does exactly
that on every push: if a table stops matching the prose, the check goes red.
