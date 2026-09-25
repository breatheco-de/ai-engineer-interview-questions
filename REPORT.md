# What public 2026 sources test an AI engineer on

24 September 2026.

This is a findings report, not a study plan. It says which decisions the public record of AI-engineer interviews actually contains, and which of those decisions come from a person describing a room rather than from a coach list.

It does not say how likely any company is to ask a question. It does not say what to study this week.

## The claim

The public record does not support one ranking. It supports two.

In the posts where someone describes a sitting, the questions that repeat are: defend a project you shipped, keep an agent loop from falling over, and choose an index. Of the 44 candidate questions we could label firmly, 11 are agent reliability, 8 are system design, and 7 are project defense.

In the study banks, the questions that repeat are system design, catalogs of evals, serving mechanics, and fine-tuning. Fine-tuning is 137 firmly labeled questions, and none of them come from a candidate. The data plane, ingest and permissions, is 22 firmly labeled questions, and none of them come from a candidate.

A curriculum built from the banks will over-teach fine-tuning, attention math, and eval catalogs, and under-teach the thing the sittings actually open with: the project the candidate already built, and whether an agent can be trusted to act.

## Where the questions came from

The lab notebook has 2,354 rows. One row is one time a question was written down, not one interview.

| Source | Rows | What it is |
|---|---|---|
| Posts on X and two interviewer blogs | 47 | A person describing a sitting, or an interviewer saying what they asked. Called **candidate** after unification. |
| Landed jobs bank | 753 | A compiled list. Where Landed marks a question as reported and cites a source we did not open, it is a **compiled report**. Follow-ups Landed wrote are a **study bank**. |
| Pallavi Shekhar's company-wise list | 616 | A study bank. Company names are tags on the page, not sittings we re-checked. |
| ombharatiya's question bank | 938 | A study bank. The author describes the company files as synthesised from public focus areas, not as leaked sittings. |

Thirty-four of the Landed rows are carried in from three Medium posts by Adil Shamim. They are cited as Shamim's compilations. They are not sittings we attended.

We did not drop a question because the source was a compilation. We dropped 27 rows that were not questions: "How to use this file," a leftover citation, and loop labels such as "take-home assignment" and "LeetCode medium/hard." That left 2,327 instances.

## How one question became one row

Wording was normalized and identical sentences were merged, including 40 spelling variants. Different prompts that share a topic were not merged. "What metrics do you use for RAG?" and "Walk through a RAG pipeline" stayed two questions. The earlier grouping had glued those together. It was not used.

The result is 1,988 questions.

| Validity | Questions | Rule |
|---|---|---|
| Candidate | 45 | At least one first-hand instance, and no other source type. |
| Compiled report | 433 | Landed reported it and cited a source we did not open. |
| Study bank | 1,507 | Pallavi, ombharatiya, or a follow-up Landed wrote. |
| Mixed | 3 | The same sentence appears in a compiled report and a study bank. |

No sentence appears in all three. A candidate post and a bank that ask about RAG in different words stayed apart on purpose.

## How a question was labeled

Labels were assigned by Jev (`typesafe/jev-1.13-20260917`), a classifier that returns one option from a list and a confidence. The state it saw was the question text. It did not see the company or the source.

A label is **firm** only when the confidence is at least 0.6 and the choice is not "unclear." Otherwise the row is **review** and is left out of the counts in this report. 1,519 priorities are firm. 469 are review.

Two priorities were added before the call, because the original list had no home for them: fine-tuning, and classic machine learning. One task was added, **explain**, meaning define or compare. Without it, "what is a KV cache?" would have been forced into "design."

The second priority was asked in a separate call, after the first priority was known. Questions in one call cannot see each other's answers, so an earlier attempt was discarded. 264 questions have a second priority at confidence at least 0.6. 568 are firmly "none." The links cycle, so this report does not draw a skill tree.

## Why a company chart is a tag chart

1,326 lab rows name a company. 1,309 of those names are tags copied from a bank. 17 were stated by the person who sat the interview: Deloitte (5), Sopra Steria (8), NetApp (4).

OpenAI's 173 tagged questions include no candidate who said they interviewed there. The figures in [figures/company-tags.png](figures/company-tags.png) are titled "Tags in study banks and compiled reports" for that reason.

## Findings

Counts below are firm labels unless a sentence says otherwise. A question that sits in more than one source is counted in each source it belongs to. The columns are not a probability of being asked.

### 1. The two rankings

| Priority | Firm questions | Candidate | Compiled report | Study bank |
|---|---|---|---|---|
| System design | 267 | 8 | 68 | 192 |
| Evals | 216 | 2 | 40 | 174 |
| Serving and cost | 181 | 1 | 22 | 158 |
| Fine-tuning | 137 | 0 | 18 | 119 |
| Agent reliability | 134 | 11 | 24 | 99 |
| Classic ML | 113 | 1 | 28 | 85 |
| Coding | 100 | 1 | 52 | 47 |
| Tokens and attention | 94 | 1 | 14 | 79 |
| Injection and gates | 47 | 1 | 9 | 37 |
| Project defense | 44 | 7 | 16 | 21 |
| Context and sampling | 32 | 2 | 3 | 27 |
| Grounding | 32 | 1 | 6 | 25 |
| API and limits | 28 | 1 | 10 | 17 |
| Hybrid search | 25 | 1 | 6 | 18 |
| Data plane | 22 | 0 | 1 | 21 |
| Embeddings | 21 | 1 | 4 | 16 |
| Chunking | 14 | 2 | 1 | 11 |
| ANN indexes | 12 | 3 | 1 | 8 |

The picture is [figures/priority-by-source.png](figures/priority-by-source.png). Each panel is one source. Removing the study-bank panel does not change the other two.

**Limit.** Forty-five candidate questions are not the industry. A zero means these posts did not describe that prompt.

### 2. What the candidate is asked to do

| Task | Firm | Of which candidate |
|---|---|---|
| Explain a concept | 922 | 27 |
| Design | 463 | 5 |
| Implement | 143 | 0 |
| Diagnose | 72 | 2 |
| Defend work they did | 47 | 3 |
| Evaluate | 26 | 0 |

The corpus mostly asks for a definition or a comparison, then for a design. The verb "evaluate" is rare even though the topic "evals" is common, because those questions ask which metrics exist, not to judge an output. Implement is a bank and compiled-report task. The one candidate mention of a coding round did not quote the problem, so it did not clear the bar.

The picture is [figures/task-by-source.png](figures/task-by-source.png).

### 3. The portfolio is tested

Seven of the 45 candidate questions ask the person to walk through a project they owned. Three of those seven have a firm task of defend. Three of the seven come from one post. Six name no company. One names Sopra Steria, and the candidate is the one who named it.

Study banks add 21 more firm project-defense questions. Those are a list a coach published, not evidence that a room asked.

**Limit.** Seven questions are not seven interviews.

### 4. The words that actually appear

RAG is named in 82 questions, 10 of them candidate. Fine-tuning is named in 63, none candidate. Attention is named in 57, none candidate. MCP is the only tool named often: 23 questions, 1 candidate. HNSW is named in 5, 1 of them candidate. Prefill and decode are named in 18, all study bank.

Pictures: [figures/concepts.png](figures/concepts.png), [figures/tools.png](figures/tools.png).

**Limit.** The lists are closed. A question that says "vector index" and never says HNSW is not in the HNSW count. A mention is not a job requirement.

### 5. Where the room and the banks disagree

Candidate questions spend their weight on agent reliability, the project the person shipped, and which index to use. Study banks spend theirs on fine-tuning, serving internals, eval catalogs, and attention math. ANN indexes are the reverse shape of fine-tuning: 12 firm questions in the whole corpus, 3 of them from a candidate.

The picture is [figures/sitting-vs-bank.png](figures/sitting-vs-bank.png). The dots are shares of each source's own firm questions, not shares of interviews.

**Limit.** The banks may be describing prompts these particular posters did not bother to write down. Absence from 45 questions is not proof a company never asks.

### 6. Almost nothing is confirmed twice

Three questions use the same sentence in a compiled report and a study bank. None use the same sentence as a candidate post.

The two that labeled firmly are a generic "design safe deployment of models," tagged Anthropic and OpenAI, and the logistic-regression loss, tagged Amazon. The third, an alignment opinion question, did not clear the bar.

**Limit.** This is same wording, not same topic. There is no question we can point to and say a sitting, a compiled report, and a study bank all asked it.

### 7. What the corpus does not ask

The 1,988 question texts do not contain the words lease, swarm, or backpressure. Idempotency appears once, in a study-bank prompt about timeouts and retries around a model provider. The number 429 appears twice, both study bank. Human approval gates appear twice, both study bank. None of these are candidate questions.

**Limit.** A question can describe a double write without using the word idempotency. We would have missed it. What holds is that these are not named prompts in this corpus.

### 8. What the banks attach to a company name

| Tag | Tagged questions | Firm | What the firm tags pile onto |
|---|---|---|---|
| OpenAI | 173 | 135 | Evals 31, fine-tuning 17, then serving, system design, and coding at 13 each |
| Anthropic | 83 | 67 | Agent reliability 19, system design 10, coding 8 |
| Amazon | 79 | 54 | Classic ML 28 |
| Microsoft | 36 | 32 | Fine-tuning, serving, and classic ML, 4 each |
| Meta | 31 | 28 | System design 12 |
| Google DeepMind | 23 | 19 | System design 5 |

The picture is [figures/company-tags.png](figures/company-tags.png). The top ten tagged questions for every company are in [rollup_company_questions.csv](data/rollups/rollup_company_questions.csv).

**Limit.** These are tags. The employers a candidate actually named are Deloitte, Sopra Steria, and NetApp.

### 9. Level

Of the 45 first-hand instances still in the unified table, 22 were coded senior from the post, 10 mid, and 13 named no level. Both banks leave level blank or unknown on every row.

**Limit.** Senior and mid are our reading of the post, not a level printed by the employer. This corpus cannot say how many junior, mid, and senior interviews exist.

## What this report will not say

- The percent of interviews that ask any question.
- That OpenAI asks what a README tags as OpenAI.
- That the banks and the sittings can be added into one total.
- That there is a skill tree. The measured links cycle: serving and tokens point at each other, and so do serving and system design. See [figures/required-links.png](figures/required-links.png).

## How to check a sentence

The working notes are [PHASE1.md](docs/PHASE1.md), [PHASE2.md](docs/PHASE2.md), [FINDINGS.md](docs/FINDINGS.md), and [FIGURES.md](docs/FIGURES.md). The row behind a claim is [unified_labeled.csv](data/unified_labeled.csv). The untouched lab notebook is [questions.csv](data/questions.csv). A reader does not need to open the 2,354-row file to see where a number in this report came from. The file is there for an audit.

---

*The AI Engineer Interview Register* — 4Geeks Academy, 2026. Licensed [CC BY 4.0](LICENSE): reuse it freely, credit 4Geeks Academy and link back to [the repository](https://github.com/breatheco-de/ai-engineer-interview-questions).
