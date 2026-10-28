# Data brief: what has been generated

Edition-to-edition changes in the Laws of Cricket, 44 editions (1752-2019), 43 consecutive pairs (diffed from 1744 via Rait Kerr's baseline).
All labels are machine/agent-drafted and Opus-checked over four passes. **None is human-verified** (`review_status = unreviewed`).

## Deliverables (`data/final/`)
| File | Rows | What |
|---|---|---|
| `changes_all_records_labelled.csv` | 7,262 | Every change record (add/remove/modify/move/renumber) with its own label row. 5,639 inherit an event label; 1,623 get a mechanical label (OCR, format, cross-reference pointers). |
| `substantive_changes.csv` | 996 | Events that are real changes: not NOT_A_CHANGE, not semantic-only (gender/pronoun/terminology/pure rewording). Qualifier/scope rewordings are kept and flagged. |

## Core tables
| File | What |
|---|---|
| `categories/event_labels_all.csv` | 1,506 labelled events: what changed, category/subtype, basis, confidence, rationale, evidence ids, dating, integrity flag, derived flags (`semantic_only`, `scope_change`, `source_edition_issue`, `substantive_change`), `label_ref`, `review_status`, `reviewer_notes`. |
| `gold/raitkerr_chronology.csv` | Rait Kerr's 138 serial changes (1744-1947), transcribed from page images. Gold recall of the diff: 11/11 on the pilot pairs. |
| `categories/raitkerr_drafts.csv` | Draft cause labels for each serial (157 rows). |
| `law_identity/` | 142 canonical Laws followed across editions (pivot, lineage, nodes). |
| `evidence/sources.csv` | 66 registered sources with reliability notes; saved texts in `evidence/text/`. |
| `events/`, `changes/`, `alignments/`, `nodes/` | Pipeline intermediates (segmentation, diff, grouping). |

## Label distribution (1,506 events)
- Category: NOT_A_CHANGE 618, STRUCTURAL 472, UNCATEGORISED 239, SEMANTIC_WORDING 53, RELOCATION 51, ENJOYMENT 42, NOVEL_EVENT 14, EXTERNAL_FORCE 11, ECONOMY 6.
- Basis: derived 765, inferred 399, none 239, stated 97, attributed 3, conjecture 3. Confidence: high 792, medium 493, low 221.
- Flags: 150 semantic-only, 11 scope-change, 96 source-edition issues. 948 events are pre-1947 (913 hand-labelled, 35 mechanical).
- Rule: no causal claim without a registered source; where none states a cause the event is UNCATEGORISED with basis `none`.

## Relocation category (taxonomy v0.3)
RELOCATION (51 primary: merge 33, pure_relocation 10, split 8; plus 34 secondary tags on events that also change a rule) records material moved within the book. Reviewed by four Opus agents over 596 candidates (`labels/relocations_{a,b,c,d}.json`, applied by `08_build_labels.py`). Plain renumbering with content in place, within-Law restructuring and segmentation noise are not relocations. A merge/split is tagged on each record that carries moved content, so one transfer can appear in two events.

## Renumbering category (taxonomy v0.4)
RENUMBERING (244 Law-level rows, `law_renumbered`): a Law keeps its text but changes number/position. The pipeline records these outside events, so they appear as `law_renumbering` rows in dataset 1 and as extra rows (`<pair>_N###`) in `substantive_changes.csv` (now 996 rows = 752 events + 244 renumberings); they are not in `event_labels_all.csv` or the review UI.

## Known limits
1. Unverified by a human. 2. 1902-1932 instruction sections are unsegmented (the 1907 new-ball-after-200-runs rule is missing as an event). 3. Several dataset editions are wrong or unreliable printings (see `DATA_INTEGRITY_FINDINGS.md`); their artefacts are labelled, not replaced. 4. Some web sources are unverified. 5. A few classifier blind spots (and/or, from/to, (a)/(b) swaps) and low-severity citation nits remain. 6. Taxonomy is v0.2.

## Verifying
`.venv/bin/python rule_changes/review_app/server.py` then open http://127.0.0.1:8765. Verdicts append to `data/review/verdicts.jsonl`; run `scripts/08_build_labels.py` then `09_build_datasets.py` to fold them into `review_status` / `reviewer_notes`. Suggested order: causal categories (73), `stated` (97), low-confidence UNCATEGORISED, `integrity = suspect`, scope changes, then a random sample.
