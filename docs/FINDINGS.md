# Findings

Date: 2026-09-24. Written only from the Phase 2 rollups and from searches of the unified question text. No figure in here is a probability of being asked.

A firm label means Jev’s confidence was at least 0.6 and the choice was not `unclear`. Review rows stay in [unified_labeled.csv](../data/unified_labeled.csv) and are not in the counts below.

The corpus is 1,988 questions: 45 from a person describing an interview, 433 from a compiled report, 1,507 from a study bank, 3 with the same wording in a compiled report and a study bank.

## 1. Priorities

System design, evals, and serving lead the firm labels, and that order is the study banks. Among the 44 candidate questions with a firm priority, the largest groups are agent reliability (11), system design (8), and project defense (7). Fine-tuning is 137 firm questions and none of them come from a candidate. The data plane is 22 firm questions and none of them come from a candidate.

| Priority | Firm | Candidate | Compiled report | Study bank |
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

**Sources.** Firm rows of [rollup_priority.csv](../data/rollups/rollup_priority.csv). Candidate column is questions that have at least one first-hand instance.

**Limit.** Forty-five candidate questions are not a sample of the industry. A zero there means these posts did not describe that prompt. Study-bank counts are how often a coach wrote the topic.

## 2. Tasks

The task this corpus asks most often is to explain a concept: 922 firm questions, 27 of them candidate. Design is next, 463 firm, 5 of them candidate. Implement is 143 firm and none of those are candidate. The verb “evaluate” is only 26 firm questions, while the priority “evals” is 216, because most eval questions ask what the metrics are, not to judge an output.

| Task | Firm | Candidate |
|---|---|---|
| explain | 922 | 27 |
| design | 463 | 5 |
| implement | 143 | 0 |
| diagnose | 72 | 2 |
| defend | 47 | 3 |
| evaluate | 26 | 0 |

**Sources.** [rollup_task.csv](../data/rollups/rollup_task.csv).

**Limit.** `explain` was added by us so that “what is X” would not be forced into design. One candidate row is “coding question, prompt not stated.” Its task did not clear the bar, which is why implement shows 0 candidate questions even though a coding round was described.

## 3. Portfolio

The sittings do test the portfolio. Seven of the 45 candidate questions ask the person to walk through a project they owned. Three of those seven have a firm task of defend. Kris’s post accounts for three of the seven. Six name no company. One names Sopra Steria, stated by the candidate.

**Sources.** [sitting_portfolio.csv](../data/rollups/sitting_portfolio.csv). Study banks add 21 further firm project-defense questions. Those are a coach list, not the evidence that a room asked.

**Limit.** Seven questions are not seven interviews. Several come from the same post. “Explain a project you owned end to end” is a firm project-defense priority, but its task confidence was 0.52, so it is not counted in the 3 firm defend rows.

## 4. Named concepts and tools

The names that actually appear are RAG (82 questions, 10 of them candidate), fine-tuning (63, none candidate), and attention (57, none candidate). MCP is the only tool that shows up often: 23 questions, 1 of them candidate. HNSW is named in 5 questions, 1 candidate. Prefill and decode are named in 18 questions, all study bank. Idempotency is named once.

**Sources.** [rollup_concepts.csv](../data/rollups/rollup_concepts.csv), [rollup_tools.csv](../data/rollups/rollup_tools.csv). Counts are questions whose text matched a closed list, not firm Jev labels.

**Limit.** If a question says “vector index” and does not say HNSW, it is not in the HNSW count. A mention is not a job requirement.

## 5. Where sittings and banks disagree

The candidate questions spend their weight on agent reliability, project defense, and which ANN index to use. The study banks spend theirs on fine-tuning, serving internals, catalogs of evals, and attention math. Those four are large in the banks and almost absent from the candidate rows. The data plane, ingest and permissions, is 21 study-bank questions and no candidate question.

ANN indexes are the opposite shape: only 12 firm questions in the whole corpus, and 3 of them are candidate.

**Sources.** The candidate and study-bank columns of [rollup_priority.csv](../data/rollups/rollup_priority.csv).

**Limit.** Disagreement with 45 candidate questions can mean the posts were thin, not that the banks invented the topic. Fine-tuning may be asked constantly and simply not what these people chose to write up.

## 6. The mixed-source core

Three questions use the same wording in a compiled report and a study bank. None use the same wording as a candidate post.

Two are firm. “How would you approach designing a system to ensure the safe deployment of AI models in production?” is system design, tagged Anthropic and OpenAI. “Write the loss function for logistic regression and prove that it has a global minimum” is classic ML, tagged Amazon and “Amazon (AWS).” The third, the most pressing unsolved problem in alignment, did not clear the priority bar.

**Sources.** `validity=mixed` in [unified_labeled.csv](../data/unified_labeled.csv). Authors on all three are landedjobs and pallavi-shekhar.

**Limit.** This is same sentence, not same topic. A sitting that asked for RAG metrics in different words was not merged with a bank that asked for RAG metrics in different words. There is no three-source core.

## 7. Absences

A search of the 1,988 question texts finds no `lease`, no `swarm`, and no `backpressure`. Idempotency appears once: a study-bank prompt to design timeouts, retries, circuit breakers, and idempotency around an LLM provider. `429` appears twice, both study bank. Human approval gates appear twice, both study bank. None of these are candidate questions.

**Sources.** Text search of [unified_labeled.csv](../data/unified_labeled.csv). The lease search used a whole word, so “release” did not count.

**Limit.** A question can describe a double write and never say “idempotency.” We would have missed that. What we can say is that the corpus does not teach these as named prompts.

## 8. Company tags

These are tags in study banks and compiled reports. They are not the probability that the company asks the question. OpenAI’s tags do not include a candidate who said they interviewed there.

| Company tag | Tagged questions | Firm | Largest firm priorities |
|---|---|---|---|
| OpenAI | 173 | 135 | Evals 31, fine-tuning 17, serving 13, system design 13, coding 13 |
| Anthropic | 83 | 67 | Agent reliability 19, system design 10, coding 8 |
| Amazon | 79 | 54 | Classic ML 28, serving 7, system design 7 |
| Microsoft | 36 | 32 | Fine-tuning, serving, and classic ML, 4 each |
| Meta | 31 | 28 | System design 12, tokens and attention 5 |
| Google DeepMind | 23 | 19 | System design 5 |

**Sources.** [rollup_company_priority.csv](../data/rollups/rollup_company_priority.csv). The top ten questions for each tag are in [rollup_company_questions.csv](../data/rollups/rollup_company_questions.csv).

**Limit.** In the lab notebook, 1,309 of 1,326 company rows are `bank_tag`. Seventeen companies were stated by a candidate, and the named employers there are Sopra Steria, Deloitte, and NetApp, not this table.

## 9. Level

Of the 45 first-hand instances still in the unified table, 22 were coded senior, 10 mid, and 13 had no level on the post. Both banks leave level unknown or empty on every row: 753 sourced-bank rows and 1,554 topic-map rows.

**Sources.** [sitting_level.csv](../data/rollups/sitting_level.csv). Bank emptiness was checked on `level_guess` in [questions.csv](../data/questions.csv).

**Limit.** Senior and mid on the first-hand rows are our reading of the post, not a level the company printed. This corpus cannot support a junior / mid / senior chart.
