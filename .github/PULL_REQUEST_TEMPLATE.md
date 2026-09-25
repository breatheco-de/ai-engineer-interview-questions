## What this changes

<!-- One or two sentences. If it changes a number, say which number. -->

## Which layer

- [ ] `data/questions.csv` — a new instance or a corrected one
- [ ] `data/unified_*.csv` — a merge, a split, or a label
- [ ] `catalog/` — regenerated, not hand-edited
- [ ] `REPORT.md` / `docs/` — prose
- [ ] `scripts/` — tooling
- [ ] Repository furniture (README, templates, CI)

## The rules this change keeps

- [ ] No count is presented as a probability that a question is asked.
- [ ] Every count is split by source type; the three sources are not summed.
- [ ] Company names keep their attribution — a `bank_tag` was not promoted to a sitting.
- [ ] The 0.6 confidence bar is unchanged, or the change to it is the point of this PR and is stated.
- [ ] Any new claim carries its limit.

## Checks

- [ ] `python3 scripts/validate_data.py` passes.
- [ ] `python3 scripts/build_catalog.py` was re-run and `catalog/` is committed in sync.

<!-- If you changed an assertion in validate_data.py, say here why the old number stopped being true. -->
