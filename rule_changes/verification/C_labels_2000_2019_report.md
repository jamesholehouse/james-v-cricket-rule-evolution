# Verification report C: labels 2000->2019, source registry, data-integrity claims

Reviewer: independent read-only audit (no pipeline run, no other file modified).
Scope: `labels/p2000_2008.py`, `p2008_2010.py`, `p2010_2017.py`, `p2017_2019.py` as compiled in
`data/categories/post1947_event_labels.csv`; `data/evidence/sources.csv`; `DATA_INTEGRITY_FINDINGS.md`.
Method: every labelled event was checked against its change records (`data/changes/<pair>.jsonl`, old_text/new_text and
word diff); every quotation was string-searched in the saved source text; numeric claims were checked in raw OCR
(`data/datasets/rule_texts/raw/`), processed text and the independent transcriptions; 9 web-only sources were fetched
(2 returned HTTP 403; the session web quota ran out before S08's web page could be fetched).

## 1. Verdict summary

| Pair | Labels in CSV | OK | Minor issue | Wrong |
|---|---|---|---|---|
| 2000_2008 | 45 | 34 | 7 | 4 |
| 2008_2010 | 74 | 28 | 26 | 20 |
| 2010_2017 | 99 | 69 | 16 | 14 |
| 2017_2019 | 50 | 39 | 8 | 3 |
| **Total** | **268** | **170** | **57** | **41** |

"Wrong" means the label states something the change records or the sources contradict. That includes a real rule change
labelled as an artefact or as wording only, a false "new", a reason the cited source contradicts, or a stated cause that
was ignored. "Minor" covers incomplete descriptions, a `basis` that overstates the evidence, a loosely trimmed quote and
similar.

Also reviewed: the 55 events with `triage = wording_only` in these 4 pairs. They are excluded from the label CSV
altogether (`08_build_labels.py` skips them). The README says all 459 events were labelled, but these 55 are not in the
CSV. At least 12 of them are real rule changes, including **6 of MCC's own 22 listed 2019 changes** (see section 3).

Headline problems:
1. **2017_2019 E057 (CRITICAL)**: MCC's 2019 change to Law 41.16 (non-striker "liable to be Run out"; new 41.16.2 and
   41.16.3) is labelled `NOT_A_CHANGE/segmentation_artefact` ("Words identical"). E060 (MCC change to 42.4.2.3.1) is
   labelled the same way. 2 of the 22 MCC changes are hidden as artefacts. Another 6 are outside the label set.
2. **2008_2010**: 17 of the 36 `wd()` labels (STRUCTURAL/wording_only, basis `stated`, "leaves the rule as it was") hide
   real rule changes. Among them are NZC's "toss" key change (E012), the new Law 19.4 "Ball beyond the boundary" (E036)
   and the new Not-out-Stumped injury defence (E084). All 36 use a general NZC remark as a *stated* cause for each
   individual edit.
3. **Mis-attributed and invented quotations from S06 (ThePapare/Cricbuzz)**. The labels quote ThePapare as saying "No
   reason stated" (E046, E048, E065, E071), but the phrase does not occur in the article. The article writer's own
   phrase "redress the balance between bat and ball" is presented as an MCC quote (E002).
4. **Stated causes ignored**: the 2013 "Finn" No-ball law (S03 gives the reason, S07 the trigger) sits under
   UNCATEGORISED E037. S07 is cited by no label at all. The 2017 tethered-bails clause (whose own text states its safety
   purpose) is inside UNCATEGORISED E102, and that label's note wrongly says it "appears elsewhere".
5. **2008 bat Law (E003/E048)**: S22 is labelled as evidence that MCC acted "in response to ... the Mongoose". The S22
   post itself says the Mongoose *conforms to* the new Law 6 that came into force on 1 Oct 2008. It is evidence against
   the causal claim, not for it.

## 2. Problem labels

Severity: CRITICAL = a significant change that MCC lists or explains is hidden or reversed; HIGH = a real rule change
mislabelled, or a cause contradicted; MEDIUM = misdescription, wrong mechanism or overstated basis on a real change;
LOW = cosmetic or incomplete.

### 2017_2019

| Event | Sev. | What is wrong | Evidence | Proposed correction |
|---|---|---|---|---|
| E057 | CRITICAL | Labelled NOT_A_CHANGE/segmentation ("Words identical"). Records 0205, 0357, 0215, 0206 and 0358 are the MCC 2019 rewrite of Law 41.16: "the bowler is permitted to attempt to run him/her out" becomes "the non-striker is liable to be Run out"; the new wording adds "whether or not the ball is subsequently delivered" and new clauses 41.16.2 and 41.16.3. Record 0216 is the dropped last sentence of 41.2 (MCC change 41.2/41.19). | `mcc_2019_changes.txt` l.515-562; the 2017 text has "the bowler is permitted to attempt to run" and 2019 has "non-striker is liable to be Run out" (processed texts). | Split the event. The 41.16 part becomes STRUCTURAL/clarification_umpire_workability, basis stated, S04: "This new change clarifies MCC's interpretation of the Law", "principally on the back of TV replays", plus secondary EXTERNAL_FORCE (TV technology). Only the 41.15 records are segmentation. |
| E060 | HIGH | Labelled segmentation ("only the connecting word and unit boundary differ"). It is MCC change 42.4.2.3.2: the part-over sentence is *inserted into* 42.4.2.3.1. 2017 has the sentence once, 2019 twice. | S04 l.589-608; sentence counts in the processed 2017 and 2019 texts. | STRUCTURAL/clarification_umpire_workability, stated, S04 ("There was a lack of clarity over the suspension of a player for 10 overs in a match limited by time"). |
| E048 | MEDIUM | what_changed misquotes the text as "'8.25 m/22.4 m' in 2017 ... '8.25 in' in 2019". The records read "8.81 m/22.4 cm ... 9 m/22.9 cm" in 2017 and "8.81 in ... 9 in" in 2019. The mechanism is also misstated: raw OCR for both 2017 and 2019 reads "m" (an OCR misread of "in"). The 2019 clean-up fixed it and 2017's did not, so this is not a "slip in the earlier digitised text". | `raw/2017_raw.txt` l.443-444, `raw/2019_raw.txt` l.445; S02 l.322 "8.81 in/22.4 cm". | Keep NOT_A_CHANGE but correct the numbers. The subtype is an OCR unit misread, not an invented number. Cite S02. |
| E049 | LOW | Same mechanism issue: raw 2019 also has "8.25 m" and "8 88 m". | `raw/2019_raw.txt` l.480-483. | As E048. |
| E053 | MEDIUM | The primary category clarification_umpire_workability understates MCC's stated reasons. MCC says the 2017 rule was "overly harsh, particularly on younger bowlers" and wants a "better and fairer Law, while still maintaining the core aim of improving player safety and enjoyment". | S04 l.351-380. | ENJOYMENT/fairness_spirit (primary) with secondary EXTERNAL_FORCE/medical_safety, or keep the label and add the fairness quote. The existing quote is verbatim. |
| E055 | MEDIUM | The rationale says "the time-wasting paragraph moves with it [into 41.2]". It does not: 41.9.3 stays in 41.9. The 41.19-to-41.9.3 record is an alignment mismatch. | Records 0213, 0189 and 0190 all sit in 41.9.3 in both editions. | Re-describe as an alignment artefact plus the 41.19.1 removal (part of E050). |
| E029 | LOW | The secondary NOVEL_EVENT/single_incident is unsupported. MCC cites "TV replays", which describes a pattern exposed by technology, not one incident. | S04 l.518. | Secondary EXTERNAL_FORCE (technology), or none. |
| E043, E044 | LOW | ENJOYMENT/fairness_spirit with basis `stated`, but MCC's stated reasons are instinctive defence (34.3) and consistency with "cannot be out Caught off a No ball" (37.3). Neither text says "fair". The E044 what_changed also omits the new 37.3.3/37.3.4 rule (whoever causes the obstruction is out). | S04 l.229-278. | basis `inferred`, or STRUCTURAL/codification_definition; complete what_changed. |
| E021 | LOW | The quote silently corrects the source. The source reads "All eight are now be included"; the label reads "All eight are now included". | S04 l.128. | Quote exactly, or mark [sic]. |
| E024 | LOW | The mechanical STRUCTURAL/wording_only label rests on "changed words: lawigtboundaries", which is OCR garbage. | Record 0058. | NOT_A_CHANGE/format_artefact. |

Verified correct in this pair: E001, E015, E017, E030, E047, E050, E054, E058 and E061. Their quotations match S04
verbatim (see section 4). The artefact labels E002-E008, E010, E018, E022, E023, E027, E028, E031-E040, E045, E046,
E051, E052, E056 and E062 were checked against the records and are genuine segmentation, format or Law-boundary shifts.
For E052 the sentence occurs twice in each edition.

### 2000_2008

| Event | Sev. | What is wrong | Evidence | Proposed correction |
|---|---|---|---|---|
| E003, E048 | HIGH | NOVEL_EVENT/equipment_exploit with basis `attributed`: "in response to unconventional bats such as the Mongoose". S22 (the forum post, 23 Mar 2010) says only that the Mongoose bats "conform to the new version of Law 6 and Appendix E, which came into force on 1st October 2008". MCC tested and approved the Mongoose in 2009 (Lord's museum record), so it post-dates the new Law and cannot have caused it. Neither the post nor the search results show an approval date of "May 2008". `attributed` is meant for a claim by a named person; S22 is anonymous. | WebFetch of the S22 URL; Lord's museum record (search result). | UNCATEGORISED/no_cause_stated, basis none (secondary STRUCTURAL/codification_definition). Keep the effective date 1 Oct 2008 from S22 as date_evidence, marked low reliability. |
| E025 | HIGH | Labelled as a "new 'Dispensing with bails' provision". The 2000 text already contains the whole provision (old record 0081: "Dispensing with bails ... (a) After a decision ... (b) If the wicket has already been broken ..."). Only the segmentation and a stray "•4." differ. | Records 0080-0083 and 0183. | NOT_A_CHANGE/segmentation_artefact. |
| E051 | MEDIUM | NOT_A_CHANGE is correct, but the rationale "figures were lost from the 2000 digitised text (raw OCR gap)" is false. Raw and processed 2000 both carry the bail figures (4⁵/₁₆, 2⅛, 1⅜, ¹³/₁₆), displaced into the next table block. | `raw/2000_raw.txt` l.697-727; record 0027 old_text. | Subtype segmentation_artefact (table layout), integrity ok. Remove it from the "cleaning artefact" count in DATA_INTEGRITY_FINDINGS. |
| E005 | LOW | "drinks-interval wording extended" is false. The 5-minute sentence is in both editions (record 0129). Only the tea/9-wickets change is real. | Records 0038 and 0129. | Drop the drinks clause from what_changed. |
| E010 | LOW | The "Additionally ... bowler's end umpire" part is in both editions. The real change is "either of the same batsmen" becoming "any batsman". | Records 0049 and 0175. | Narrow the description. |
| E022 | LOW | Wording_only with "no change of rule", although replacing a closed list of Laws with "any of the Laws" broadens the rule. | Record 0069. | UNCATEGORISED, or STRUCTURAL/consequential with basis inferred. |
| E012, E026, E027, E028 | LOW | Mechanical "minor wording" labels where only list labels such as "(b) below" or "(iv) above" moved between units. | Records. | NOT_A_CHANGE/format_artefact (a tooling issue in 08b). |

The NOT_A_CHANGE claims E046 and E047 are confirmed (section 6). The UNCATEGORISED descriptions E001, E007, E009, E016,
E019-E021, E024, E033, E034, E036-E040, E043 and E044 match their records.

### 2008_2010

Systematic issue (MEDIUM, all 36 `wd()` labels): S15 says only that MCC "modernised the Laws to make them easier to
understand", in general. Using it as a *stated* cause for each individual edit overstates the evidence; the basis should
be `inferred`. More seriously, the 17 `wd()` labels below contain real rule changes but assert "a rewording that leaves
the rule as it was".

| Event | Sev. | Real change hidden under "wording only" (or other error) | Proposed |
|---|---|---|---|
| E012 | HIGH | The toss must now take place "in the presence of one or both of the umpires". The decision is notified "as soon as the toss is completed ... and the umpires" instead of "10 minutes before" the start. A limited-innings agreement "must also include criteria for determining the result". A completed innings now includes "the retirement of a batsman". The toss is one of NZC's 8 key changes (S15). | UNCATEGORISED (S01, S15), as with E019 and E054. |
| E036 | HIGH | Adds new Law 19.4 "Ball beyond the boundary" (fielding or catching after the ball has crossed the boundary; airborne fielder). | UNCATEGORISED. |
| E084 | HIGH | Adds a new defence: the striker is not out Stumped "if he has left his ground to avoid injury". Stumping now needs "a ball which is not a No ball is delivered" and "has not attempted a run". | UNCATEGORISED. |
| E011 | MEDIUM | Law 10 changes: when time is short, the batting captain may still have the 7 minutes of rolling, with the delay taken out of playing time; the debris-clearance regime is rewritten (before each day, between innings, at meal intervals; by hand if sweeping would harm the pitch). | UNCATEGORISED. |
| E021 | MEDIUM | New 15.8: "retirement of a batsman is not to be considered equivalent to the fall of a wicket". Drinks are taken if "a wicket falls or a batsman retires". | UNCATEGORISED. |
| E025 | MEDIUM | New 16.9(c), the conclusion of a match under a 12.1(b) agreement; the reference becomes "5(a)". | UNCATEGORISED. |
| E031 | MEDIUM | For deliberate short runs the warning goes to both batsmen; all runs except "any runs awarded for penalties" are disallowed (previously only the No ball/Wide penalty and two named penalties survived). | UNCATEGORISED. |
| E039 | MEDIUM | The bar on a substitute acting "as captain on the field of play" is removed from Law 2.3. The 15-minute absence becomes "15 minutes of playing time". For a player returning without permission, completed runs are now scored. | UNCATEGORISED. |
| E040 | MEDIUM | Runner rules: an injured striker out of his ground is out Run out "notwithstanding Law 38.2(e)"; he is Stumped only off a ball that is not a No ball; runs are "disallowed". | UNCATEGORISED. |
| E046 | MEDIUM | New Law 21.4: a match under a 12.1(b) agreement takes its result from the agreement; 21.6(b) is redefined. what_changed mentions only a cross-reference title. | UNCATEGORISED. |
| E047 | MEDIUM | Mistakes in scoring now cover limited-overs innings, with times taken at the call of Time. | UNCATEGORISED. |
| E052 | MEDIUM | A Dead ball for a striker not ready no longer needs "adequate reason" for the call itself, but the ball counts in the over unless there was adequate reason. New Dead ball 23.4(b)(vii) for deliberate distraction under 42.4/42.5. | UNCATEGORISED. |
| E053 | MEDIUM | The validity-of-ball rule (23.6) is rewritten with new exceptions (2.6, 41.2, 42.5). | UNCATEGORISED. |
| E059 | MEDIUM | New leg-bye rule on subsequent inadvertent contact; runs credited to the striker after later contact with his bat; the "wilful lawful second strike" condition. | UNCATEGORISED. |
| E090 | MEDIUM | Illegal fielding: completed runs are now credited and the No ball/Wide penalty stands. Ball hitting a helmet: completed runs are scored and the penalty is added to the No ball/Wide. | UNCATEGORISED. |
| E092 | MEDIUM | The ball-condition test changes to "deterioration ... greater than is consistent with the use it has received" (overlaps E093). | Merge with E093. |
| E094 | MEDIUM | "Both the above caution and final warning shall continue to apply even though the bowler may later change ends" is removed; the time-wasting trigger becomes "either umpire considers". | UNCATEGORISED. |
| E074 | MEDIUM | NOT_A_CHANGE/segmentation ("no change"), but the offence of returning the ball now excludes "a hand not holding the bat" and adds "while the ball is in play"; "consent of the opposing side" becomes "consent of a fielder". | UNCATEGORISED. |
| E005 | MEDIUM | what_changed implies a new handle-material restriction. The 1/10 and 1/5 restriction is already in 2008 (old record 0587); only Grades become Types. | STRUCTURAL/terminology. |
| E006 | MEDIUM | "New limit that the toe insert ..." is false; it is already in 2008 (old record 0602). Missed: the commercial-identification thickness changes from "0.08 in/0.2 mm" (2008, raw OCR "0.08 m/0.2 mm", internally inconsistent) to "0.008 in/0.2 mm" (2010, matching S01 l.3050). | A correction of a printed error, not a policy change. Describe it as such. |
| E067 | MEDIUM | Lists only pre-match checks, but contains the main "ground, weather and light" change: the captains' option to play on in unsuitable conditions is removed; the umpires alone decide whether conditions are "dangerous or unreasonable"; both terms are defined. | Rewrite what_changed; the category stays UNCATEGORISED. |
| E055 | LOW | Omits that the front-foot rule now has "three conditions" (24.5). | Complete what_changed. |
| E096 | LOW | Conclusion correct, mechanism wrong. Raw 2010 OCR already reads "815/16 in/22.4cm" (`raw/2010_raw.txt` l.587), so this is an OCR misread, not an "AI clean-up slip". | Fix the rationale. |
| E098 | LOW | Junior "8 5/8" is confirmed as a clean-up error (raw "8“/i6", i.e. 8 11/16). Missed: women's lower limit "8 1/4" becomes "8 1/2" (raw "8V2"; S01 reads 8¼; 21.0 cm = 8.27 in), a second artefact in the same event. | Add it. |
| E023, E033, E045, E049, E072, E095 | LOW | Under-described real edits: Call of Time "when the ball is dead"; "Notwithstanding any agreement under 12.1(b)"; the umpire-miscounting rule 22.5(b); "designated a boundary by the umpires before the toss"; new definitions of avoidable damage and of the protected area. | Complete what_changed. |

The quotes in the p2008_2010 docstring were verified: S01 "necessary amendments arising from experience and practical
application of the Code" (`thapos_2000code.txt` l.28) and S03 "The change made in 2010 to outlaw this practice has been
over-written by playing regulations in all professional and most amateur cricket" (`mcc_2013_5th_edition_changes.txt`
l.221-223).

### 2010_2017

| Event | Sev. | What is wrong | Evidence | Proposed |
|---|---|---|---|---|
| E037 | HIGH | UNCATEGORISED with "no source found states a reason". The event contains the 2013 Law 24.6 (bowler breaking the wicket in delivery is a No ball). For that law S03 states the reason ("removes any doubt over whether the striker may have been distracted ... whilst crediting him with any runs") and S07 states the trigger (Steven Finn, 2012) and MCC's rationale ("provides clarity ... removes the need for a subjective assessment"). S07 is registered and named in the docstring but cited by no label. The event also contains the 2017 underarm-delivery No ball, "Fielder intercepting a delivery", and the over-head-height bouncer No ball (S05). | S03 l.545-560; S07 (fetched); record 0279+. | Split the event. Law 24.6 becomes NOVEL_EVENT/single_incident (S07) with secondary STRUCTURAL/clarification, basis stated (S03); date 1 Oct 2013. |
| E102 | HIGH | Contains the 2017 tethered-bails clause, 8.3.4 ("Devices aimed at protecting player safety by limiting the distance that a bail can travel off the stumps will be allowed", change 0854). The note says this "appears elsewhere in Law 8", which is false. The Law text itself states the purpose (player safety). | Change 0854; processed 2017 l.501-503. | EXTERNAL_FORCE/medical_safety, basis stated (the Law text), with S06 for context. The S06 wording is the article's ("injuries like the one suffered by South Africa's Mark Boucher in 2012 who was partially blinded by a flying bail"), not MCC's, and the label paraphrases it inside quote marks. |
| E053 | HIGH | Says there is a "new 'Protective helmets belonging to the fielding side' provision". That provision has existed since at least 2008 (2008_2010 E090, record 0441). The only record is a restatement of fielding-the-ball. EXTERNAL_FORCE/medical_safety (inferred) is unsupported: the cited S05 line ("Batsman can now be caught, stumped, or run out from a ball deflecting off a fielder's helmet") is about a different change, which actually sits in E035/E072. | Records; S05 item 6. | UNCATEGORISED or a format artefact; move the S05 helmet item to E035/E072. |
| E002 | HIGH | Basis `stated`: "News reports quote MCC that the new bat limits are ... 'the desire to redress the balance between bat and ball'". In S06 this sentence is the Cricbuzz writer's own, not a quotation from MCC (WebFetch of S06). S02's general objective "to maintain a fair balance between bat and ball" is real (S02 l.21-22) but not tied to the bat limits in the text. The new depth and edge limits (2.64 in/6.7 cm, 1.56 in/4.0 cm, bat gauge) are in **E095** (change records), not in E002's Appendix B records. | S06 fetch; c1017 E095 record. | ENJOYMENT/bowler_batsman_balance, basis `inferred` (S02 objective), placed on E095. E002 becomes STRUCTURAL/reorganisation (new Type D bats). |
| E095 | MEDIUM | The primary STRUCTURAL/reorganisation hides the substantive 2017 change, the bat size limits. | As above. | Primary ENJOYMENT/bowler_batsman_balance (inferred); secondary reorganisation. |
| E006 | MEDIUM | The covers rules are not just "restated". The default reverses: 2010 says "shall not be completely covered ... unless provided otherwise"; 2017 says "Unless determined otherwise ... on each night ... the whole pitch and ... 4 ft/1.22 m beyond it ... shall be covered". | Records. | Rewrite what_changed. |
| E009 | MEDIUM | STRUCTURAL/consequential ("length becomes duration"), but the 9-wickets-down rule changes from 2 to 3 minutes and is extended to the lunch interval, and drinks intervals change from "captains agree" to "umpires determine". | Records. | UNCATEGORISED. |
| E010 | MEDIUM | Reorganisation (basis stated), but includes a numeric change: an interval is taken immediately if a wicket falls with "less than 2 minutes" becoming "less than 3 minutes" before the interval. | Record. | UNCATEGORISED. |
| E027 | MEDIUM | Describes a "new rule" that the batting side scores runs completed before an Obstructing-the-field offence. That rule already existed in Law 37.5 (2010); here it is relocated into Law 18. | 2008_2010 record 0408. | STRUCTURAL/reorganisation. |
| E072 | MEDIUM | The primary EXTERNAL_FORCE/legal_social (gender-neutral) is wrong for an event whose substance is the boundary-catch rules and the removal of "not a fair catch if the ball lodges in a protective helmet". S03 gives reasons for the 2013 boundary-catch rewrite ("give additional clarity ... when fielders work as a team"; "fully clarified"), and S05 item 6 covers the 2017 helmet change. | S03 l.709-735; S05. | STRUCTURAL/clarification (S03, stated) for the 2013 part; UNCATEGORISED for the helmet part. |
| E074 | MEDIUM | "Consequential", but includes the 2017 change in which the umpire calls Dead ball after a lawful second strike, delayed to allow a catch, which replaces the old run-scoring scheme. | Records. | UNCATEGORISED. |
| E075 | MEDIUM | "Consequential", but adds that the striker is not out Hit wicket if "the delivery is a No ball" (a new 2017 rule). | Record. | UNCATEGORISED. |
| E090 | MEDIUM | Reorganisation, but short-pitched bowling is redefined: "fast" is dropped (any speed), "speed" and "skill of the striker" are added, and protective equipment is disregarded. | Records. | UNCATEGORISED. |
| E083 | MEDIUM | NOT_A_CHANGE is right for the ball size. The mechanism ("AI clean-up slip") is wrong: raw 2010 OCR has "815/16". The event also hides real changes: balls are "determined by the umpires" (previously approved by umpires and captains), and the new-ball count is "excluding any part overs". The 2017 value is written "8.81 m", not "8.81 in". | Records; `raw/2010_raw.txt` l.587. | Split: numeric artefact plus UNCATEGORISED. |
| E046, E048, E065, E071 | MEDIUM | All four quote ThePapare: "'No reason stated'". The phrase does not occur in the article (WebFetch, exact search). In E046 the quote "split into two Laws, one for batsmen (Law 25) and one for fielders (Law 24)" is a paraphrase; the article says "divided into two separate Laws, relating to the batsmen (Law 25) and the [fielders] (Law 24)". | S06 fetch. | Replace with "S06 gives no reason". |
| E091 | MEDIUM | UNCATEGORISED, while its own note quotes MCC's reason for the 2017 non-striker change, carried in S06 from MCC's summary: "it is the batsman who is attempting to gain an advantage"; "stay within your ground until the bowler has released the ball". | S06 fetch. | Label the 41.16 part with basis `attributed` (S06 quoting MCC), e.g. ENJOYMENT/fairness_spirit. |
| E070 | LOW | Rationale is the generic 2017 reorganisation. S03 states the specific 2013 reason for dropping Handled the ball from the Bowled exceptions (l.641-653). | S03. | STRUCTURAL/consequential, stated, S03, dated 2013. |
| E036 | LOW | The S03 quote silently drops the parenthesis "(Bowler attempting to run out non-striker before delivery)". | S03 l.532-534. | Add an ellipsis. |
| E015 | LOW | Cites S15 (the 2010 NZC piece) for a 2010-to-2017 change. The 2010 toss change belongs to the 2008_2010 pair (E012 there). | - | Drop S15. |
| E035 | LOW | Omits that "it lodges in a protective helmet worn by a fielder" is removed as a dead-ball event (the 2017 helmet change, S05 item 6) and that Lost ball is folded in. | Records. | Complete what_changed. |
| E004, E007, E088, E104 | LOW | E004 pairs an UNCATEGORISED primary with an ENJOYMENT secondary. E007 omits "duration determined under Law 2.3". E088 omits the new ball-tampering procedure ("ask the captain of the opposing side"). E104 removes a provision but is labelled "consequential". | Records. | Adjust. |

Note on the 2010_2017 review: events with many records (E002 with 50, E003 with 63, E029 with 48, E090 with 57) were
checked on their first records and by keyword search, not record by record (see residual risks).

## 3. 2017_2019: mapping to the 22 MCC changes (S04)

| # | MCC change | Event | Status |
|---|---|---|---|
| 1 | Preamble "umpires" to "match officials" | E011 | **not labelled** (wording_only triage) |
| 2 | 11.2.2 cross-references | E012 | **not labelled** |
| 3 | 15.1 declared innings completed | E015 | OK |
| 4 | 16.3.3 | E017 | OK |
| 5 | 16.7 "innings completed" | E019 | **not labelled** |
| 6 | 18.6 | E021 | OK (quote typo silently corrected) |
| 7 | 21.6 | E029 | OK (secondary category doubtful) |
| 8 | 21.12 | E030 | OK |
| 9 | 29.1 | E037 | **not labelled** |
| 10 | 30.1 | E041 | **not labelled** |
| 11 | 33.4 cross-reference | E042 | **not labelled** |
| 12 | 34.3 | E043 | OK (basis) |
| 13 | 37.3 | E044 | OK (basis; incomplete what_changed) |
| 14 | 39.3.1 | E047 | OK |
| 15 | 39.3.2 | E047 | OK |
| 16 | 41.2/41.19 | E050, E055 (plus record 0216 in E057) | OK, with E055's rationale wrong |
| 17 | 41.7 | E053, E054 | OK (category question) |
| 18 | 41.16 | **E057** | **mislabelled NOT_A_CHANGE** |
| 19 | 42.1.5 | E058 | OK |
| 20 | 42.4.2.3.2 | **E060** | **mislabelled NOT_A_CHANGE** |
| 21 | 42.7 | E061 | OK |
| 22 | Appendix A waist definition | E001 | OK |

No label is mapped to a wrong MCC change. Not on MCC's list but in the data: E020 (18.3.2 "the latter" becomes "the run")
and E026 (an OCR garble, "within" read as "v. :*"); both are unlabelled.

## 4. Quotation audit

Verified verbatim (exact string found in the local text):
- **S04** (`mcc_2019_changes.txt`): E001, E015, E017, E029, E030, E043 (main quote), E047 (both), E050, E053, E058,
  E061 (three fragments). E021 is near-verbatim; the source's grammar error was silently corrected. E044 is truncated
  ("for this Law" dropped) without marking.
- **S02** (`lords_2017_code_4th_ed_2026.txt` l.20-53): the RE, GN, "maintain a fair balance between bat and ball", "to
  make the Laws easier to understand" and "to give umpires more mechanisms to address instances of poor behaviour by
  players" quotes. The S02 statements are in the 2026 4th-edition preface, which describes the 2017 objectives
  retrospectively.
- **S03** (`mcc_2013_5th_edition_changes.txt`): E035 (l.528), E042 (l.621-627), E050 (l.220-224), E071 (l.779-782),
  E078 (l.920-922), E084 (l.124-127). E036 drops a parenthesis without marking it.
- **S01**: the p2008_2010 docstring quote (l.28).

Problems:
- **S06 (ThePapare)**: "No reason stated" is not in the article (E046, E048, E065, E071; also the E046 note). The
  "redress the balance between bat and ball" phrase is the article writer's, presented as an MCC quote (E002). The E046
  "split into two Laws ..." quote is a paraphrase. The E102 Boucher quote is condensed inside quote marks. The E094
  phrase "provide the umpires with appropriate on-field sanctions to deal with deteriorating levels of behaviour" is
  from MCC's summary as quoted in S06 (confirmed); the leading words "the need both to" could not be confirmed verbatim.
- **S22**: the label paraphrase (an approval date of May 2008; "in response to ... the Mongoose") is not in the source,
  and the source implies the opposite causal order.
- No Law number was found to be misattributed in a quotation. One numbering slip: E035's what_changed says "Law 16.9";
  the 2017 text says 12.9 (16.9 is the 2013 numbering).

## 5. Source-registry audit (`data/evidence/sources.csv`)

| Id | Finding |
|---|---|
| S01 | OK. Preface signed by K Bradshaw and dated 5 May 2010 (`thapos` l.78-80). |
| S02 | OK. The preface is signed by R.S. Lawson; the 4th edition is dated 1 October 2026. Note that its preface statements are retrospective (2026) about the 2017 objectives. |
| S03 | OK as text; the URL is a Sri Lanka Cricket mirror, not an MCC host. "Official MCC explanation" is correct by content. |
| S04 | OK; 22 changes confirmed; dated "December 2018" in the text. |
| S05 | OK ("no rationale given" is true). Item 6 (helmets) is misapplied in label 2010_2017 E053. |
| S06 | **Inaccurate.** The article is Cricbuzz content republished by ThePapare on 12 Apr 2017 (registry says only "2017"). The note "Quotes MCC reasons for bat limits, tethered bails, non-striker run out and Law 42" is wrong for bat limits and tethered bails, whose reasons are the writer's. MCC is quoted only for the non-striker run-out and Law 42. |
| S07 | Verified: Kent CCC, 21 Feb 2013; Finn incidents (Headingley, Aug 2012); John Stephenson's rationale. **Cited by no label**, although it supports the reason for the 2013 Law 24.6 inside 2010_2017 E037. |
| S12 | Verified content (1935/1937, 1970-71 reversion; reason only for 1935). Missing metadata: author Martin Chandler, 12 Sep 2011. "1972 LBW change" is not explicit on the page. |
| S13 | Not fetched (not used in this scope). |
| S14 | Verified: "Updated Code of Laws comes into force", 1 April 2019. It says "MCC listened to significant feedback" and gives the 22-change total. |
| S15 | Verified: NZC, 17 Jun 2010; "Eight key changes"; four named; the modernisation remark is general. |
| S19 | Verified: Timed out became a specific dismissal "in the 1980 code"; two minutes; the 1919 Heygate ruling. |
| S20 | HTTP 403; unverified. |
| S21 | HTTP 403; unverified. |
| S22 | **Inaccurate and over-interpreted.** The forum post (23 Mar 2010) says the Mongoose conforms to the new Law 6 and Appendix E in force from 1 Oct 2008. It does not say MCC "approved ... in May 2008", and it does not "link" the Law to the Mongoose as a cause. A web search also confirms MCC approved the Mongoose in 2009. One row bundles 3 different sources under one URL. |
| S08 | The quoted note "contained no alterations to the Laws but corrections and a few additions to the Notes" is **not in the local copy** `acs_1947_second_edition.txt`. The web page could not be fetched (quota), so this is unverified. |
| S17, S18 | Project-derived; fine as registry entries, but S17 is used to support "AI clean-up invented" in cases where raw OCR shows OCR misreads (see section 6). |

## 6. DATA_INTEGRITY_FINDINGS.md table: verification

| Edition | Claim | Verdict |
|---|---|---|
| 1947 | Text 9 to 9 1/8 in.; raw has no digits; ACS 8 13/16-9 | **Confirmed.** Raw l.147 reads "not less than inches, nor more than 9 inches". The clean-up invented the lower figure *and* changed the upper limit from 9 to 9⅛. ACS 1947 l.73 confirms 8 13/16-9. |
| 1952 | 8 7/8-9; bat 4 1/2; bails 4 1/2; raw "8ti?", "42"; ACS 8 13/16-9, 4 1/4, 4 3/8 | **Confirmed** (raw l.191, 211 and 228; ACS 1st, 2nd and 4th editions). |
| 1962 | Bat 4.5; bails 4.5; projection 1 in.; raw "4\|"; ACS 4 1/4, 4 3/8, 1/2 | **Partly confirmed.** Bat and bails are as stated (raw "4\|"). The projection's raw OCR already reads "**1 inch**" (raw l.197), so that error is an OCR misread, not a clean-up invention. |
| 1968 | Covers 8 ft; bails 4 5/16; bat 4 1/2; raw "distance than feet", "4-J"; ACS 3 1/2 ft, 4 3/8, 4 1/4 | **Confirmed**, with a precision fix: "4-J" is the bails reading (raw l.197); the bat's raw has no digit at all ("exceed inches", l.177). The ACS comparison is with the 1970 4th edition (and the 1st and 2nd editions all agree). |
| 2000 | Ball 8 3/4; women 4 7/8, 5 5/8 oz; no matching figure in raw; MCC 2010 8 13/16, 4 15/16, 5 5/16 | **Confirmed.** Raw "8'K>" is garbled. Raw "5s/i6" (l.617) actually reads 5⁵/₁₆, which contradicts the processed 5⅝ and strengthens the claim. MCC 2010 (S01 l.495 and 530) confirms. |
| 2010 | Ball 8 15/16; junior 8 5/8; raw "n/a" | **Partly refuted.** Raw exists. The ball reads "**815/16** in/22.4cm" in raw OCR (l.587), so it is an OCR misread, not an AI invention. The junior value is a clean-up error (raw "8“/i6", i.e. 11/16). Missed: women's lower limit "8 1/2" (raw "8V2"; MCC 8¼). |
| 2017 | Ball circumference "8.25 m"; raw n/a | **Inaccurate.** The men's ball reads "8.81 m/22.4 cm ... 9 m"; "8.25 m" is the women's lower limit. Raw exists and reads "m" in both 2017 and 2019 (an OCR misread of "in"; the 2019 clean-up corrected it, 2017's did not). This is not an invented number. |
| 2019 | Bat covering 0.004 in./0.1 cm; raw n/a; MCC 2026 0.04 | **Confirmed**, but raw is not "n/a": it reads "0 04 m/0.1 cm" (raw l.4247), so the clean-up turned a correct 0.04 into 0.004. S02 l.2847 confirms 0.04 in/0.1 cm. |

Other statements in the document:
- **1952 text and Laws 30/31: refuted.** The 1952 dataset text has Law 30 "except his hand" with Note 1 "deliberate
  kicking or 'kneeing' ... shall immediately call 'Dead Ball'", and Law 31 "if either or both of the bails be previously
  off". Both are exactly ACS's *Original* (pre-amendment) 2nd-edition wording (`acs_1947_second_edition.txt` l.596-599
  and l.618). The 5 May 1954 versions ("hand holding the bat"; "if both bails be off") are **not** in the 1952 text.
  This instance therefore gives no evidence that the "1952" printing post-dates 1954. (It differs from the 1947 text in
  Law 30 Note 1, which matches ACS's 1952 second edition.)
- **1890 reversion: confirmed, with a caveat.** 12 of the 39 modified records from 1890 to 1892 return to wording found
  verbatim in 1884 but not in 1890. Several are transcription typos in the 1890 dataset text ("commencemen", "no less
  than"), not evidence of a separate printing.
- Counts: 16 `cleaning_artefact_numeric` labels, 21 `suspect`, 112 UNCATEGORISED and 459 rows: **confirmed** in the CSV.
  However, 2000_2008 E051 is not a cleaning artefact (layout), and 2008_2010 E096, 2010_2017 E083 and 2017_2019
  E048/E049 are OCR misreads rather than AI-invented numbers. The opening claim "the clean-up sometimes invents a
  plausible number" holds for 1947, 1952, 1962 (bat/bails), 1968, 2000, 2010 (junior) and 2019, but not for every row.
- The "Laws 2/3 boundary in 2017/2019" relocation statement is **confirmed** (2017_2019 E027 and E038-E040 are verbatim
  moves).

### NOT_A_CHANGE / cleaning_artefact_numeric claims requested

| Label | Verdict |
|---|---|
| 2000_2008 E046 | Confirmed (not a change). The mechanism is clean-up of garbled OCR. |
| 2000_2008 E047 | Confirmed; raw "5s/i6" supports it. |
| 2000_2008 E051 | Not a change, but the reason is wrong: the figures are present, displaced by the table layout. This is a segmentation artefact. |
| 2008_2010 E096 | Confirmed not a change; the mechanism is an OCR misread (raw "815/16"). |
| 2008_2010 E098 | Confirmed (junior); a second artefact in the same record was missed (women's 8 1/2). |
| 2010_2017 E083 | Ball part confirmed (OCR mechanism); other records in the event are real changes. |
| 2017_2019 E009 | Confirmed; raw "0 04 m". |
| 2017_2019 E048 | Not a change, confirmed; what_changed quotes wrong numbers; OCR unit misread in both years. |
| 2017_2019 E049 | Confirmed; the same OCR mechanism. |

## 7. Systematic patterns of error

1. **Artefact or wording-only labels applied to whole events that mix noise with real changes.** The event grouper puts
   a real rewrite and segmentation noise in one event, and the label then describes only the most visible record
   (2017_2019 E057 and E060; 2008_2010 E074; 2010_2017 E083; many 2008_2010 `wd()` labels).
2. **Using a template helper as the cause.** `wd()` (2008_2010), `conseq()` and `reorg()` (2010_2017) attach a general
   source statement as a `stated` cause and assert "rule unchanged" without per-event checking. Most of the "wrong"
   verdicts come from these helpers.
3. **The coverage gap at triage.** Events triaged `wording_only` never reach the label CSV. That excludes 6 of the 22
   MCC 2019 changes and other real edits (2000_2008 E014/E015/E018: Law 2.6 penalties removed from the boundary and
   Lost ball provisions; E041: the 42.7 warning sequence changed; 2008_2010 E030, E038, E089, E097).
4. **Secondary-press handling.** Phrases are put in quote marks that are not in the source, and journalists' words are
   attributed to MCC.
5. **Available stated causes not used** (S07; S03 for the 2013 Laws 24.6, 19/32 and 30; the tethered-bails text; S06's
   MCC quote on the non-striker run-out), while weaker or contradicting sources are used elsewhere (S22).
6. **Numeric-artefact mechanism overgeneralised.** Several "AI clean-up" findings are OCR misreads that are already
   present in the raw text. The conclusion (not a change to the Laws) is still right.
7. **"New" asserted without checking the old edition** (2000_2008 E025; 2008_2010 E005 and E006; 2010_2017 E027 and
   E053).

## 8. Verified correct

- All verbatim S04 quotations in p2017_2019 except two minor edits, and every S02 and S03 quote except one unmarked
  omission.
- The 2017_2019 label-to-MCC mapping for 14 of the 22 changes. The Law 2/3 relocation artefacts.
- 2000_2008 UNCATEGORISED descriptions (17 of 20 accurate); E046 and E047 artefacts.
- 2008_2010 UNCATEGORISED labels E010, E019, E022, E026, E027, E033, E037, E041, E042, E050, E051, E054, E062, E064,
  E065, E069, E071 and E093 describe their records correctly; E103 and E104 are format artefacts.
- 2010_2017: E001, E005, E011, E016, E017, E024, E029-E032, E034, E038, E042, E043, E049-E051, E054-E056, E065, E069,
  E071, E076-E082, E084, E086, E087, E094, E099 and E101 are acceptable.
- DATA_INTEGRITY rows for 1947, 1952 and 2000, and the counts.

## 9. Residual risks

- In 2010_2017 the large events (E002, E003, E029, E090, E062 and others with more than 20 records) were checked on
  their first records plus targeted searches. Further hidden substantive edits are likely, given patterns 1-2.
- Unverified web sources: S08 (the quoted note is missing from the local copy), S13, S20 and S21 (HTTP 403). The S06
  attributions rely on WebFetch summaries (one exact-phrase search negative for "No reason stated").
- Edition identity: the "2008" text already contains the 52%-handle rule. Whether that rule pre-dates the 2009
  Mongoose approval was not confirmed from an MCC source, so a later-printing issue for "2008" cannot be excluded.
- These findings apply to the current labels and to `sigs.json`-guarded events. Any pipeline re-run (by another
  reviewer) may renumber events.
