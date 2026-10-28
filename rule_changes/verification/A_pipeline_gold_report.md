# Verification report A: pipeline code, reproducibility, gold transcription, Rait Kerr drafts

Reviewer scope: `rule_changes/scripts/*.py` (code review), a reproducibility run of `run_pipeline.sh` and `08_build_labels.py`,
the gold file `data/gold/raitkerr_chronology.csv` checked against the page images (book pp. 66-87, image00095-image00116), and
the citations and rationales in `data/categories/raitkerr_drafts.csv`. Date of review: 2026-10-26. No file other than this
report was modified. The pipeline's own outputs were rewritten by the run, but they came out byte-identical, as shown below.

## Verdict summary

- **Reproducibility: PASS.** The pipeline and the label builder give byte-identical outputs. I ran them twice: once as is, and
  once with `PYTHONHASHSEED=12345`. Each time I compared `rule_changes/data` and `rule_changes/labels` against a snapshot taken
  before the run (`diff -rq`), and nothing differed. The gold build (`build_gold.sh`), run in a scratch copy, also reproduces
  `raitkerr_chronology.csv` byte for byte. I found no nondeterminism.
- **Gold transcription: GOOD, with a few real errors.** I checked every printed page of the chronology, which covers all 138
  serials plus the unnumbered 1884 and 1947 items. Serial numbers, dates, particulars text and prior/later references are
  almost all correct. I found 1 wrong number in the particulars (serial 22, 4¾ where the book prints 4¼) and 1 wrong
  reference (54a prior). The bold markup has systematic errors: 6 serials on p.74 are missing it, and 3 rows are marked "ALL"
  wrongly. 3 start pages are wrong, and the section letter is missing for serials 13-20. The handwritten annotations and
  struck-through text on pp.74-75 are handled well.
- **Code: no crash bugs, but several silent failure modes.** The pipeline can drop or misclassify real rule changes without any
  warning. Most serious: a one-word change in a long sentence that keeps similarity at or above 0.97 (e.g. may -> must)
  is discarded before grouping into events. All edits inside "xref" units are discarded. Moves never get numeric
  cues or a numeric audit. 42 post-1947 events that 08b itself calls "substantive" are triaged out of labelling. `_numvals`
  silently drops decimal values written with the "in." unit, and drops numbers that follow a Law reference. The 07 "supported"
  verdict is close to meaningless for small integers.
- **Rait Kerr drafts: citations hold up.** About 35 rationales were checked against the OCR text, and the quotes and page
  claims are accurate. There are 3 mild overreaches (serials 54/55, 99 secondary, 101 secondary).

## Findings

### HIGH

**H1. Near-identical modifies are dropped as non-substantive even when a modal or negation word changes.**
`02_diff_editions.py:229,248` (`TRIVIAL_MIN = 0.97`, line 37) marks a modify `substantive=False` when similarity is >= 0.97
and there is no numeric cue. `06_group_events.py:226` then keeps only substantive records, so these changes never become
events and are never labelled.
Evidence (`/tmp/rc_probe2.py` over all change files): 59 non-substantive modifies change a modal, negation or restriction word.
Most are quote or hyphen noise, but several are real rule changes:
- `2017_2019_0041` (Law 17): "he/she **may** subsequently call Over" -> "he/she **must** subsequently call Over" (sim 0.989).
- `2008_2010_0357` (Law 32): "in the case of the wicket-keeper, in his pads" -> "the wicket-keeper **only**" (0.982).
- `2000_2008_0068` (Law 22): "provided **only** that he does not bowl two overs..." -> "only" removed (0.986).
- `1820_1823_0001`: "must weigh not less than..." -> "MUST not weigh less than..." (0.97).
- `2008_2010_0131/0326`, `2010_2017_0163/0165`: will <-> shall.

Fix: before calling a modify trivial, run 08b's token test on it. Make the record substantive if any changed token is in
08b's `KEEP` set or is a number. Better still, drop the similarity shortcut and use the token classifier alone.

**H2. Edits inside "xref" units are always non-substantive, but in 1902-1939 those units hold real rule notes.**
`02_diff_editions.py:229,248` sets `substantive = ob["kind"] != "xref" and ...`. The segmenter labels a unit "xref" when it
starts with "(See", but `split_sentences` (`01_segment_laws.py:137`) does not split after ".)". The cross-reference therefore
swallows the sentence that follows it. Data check (`/tmp/rc_probe6.py`): 81 xref units in 1902-1939 carry more than 20
characters of rule text. One example is 1913 Law 16: "(See Laws 13, 23, 28 and 32 and Notes.) A Batsman cannot be stumped
off a No Ball (Law 16)." That is Rait Kerr serial 120. Another is `1923_1932_0040`, where the ball is no longer dead on hitting
the umpire "unless it lodges in his pocket or clothing". Any edit to these notes is silently dropped.
Fix: in `split_sentences`, also split after `.)`, `."` and `.”`. Only treat a unit as xref when it is nothing more than the
parenthetical reference.

**H3. 42 post-1947 events that 08b classifies "substantive" are never labelled.**
`06_group_events.py:212,267` triages an event as `wording_only` when it is modify-only, has mean similarity >= 0.85 and has no
numeric cue. `08_build_labels.py:85` skips every event that is not triaged `label`. Post-1947 wording_only events by 08b class:
substantive 42, minor_wording 18, format_only 12. At least 15 of the 42 change a modal or restriction word, for example
`2008_2010_E056` (runs awarded for a No ball), `2008_2010_E038` (must/shall, "nominated"), `1952_1962_E001` (except ... Australia,
South Africa...). The README's claim "done for all 459 events" therefore leaves out these 42 events, which are not in the CSV
at all.
Fix: triage on 08b's class, not on similarity. At minimum, queue wording_only events whose `text_diff_class` is "substantive".

**H4. `_numvals.values` silently drops many real dimensions and numbers.** (`_numvals.py:15-18`)
Probes (`/tmp/rc_probe3.py`):
- `"4.25 in."` -> `[]` and `"width 4.25 in. maximum"` -> `[]`. "in"/"in." is missing from the unit whitelist in the `REFS`
  lookahead, so any decimal of 1-2 digits written with "in." is read as a clause reference and dropped. The 2017/2019 texts
  contain "2.5 in", "1.38 in", "1.2 in" and "0.04 in". `"0.04 in./0.1 cm"` -> `[0.1]`, and this is the very 2019 bat-covering
  value listed in DATA_INTEGRITY_FINDINGS.
- `"between 8.5 and 9 in"` -> `[9.0]`. A bare decimal without a whitelisted unit is dropped.
- `"Law 42.17, 5 Penalty runs"`, `"under Law 24, 6 runs"`, `"Law 2.6 and 5 penalty runs"` -> `[]`. The REFS list-continuation
  `(,|and|&|or|to) \d+` swallows the next number, even when it is a run or penalty value. This pattern is common in 2000+ texts.
- `"8 13⁄16"` (U+2044 fraction slash) -> `[8, 13, 16]`. `"Laws 1-4"` -> `[4]`. The documented limitations (ASCII "1/2" read
  as 1 and 2, superscript fractions such as `8¹³/₁₆` in 1968 and 2000) are real, as stated.

Effect: missing `cue_added`/`cue_removed`, so a numeric change can be typed as "rewording" and triaged out (see H3). 07 also
cannot audit values it never extracts. The DATA_INTEGRITY table cannot be produced from these tools for the 2017/2019 inch
values.
Fix: add `in\b|in\.|ins?\b` to the unit whitelist. Allow a bare decimal unless it is preceded by Law/Note/clause context
(test the left context, not the right). Stop the REFS continuation from consuming a number that is followed by a unit or by
runs/overs/balls. Add the U+2044 slash and the super/subscript digits.

### MEDIUM

**M1. `08b` classifies any single-digit number change as "numbering_only", and `08` then auto-labels it NOT_A_CHANGE with
confidence "high".** `08b_classify_text_diff.py:68` drops every token `#d` of length 2 as a "list marker". Probe:
`classify("an over shall consist of 6 balls", "... 8 balls")` -> `('numbering_only', ['#6','#8'])`. The same happens for
5 -> 6 penalty runs, 4 -> 9 inches and 2 -> 3 minutes. Today's numbering_only events are all genuine stray list numbers (I
checked all of them with `/tmp/rc_probe4.py`), so no current label is wrong. But any future or unlabelled event with a real
digit change would be silently stamped `NOT_A_CHANGE/format_artefact/high`.
Fix: treat `#d` as a list marker only when it appears in one text and has no counterpart in the other (an insert or delete),
and never when it is part of a replace.

**M2. Moves never get numeric cues or a numeric audit.** `02_diff_editions.py:292` (move records have no `cue_*` fields). 07
(`:96`) and 08b (`:256`) skip relocation events, and also new_law/law_removed. 16 move records have different number sets on
the two sides, e.g. `1857_1884_0107` [1,2,5,20] -> [5,22], `1932_1939_0109`, `1939_1947_0283` [] -> [2]. A clause that was
moved and also had a value changed (similarity >= 0.80 still allows that) is reported only as a relocation. Whole-Law
additions are never checked for invented numbers either, which matters because the AI clean-up is known to invent them.
Fix: compute cues for moves. In 07, audit the values of new/removed Laws against raw OCR.

**M3. The 07 "supported" verdict is very weak.** `07_audit_numeric_cues.py:77` counts a value as supported if it appears
anywhere in the edition's raw OCR or reference text. Measured: every integer 0..30 appears in the raw OCR of 1947, 1980, 2000
and 2019 (2019 also contains 0.5 and 4.25). Any changed small integer is therefore "supported" automatically. The README and
findings treat 451 "supported" verdicts as evidence.
Fix: test the value in its local context (for example the value plus the next unit word, or a fuzzy window around the
sentence), or report "uninformative" for values that are ubiquitous in the corpus.

**M4. The label signature is weak.** `08_build_labels.py:34-36` hashes only the Law numbers and the first 120 characters of
each digest. A pipeline change that alters the event type, the change_ids or text after character 120 keeps the same signature,
so the hand label silently attaches to a different event. Labels with no stored signature are accepted and stored on first
sight, with no protection. Fix: hash `event_type`, `change_ids` and the full digests.

**M5. Segmentation silently absorbs content when OCR damages a Law number, and there is no completeness check.**
- 1939: "I.—The side which bats first..." (OCR "I" for "1") puts One-Day Law 1 inside main Law 55. The ONE DAY MATCHES section
  then has only Law 2 (nodes show `ONE DAY MATCHES:1 [2..2]`).
- 1900: the declaration Law is printed "1.—" after Law 53, so it is merged into Law 53 (main runs 1..53). 1900 also has an
  "INSTRUCTIONS TO UMPIRES" section and no SINGLE WICKET section, so 1896->1900 and 1900->1902 show section-level add/remove noise.
- `LAW_MARK` (`01_segment_laws.py:78`) accepts "N word" with no dot (`\s+` alternative), so a body line that wraps to start with
  "4 runs ..." can open a spurious Law when expected <= 4 <= expected+2.
- Titles are empty for almost all Laws in 1828-1932 (e.g. 1892-1932: 54-57 of 54-57). This weakens the title term in
  `assign_laws`.
Fix: assert per edition that main Laws run 1..N with no gaps and that each expected appendix section is present, and warn on
any OCR-like Law marker (I., l., O.).

**M6. Gold: bold markup errors.** "Bold" records Rait Kerr's own "fresh light" claims, so these errors change the meaning.
- Serials **52, 53, 54a, 54b, 55, 56** (p.74, image00103): the whole printed text is bold, and the date "Before 1811" is bold
  too. Gold `bold_text` is empty for all six. Correct value: `ALL`. For 54a and 55, the struck-through sentences are bold as well.
- Serial **58** (p.75): only "The “No ball” Law was again modified with the object of curbing round-arm bowling." is bold. Gold
  wrongly includes "The resulting Law was so complicated ... in their campaign."
- Note row "Before 1821" (p.75): only "The changes listed in Serial Numbers 59 to 61 were almost certainly made in 1819," is
  bold. Gold says `ALL`.
- Serial **70** (p.76): no part of it is bold, neither date nor text. Gold says `ALL`. Correct value: empty.
- Serial **68** (p.76): "(Vide G. B. Buckley, Fresh Light on Pre-Victorian Cricket.)" is not bold. Gold says `ALL`, which is
  slightly wrong.
- Heading "The Revision of 1774" (p.70): the first clause "This revision was carried out by a committee representing Kent,
  Hampshire, Surrey, Sussex, Middlesex and London—" is not bold. Gold says `ALL`.
- Not captured: bold *dates* whose text is not bold. Serial 74's "May 14th 1835" is bold (p.77). That is Rait Kerr flagging the
  date as new information. Consider a `date_bold` flag.

### LOW

**L1. Gold: wrong number in the particulars of serial 22.** The particulars read "limited the width of the bat to **4¾**
inches". The page (p.69, image00098) prints **4¼**, and the gold's own `bold_text` correctly says 4¼. Fix: 4¾ -> 4¼.

**L2. Gold: serial 54a prior reference.** The page prints "4, 16" against the first line of 54, and "4" again against the
second paragraph. Gold 54a has `prior=16`. Correct value: `4; 16`. Gold 54b `prior=4` is correct.

**L3. Gold: wrong start pages.**
- Serial 38 starts on p.71 ("c. 1787 38 The second Maidstone edition in-"); gold says 72.
- Serial 120 starts on p.83; gold says 84.
- Serial 137 starts on p.86; gold says 87.
Other multi-page entries (30, 94b, 131b and so on) are recorded consistently with their start page.

**L4. Gold: `section` is blank for serials 13a-20c.** Section D starts at serial 11 on p.67 and runs to 20c; section E starts at
21. The helper says section is set for the 1744 code, but only the first rows of each section carry it (A 4 rows, B 5, C 1,
D 2, E 2). Correct value: `D` for the 14 rows 13a-20c.

**L5. Gold schema ambiguities.**
- `''` in prior/later means both "em dash printed" and "nothing printed" (e.g. 80b, 94b, 132 later, u5).
- Transcriber notes go into the `annotation` column, which is documented as "handwritten marginal note" (serial 80a).
- The heading and note rows are summaries, not verbatim text (the "Note to Serial Numbers 8 and 9" and the 1774/1788/1835
  headings), although the helper says particulars are verbatim.
- Unnumbered ids `u2`..`u5` are used for both 1884 and 1947 (sub column, serial blank), so `(serial, sub)` is not a unique key.

**L6. 02 dead or misleading code.**
- The docstring says Laws are aligned by "order-preserving weighted alignment", but `assign_laws` uses linear_sum_assignment.
- The `threshold` argument (`LAW_MATCH_MIN`) is ignored; the thresholds are hard-coded at line 107.
- `REF_NUM` and `CLAUSE_REF` (lines 131-134) are unused.
- `law_sim` adds +0.05 for the same number while `assign_laws:103` subtracts 0.05, but `law_sim` is capped at 1.0. Identical
  Laws with the same number therefore report similarity 0.95, and an identical Law with a *different* number reports 1.0.

**L7. 06 clustering mixes coordinate systems.** `pos()` (`06_group_events.py:190`) uses `unit_to` (new edition) for
add/modify and `unit_from` (old edition) for removes. The `GAP=3` clustering then compares indices from different editions,
which can merge unrelated edits or split one edit. Event ordering also sorts Law numbers as strings ("10" < "2"). That is
cosmetic, but event ids depend on it.

**L8. Re-segmentation fallback can mask add+remove.** `02_diff_editions.py:249-260` merges all leftover units of a Law into one
"modify" when the concatenations have sim >= 0.5. The fallback is lenient, and the record has no `path_from`.

**L9. `05_raitkerr_category_drafts.py` `check()`** validates categories but not subtypes or `basis` against the taxonomy.
`08_build_labels.py` does validate them.

**L10. `build_gold.sh` uses `python3` (system), not the venv.** `_gold_finalise.py` needs pandas. It worked here, but the
build is environment-dependent.

## Rait Kerr drafts (`raitkerr_drafts.csv`): citation check

The page markers in the OCR text are lone numbers, and many are missing, so I placed each phrase between its neighbouring
markers. These cited quotes and claims were found at the cited chapter and page (+/- 1):

- 22 (Ryegate, 4¼, "no more risks should be run", p.22)
- 23/24/31/33 ("careless drafting", p.22)
- 34 (Lumpy/Small, "hard thing upon the bowler", p.23)
- 40 ("bad conditions make for bad cricket", "tremendous advance", p.23)
- 41/43 ("strict keeping", p.23)
- 47 ("assistance to the bowler ... new ball", p.24)
- 54/55 (Willes, ch.2 p.26)
- 56 ("probably resulted", 1810 Beauclerk/Lambert, p.29)
- 58 (ch.6 p.75 quote)
- 59 ("designed to help the bowler", p.29)
- 70 (Knight/Ward May 1828, p.28)
- 72 ("restraint on the New style was insisted on", p.29)
- 74 ("came to a head in 1834", p.28/29)
- 76 ("selling of matches", p.19-20)
- 78 ("burlesque", "primarily directed", ch.4 p.55)
- 84 ("pin prick", p.33)
- 87 ("all directed towards", p.32)
- 89 (Denison/Mynn, p.32-33)
- 90 ("full assault", p.33)
- 97 ("immediately preceding", p.35)
- 100 ("forced the issue", p.37)
- 101 ("clearly designed to help the bowlers", p.39)
- 102 (County Secretaries, p.39)
- u1-u3 ("by defining terms, supplying omissions, and better wording", p.42)
- u4 (Lord Harris amendment, p.42)
- 108/116 ("designed to save time", p.52)
- 113 (either umpire / throwing, p.49)
- 114 (Australia, Old Trafford 1899, p.55)
- 117 (Thoms 1888, "good judges ... a mistake", p.52)
- 122 ("unwittingly provided an admirable trial", p.52)
- 125 ("extensive trials at home and overseas", p.53)
- 128 (Lyttelton, pitches, p.49-51)
- 129 ("actual experience", p.63)
- 130 ("elasticity", p.60)
- 131a ("one-sided", p.62)
- 131b (eight-ball over, Australia/South Africa, p.52)
- 135 ("unsatisfactory nature", p.62)
- 136/120 (Bradford League 1943, p.60)

Overreaches (LOW):

- **54a/55**: the rationale says "Rait Kerr's annotation". The handwriting's author is unknown; it is an annotation in the
  scanned copy. The printed (struck) text supports the round-arm reading, so the claim can rest on that instead. Reword to "the
  struck printed text and a handwritten annotation in the scanned copy".
- **99 secondary `STRUCTURAL/drafting_omission`**: the 1863 resolution failed for lack of due notice, which is a procedural
  failure, not an omission in drafting the Laws. Remove it or choose a procedural subtype.
- **101 secondary `EXTERNAL_FORCE/pitch_technology`**: p.39 says the change was "clearly designed to help the bowlers". The
  pitch-improvement passage that follows describes the later period, after over-arm bowling. The secondary is an inference and
  should have basis "inferred", or be dropped.

## Things verified OK

- Reproducibility: as described in the summary. `run_pipeline.sh` printed: `141 canonical main Laws ... 0 conflicts`,
  `TOTAL {...}`, `Counter({'unchecked': 850, 'supported': 451, 'suspect': 41})`, `recall 11/11`. `08_build_labels.py` printed:
  `459 labelled, 0 still unlabelled`.
- Gold: every printed page of the chronology was compared with the image. All serial numbers, dates and particulars match apart
  from L1, and all prior/later references match apart from L2.
  - Unusual reference cases are transcribed exactly as printed: 5 (25; 47), 9 (28; 60), 13a (30, 41, 51), 14a (31, 108),
    27 (7, 11 / 52, 53), 63 (52, 53 / 1947), 80a (71/89 and 74/90), 121 (114, 119 / 123, 124), 130 (47, 122), and 112/113/125/128
    using years 1884/1947.
  - The unnumbered 1884 items (u1a-u6, including the u1a/u1b split at the "49 112" line) and the 1947 items (u1-u5) match the
    page. So do serials 4, 13, 20, 32, 80, 89, 99, 120, 121 and 128.
  - Handwriting is handled well. On p.74 (image00103) the long marginal note ("insert in Bold against marginal heading", Buckley
    / Morning Herald 1 June 1809 ... "vide Chapter 2") is transcribed accurately on serial 52. The struck-through sentences of
    54 and 55 are captured in `struck_text` and kept out of the particulars. On p.75 (image00104) the inserted note "In September
    of the same year The Leeds' Mercury referred to the changes as ones 'which seem to be generally adopted'" is captured on the
    "Before 1821" row (inner quote marks omitted). image00105 (p.76) has no handwriting.
  - `_gold_finalise` QA: no missing serials and no dangling references. The 2 non-reciprocal references (53->63, 81->92) are as
    printed.
- Law identity spot checks: Caught is 16 (1835-57), 22 (1884-1939), 35 (1947-68), 32 (1980-2010) and 33 (2017-19), which matches
  CLAUDE.md. The Wide Ball lineage and 1947 Law 28/29 match the ACS 1947 transcription. 1962 Law 46 exists in the nodes, so the
  README statement "1962 is missing Law 46 in segmentation" is out of date.
- Each edition's raw OCR files exist where 07 looks for them (1939a/b handled).
- The 03 gold regexes hit for all 11 entries (lenient, as documented).

## Residual risks

- No pre-1947 event labels exist, and the 1939->1947 pair (the 1947 recode) is excluded from `08_build_labels.py` by
  `FIRST_YEAR=1947`. Its causes exist only in Rait Kerr's drafts.
- H1-H4 mean the recall of real changes is unknown. The 11/11 gold recall covers only a few pairs and is lenient. Pre-1947 gold
  recall should be extended to all 138 serials, and the edit types behind H1/H2 (modal changes, notes) should be checked
  specifically.
- The edition-to-printing mismatch and the AI clean-up artefacts (documented) remain the dominant data risk. The numeric
  audit (M3, H4) is too weak to catch them reliably.
- I did not re-review the hand labels in `labels/p*.py` (outside scope A).
- Probe scripts used: `/tmp/rc_probe1-6.py`, `/tmp/rc_rk.py`. Pre-run snapshot: `/tmp/rc_snapshot/`.
