# Verification D: second pass over the applied fixes (reports A, B and C)

Read-only review. The only file written is this report. I ran the builder (`08_build_labels.py`) and the gold rebuild
(`build_gold.sh` steps) on a copy in a scratch directory. The copy's label CSV is byte-identical to
`data/categories/post1947_event_labels.csv`, and the rebuilt gold CSV is byte-identical to `data/gold/raitkerr_chronology.csv`.
Event ids below are the **current** ones. Report B/C ids are given as `B:`/`C:` and were resolved to current events by record
overlap with the builder's own `resolve()`.

## Verdict summary

| Verdict | Count | Scope |
|---|---|---|
| FIXED | 108 | B problem labels 53, B uncovered changes 4, C 2017_2019 9, C 2000_2008 6, C 2008_2010 23, C 2010_2017 9, MCC 2019 mapping 4 |
| PARTLY | 11 | |
| NOT FIXED | 12 | |
| WRONGLY FIXED | 3 | 2008_2010 (merge logic x2, and a hidden-change text attached to the wrong Law) |
| N/A | 1 | B 1962_1968:E014 (that event no longer exists) |

**New errors found: 12 distinct problems.** The two most serious:

1. **HIGH.** The text classifier (`_textclass.py`) still hides real changes, and records it rates `format_only` or `minor_wording` are
   **never grouped into events, so they are never labelled**. This hides 3 of MCC's 22 listed 2019 changes:
   - #1, Preamble "umpires" -> "match officials" (record 2017_2019_0001, `minor_wording`, in no event).
   - #8, Law 21.12 (2017_2019_0098, `format_only`, in no event).
   - #11, Law 33.4 (2017_2019_0146, `format_only`, in no event).

   It also hides B's 1957 Law 16 consequential change (1952_1962_0012). Across the 10 post-1947 pairs, 345 `minor_wording`,
   571 `format_only` and 58 `ocr_noise` modify-records sit in no event.
2. **HIGH.** The builder's merge rule ranks a categorised label above an UNCATEGORISED one. When a corrected "real change" label
   and an old `wd()` "rewording that leaves the rule as it was" label land on the same event, the wrong one becomes primary. This
   happens in 2008_2010_E029, E060 and E074, and each row asserts both "rule unchanged" and "hides substantive rule changes".

The other new errors are medium or low severity: an out-of-taxonomy `secondary_subtype`, an `ocr_noise` rule that swallows real
one-word swaps, stale event cross-references, `basis=stated` still used for whole-revision prefaces in about 55 labels, and a few
doc counts. Overall, the targeted high-severity fixes from B and C were mostly applied correctly: Law 41.16, 42.4.2.3, the
front-foot no-ball, Mongoose, Finn, tethered bails, the 1952 dating and the full-pitch LBW change. The remaining risk is
systemic (the classifier, the triage of unevented records, the merge logic), not individual labels.

---

## 1. B and C problem rows: status

### Priority items named in the brief

| Item | Current event | Verdict | Evidence |
|---|---|---|---|
| 2017_2019 Law 41.16 rewrite (C:E057) | 2017_2019_E058 | FIXED | STRUCTURAL/clarification_umpire_workability, stated, S04 "principally on the back of TV replays". The notes say "Event mixes the 41.16 rewrite with 41.15 segmentation". The 41.15-only records are now E057, labelled segmentation (records 0194/0354, a "5 ft/" + "m in front" split): correct. **But** `secondary_subtype = technology` is not an EXTERNAL_FORCE subtype in `taxonomy_v0.json` (see section 6). what_changed says "(see E050)", but E050 is now a mechanical format artefact; the 41.2 rewrite is E049. |
| 2017_2019 42.4.2.3 (C:E060) | 2017_2019_E060 | FIXED | "part-over sentence ... inserted into 42.4.2.3.1 ... MCC change 42.4.2.3.2", stated, S04. |
| 1968_1980 front-foot no-ball (B:E028) | E028 | FIXED | "KEY CHANGE: the foot-fault test switches ... to the FRONT-FOOT rule". UNCATEGORISED with consolidation as secondary. The 1980 processed text l.806 has "some part of the front foot". |
| 1968_1980 20-over last hour (B:E014) | E014 | FIXED | "a minimum of 20 six-ball (15 eight-ball) overs must be bowled in the last hour". Present in 1980 text l.423-426. |
| 1968_1980 leg-bye (B:E030) | E030 | FIXED | "'tried to avoid being hit by the ball'" (1980 l.933). |
| 1968_1980 ground/weather/light (B:E036) | E036 | FIXED | "umpires become the sole judges ...". UNCATEGORISED. |
| 1968_1980 helmet catches (B:E043) | E043 | FIXED | "new protective-helmet rules". These are in the dataset 1980 text (l.741, 1082, 1093), so no S11 dating problem. |
| 1980_1992 LBW full-pitch (B:E012) | 1980_1992_E009 | FIXED | UNCATEGORISED: "no longer has to be one that 'would have pitched in a straight line'". |
| Mongoose / Law 6 (C:E003/E048) | 2000_2008_E003, E051 | FIXED | UNCATEGORISED, basis none. "S22 ... says only that the Mongoose bats 'conform to the new version of Law 6' ... MCC tested and approved the Mongoose in 2009, after the new Law". |
| Finn law (C:2010_2017 E037) | 2010_2017_E041 | FIXED | NOVEL_EVENT/single_incident, stated, S07+S03. The S03 quote is verified in the local text. The S07 quote "provides clarity ... removes the need for a subjective assessment" is web-only; I could not verify it. |
| Tethered bails (C:E102) | 2010_2017_E109 | FIXED | EXTERNAL_FORCE/medical_safety, stated on the Law text. "Devices aimed at protecting player safety by limiting the distance that a bail can travel" is present in S02 l.495 and in 2017 processed l.498. The Boucher sentence is now credited to the writer, not MCC. |
| 1947_1952 Law 30 kicking Note dated 1952 (B:E011/E026) | 1947_1952_E010, E024 | FIXED | date_evidence "Wording of the 2nd edition as adopted 7 May 1952 (ACS 'Original Law 30')". This is confirmed by acs_1947_second_edition.txt l.591-595 ("Original Law 30 ... shall immediately call "Dead Ball" ... touching a raised knee"). The 1954 body change "hand holding the bat" is now in 1952_1962_E008 (record 1952_1962_0036). |

### Report B, remaining rows

| B row | Current | Verdict | Reason |
|---|---|---|---|
| 1947_1952 E005 | E005 | FIXED | Stated, S09 quote verified (acs_1947.txt l.237). Minor: the subtype `codification_definition` fits poorly for a local variation being abolished. |
| E010 | E009 | FIXED (1954 clause dropped) | But it is `basis=stated` with no source stating a cause (see section 4). |
| E013, E012, E031 | E012, E011, E030 | FIXED | |
| E006 | E006 | PARTLY | what_changed now says Note 2 on Law 1, but the rationale still says "The same idea moves from the Law's body into a Note". |
| 1952_1962 E002, E004, E008, E010, E003 | same ids | FIXED | |
| E011 | E012 | PARTLY | Two layers are described in the rationale, but the event is not split. The primary is still STRUCTURAL/notes_revision. The undated sentence is also labelled separately as n-label E013, so the same change is described twice. |
| E013, E014, E016 | E014, E016, E018 | FIXED | |
| 1962_1968 E014 | (orphan) | N/A | The ball-notation event no longer exists. The integrity point is in the DATA_INTEGRITY table (1968 "correct by luck"). |
| 1968_1980 E017, E020, E056, E029, E032, E053, E015, E047, E050, E002, E013, E033, E048, E061 | same ids | FIXED | E013 mentions tea/drinks only in the rationale, not in what_changed. |
| 1968_1980 E063 (in the E029... group) | E063 | **NOT FIXED** | what_changed lists only dimensions. Records 1968_1980_0031 ("captains may agree ... to dispense with ... bails" -> "the Umpires may decide") and 0371 (new "Junior Cricket ... Width - 8 inches") are in this event. There is no UNCATEGORISED secondary (the secondary is NOT_A_CHANGE with an empty subtype). |
| 1980_1992 E007, E014, E016, E010, E017 | E004, E011, E013, E007, E014 | FIXED | E004 gives the keep-wicket point in the rationale only. |
| 1992_2000 E018, E014, E006, E016, E021, E024, E032, E035, E036, E037, E041, E047, E050 | E019, E014, E006, E017, E022, E025, E033, E036, E037, E038, E042, E047, E050 | FIXED | All rewrites now carry secondary UNCATEGORISED plus a notes line. |

### Report B, real changes not covered

| B item | Verdict | Evidence |
|---|---|---|
| 1952_1962 "hand holding the bat" | FIXED | Record 1952_1962_0036 is in E008, which is labelled with it. |
| 1952_1962 E001 "Except in the United Kingdom" | FIXED | n1952_1962 E001. |
| 1947_1952 "the West Indies" (now record 1947_1952_0016) | PARTLY | The record is inside 1947_1952_E002, whose what_changed ("Rolling Note revised: normal rolling ... half an hour ...") does not mention it. Only the n1952_1962 E001 rationale mentions it in passing. |
| 1952_1962 Law 16 "Laws 14 and 15" -> "Law 14" (now 1952_1962_0012) | **NOT FIXED** | In no event. `_textclass.toks()` strips Law references (`REFS.sub`), so the record classifies as `format_only`. |
| 1980_1992 stumped "other than a protective helmet" | FIXED | n1980_1992 E012. |
| 1962_1968 drying "in the United Kingdom" | FIXED | n1962_1968 E013. |
| 1947_1952 Law 27 -> 25 (now 1947_1952_0081) | NOT FIXED (LOW) | In no event (`format_only` via REFS). |

### Report C, by pair

| C row | Current | Verdict | Reason / evidence |
|---|---|---|---|
| 2017_2019 E048, E049 | E047, E048 | FIXED | "OCR unit misread". The figures agree with raw: 2017_raw l.444 "8.81 m/22 4 cm"; 2019 processed l.283 "8.81 in". |
| E053 | E053 | FIXED | ENJOYMENT/fairness_spirit, with the S04 quotes. |
| E055 | E056 | PARTLY | The rationale now says "Alignment artefact ... stays in Law 41.9". what_changed still says the paragraph is "re-ordered into the rewritten Law 41.2", which contradicts it. The category is still STRUCTURAL/consolidation_merge (stated), and "(see E050)" is stale. |
| E029 (21.6) | E028 | FIXED | Secondary EXTERNAL_FORCE, but with the invalid subtype `technology`. |
| E043, E044, E021, E024 | E042, E043, E022, E025 | FIXED | |
| 2000_2008 E025, E051, E005, E010, E022 | E024 (n), E053, E005, E009, E020 | FIXED | |
| E012/E026/E027/E028 | | PARTLY | E012 and E027 are now format artefacts. E026 ("changed words: iv") and E028 ("changed words: ii") are still mechanical STRUCTURAL/wording_only. |
| 2008_2010 `wd()` basis | | FIXED | Now `inferred`. |
| E012, E036, E084, E011, E021, E025, E039, E040, E046, E047, E052, E053, E090, E092, E094, E074, E005, E006, E067, E055, E096, E098 | E013, E033, E088, E012, E020, E023, E038, E039, E045, E047, E053, E054, E094, E096, E098, E077, E006, E008, E069, E056, E101, E103 | FIXED | Spot-checked against the records. For example, E013 holds 0115 "in the presence of one or both of the umpires" and 0117 "As soon as the toss is completed". E033 holds 0771 "Ball beyond the boundary". E088 holds 0432 "left his ground to avoid injury". |
| **E031** | E029 (merged with C:E032) | **WRONGLY FIXED** | The primary is the old `wd()` label: STRUCTURAL/wording_only, rationale "This change is a rewording that leaves the rule as it was". The corrected text is only an "ALSO". The event holds 0216 ("disallow all runs ... other than the penalty for a No ball or Wide, or penalties under Laws 42.5 ... and 42.13" -> "other than any runs awarded for penalties"), a real change. |
| **E059** | E060 (merged with C:E060) | **WRONGLY FIXED** | Same mechanism: primary STRUCTURAL/wording_only "leaves the rule as it was"; the leg-bye rule change is demoted to secondary. |
| **E023/E033/E045/E049/E072/E095 (under-described)** | E021, E030, E044, E050, **E075**, E099 | **WRONGLY FIXED** | 2008_2010_E075 is Law 32 (Caught; records 0363-0368). Its what_changed says "ALSO a real rule change: new definitions of avoidable damage and of the protected area". Those definitions are Law 42 records (0517-0565, 0840-0841, all in **E099**), and E099's label does not mention them. C's descriptions were mapped onto the six events one position off: "designated a boundary by the umpires before the toss" is record 0367 in E075. |
| 2010_2017 E037, E102, E053, E002, E095 | E041, E109, E059, E002, E102 | FIXED | |
| E046/E048/E065/E071 "No reason stated" | E051, E053, E071, E077 | FIXED | The phrase is gone from the CSV and the labels. The E046 quote is now the article's wording with "[fielders]". |
| E091, E036, E015 | E097, E040, E014 | FIXED | |
| E006 | E006 | PARTLY | Now UNCATEGORISED, but what_changed still says covers rules are "restated". The default reversal C described is not stated. |
| **E009** | E009 | **NOT FIXED** | Still STRUCTURAL/consequential, stated, "'length' becomes 'duration'". The records in the event: 0171 "2 minutes" -> "3 minutes" and "For the lunch interval and for the tea interval"; 0172 "captains agree" -> "umpires determine"; 0176 "the captains and umpires shall agree" -> "the umpires shall determine". |
| **E010** | E010 | **NOT FIXED** | Still reorganisation, stated. Record 0185: "less than 2 minutes" -> "less than 3 minutes". |
| E027 | E026 | PARTLY | Re-categorised to consequential (inferred), but what_changed still says "new rule that if a batsman is dismissed Obstructing the field the batting side also scores ... runs". C showed that rule already existed in Law 37.5 (2010). |
| E072 | E078 | PARTLY | Secondary UNCATEGORISED added, but the primary is still EXTERNAL_FORCE/legal_social (stated) for an event whose substance is the boundary-catch rules. |
| E090 | E095 | PARTLY | Secondary UNCATEGORISED added. The primary is still reorganisation with basis `stated` from the whole-revision preface. |
| **E074, E075** | E080, E081 | **NOT FIXED** | Both still "consequential", stated (RE preface). The lawful-second-strike Dead-ball change and the new "not out Hit wicket if No ball" are not mentioned. |
| **E083** | E090 (merged) | **NOT FIXED** | The merged text still reads "The 2010 text's '8 15/16' was an AI clean-up slip" and "written 8.81 in. in 2017". Raw 2010 l.587 reads "815/16 in/22.4cm" (an OCR misread). 2017 processed l.285 reads "8.81 m". |
| E070, E004, E104 | E076, E004, E111 | NOT FIXED (LOW) | E070 still uses the generic preface rather than S03's 2013 reason. E004 still pairs an UNCATEGORISED primary with an ENJOYMENT secondary. E104 still calls a removal "consequential". |
| E035 | E037 | PARTLY (LOW) | The helmet and Lost-ball parts were added. The "Law 16.9" numbering slip remains (2017 is 12.9). |

### MCC 2019 mapping (C section 3, the items C marked not labelled)

| MCC # | Verdict | Evidence |
|---|---|---|
| 1 Preamble "umpires" -> "match officials" | **NOT FIXED** | Record 2017_2019_0001, class `minor_wording` (['umpires','match','officials']), in no event, so it has no label. |
| 2 11.2.2 | FIXED | E013, stated, S04. |
| 5 16.7 | FIXED | E020. |
| 8 21.12 | PARTLY | The text is attached by the merge to E028 (21.6), with a "consequential" primary. The 21.12 record itself (2017_2019_0098, "20.4.2.4 to 20.4.2.9" -> "20.4.2.4, 20.4.2.5, 20.4.2.6, 20.4.2.8 or 20.4.2.9") is `format_only` and in no event. |
| 9 29.1, 10 30.1 | FIXED | E037, E041. |
| 11 33.4 | **NOT FIXED** | Record 2017_2019_0146 ("Law 18.11.1 (Batsman returning to original end)" -> "Law 18.12.1 ...") is `format_only` (REFS stripping) and in no event. S04 l.215: "There was an incorrect cross-reference in Law 33.4, which referred back to Law 18.11 rather than 18.12". |

---

## 2. n-modules and the mechanical `ocr_noise` class

### Sample of n-labels checked against records (47 events)

I checked these against the old/new text in `data/changes`. The claim holds for:
- 2008_2010: E001, E007, E009, E010, E016, E017, E022, E026, E028, E031, E032, E035, E036, E042, E048, E049, E057, E061, E068,
  E076, E078, E081, E083, E084, E089, E092, E104.
- 2000_2008: E023, E024, E025, E030, E041, E052.
- 2010_2017: E017, E021, E055, E086, E099, E104.
- Earlier pairs: 1947_1952 E016; 1952_1962 E011; 1962_1968 E012; 1980_1992 E010; 1992_2000 E015, E043; 2017_2019 E021, E052.

Questionable "rule unchanged" claims (LOW-MEDIUM):

| Event | Claim | Text |
|---|---|---|
| 2008_2010_E058 (`wd`) | "rule is unchanged in effect" | 0319: "passes wide of the striker where he is **standing**" -> "where he is and which also would have passed wide of him standing in a normal guard position" (the 2010 text matches S01 l.1798). Dropping "standing" plausibly changes the judging position. |
| 2008_2010_E095 (`wd`) | same | 0459: "the umpires shall not interfere with the progress of play, except as required" -> "shall not interfere with the progress of play **without appeal** except as required". |
| 2008_2010_E046 (`wd`) | same | 0254: "as the result of an award of 5 penalty runs **at the end of the match**" -> qualifier dropped. |
| 2010_2017_E064 (`conseq`) | "cross-references renumbered" | 0401 adds "or by a fielder in the manner described in 29.1.1.5" to the no-bails rule. |

### `ocr_noise` scan

All 139 records in the whole dataset that classify as `ocr_noise` were inspected (pairs listed in the scratch output). Most are
genuine (docs/does, oft/off, arc/are, tho/the). False negatives from real data:

| Record | Old -> new | Problem |
|---|---|---|
| 1835_1857_0034 | "stop the ball with his **hat**" -> "with his **bat**" | Two real words; one edition's text is wrong (hat is historically right). `_noise_pair('hat','bat')` is True (freq 29 vs 1020, ratio 0.67). A text error is hidden as noise rather than flagged. |
| 2008_2010_0178 | "Practice on the **field**" -> "Practice on the **outfield**" | 'outfield' (freq 52) is treated as garbage for 'field' (662). Here it is a heading mismatch, but the rule would swallow a real field/outfield change. |
| 1962_1968_0056, 0114 | "fieldsmen" <-> "fieldsman" | A singular/plural swap is treated as noise. |
| 1962_1968_0128 | "results" -> "result" | Same. |

Adversarial tests of `classify()`:

| Old -> new | Class |
|---|---|
| may -> many; no -> on; dropping or adding 'not' | substantive (correct) |
| "his hat" -> "his bat"; "result" -> "results"; "fieldsman" -> "fieldsmen"; "wide" -> "wider"; "caught" -> "bought" | **ocr_noise** |
| "the **captains** shall decide" -> "the **umpires** shall decide" | **minor_wording** |
| "outside the **leg** stump" -> "**off** stump" | **minor_wording** |
| "the **bowling** crease" -> "the **popping** crease" (the 1980 front-foot change) | **minor_wording** |
| "the striker" -> "the non-striker" | **minor_wording** |
| "the **bowler's** end umpire" -> "the **striker's** end umpire" | **minor_wording** |
| "retires hurt" -> "retires" | **minor_wording** |

A `minor_wording` record outside an event is never labelled, and inside a small event it gets the mechanical "the rule is unchanged
in effect". Real examples in no event:
- 2017_2019_0001 (MCC change #1).
- 2008_2010_0213 ("inform the batsmen, the captain ..." -> "inform the captain ...").
- 2010_2017_0417 (Law 33 "Handled the ball" dropped from the list of Laws the striker remains subject to).
- 2008_2010_0261 ("from each wicket" -> "from each end").

Counts of records in no event (`minor_wording` / `format_only`):

| Pair | minor_wording | format_only |
|---|---|---|
| 1947_1952 | 24 | 30 |
| 1962_1968 | 23 | 88 |
| 2008_2010 | 127 | 110 |
| 2010_2017 | 89 | 79 |
| 2017_2019 | 28 | 150 |

The README's "every one of the 536 events ... carries a label" is true, but it is not "every change".

The REFS problem: `toks()` deletes Law/clause references, so any change in *which* Law is referred to is `format_only`. 90
records in no event have differing reference strings. Most are renumbering, but MCC #8 and #11, 1952_1962_0012 and
2008_2010_0424 (removes "and 42.17(b)") are content changes.

---

## 3. Gold CSV and raitkerr_drafts

| Item | Verdict | Evidence |
|---|---|---|
| L1 serial 22 | FIXED | "limited the width of the bat to 4¼ inches". |
| L2 54a prior | FIXED | `4; 16`. |
| L3 start pages | FIXED | 38 -> 71, 120 -> 83, 137 -> 86. |
| L4 section D | FIXED | All rows 11-20c have D. |
| M6 bold | FIXED | 52-56 ALL; 58 first sentence only; 70 empty; 68 without "(Vide ...)"; "Before 1821" note first clause; 1774 heading no longer ALL. |
| `_gold_finalise.py` QA | OK | Rebuild is reproducible and identical. Output: "rows: 172, change rows: 164, serials 1-138, missing: []; dangling refs: []; non-reciprocal refs: 2 (63<-53, 92<-81)". The two non-reciprocal refs were already present and A judged the references correct apart from L2. |
| `build_gold.sh` uses the venv | FIXED | |
| drafts 99 | FIXED | Secondary removed; note "a procedural failure of notice, not a drafting omission". |
| drafts 101 | FIXED | Secondary removed. |
| drafts 54a, 55 | PARTLY | They say "the printed (struck-through) text and a handwritten annotation of unknown authorship ... read this as 'the first evidence of the attack ...'". The quoted words are the struck printed text (gold `struck_text`). The gold `annotation` column is **empty** for 54a and 55, so the "handwritten annotation" reading is not recorded anywhere in the gold. Evidence for 55 still says "(annotation)". |
| drafts 54b | OK | |

---

## 4. Basis / evidence rules

17 `stated` labels were spot-checked. Every quoted string in a stated or attributed label was searched in the local texts.
- All S04 quotes are verbatim.
- The S02 preface quotes (RE, GN, objectives) are verbatim; they span the two-column layout, l.28-53.
- The S03 quotes (Finn, practice, conclusion of match, Governing Body for the match) are verbatim.
- The S09 Sept-1951 quote is verbatim.

The problems are with the *basis*, not the quotes:

| Label | Problem |
|---|---|
| 1947_1952_E014, E015 | `basis=stated` while the rationale says "Interpretive Note added in the 2nd edition (absent from the 1st); **no cause stated**." A direct contradiction. |
| 1947_1952_E007, E009 | `stated` on "ACS describes the 2nd edition's changes as corrections and a few additions" (a whole-revision remark, which S08's registry note says is not in the local copy) and on "Law 31 and Law 30 refer to it". No cause is stated. |
| 1968_1980_E055 | consolidation_merge still `stated`. The other 41 restructure labels in this pair are now `inferred`, so the 1968_1980 restructure point is FIXED apart from this one. |
| 1992_2000_E001, E051 | consolidation_merge `stated` on the S01 whole-revision preface. |
| 2010_2017, 50 labels | 34 `consequential` and 16 `reorganisation` labels have `basis=stated` whose only support is the S02 preface "A new Code was necessary to rationalise these amendments ...". Examples: E009, E010, E080, E081, E095, E111. The `conseq()` helper in `labels/n2010_2017.py` still sets `"stated"`. This contradicts CLAUDE.md ("prefaces that state the aim of a whole revision give `inferred`"). |
| 41 rows, 1968_1980 | The rationale still says "is confirmed in the ACS transcription of the 1980 Code (S11)". B pattern 3 and the S11 registry note say S11 "does not confirm 1980 wording". NOT FIXED in the text. |
| 2010_2017_E090 | The rationale quotes S03 ("confirms that it is now the Governing Body for the match ...", verbatim at S03 l.125-126), but `evidence` is S02;S17;S01, with no S03. |
| 2010_2017_E101 | "the need both to provide the umpires ..." is still presented as an MCC quote. C could not confirm "the need both to"; it is not in any local text (S06 only). |

---

## 5. sources.csv and DATA_INTEGRITY_FINDINGS.md against report C sections 5 and 6

| Item | Verdict |
|---|---|
| S06 (date 2017-04-12; MCC quoted only for non-striker and Law 42; no "No reason stated") | FIXED |
| S07 now cited | FIXED (2010_2017_E041) |
| S12 author/date; "1972 not explicit" | FIXED |
| S22 rewritten (conforms; no May 2008 approval; 2009 approval) | FIXED |
| S08 note (quote not in local copy) | FIXED. It understates slightly: B did verify the sentence on the live ACS page. |
| S11 caution, S17 mechanisms, S02 retrospective | FIXED |
| S13 note "ComBat bat origin of wooden-blade requirement" | NOT FIXED (B finding). B reports that live S13 says only "the Laws have provided that the blade of the bat must be made of wood"; the 1968_1980_E061 label itself says this. |
| DATA_INTEGRITY rows | All FIXED as C proposed: 1962 projection "OCR misread"; 2010 "815/16" OCR misread plus women's 8 1/2; 2017 "8.81 m" in both raw texts; 2019 "0 04 m"; 1968 bat "exceed inches"; 2000 bail-figure displacement "not an error"; 1952 Laws 30/31 claim withdrawn; 1890 typo caveat. The figures were checked against raw: 2010_raw l.587; 2017_raw l.444; 2019_raw l.445. |
| DATA_INTEGRITY intro | Minor inconsistency: it says everything in the table "is recorded as `NOT_A_CHANGE / cleaning_artefact_numeric` labels". The 2000 bail row is labelled `segmentation_artefact` (2000_2008_E053) and the 2008 covering row is `STRUCTURAL/terminology` (2008_2010_E007). |

---

## 6. Other problems found

| # | Severity | Problem | Evidence |
|---|---|---|---|
| 1 | HIGH | Merge rule picks the wrong primary | `08_build_labels.py` `resolve()`: `(ol["category"] not in ("UNCATEGORISED","NOT_A_CHANGE"), obo) >= ...`. A STRUCTURAL/wording_only label beats a corrected UNCATEGORISED one. Affected: 2008_2010_E029, E060, E074 (E074 holds the new catch-start rule "comes into contact with some part of a fielder's person other than a protective helmet" under a "wording only" primary). Also 2017_2019_E028 (the 21.12 fairness change sits under "consequential"). |
| 2 | MEDIUM | Builder does not validate `secondary_subtype` | 2017_2019_E028 and E058 have `EXTERNAL_FORCE/technology`; the taxonomy's EXTERNAL_FORCE subtypes are equipment_manufacture, pitch_technology, dress_fashion, medical_safety, legal_social. 1968_1980_E063 has secondary NOT_A_CHANGE with an empty subtype. |
| 3 | MEDIUM | Stale event cross-references after re-resolution | 2017_2019_E058 and E056 "(see E050)" (should be E049). 1947_1952_E009 "(E011, E013)" (now E010, E012). n1952_1962 E013 "see E011 of this pair" (the 1953 Note is now E012; E011 is Stumped segmentation). n1980_1992 E012 "run-out rebound exception in E014" (now E011). |
| 4 | LOW | Orphaned hand labels are silently dropped | 11 orphans. Most are harmless. One, 2008_2010:E022 ("batsmen at the wicket may deputise ... drinks"), now sits in E020, unmentioned. The old 2008 text already had the deputising rule via Law 3 (record 0615), so no real change was lost. |
| 5 | LOW | README.md l.49 "40 of 136 changes carry no stated cause" | raitkerr_drafts.csv has 157 rows, 41 with basis `none` (40 UNCATEGORISED + serial 36 STRUCTURAL/basis none). |
| 6 | LOW | Duplicate description | 1952_1962_E012 and E013 both describe "The captain shall take the bowler off as directed". |

## Not verified

- Web-only sources: S07, S13, S20, S21, and the live S06/S22 text.
- C's 2008_2010 triage-gap events E030/E038/E089/E097. C gave no descriptions, so I could not map them to current ids.
- 2010_2017 E007/E088 beyond reading the label text.
- The 2008_2010 hidden-change texts other than those listed in section 1 were checked only for E013, E033, E088, E029 and E075.
