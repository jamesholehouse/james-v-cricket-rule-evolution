# Verification E: third pass (round-3 changes)

Read-only review. The only project file written is this report. All scripts were run on a copy in a scratch directory.
`run_pipeline.sh` + `08_build_labels.py` on the copy reproduce `data/changes/`, `data/events/`, `labels/keys.json` and
`post1947_event_labels.csv` byte-for-byte (gold recall 11/11; 555 labelled, 0 unlabelled). Event ids below are **current**
ids. Where a D-report id has since shifted, the label is identified by its `label_ref`.

## Verdict summary

| Scope | Result |
|---|---|
| D items re-checked | 27 FIXED, 7 PARTLY, 9 NOT FIXED. 1 D item was a false alarm (2010_2017_E065). |
| MCC 2019 list (22 changes) | 22/22 have an event and a fitting label. |
| Schema/consistency | 0 taxonomy, basis or source-id violations; 0 duplicate event_id/sig; counts in README/CONTINUATION (555, 0 unlabelled) match. 16 rows have `?` in `label_ref` (builder bug). |
| Random sample, 40 rows (seed 20261027) | 33 correct, 6 minor issue, 1 wrong. |
| New errors found | 1 HIGH, 5 MEDIUM, 11 LOW. |

Most serious:
1. **HIGH: 2010_2017_E095 hides the 2017 fake-fielding and distraction-penalty changes.** Its 16 records include "distract, **deceive** or obstruct" (0525, 0526, 0527) and "award 5 Penalty runs" on the first instance of deliberate distraction (0522, 0523). They also include the ball-tampering procedure ("ask the captain of the opposing side if he/she would like the ball to be replaced", 0517; "any further instance **in the match by that team**" instead of "in that innings", 0520) and "the ball shall not count as one of the over" (0598). The label describes only the drying cloth (Law 41.3). The words "'deception' added to the distraction clause" sit instead on **2010_2017_E047**, a one-record event (0751, a removed "(Umpire calling and signalling Dead ball)" pointer in Law 22) labelled STRUCTURAL/consequential. This problem predates round 3, but reports A-D missed it.
2. **MEDIUM: the classifier still drops real one-phrase changes before labelling.** They are classed `minor_wording`, are in no event and get no label (section 1).
3. **MEDIUM: 2017_2019_E022 ("may" -> "must" call Over) is probably an AI clean-up invention.** The raw 2019 OCR reads "he/she rr" (2019_raw l.1332), and raw 2017 reads "ma>" (l.1330). The change is not on MCC's 22-item list. It is labelled UNCATEGORISED with `integrity=ok` as if it were real.

---

## 1. `_textclass.py` round-3 rules: false-negative hunt

**What I scanned.** Every post-1947 `modify` record was re-classified with the current code. In-event and not-in-event counts:
`ocr_noise` 26 (all in no event), `minor_wording` 265 not in event, `format_only` 508 not in event, `numbering_only` 11 (all in
events), `xref_change` 78 in no event (all in 2010_2017, by design).

**`ocr_noise`.** I inspected all 26. All are genuine OCR or typo noise: docs/does, arc/are, pased, froi, becaus, penally, taxe, inninas,
batman, stateo, pitcte. Three pair two real words but are still errors in context: 1980_1992_0028 "partial or complex" (Throw
definition), 1980_1992_0043 "repeal/repeat the above procedure", and 2017_2019_0088 "Executive of the offend side". **No false
negatives on real data.** The tightened rule (same first letter, rare <= 15, 25x rarer) now classes hat/bat, caught/bought,
field/outfield and captains/umpires as `substantive`. Remaining adversarial misses:

| old -> new | class |
|---|---|
| "the ball is wide" -> "wider" | ocr_noise ("wider" has frequency 0, so any unseen inflection of a frequent word is noise) |
| "the striker" -> "the non-striker" | minor_wording (hyphen joining gives 'nonstriker', ratio 0.82 >= 0.8, so it is not a "swap") |
| "if a batsman retires hurt" -> "retires" | minor_wording (one content word deleted; the threshold is 2) |
| "he shall be given out" -> "given in" | minor_wording ('in' is a STOP word, so the swap check is skipped) |
| "in the circumstances of (a) above" -> "(b) above"; "under 2(a)" -> "2(b)"; "conditions (a), (b) and (c)" -> "(a) and (c)" | format_only |
| "Law 33 (Handled the ball)" -> "Law 34 (Hit the ball twice)" | xref_change, with no word tokens (REFS strips titles of up to 60 chars). This is not substantive in 2010_2017. |

**Real changes still hidden (`minor_wording`, no event, no label).** From all 265 records:

| Record | Old -> new | Note |
|---|---|---|
| 2010_2017_0589 | "It is unfair to cause deliberate damage to the pitch" -> "deliberate **or avoidable** damage" | Widens the offence. E097 covers the batsman paragraphs only. |
| 2010_2017_0318 | "a serious injury" -> "a **possibly** serious injury" (dead-ball trigger) | Lowers the threshold. |
| 2010_2017_0537 | "This caution shall apply throughout the innings" -> "shall apply **to that bowler** throughout the innings" | Narrows the caution. |
| 2008_2010_0344 | "if a fielder pulls a stump out" -> "if a fielder **strikes or** pulls a stump out" | Extends the put-down rule. MCC re-amended it in 2019 (#9). |
| 2008_2010_0213 | "inform **the batsmen**, the captain of the fielding side ..." -> "inform the captain ..." | D flagged this. NOT FIXED. |
| 2000_2008_0105 | Stumped (iv): "his wicket is put down by the wicket-keeper" -> "is **fairly** put down" | Minor, but it is a qualifier. |
| 2008_2010_0320 | Wide: "to be able to hit it **with his bat** by means of a normal cricket stroke" -> qualifier dropped | Low. |

I checked the rest; they are plurals, articles, OCR garble or pronoun/gender changes. Several umpire/umpires flips reverse in the
next edition (1947_1952_0079/0080, 1952_1962_0020, then 1962_1968_0024), which points to transcription noise rather than real changes.

**List-label stripping.** `toks()` drops every single letter and the roman numerals i-x. It can hide real changes:
- Sub-item cross-references:
  - 2000_2008_0051 "42.5(b)(iii)" -> "42.5(b)(iv)" is `format_only` and in no event.
  - 2008_2010_0240 and 0243 "Law 18.12(a)" -> "Law 18.12(b)" are `format_only`.
  - 2008_2010_0068 "as specified in 6(d) below" -> "in 6 below" is `format_only`.

  `ref_sig()` only compares the numeric part, so a letter-only change is invisible. On real data these are all consequential (LOW).
- The unit letter "m" is dropped. The 2017 "8.81 m" -> 2019 "8.81 in" records (2017_2019_0002, 0005, 0007) are now `minor_wording`
  and in no event, so the labels p2017_2019:E048/E049 (`cleaning_artefact_numeric`, the 2017 "m" OCR misread) are orphaned. The
  DATA_INTEGRITY table (row "2017") and its intro still say this artefact "is recorded as NOT_A_CHANGE / cleaning_artefact_numeric
  labels". For the 2017 women's "8.25 m" this is no longer true anywhere. The 2017 men's ball survives only inside 2010_2017_E091.
- Code defect: `... or x in ("a", "i") and False` in `toks()` is dead code (`and False`), so 'a' and 'i' are always dropped. This is
  harmless for 'a', which is a STOP word.
- Side effect of the hyphenation join: "Weight, from" -> "Weight- from" becomes 'weightfrom', which makes 2017_2019_0006 `substantive`.
  It needed a hand label (nd2017_2019 E054). LOW.

**`xref_change`.** This correctly surfaces 1952_1962_0012, 2017_2019_0098 and 0146. Excluding pair 2010_2017 hides 78 records. I
checked 0417, 0436, 0461, 0220, 0337 and 0181: all are consequential (Handled the ball merger, renumbering, the helmet change), so
nothing real is lost.

## 2. D items marked NOT FIXED / PARTLY / WRONGLY FIXED (plus D's other open points)

| D item | Current row | Verdict | Evidence |
|---|---|---|---|
| B 1947_1952 E006 (rationale "moves into a Note") | 1947_1952_E006 | FIXED | Rationale: "Note 2 on Law 1 is replaced by the new Note ...". |
| B 1952_1962 E011 (two layers, unsplit, duplicated) | 1952_1962_E015 (p:E011) + E016 (n:E013) | PARTLY | Still one event. "The captain shall take the bowler off as directed" is described in both rows. |
| B 1968_1980 E063 (dispense bails, junior wickets) | 1968_1980_E063 | FIXED | what_changed: "the decision to dispense with bails passes from the captains to the umpires, and junior-cricket wicket dimensions (width 8 inches) are added"; secondary UNCATEGORISED. (`integrity=ok` although the row records the 1968 '4 5/16' artefact.) |
| B 1947_1952_0016 "the West Indies" | 1947_1952_E002 | FIXED | Now in what_changed. |
| B 1952_1962_0012 (Laws 14 and 15 -> Law 14) | 1952_1962_E003 (nc) | FIXED | UNCATEGORISED, secondary consequential, ACS date 1 May 1957. |
| B 1947_1952_0081 (Law 27 -> 25) | 1947_1952_E028 (nc) | FIXED (has a label) / **label wrong** | See section 3. |
| C 2017_2019 E055 (41.9 alignment) | 2017_2019_E061 | FIXED | No contradiction; no "(see E050)". |
| C 21.6 secondary `technology` | 2017_2019_E033 | FIXED | Secondary EXTERNAL_FORCE with empty subtype (valid, but uninformative; same for E063). |
| C 2000_2008 E026/E028 | E026, E028 | FIXED | Specific OCR and cross-reference descriptions. |
| C 2008_2010 E031 (merge, WRONGLY FIXED) | 2008_2010_E029 | PARTLY | Primary is now UNCATEGORISED (real change). The rationale still ends "This change is a rewording that leaves the rule as it was" and the secondary is STRUCTURAL/wording_only. |
| C 2008_2010 E059 (merge, WRONGLY FIXED) | 2008_2010_E058 | PARTLY | Same pattern. |
| C 2008_2010 E072/E099 mismatch (WRONGLY FIXED) | E073 (Law 32), E096 (Law 42) | FIXED | E073 describes the "designated a boundary by the umpires before the toss" catch rule. E096 carries the avoidable-damage and protected-area definitions. |
| C 2010_2017 E006 | 2010_2017_E007 | FIXED | Covers default reversal stated ("shall not be completely covered" -> "shall be covered"). |
| C E009 (NOT FIXED) | 2010_2017_E009 (merged) | FIXED | UNCATEGORISED, "2 to 3 minutes ... extended to the lunch interval ... umpires determine". Record 0176 is now also labelled in E010 (duplicate, LOW). |
| C E010 (NOT FIXED) | 2010_2017_E011 | FIXED | "'less than 2 minutes' becoming 'less than 3 minutes'"; UNCATEGORISED. |
| C E027 | 2010_2017_E028 | FIXED | "the rule already existed in Law 37.5 of the 2010 text and is relocated". |
| C E072 | 2010_2017_E079 | FIXED | Primary clarification, stated on S03 (2013 boundary-catch rewrite), plus secondary UNCATEGORISED for the helmet change. |
| C E090 | 2010_2017_E096 (merged) | FIXED | Primary UNCATEGORISED. |
| C E074, E075 (NOT FIXED) | 2010_2017_E081, E082 | FIXED | E081 mentions the Dead ball after a lawful second strike. E082 says the No-ball Hit-wicket exemption is "new in 2017", which overclaims (section 3). |
| C E083 "AI clean-up slip" (NOT FIXED) | 2010_2017_E091 | FIXED | "OCR misread kept in the text (raw 2010 l.587 reads '815/16 in/22.4cm')". |
| C E070 | 2010_2017_E077 | FIXED | S03 reason cited. |
| C E004 (UNCATEGORISED + ENJOYMENT secondary) | 2010_2017_E004 | NOT FIXED (LOW) | Still secondary ENJOYMENT/fairness_spirit with basis none. |
| C E104 ("consequential" for a removal) | 2010_2017_E111 | PARTLY (LOW) | Now "a removal, not only a renumbering", but still STRUCTURAL/reorganisation. The "Insufficient time to complete rolling" provision (0730/0731) is absent from the 2017 text. |
| C E035 ("Law 16.9") | 2010_2017_E037 | FIXED | "Law 12.9"; the 2017 text l.935 has "12.9 Conclusion of match". |
| MCC #1, #8, #11 | 2017_2019_E013, E034, E048 | FIXED | |
| D sec.2 wd: 2008_2010 "standing in a normal guard position" | 2008_2010_E056 | NOT FIXED (MEDIUM) | Still "the rule is unchanged in effect". The new wide test adds a second condition. |
| D sec.2 wd: "without appeal" | 2008_2010_E092 | NOT FIXED (LOW) | Still wording_only. |
| D sec.2 wd: "at the end of the match" | 2008_2010_E046 | NOT FIXED (LOW) | Still wording_only. |
| D sec.2: 2010_2017 "or by a fielder ... 29.1.1.5" | 2010_2017_E065 | Not a change | 2010's "as described in 1(a)" already included the fielder (28.1(a)(iv)). The D flag was a false alarm. |
| D: 2008_2010_0424 ("and 42.17(b)" removed) | 2008_2010_E084 | NOT FIXED (LOW) | The label "provision restated" does not mention it. |
| D: 2008_2010_0213 (batsmen no longer informed) | no event | NOT FIXED (LOW) | `minor_wording`. |
| drafts 54a/55 annotation | raitkerr_drafts | FIXED | The gold serial 52 `annotation` now holds the handwritten note naming 54, 55 and 56. |
| D basis: 1947_1952 E007/E009/E014/E015 | E007, E009, E014, E016 | FIXED | All `inferred`. |
| D basis: 1968_1980 E055; 1992_2000 E001/E051 | same | FIXED | `inferred`. |
| D basis: about 50 2010_2017 preface-`stated` labels | | PARTLY | 5 remain, each `stated` on the S02 preface or "MCC preface": 2010_2017_E002, E013 (nd), E041 (nd), E104 (p:E096), E108 (nc:E104). Three of these were written in round 3. |
| D: 41 rows "confirmed in ACS 1980 (S11)" | | FIXED | 0 rows. |
| D: E090 quotes S03 without citing it | 2010_2017_E091 | NOT FIXED (LOW) | The rationale quotes "MCC (2013, S03): the change 'confirms that it is now the Governing Body...'" but `evidence = S17;S01;S02`. |
| D: E101 "the need both to provide the umpires ..." as an MCC quote | 2010_2017_E102 | NOT FIXED (LOW) | Still presented as MCC wording; not in any local text. |
| D: S13 note | sources.csv | FIXED | |
| D: DATA_INTEGRITY intro ("recorded as cleaning_artefact_numeric") | | NOT FIXED (LOW) | Unchanged, and now also false for the 2017 "m" row (section 1). |
| D #1 merge-primary rule | builder | FIXED in code (`real()`), PARTLY in text | Contradictory "leaves the rule as it was" text survives in merged rows 2008_2010_E029, E058, E072, E077. |
| D #2 secondary-subtype validation | builder | FIXED | `check()` asserts it. |
| D #3 stale cross-references | | PARTLY | 1947_1952_E023 "the new Note in E016" (the Law 37 Note is E018; E016 is Law 34). 2010_2017_E002 "limits are in E095" (they are in E103; E095 is Law 41). Both use the p-file id space. |
| D #5 README "40 of 136" | README l.49 | FIXED | "41 of 157". |
| D #6 duplicate description | 1952_1962_E015/E016 | NOT FIXED (LOW) | |

## 3. Round-3 and other targeted labels against the texts

nc/nd modules (all 16 labels checked against their records):

| Label -> row | Verdict | Evidence |
|---|---|---|
| nc1947_1952 E028 -> 1947_1952_E028 | **Wrong rationale (MEDIUM)** | Rationale: "The Law on the over was renumbered in the 1947 Code". Law 25 is "Dead" ball and Law 27 is No ball in **both** the 1947 text (l.157, 215) and the 1952 text (l.152, 212). The ACS 1st-edition transcription already reads "Under Law 25 the ball is 'Dead' on 'Over' being called" (acs_1947.txt l.866), while the raw 1947 OCR reads "Law 27" (l.1198). This is a misprint or transcription error in the dataset's 1947 copy corrected in 1952, not a consequential renumbering. It should be NOT_A_CHANGE or an erratum (drafting fix) with that rationale. |
| nc1947_1952 E035 -> E035 | Minor issue | "the stray reference 'Law 46, Note (5)' is removed": 1952 still has "Law 46, Note 5 (i) is applicable in such cases" (1952_processed l.721). This is a segmentation/notation artefact, not a removal. |
| nc1952_1962 E003 | Correct | |
| nc1962_1968 E005 | Correct | ACS 1st edition "Law 10, Note 3"; ACS 4th edition "Note 2". |
| nc1980_1992 E004 | Correct | |
| nc2010_2017 E067 -> E071 | Correct | |
| nc2010_2017 E104 -> E108 | Correct content; basis `stated` on the preface (LOW) | |
| nc2017_2019 E017, E026 | Correct | |
| nc2017_2019 E050 -> E048 | Correct | S04 l.215 quote verified. |
| nd2010_2017 E010 | Correct | 0176 "captains and umpires shall agree" -> "umpires shall determine". Also described in the merged 2010_2017_E009 (duplicate). |
| nd2010_2017 E013, E041 | Correct content; basis `stated` on the preface (LOW) | |
| nd2010_2017 E040 | Minor issue | "a new dead-ball item 'satisfied that the ball in play cannot be recovered'": this is the former Lost-ball Law folded into Dead ball (E037 says "Lost ball is folded in"), not new. |
| nd2017_2019 E054 | Correct | |

p2010_2017 rewrites (E006, E009, E010, E027, E072, E074, E075, E083, E090, E070, E104, E035): see section 2. The only remaining problems
are E075 -> 2010_2017_E082 and E104 -> E111. **E082** says the striker "is not out Hit wicket if the delivery is a No ball (new in 2017)",
but 2010 Law 24.15 already allowed dismissal off a No ball only under Laws 33, 34, 37 and 38 (2010_processed l.1990-1993). The explicit
listing in Law 35 is new; the rule is not (LOW). E111 is covered in section 2.

p1968_1980 E063 is FIXED. E055 is `inferred` (FIXED), but its secondary ENJOYMENT/fairness_spirit carries no stated cause. p1947_1952
basis changes are FIXED: E007, E009, E014, E016 and E018 are `inferred`, and E005 stays `stated` on the verified S09 quote.

Other label errors found while checking:

| Row | Severity | Problem |
|---|---|---|
| 2010_2017_E095 | HIGH | See the summary. 16 records: fake fielding (0525-0527), first-instance 5 penalty runs for distraction (0522/0523), tampering procedure (0517, 0520), 0598. The label covers only 0516 (drying cloth). |
| 2010_2017_E047 | MEDIUM | "'deception' added to the distraction clause" is attached to a one-record Law 22 pointer removal (0751). |
| 2017_2019_E022 | MEDIUM | "may" -> "must" is unsupported by raw OCR (2019 "rr"). It should be `integrity=suspect` (likely NOT_A_CHANGE/cleaning artefact). |
| 2010_2017_E002 | LOW-MED | A "new Type D bat category" and the removal of the Type B/C level rule (0840-0842) sit under STRUCTURAL/reorganisation with basis `stated` (preface) and no UNCATEGORISED secondary, against the CLAUDE.md rule "a restructure label must not hide a policy change". Stale "E095". |
| 2000_2008_E020 (merged) | LOW | The primary is STRUCTURAL/consequential, but its own text says "a closed list of Laws is replaced by all Laws, which broadens the rule" with no source. That makes it a real change, so the primary should be UNCATEGORISED. |
| 2010_2017_E039 (merged) | LOW | Primary terminology. The merged part (dead ball if the bowler does not release, S03) is a stated clarification that loses its own category, because merge only adds a secondary when categories differ. |

## 4. MCC 2019 list (S04, 22 changes)

| # | Change | Row | Label |
|---|---|---|---|
| 1 | Preamble umpires -> match officials | E013 | STRUCTURAL/terminology, stated S04 |
| 2 | 11.2.2 | E014 | clarification, stated |
| 3 | 15.1 declared innings completed | E018 | codification_definition, stated |
| 4 | 16.3.3 | E019 | consequential, stated |
| 5 | 16.7 | E021 | clarification, stated |
| 6 | 18.6 | E024 | codification_definition, stated |
| 7 | 21.6 | E033 | consequential, stated (+EXTERNAL_FORCE, empty subtype) |
| 8 | 21.12 | E034 | ENJOYMENT/fairness_spirit, stated ("It was felt that this was unfair") |
| 9 | 29.1 | E043 | clarification, stated |
| 10 | 30.1 | E047 | clarification, stated |
| 11 | 33.4 | E048 | clarification, stated |
| 12 | 34.3 | E049 | ENJOYMENT/fairness_spirit, inferred |
| 13 | 37.3 | E050 | ENJOYMENT/fairness_spirit, inferred |
| 14, 15 | 39.3.1, 39.3.2 | E053 | clarification, stated (both in one event) |
| 16 | 41.2/41.19 | E055 + E061 | consolidation_merge, stated |
| 17 | 41.7 | E059 (+E060) | ENJOYMENT/fairness + EXTERNAL_FORCE/medical_safety, stated |
| 18 | 41.16 | E063 | clarification, stated (+EXTERNAL_FORCE, empty subtype) |
| 19 | 42.1 | E064 | ENJOYMENT/fairness_spirit, stated |
| 20 | 42.4.2.3.2 | E065 | clarification, stated |
| 21 | 42.7 | E066 | ENJOYMENT/fairness_spirit, stated |
| 22 | Appendix A waist | E001 | clarification, stated |

All 22 are present and correctly labelled.

## 5. Schema and consistency

- 555 rows. Categories: STRUCTURAL 257, UNCATEGORISED 170, NOT_A_CHANGE 107, ENJOYMENT 12, EXTERNAL_FORCE 8, NOVEL_EVENT 1. 555 events in `data/events` for the 10 pairs; `unlabelled_events.csv` is empty. The README and CONTINUATION figure (555, 0 unlabelled) matches; 170/555 = 30.6% UNCATEGORISED matches "about 30%".
- Every primary and secondary subtype is in `taxonomy_v0.json`. UNCATEGORISED always has basis `none`; NOT_A_CHANGE always `derived`. Every evidence id is in `sources.csv`. There are no duplicate event_ids or sigs.
- **`label_ref` contains `?` in 16 merged rows** (e.g. 2008_2010_E048 `n2008_2010:E048+?+?`, 2010_2017_E009 `n2010_2017:E008+?+?`, 2017_2019_E030 `?+nb2017_2019:E034`). Cause: in `resolve()`, `l["_ref"]` is set only on the non-merge path, so the label arriving second has no `_ref` when `merge_labels` runs. The merge notice also prints a self-reference ("2000_2008:E022: merged with 2000_2008:E022") whenever the arriving label wins.
- Stale docs:
  - README l.19 still says "A smaller second verification ... is still to be run".
  - CLAUDE.md l.113 says "Three Opus verification reports" (there are four, five with this one).
  - The DATA_INTEGRITY intro claim is covered in section 2.

## 6. Merged rows and orphaned labels

**Merged rows (15).** Judgement of each primary:

| Row | Judgement |
|---|---|
| 2008_2010_E029, E058, E072, E077 | Primary correct (UNCATEGORISED). The secondary text "rewording that leaves the rule as it was" contradicts it. |
| 2008_2010_E048 | OK (clarification; wicket -> end is equivalent). |
| 2008_2010_E049 | OK (codification + UNCATEGORISED secondary). |
| 2010_2017_E009, E034, E091, E096 | OK (UNCATEGORISED primary). |
| 2010_2017_E033, 2017_2019_E030, 2017_2019_E060 | OK. |
| 2010_2017_E039 | Acceptable; the stated S03 clarification is absorbed without its own category. |
| 2000_2008_E020 | Wrong primary (see section 3). |

**Orphans (17).** None dropped a real change:

| Orphaned label | Why nothing real was lost |
|---|---|
| 1947_1952:n:E010, 1952_1962:n:E007 | docs/arc OCR; records 0033/0030 are `minor_wording` in no event. |
| 1947_1952:E029 | Drier-sentence move (relocation; E034 still has the other half). |
| 1962_1968:E014, 1980_1992:E021, E022, 2000_2008:E050 | Notation only; records `format_only`. |
| 1992_2000:E043, E044 | Law 38 restatements; covered by the 1992_2000_E044 Law 38 rewrite label. |
| 2000_2008:E025 | Covered by n2000_2008:E024 on the same records. |
| 2008_2010:E022 | Deputising already existed via 2008 Law 3, record 0615 (D). |
| 2010_2017:n:E047 | Cross-reference only. |
| 2010_2017:E058 | Records 0400/0403 are in labelled E065. |
| 2017_2019:nb:E028, nb:E030 | 2019 OCR garble. |
| **2017_2019:E048, E049** | No rule change lost, but the documented 2017 "m"-for-"in" integrity artefact now has no row (section 1). |

## 7. Independent quality estimate: random 40 (seed 20261027)

- **Correct, 33:** 1980_1992_E015; 1952_1962_E013, E003; 1992_2000_E035, E017, E045; 2010_2017_E043, E055, E056, E068, E018; 1968_1980_E026, E003, E012, E043, E008; 2000_2008_E016, E022, E045, E003, E049; 1947_1952_E027, E029, E012; 2017_2019_E017, E019, E009, E067; 2008_2010_E064, E002, E043, E006, E041.
- **Minor issue, 6:**

| Row | Issue |
|---|---|
| 1968_1980_E055 | ENJOYMENT secondary without a stated cause; the new captains' responsibility is filed under consolidation. |
| 1992_2000_E032 | Umpire arrival 30 -> 45 minutes before the start and the new "not changed ... unless injured or ill" are not named in what_changed (only the secondary UNCATEGORISED signals them). |
| 1992_2000_E052 | New "not likely to cause unacceptable damage to the ball" covering requirement not named. |
| 1992_2000_E033 | New "not out Bowled if the ball touched another player or an umpire" not named. |
| 2010_2017_E042 | NOVEL_EVENT/single_incident (Finn) is the primary for a bundle that also holds the underarm No ball, caution -> warning and front-foot changes. |
| 2010_2017_E002 | Type D bat under reorganisation/stated; stale E095. |

- **Wrong, 1:** 2008_2010_E056 (normal-guard-position wide test labelled "rule unchanged").

On this sample about 82% are fully correct (95% CI roughly 68-92%) and about 2.5% are wrong. The targeted errors in section 3, especially
2010_2017_E095, show that big multi-record events in the rewrite pairs are where under-description concentrates, and the random
sample under-represents them.

## Not verified

- Web-only sources: S06 (the E102 "need both" quote), S07, S14, S15 and live S22.
- The real MCC 2019 wording of Law 17.5.2 (I inferred the E022 artefact from raw OCR plus the 2026 4th-edition "shall").
- Whether the dataset's 1947 printing truly read "Law 27" (raw OCR says so; ACS says "Law 25").
- Large rewrite events (1968_1980, 1992_2000, 2008_2010, 2010_2017) beyond the rows named here. I read only the first 7 records of each
  sampled event.
