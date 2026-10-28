# Guide to the review UI

The UI lets you check, one row at a time, every label in the dataset against the old and new text and the cited evidence, and record a verdict. It shows **1,750 rows**: the 1,506 pipeline events plus the 244 Law-level RENUMBERING rows (ids like `1939_1947_N012`).

## 1. Start it
From the repo root:
```
.venv/bin/python rule_changes/review_app/server.py
```
Open http://127.0.0.1:8765 (use `--port 9000` if it is busy). It runs until you press Ctrl+C. Restart it after rebuilding the data, because it reads the CSVs once at start-up. Needs only the Python standard library.

## 2. The screen
**Left panel (list).**
- Filters: free-text search (explanation, rationale, Law title, event id), edition pair, category, review status, basis, confidence, "substantive only", "integrity: suspect".
- Each row: event id, Law, a coloured status tag, tags for category / basis / confidence, and `semantic` or `edition` flags.
- The line under the filters counts how many rows you have reviewed, by status.

**Right panel (the selected row), top to bottom.**
1. *Label*: category/subtype (and a secondary category if the event also does something else), confidence, basis, integrity, derived flags, dating evidence, and the file the label came from.
2. *What changed* and *Rationale*: the claim and the reason given for it. *Notes* shows corrections and, for relocations, the previous label.
3. *Evidence*: each cited source with title, publisher, date, reliability note and a link where one exists. Rait Kerr serials named in the label appear as quoted entries.
4. *Whole Law side by side* (default tab): the complete old Law (left) and new Law (right) in book order, aligned paragraph by paragraph, with deleted words in red and added words in green. Unchanged paragraphs are dimmed (tick "hide unchanged text" to hide them); paragraphs that belong to this event carry a blue bar and an "in this event" badge. Paragraphs found only on one side are tinted. If the Law number cannot be matched (heading blocks, the single-block 1752 text) the view uses the Laws containing the event's own units and says so; some rows (for example a section removed entirely) have no Law text, so use the records tab.
   *Changed records* (second tab): every record of the event, each one sentence/clause the diff found. A reworded or moved clause can show as a "remove" in one record and an "add" in another. Renumbering rows show only the Law numbers.
5. *Verdict bar* (sticks to the bottom): note box, proposed category/subtype boxes, and buttons.

## 3. Verdicts
| Verdict | Key | Use when |
|---|---|---|
| Confirm | `c` | The label, category and evidence all hold up. Moves to the next row. |
| Edited | `e` | The label is partly right. Write what should change in the note, fill the proposed category/subtype if you can. |
| Reject | `x` | The label is wrong (e.g. an artefact called a rule change, or the reverse). Say why in the note. |
| Needs research | `r` | You cannot decide without more evidence. |
| Clear | button | Back to unreviewed. |

`j`/`k` move to the next/previous row in the current list. Keys are ignored while you type in a box. Saving is immediate: each click appends a line to `data/review/verdicts.jsonl` (the last line per row wins, and the file is plain text you can diff in git).

## 4. Suggested order
1. The 73 causal rows: category NOVEL_EVENT, ENJOYMENT, EXTERNAL_FORCE, ECONOMY. They make claims about *why*.
2. Basis `stated` (97): check that the source really states the cause of *this* change, not of the revision as a whole.
3. Category RELOCATION (51 primary) and RENUMBERING (244): confirm the text really moved or kept its text under a new number.
4. UNCATEGORISED with confidence `low`; integrity `suspect`; SEMANTIC_WORDING with `qualifier_scope`.
5. NOT_A_CHANGE: filter by category and read a sample of each subtype. See `NOT_A_CHANGE_EXAMPLES.md` for what to expect; spend the most time on `edition_artefact`, where the wording differences are real.
6. A random sample (say 5%) of everything else.

## 5. What to check on a row
- Does the old/new text show what the explanation says? Numbers are the most error-prone (OCR and clean-up errors): compare against the raw OCR in `data/datasets/rule_texts/raw/` or the ACS transcriptions in `data/evidence/text/`.
- Is the category right? A wording change is not a rule change; a move that also changes the rule should have the rule change as primary.
- Does the cited source say what the rationale claims? Open the link or the saved text.
- Dates: editions can lag Rait Kerr's date by one or more editions; the dating field should say so.
- Is it a dataset artefact (wrong printing, segmentation, OCR) rather than a real change?

## 6. Turning verdicts into corrected data
Verdicts are a record; they do not change labels by themselves.
1. **Folding verdicts into the datasets.** Run, from the repo root:
   ```
   .venv/bin/python rule_changes/scripts/08_build_labels.py
   .venv/bin/python rule_changes/scripts/09_build_datasets.py
   ```
   This fills `review_status` and `reviewer_notes` in `data/categories/event_labels_all.csv`, `data/final/substantive_changes.csv` and (for renumbering rows) the Law-level rows. Restart the UI afterwards.
2. **Changing a label permanently.** Add an entry to `labels/overrides.json` (`event_id`, the row's `sig`, a `why`, and a `set` block with the new category, subtype, confidence, basis, plus `append` text), or edit the label module named in the row's `label_ref`. Relocation tags live in `labels/relocations_*.json`. Then rerun the two scripts. Never edit the CSVs by hand: the next build overwrites them.
3. **Renumbering rows** are made by `09_build_datasets.py` and cannot be overridden; reject them in the UI and note it, then change the script if a pattern is wrong.

## 7. Things to know
- A row's list entry shows only the first 140 characters of the explanation; open it for the full text.
- The old/new panel shows every record of the event, which can be dozens in the big rewrites (1968–80, 2008–10, 2010–17).
- The 1902–1932 instruction sections are not segmented, so some "new" 1939 notes are really moves; the label notes say when this applies.
- Several dataset editions are wrong or unreliable printings (see `DATA_INTEGRITY_FINDINGS.md`). A difference caused by one of these is labelled NOT_A_CHANGE / edition_artefact.
- The UI shows only the first 8 Rait Kerr entries named in a label.
- Verdict file and project data are committed to git, so your review history is versioned: commit `data/review/verdicts.jsonl` after each session.
