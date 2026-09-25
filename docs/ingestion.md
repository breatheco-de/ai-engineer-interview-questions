# Question register — ingestion

Date: 2026-09-24. One row is one question instance, not one topic.

## Files

| File | What it is |
|---|---|
| [questions.csv](../data/questions.csv) | Every instance: first-hand X sits, Landed, and Pallavi. Filter on `evidence_tier` and `confidence`. Do not read `company` without reading `company_attribution`. |
| [unified_questions.csv](../data/unified_questions.csv) | Phase 1. One row per question. Validity and sources attached. |
| [unified_labeled.csv](../data/unified_labeled.csv) | Phase 2. Jev priority, task, layer, failure. `primary_use=firm` means confidence ≥ 0.6 and not unclear. |
| [FINDINGS.md](FINDINGS.md) | Phase 3. Nine findings. Each has a source line and a limit. |
| [FIGURES.md](FIGURES.md) | Phase 4. One picture per finding that needs one. Panels are per source. |
| [REPORT.md](../REPORT.md) | Phase 5. The published report: methods, findings, and limits. |
| [jev_questions.json](../data/schema/jev_questions.json) | Earlier Choice schema. The live criteria are in [PHASE2.md](PHASE2.md). |

## Phase 1

Unified table: [unified_questions.csv](../data/unified_questions.csv) (1,988 questions). Method and audit: [PHASE1.md](PHASE1.md). This lab file was not rewritten.

## Inclusion rule (2026-09-24)

Trust-first. The research includes the whole register. It does not drop a question because the source is a compilation. Every count in the paper is broken out by source. A question from Shamim's Medium post is cited as Shamim, not as a sitting we attended. Rows are not added together into one "percent of interviews" number.

- First-hand (`1_first_hand`): 35 rows, 9 sittings.
- Landed company tables (`LANDED-{company}`): reported rows, `confidence=medium`, company is a **bank tag**. Source ids were not re-opened.
- Landed question bank `ai-interview-questions` (`LANDED2-*`): main prompts are `reported`. `confidence=medium` only when a company is named and the “where asked” line is not a compendium. Follow-ups on the same card are `representative`, `confidence=low`, `include_in_paper=appendix`. The linked source was not re-opened.
- Pallavi (`PALLAVI-*`): `evidence_tier=2b_topic_map`, `confidence=low`, `company_attribution=bank_tag`, `include_in_paper=no`. Company comes from an "Asked at" line or a company heading. Not a sitting we re-verified.
- ombharatiya (`OMB-*`): `evidence_tier=2b_topic_map`, `confidence=low`, `include_in_paper=no`. Topic files have no company. Company-file questions are `representative`: the author says they are synthesised from public focus areas, not leaked sittings. `company_attribution=bank_tag`.

## Who fills what

Human or the parser, before Jev:

- `question_text`, `source_url`, `source_author`, `source_date`
- `evidence_tier`, `reported_or_representative`, `verification_status`, `confidence`
- `company` when a candidate named the employer (`company_attribution=stated_by_candidate`), or when a bank tagged it (`bank_tag`). Blank if nobody named one.

Jev, later, one request per row, state = `{question_text, source_line}`:

- skill, layer, round, seniority, failure mode
- the Noul checks in `jev_questions.json`

Code, after Jev:

- if any Choice confidence is under 0.6, or the winning option is `unclear`, set `review_status=review`
- Jev must not write `company`, `evidence_tier`, or `source_url`

Current rows have `review_status=human_seed` and empty `jev_*` columns. Skill labels on first-hand rows were set by hand. Landed and Pallavi skills are keyword heuristics (`coded_by=landed_parser` or `pallavi_parser`), not Jev.

## Confidence

- `high` — the author quoted the probe from their own sitting or said they asked it.
- `medium` — a real sitting, but the post listed topics rather than prompts; or Landed’s company table with an opaque candidate-report id; or a second-hand “asked my friend.”
- `low` — a compiled bank (Shamim-via-Landed, Pallavi).

Empty `source_url` is a reject. None of the current rows have one.

## First-hand sittings

| id | date | author | note |
|---|---|---|---|
| SIT-KRIS1 | 2026-07-23 | kris_aieng | Senior AI/ML, exact list |
| SIT-KRIS2 | 2026-07-29 | kris_aieng | HNSW vs IVF, 50–100M |
| SIT-DELOITTE | 2026-03-04 | DeepjyotixDeka | topics, Hyderabad |
| SIT-SOPRA | 2026-09-16 | Pksingh900 | topics, not verbatim |
| SIT-MAYANK | 2026-09-06 | MayankPuvvala | 10ms vs 310ms |
| SIT-BHANU | 2026-09-04 | Bhanupratap241 | focus areas |
| SIT-AKSHAY | 2026-07-24 | ConsciousRide | reconstructed probe |
| SIT-LAMHOT | 2026-09-19 | lamhot_ai | interviewer |
| SIT-KARTHIK | 2026-09-21 | karmakarthik | second-hand |
| SIT-MAYANKV | 2026-08-18 | MayankPuvvala | Voice AI, Bangalore |
| SIT-LAXANA | 2026-09-02 | LaxanaRana | round 1 topics: gradient descent, RAG, embedding model |
| SIT-NETAPP | 2026-08-09 | ajay_2512x | SDE-1 onsite, not an AI Engineer title. RAG + AWS, locks, SAGA |
| SIT-INT-KNOW | 2026-09-17 | javarevisited | interviewer: “How do you know it works?” |
| SIT-INT-RAG | 2026-09-17 | javarevisited | interviewer: design an enterprise RAG assistant |
