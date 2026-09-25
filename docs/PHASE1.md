# Phase 1 — unified questions

Date: 2026-09-24. Lab notebook unchanged: [questions.csv](../data/questions.csv) (2,354 rows).

## Result

[unified_questions.csv](../data/unified_questions.csv): **1,988 questions**, from **2,327** source rows.

| Validity | Questions | Meaning |
|---|---|---|
| candidate | 45 | A person described the interview, or an interviewer said they asked it. |
| compiled report | 433 | Landed marks it reported and cites a source we did not open. Includes Shamim via Landed. |
| study bank | 1,507 | Pallavi, ombharatiya, or a follow-up Landed wrote. |
| mixed | 3 | Compiled report and study bank use the same wording. No candidate row shares exact wording with a bank. |

958 questions carry at least one **bank tag**. 17 carry a company **stated by a candidate**. Tags were not promoted.

526 questions name at least one concept from the closed list. 76 name at least one tool. The rest are blank on purpose.

## How a row was built

1. Dropped non-questions: “How to use this file” (7), a citation shell, “HR call (selective)”, and 18 loop labels (take-home, “LeetCode medium/hard”, “candidate tip”, “SQL questions (not further specified)”, and similar). Those rows remain in the lab notebook.
2. Grouped by normalized wording. The old `canonical_id` was not used. It had glued different prompts (RAG metrics with “walk through a pipeline”, single-head attention with multi-head).
3. Merged 40 pairs at string similarity ≥ 0.90 inside the same token block. Checked by hand: they are spelling and contraction variants, not different prompts.
4. Validity is **mixed** only when more than one source type is present. Two study banks on the same wording stay `study bank`.
5. Company names stay split: `companies_stated` vs `companies_bank_tag`.
6. Concepts and tools are closed lists. A cell is a list of those names, or blank. `decode(` as in a tokenizer’s `decode(ids)` is not counted as prefill/decode.

Different prompts that share a topic were **not** merged. “What metrics do you use for RAG?” and “Walk through a RAG pipeline” are two rows. That is why almost no candidate question is `mixed`: the sittings and the banks do not use the same sentence.

## Audit (seed 24, stratified)

| id | Verdict | Why |
|---|---|---|
| UQ-1937 | Pass | One Pallavi row. Study bank. Company tag Cognition, not a sitting. |
| UQ-1003 | Pass | Landed follow-up. Concepts FlashAttention and attention match the words. No tool named. |
| UQ-1613 | Pass | ombharatiya. BLEU/ROUGE are not on the concept list, so the concept cell is blank. |
| UQ-0411 | Pass, thin | “Cell towers are down; what changes?” is a follow-up whose parent is another row. Still a question. Study bank. |
| UQ-0608 | Pass | Landed reported row. Compiled report. No company on that card. |
| UQ-0549 | Pass | Landed system-design card. Compiled report. No company in the cell. |
| UQ-0573 | Pass, dirty source | One Landed cell contains two wordings stuck together. We did not split a single instance. Compiled report. OpenAI is a bank tag. |
| UQ-0673 | Pass | Laxana’s sitting. Candidate. No company named. |
| UQ-1766 | Pass | Same Akshay post, term he said they asked, prompt not quoted. Candidate. |
| UQ-0258 | Pass | Same logistic-regression prompt in Pallavi and Landed. Mixed. Bank tags “Amazon” and “Amazon (AWS)” were not collapsed. |

No concept or tool value sits outside the closed lists.
