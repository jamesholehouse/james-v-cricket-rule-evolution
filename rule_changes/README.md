# rule_changes: edition-to-edition change dataset (work in progress)

Goal: for every pair of consecutive editions of the Laws of Cricket, record what was added, removed,
modified or moved (and at what level), classify why, back it with evidence, and have a human verify it.
Plan: `~/.claude/plans/cozy-puzzling-token.md` (approved). Run everything from the repo root with `.venv/bin/python`.

## Status

| Step | State |
|---|---|
| Rait Kerr (1950) ch. 6 gold chronology | done: `data/gold/raitkerr_chronology.csv` (138 serials; `scripts/build_gold.sh`) |
| Segmentation, all 44 editions | `scripts/01_segment_laws.py` + `scripts/01b_segment_eras.py` |
| Deterministic diff, all 43 consecutive pairs | `scripts/02_diff_editions.py` -> `data/changes/`, `data/alignments/` |
| Gold recall check | 11/11 pilot-pair entries found (`scripts/03_validate_gold.py`) |
| Law-number / identity table | `scripts/04_build_law_table.py` -> `data/law_identity/` (law_pivot.md, law_lineage.csv, law_nodes.csv) |
| Change events (grouped records) | `scripts/06_group_events.py` -> `data/events/`; mechanical checks `07`, `08a`, `08b`, `08c` |
| Categories + evidence, pre-1947 | Rait Kerr's own entries (drafts) plus all 948 pre-1947 diff events (913 hand-labelled, 35 mechanical) (labels/q*.py): `scripts/05_raitkerr_category_drafts.py` -> `data/categories/raitkerr_drafts.csv` |
| Categories + evidence, post-1947 | **every one of the 1,506 events of all 43 pairs 1744->2019 carries a label (post-1947 labels in `labels/p*,n*`, pre-1947 in `labels/q*.py`; `data/categories/event_labels_all.csv`; final datasets in `data/final/`)** (hand labels in `labels/p*.py` and the later `labels/n*.py`/`nb*`/`nc*`/`nd*` modules, mechanical labels for format/OCR-noise/minor-wording events), all unreviewed; built by `scripts/08_build_labels.py` -> `data/categories/post1947_event_labels.csv`; sources in `data/evidence/sources.csv` |
| Verification | Opus verification reports A-E in `verification/` (A pipeline+gold, B labels 1947-2000, C labels 2000-2019, D second pass, E third pass); findings applied round by round (see `CONTINUATION.md`). A fourth pass follows the 1744-1947 labelling |
| Review UI | built: `review_app/server.py` (stdlib only) + `index.html`; verdicts -> `data/review/verdicts.jsonl`, folded in by `08_build_labels.py`. See `DATA_BRIEF.md` |

Run everything downstream of the processed texts with `scripts/run_pipeline.sh`, then `scripts/08_build_labels.py`.
See `DATA_INTEGRITY_FINDINGS.md` for the clean-up artefacts found and the tooling's known limitations.

## Data model notes

- `data/nodes/<year>.jsonl`: one row per unit (sentence/clause/note); `kind` = body | note | xref | heading;
  `label` holds a leading `(a)`-style marker. Headings and Law titles are kept but not diffed.
- `data/changes/<a>_<b>.jsonl`: candidate change records (`op` add/remove/modify/move/renumber,
  `granularity` law/clause/note/cross-reference, `substantive` heuristic, number cues, word diff). No categories yet.
- `data/alignments/<a>_<b>.json`: Law-to-Law alignment by text similarity (detects renumbering) + pair stats.

## Known limits

- Edition lag: a change dated by Rait Kerr to year Y may only appear in a later edition (e.g. #112 and #115,
  dated 1899-1900, are absent from the 1900 text and appear in 1902).
- The 1890 text differs from both 1884 and 1892 in small wording ways (and reverts in 1892), so it may be a
  different printing; wording-only differences there are noise for the categorisation step.
- `substantive` is decided by the token-level classifier `scripts/_textclass.py` (numbers, modal/negation words, content words inserted or
  deleted; OCR garbage ignored); wording-only edits are kept but flagged.
- Gold regexes in `03_validate_gold.py` are lenient; a hit means a matching record exists, not that it is the best one.
- 1939 carries inline "(Introduced/Revised <date>)" tags: useful built-in dating evidence for the next phase.
- Law identity is content-based (optimal 1:1 matching with title/number agreement). Pre-1884 "Laws" are heading blocks
  (or one pseudo-Law in 1752), so early lineage rows are weak; the 2017 text has no LAW 28/29 headings (recovered from clause
  numbers).
- The big rewrites (1968->1980, 1992->2000, 2008->2010, 2010->2017) produce hundreds of "substantive" records that are mostly
  rewording of rewritten text; they need event-level grouping before categorisation.
- Category frequencies in `raitkerr_drafts.csv` reflect Rait Kerr's own framing (bowler/batsman balance, round-arm bowling),
  not an independent view; `basis` records how each cause is known, 41 of 157 draft rows carry no stated cause. In the post-1947 labels `basis = stated` means a source states the cause of that specific change; the MCC prefaces state the aim of a whole revision, so consolidation/restructure labels use `inferred`.
