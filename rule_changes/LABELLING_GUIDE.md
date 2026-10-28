# Hand-labelling guide (events -> category + evidence)

Applies to every event that the builder (`scripts/08_build_labels.py`) cannot label mechanically. One label per event, written in a
module `rule_changes/labels/q<PAIR>.py` (one module per edition pair, e.g. `q1830_1835.py`), using the helper in `labels/_h.py`:

```python
"""Labels for 1830 -> 1835."""
from _h import make
PAIR = "1830_1835"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
L("E012", "<what changed, concretely: quote key old/new words>", "ENJOYMENT", "bowler_batsman_balance", "medium", "stated",
  "<rationale: what the source says and why that is the cause>", ["S16"], sec="", secsub="", date="<when/dating evidence>",
  integrity="ok", note="")
```
Event ids (`E012`) are those printed by `.venv/bin/python rule_changes/scripts/show_events.py <PAIR> --unlabelled` (old/new text of each
event; use `--max-records 40 --chars 600` for more). Validate WITHOUT writing any project file:
`.venv/bin/python rule_changes/scripts/check_label_module.py rule_changes/labels/q<PAIR>.py`.
Never run `08_build_labels.py` and never edit another module, `sources.csv`, or data files (other agents work in parallel).

## Fields
- `what`: what the rule change is, concretely, quoting the old/new wording. If the event is OCR/typography noise, say so.
- `cat`, `sub`: from `schema/taxonomy_v0.json` (v0.1). Categories: NOVEL_EVENT, EXTERNAL_FORCE, ECONOMY, ENJOYMENT, STRUCTURAL,
  SEMANTIC_WORDING, UNCATEGORISED, NOT_A_CHANGE. NOT_A_CHANGE subtypes: format_artefact, cleaning_artefact_numeric,
  segmentation_artefact, ocr_noise. SEMANTIC_WORDING (user-defined): a re-write that does not necessarily change what the rule
  requires but may change how it is read or enforced - subtypes modal_strength (may/must/shall/should), qualifier_scope
  (qualifying words), pronoun_gender, terminology_term, clarifying_rewrite. Pure gender-neutral/pronoun/terminology changes are
  "semantic only": keep them as events, category SEMANTIC_WORDING (or the cause category with a rationale containing "gender-neutral").
- `conf`: high / medium / low. `basis`: stated (a source states the cause of THIS change), attributed (a named person/body is
  reported as claiming it), inferred (you infer it from context; say so), conjecture, derived (NOT_A_CHANGE/artefacts), none
  (UNCATEGORISED only). UNCATEGORISED must have basis "none"; NOT_A_CHANGE must have "derived".
- **No claim without evidence.** A causal category (not UNCATEGORISED/STRUCTURAL/NOT_A_CHANGE/SEMANTIC_WORDING) needs a rationale and
  at least one registered source id. If no source gives a reason, use UNCATEGORISED / basis none / "no_cause_stated" and say what
  you searched. A preface that states the aim of a whole revision does not state the cause of one provision: use `inferred`.
- A restructure/merge label must not hide a policy change: describe the real change and add `sec="UNCATEGORISED", secsub="no_cause_stated"`.
- Do not trust numbers. The processed texts contain AI-clean-up inventions and OCR misreads (see DATA_INTEGRITY_FINDINGS.md). Early
  editions (1752-1830) also differ in capitalisation, long-s, spelling and punctuation: that is `format_artefact`/`ocr_noise`, not a change.
  Check raw OCR in `data/datasets/rule_texts/raw/<year>_raw.txt` for any numeric change and mark `integrity="suspect"` if unsupported.
- Edition lag: a change dated by Rait Kerr to year Y may appear only in a later edition; say so in `date`.
- Small wording changes may carry semantic information: label them SEMANTIC_WORDING with a rationale saying what could change in
  enforcement, rather than silently dismissing them. Do not label them as rule changes unless a source or the text shows the rule changed.
- Quotes must be exact. Never put a journalist's words in quote marks as if from MCC. Cross-reference other events by what they
  contain, never by event id.

## Evidence
- S16 = Rait Kerr, *The Laws of Cricket: Their History and Growth* (1950). Chronology of ~138 changes 1744-1947:
  `data/gold/raitkerr_chronology.csv` (serial, date, particulars, prior/later links, bold = his own claims of new information) and
  the full text `the_laws_of_cricket_rait_kerr_1950/the_laws_of_cricket_rait_kerr_1950.txt` (chapters 2-5 give causes; ch.6 the chronology).
  Draft labels for each serial: `data/categories/raitkerr_drafts.csv` (unreviewed; do not copy blindly). Cite as evidence `["S16"]` and
  put the serial number(s) in the rationale ("Rait Kerr serial 88"). Match events to serials by date and subject.
- Other registered sources: `data/evidence/sources.csv` (S01-S22; local texts in `data/evidence/text/`). Use WebSearch/WebFetch for
  further primary or good secondary sources (MCC, ACS, Wisden, Cricinfo, Wikipedia as last resort). New sources go into
  `data/evidence/new_sources_<yourgroup>.csv` with the same header as sources.csv and ids S<group>-NN (e.g. S31-01); record
  title, publisher/author, date, url, type, local_text (leave empty), reliability_note. Cite them by id in labels.
- Pre-1884 editions are segmented as heading blocks, so "Laws" in the early pairs are weak; judge by the text of the event.

## Output
Write the module(s) for your pairs, run the checker until it reports 0 problems and no events needing a label are missing, then
reply with: counts per category/basis, the events you were unsure about (with why), any questions for the project owner about
small wording issues (e.g. whether a may/must change should count as a rule change), and the new sources you added.
