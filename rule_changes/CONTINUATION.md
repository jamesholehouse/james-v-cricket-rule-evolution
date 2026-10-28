# Continuation notes (session hand-over)

Written when the context window was nearly full. Read this, then `CLAUDE.md`, `rule_changes/README.md`, `rule_changes/DATA_INTEGRITY_FINDINGS.md`,
and the three Opus verification reports in `rule_changes/verification/` (A_pipeline_gold_report.md, B_labels_1947_2000_report.md,
C_labels_2000_2019_report.md). Plan of record: `~/.claude/plans/cozy-puzzling-token.md` (approved).

## What this project is
`/home/jamesh/GitHub/cricket-rule-evolution` is the user's fork (origin = jamesholehouse/james-v-cricket-rule-evolution, upstream =
ZaniuSchiaaa/cricket-rule-evolution) of the data/code for the paper on 268 years of the Laws of Cricket. The user (James Holehouse,
co-author) wants a dataset of year-to-year rule changes: what was added/removed/modified/moved (at what tree level), why (categories:
novel on-field event / external cultural force / economy / enjoyment / uncategorised, open to revision; I added STRUCTURAL and
NOT_A_CHANGE), with historical evidence, and a human-verification UI. Steps: (1) change dataset, (2) categorise + evidence,
(3) human verify with a UI. Work is in `rule_changes/` (uncommitted; nothing has been committed or pushed). Use `.venv/bin/python`
(repo root). Main paper PDF `cricket_PNAS_format-6.pdf` is a 0-byte failed copy (never read); SI PDF was read.

## State at hand-over
Done: Rait Kerr 1950 ch.6 gold (138 serials, `data/gold/raitkerr_chronology.csv`, rebuild `scripts/build_gold.sh`); segmentation of all 44 editions
(`01_segment_laws.py`, `01b_segment_eras.py`); diff of all 43 pairs (`02`); Law identity table (`04`, `data/law_identity/`); events (`06`);
mechanical checks (`07` numeric audit, `08a` ACS presence, `08b` text-diff class, `08c` found-elsewhere); label builder (`08_build_labels.py`);
hand labels `labels/p<pair>.py` for post-1947 pairs (459 labelled events); evidence store `data/evidence/{sources.csv,text/,raw/}`;
Rait Kerr draft labels `data/categories/raitkerr_drafts.csv` (`05_...py`). `scripts/run_pipeline.sh` rebuilds everything downstream of
processed texts (then run `08_build_labels.py`). Not started: labels for 1744-1947 diff records; review UI.
Key finding already documented: the AI clean-up of the digitised texts invents numbers where OCR was illegible (see DATA_INTEGRITY_FINDINGS.md).

## Opus verification (user asked: verify everything with Opus 5.5, then "fix the findings")
Three Opus agents reported (files above). Headline findings to FIX (details in the reports):
A (pipeline/gold):
 - `02_diff_editions.py` (~lines 229, 248): modify with sim>=0.97 and no number change is "trivial" -> real one-word changes (may->must, "only") lost.
 - xref units (kind 'xref') always ignored in diff, but 81 contain real notes (splitter does not split after ".)") e.g. 1913 Law 16 "cannot be stumped off a No Ball" = Rait Kerr 120.
 - 42 post-1947 events marked triage wording_only by 06 but substantive per 08b never reach labelling (also 55 events in 2000-2019 per C).
 - `_numvals.py` drops "4.25 in.", numbers after Law refs, unit-less decimals ("8.5 and 9 in").
 - 08b treats any single-digit change as numbering_only (6->8 balls) -> auto NOT_A_CHANGE; moves get no number check; 07 'supported' verdict weak
   (integers 0-30 always in raw OCR); sig hashes only first 120 chars; damaged Law numbers merge Laws (1939 One-Day Law 1 "I.-"; 1900 declaration Law).
 - Gold CSV: serial 22 must read 4 1/4 (not 4 3/4); 54a prior "4; 16"; bold markup for 52-56 (ALL), 58 (first sentence), "Before 1821" note, 70 (none), 1774 heading;
   start pages 38->71, 120->83, 137->86; section D for 13a-20c; README says 1962 missing Law 46 (now present).
 - raitkerr_drafts: 54/55 call handwriting "Rait Kerr's annotation" (author unknown); 99 secondary drafting_omission wrong (failed on notice); 101 pitch-technology secondary overreach.
B (labels 1947-2000): wrong: 1947_1952 E011/E026 (kicking/kneeing Note and raised-knee signal are in the ACS "Original Law 30" = 1952 wording; 1954 amendment only added
 "hand holding the bat"; dataset 1952 is a genuine 1952 printing, no 1953/54 amendments - also fix DATA_INTEGRITY_FINDINGS); 1947_1952 E005 (reason IS stated in S09: Sept 1951 Australian Board
 follow-on 150 not 200); five 1968_1980 "restructure" events hide policy changes (E014 min 20 overs last hour; E028 front-foot no-ball; E030 leg byes "tried to avoid being hit";
 E036 umpires judge ground/weather/light; E043 helmet catches); 1980_1992 E012 is a real LBW change; 1992_2000 E018 wrong (2000 text has LAW 20 LOST BALL); wrong Law names:
 1952_1962 E010 (Law 39 is LBW not Stumped), 1992_2000 E014 (practice was Law 15.2), 1980_1992 E017 (42.10 is Time Wasting). Uncovered real changes: 1952_1962 record 0034 (1954 "hand holding the bat"),
 1952_1962 E001 (rolling note "Except in the United Kingdom", ACS late 1962/early 1963), 1947_1952 record 0016, 1952_1962 record 0011, 1980_1992 E015 (stumped rebound "other than a protective helmet").
 Patterns: ~101 restructure labels use basis 'stated' but MCC preface states aim of the whole revision -> use 'inferred'; S11 (ACS 1980) includes later amendments so "confirmed in ACS 1980" does not confirm 1980 wording;
 1980_1992 E014/E016 categorised EXTERNAL_FORCE without evidence of cause -> UNCATEGORISED or lower confidence.
C (labels 2000-2019): 2017_2019 E057 hides MCC Law 41.16 rewrite (CRITICAL), E060 hides Law 42.4.2.3.1; six more of MCC's 22 changes (E011,E012,E019,E037,E041,E042) triaged wording-only, unlabelled;
 2008_2010: 36 'wording_only' labels cite a general NZC remark as a stated cause but 17 contain real rule changes (E012 toss, E036 Law 19.4, E084 injury stumping defence); E074 wrongly NOT_A_CHANGE;
 quotes: "No reason stated" attributed to S06 in E046/E048/E065/E071 not in article; 2010_2017 E002 presents journalist's "redress the balance between bat and ball" as MCC quote;
 2010_2017 E037 (Finn law 24.6: reason in S03, trigger in S07) wrongly UNCATEGORISED; tethered bails (E102) wrongly UNCATEGORISED with wrong note; 2000_2008 E003/E048 Mongoose claim backwards (S22 says Mongoose conforms to the new Law 6);
 2000_2008 E025 "new" dispensing-with-bails already in 2000 text; data-integrity table fixes: 1962 1-inch projection is already in raw OCR; 2010 ball '8 15/16' is an OCR misread (raw has it) and a second artefact (women's ball 8 1/2) missed;
 2017 men's ball reads "8.81 m" not "8.25 m", raw OCR misread 'm' in both 2017 and 2019; 1952 Laws 30/31 claim refuted (1952 has pre-1954 wording); 1890 claim: some reversions are transcription typos; 2000_2008 E051 is table-layout displacement not lost figures;
 sources.csv: S06/S22 notes inaccurate, S12 missing author/date, S08 quote not in saved local copy.

## Fix plan (order)
1. Builder robustness: resolve hand labels by content signature (not event id) so pipeline fixes do not orphan labels; queue = triage 'label' OR text_diff_class 'substantive'.
2. Code fixes (_numvals, 02 substantive rule via 08b classify, xref splitting in 01, 08b numbering rule, sig length, move number checks).
3. Re-run `run_pipeline.sh`; check `03_validate_gold.py` still 11/11; re-label new/changed events; apply every B/C label correction; correct basis 'stated'->'inferred' for restructure labels; fix sources.csv and DATA_INTEGRITY_FINDINGS.md; fix gold CSV; update README/CLAUDE.md.
4. Re-run a second (smaller) Opus verification on the changed material; report honestly what remains. Then ask the user about committing (nothing committed yet; never commit without being asked).

## Progress log (append below as fixes land)
- builder now resolves hand labels by change-record overlap (labels/keys.json), queue = all events; 44 events unlabelled at this point (to label)
- Opus B/C corrections applied to existing labels p1947_1952..p2017_2019 (dating errors, hidden policy changes -> UNCATEGORISED with secondary restructure, restructure basis stated->inferred, wrong Law names, quote fixes, Mongoose claim removed, E057/E060 2017_2019 now real 41.16/42.4.2.3 labels, Finn law E037, tethered bails E102). Builder validates: 431 labelled / 125 unlabelled / 21 resolution problems (those orphans need n-modules).
- TODO next: labels/n<pair>.py for the 125 unlabelled events + orphaned labels; gold CSV/raitkerr_drafts fixes; sources.csv; DATA_INTEGRITY_FINDINGS; README/CLAUDE.md; second Opus verification.
- Pipeline fixes: `_textclass.py` now has `ocr_noise` (rare token vs near-identical frequent word) and treats inserted/deleted content words (>=2) as substantive; taxonomy gained NOT_A_CHANGE/ocr_noise; builder merges two hand labels that share an event and keys n-labels as `pair:n:Exxx`.
- Labels: all 536 post-1947 events labelled (new modules labels/n*.py for the 125 previously unlabelled events). Orphaned old labels (event vanished) are reported by the builder, not written.
- Gold CSV corrections (L1-L4, M6) are in `_gold_finalise.py`; raitkerr_drafts 54/55/99/101 fixed; 05 now validates subtypes/basis; build_gold.sh uses the venv.
- sources.csv (S02, S06, S08, S11, S12, S17, S20, S21, S22), DATA_INTEGRITY_FINDINGS.md, README.md and CLAUDE.md updated. 03_validate_gold: 11/11.
- Remaining: second (smaller) Opus verification of changed material; user decision on committing; labels for 1744-1947 diff records; review UI.
- Second Opus pass (verification/D_second_pass_report.md): 108 FIXED / 11 PARTLY / 12 NOT FIXED / 3 WRONGLY FIXED. Applied afterwards: merge-primary rule (real-change label outranks wording_only/NOT_A_CHANGE), tighter ocr_noise rule (same first letter, rare token <=15 occurrences, 25x rarer), real word swaps now substantive, secondary-subtype check in builder (technology -> empty), conseq/reorg helpers 'inferred', 16+ extra labels in labels/nb*.py (keyed `pair:nb:Exxx`), S13 note, README counts. 552 events labelled, gold 11/11.
- STILL OPEN from D: changes of a cross-referenced Law number are invisible to the classifier (toks() strips Law refs), so MCC 2019 Law 21.12 and 33.4 and B's 1957 Law 16 change (1952_1962_0012) have no event; 2010_2017 E009/E010/E080/E081 and 2000_2008 E026/E028 labels, 1968_1980 E063 (bails/junior wickets), stated-basis leftovers (1947_1952 E007/E009/E014/E015, 1968_1980 E055, 1992_2000 E001/E051), 41 labels citing S11 for 1980 wording, stale 'see E0xx' cross-references in label text, 2010_2017 E090 text and S03 citation.
- Round 3 (user: 'fix the cross-reference blind spot and the open label gaps'): `_textclass.classify` now returns `xref_change` when only a cited Law/clause number differs (counts as substantive except for pair 2010_2017, i.e. 2017 renumbering) and ignores list labels ((b), (iv)); `08_build_labels.py` writes a `label_ref` column (source file:id of each label). MCC 2019 Preamble, 21.12 and 33.4 and the 1957 Law 16 change now have events and labels. Rewrote the remaining D items: 2010_2017 E006/E009/E010/E027/E072/E074/E075/E083/E090/E070/E104/E035; 1968_1980 E063 (flagged) and E055 (inferred); 'stated' -> 'inferred' for 1947_1952 notes and 1992_2000 E001/E051; S11 wording; stale 'see E0xx' removed; drafts 54a/55 cite the annotation on gold serial 52. 555 events labelled, 0 unlabelled, gold 11/11.
- Not re-verified by Opus after round 3.
- Round 4 (user: fix third-pass findings; fourth pass; label 1744-1947 and everything else; new 'semantic wording' category; keep semantic-only; two datasets):
  * Taxonomy v0.1 adds SEMANTIC_WORDING (modal_strength, qualifier_scope, pronoun_gender, terminology_term, clarifying_rewrite); builder adds `semantic_only` and `substantive_change` columns and writes `event_labels_all.csv` (all pairs 1744-2019; `post1947_event_labels.csv` is the filtered view). Classifier: inflections no longer OCR noise, real word swaps/in-out swaps/'striker'->'non-striker' are substantive, list labels b-h/romans (not 'm') ignored.
  * Third-pass findings fixed in labels (E095 fake-fielding/tampering event, wide-test, may/must suspect, 1947_1952 Law 27/25 misprint, basis downgrades, stale refs, S03 evidence, merged-row text, label_ref bug).
  * 9 Opus labelling agents (groups g1-g9) write labels/q<PAIR>.py for the 948 pre-1947 events (913 hand-labelled) (guide: LABELLING_GUIDE.md; tools: scripts/show_events.py, scripts/check_label_module.py); new sources in data/evidence/new_sources_g*.csv.
  * `scripts/09_build_datasets.py` builds data/final/changes_all_records_labelled.csv (every record has a label row) and data/final/substantive_changes.csv.
  * DO NOT re-run run_pipeline.sh while labelling agents work (event ids must stay fixed).
- Round 4 results: 9 labelling agents finished (all q*.py modules written, 0 checker problems); new sources merged into sources.csv (S31-S39, 66 sources total). event_labels_all.csv = 1,506 events, 0 unlabelled. Decisions from the user: SEMANTIC_WORDING category (done), semantic-only kept+flagged, NOT_A_CHANGE/edition_artefact (taxonomy v0.2; blank NOT_A_CHANGE subtypes normalised to it; `source_edition_issue` flag), `scope_change` flag (qualifier_scope rows stay SEMANTIC_WORDING but count as substantive), instruction-section segmentation deferred. Datasets: data/final/changes_all_records_labelled.csv (7,262 records, each with a label row) and substantive_changes.csv (742 events).
- NEXT: fourth Opus pass over round 4 (pre-1947 labels + classifier + datasets).
- Fourth pass (verification/F1-F4): F1 post-1947/tooling (1 HIGH, 4 MEDIUM, 9 LOW), F2 labels 1752-1857 (122/137 correct, 5 wrong), F3 labels 1857-1923 (141/159 correct, 4 wrong; unsegmented Instructions-to-Umpires gap), F4 labels 1923-1947 (169/185 correct, 1 wrong). Applied: builder merge ranking prefers substantive labels and keeps the second label's category/suspect flag, stricter fallback matching (token_sort_ratio >= 75; 4 events relabelled), stricter edition regex, labels/overrides.json with 27 corrections, 4 new labels. Not applied (LOW): classifier blind spots (and/or, from/to, (a)/(b) swaps), seven 'ch. 5' vs ch.4 citations, source-note nits, duplicate descriptions.
