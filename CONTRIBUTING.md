# Contributing

This register is only as good as the evidence under it, and the thinnest part is the part that
matters most: **45 questions come from someone describing a room they actually sat in.** Everything
else is a compiled report or a coach's study bank.

So the contribution that helps most is not a longer list. It is a better-attested one.

## What to send

### 1. A sitting you actually did — the most valuable thing here

You interviewed somewhere and you wrote down what you were asked. That is a first-hand instance,
and it is the only evidence tier that describes an interview rather than a topic someone thinks you
should study.

Open a [new sitting issue](../../issues/new?template=new-sitting.yml) with:

- **The questions, as close to verbatim as you can manage.** "They asked about RAG" is a topic.
  "Walk through the RAG pipeline you built and which embedding model you used" is a question. Both
  are usable; the second is worth far more.
- **A public link**, if the post is public — a thread on X, a blog post, a LinkedIn write-up. A row
  with no `source_url` is a reject, which is why the register has none.
- **The employer**, if you are willing to name it. If you name it, it is recorded as
  `stated_by_candidate` and it is one of the few company names in here that means anything.
- **The round and the level** as the employer described them, if they did.

We will not invent a level, a round or a company you did not state. Blank is a legitimate value and
most rows use it.

### 2. A correction

Open a [correction issue](../../issues/new?template=correction.yml). The common ones:

- **A mislabel.** `UQ-0421` is tagged `evals` but it is really asking about serving cost. Quote the
  id and say what it should be.
- **A bad merge.** Two different prompts were collapsed into one row. Phase 1 deliberately kept
  "What metrics do you use for RAG?" and "Walk through a RAG pipeline" apart; if something slipped
  through, it is a bug.
- **An over-claim.** A sentence in the report, the catalog or a figure title says more than the data
  supports. This is the correction we most want to receive.
- **A dead source URL**, or a source that turns out to be a compilation of a compilation.

### 3. A new bank or list

Useful, but it enters as `study bank` — the lowest tier — unless the author says these are questions
they were asked or asked. That is not a snub; it is the whole point of the grading. Say in the issue
what the author claims about their own sources.

## The rules a change has to keep

These are not style preferences. They are what makes the register worth citing, and a pull request
that breaks one will be asked to change.

1. **One row is one instance, not one interview.** Nothing in here may be turned into a percentage
   of interviews.
2. **A company name never loses its attribution.** `stated_by_candidate` and `bank_tag` are
   different kinds of fact and are stored in different columns. A tag is never promoted to a
   sitting, and a figure or table that shows company names says so in its title.
3. **Every count is split by source type.** The three sources are never summed into one ranking.
4. **The 0.6 bar holds.** A label counts only when confidence is at least 0.6 and the choice is not
   `unclear`. Review rows stay in the file and out of the counts.
5. **Evidence tier is never upgraded to make a point.** A compilation stays a compilation. Shamim
   via Landed is cited as Shamim.
6. **Every claim carries its limit.** The report's format is: one sentence you can disagree with,
   then the sources, then the limit. A new finding follows it.

## Working on the repo

```bash
python3 scripts/validate_data.py    # 85 checks; must pass before a PR is mergeable
python3 scripts/build_catalog.py    # regenerate catalog/ after any data change
```

Both run in CI on every push and pull request.

- **`catalog/` is generated.** Do not edit those pages by hand; change the data or the script and
  re-run. A hand edit will be overwritten on the next build.
- **`data/questions.csv` is the lab notebook and stays append-mostly.** New instances are added with
  a new `instance_id`; existing rows are corrected, not rewritten to fit a conclusion.
- **If you change a number, change it everywhere.** `validate_data.py` asserts the headline counts
  the report quotes. If your change is right, the assertion is what needs updating, and that update
  should be visible in the diff and explained in the PR.
- **If a change weakens a claim, weaken the claim.** Do not soften the data.

## What will be declined

- A dump of AI-generated interview questions. This register records what sources say, not what a
  model can invent.
- A question with no source URL.
- A company attribution based on "I heard they ask this."
- A ranking that merges the sources, or any framing of a count as a probability. That is the one
  thing this repository exists to refuse.

## Code of conduct

Be straight with the evidence and courteous with people. Do not post anyone's name, employer or
interview performance without their consent — including your interviewer's.
