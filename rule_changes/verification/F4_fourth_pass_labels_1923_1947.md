# F4 – Fourth-pass verification of labels 1923→1932, 1932→1939, 1939→1947

Verifier: independent adversarial pass (read-only; nothing in the project was modified except this file).
Scope: `labels/q1923_1932.py`, `q1932_1939.py`, `q1939_1947.py`, the matching rows in `data/categories/event_labels_all.csv` (185 rows: 39 + 56 + 90; 6 are mechanical labels), the new sources S38-01..04 and S39-01..02.
Method: every event was printed with `show_events.py` (up to 60 records, 600–900 chars) and checked against the raw OCR (`1923_raw.txt`, `1932_raw.txt`, `1939a_raw.txt`, `1947_raw.txt`), the processed 1947 text, the ACS 1947 transcription (`acs_1947.txt`), the Rait Kerr text and `raitkerr_chronology.csv`. The 1932→1939 "moves" were checked with a 3-gram overlap script (run from the scratchpad) on every `add` record against `1932_raw.txt`, and then by hand.

## Verdict summary

| Pair | Rows | Correct | Minor | Wrong |
|---|---|---|---|---|
| 1923_1932 | 39 | 38 | 1 | 0 |
| 1932_1939 | 56 | 55 | 1 | 0 |
| 1939_1947 | 90 | 76 | 13 | 1 |
| **Total** | **185** | **169** | **15** | **1** |

Overall the labels are good. The Rait Kerr serials 122–138 (and u1–u5 for 1947) are matched correctly. Every Rait Kerr and MCC-preface quote I checked is exact, apart from OCR noise in the source. No numeric claim is wrong. The one substantive error is that a 1939 rule dropped in 1947 is labelled as a move (E028/E027). Most minor problems are real changes inside STRUCTURAL labels that the label does not mention, or `stated` used where the project's own rule calls for `inferred`.

### Checks that passed
- **Rait Kerr serials.** 122 (ball), 123/124 (follow-on, declarations), 125 (wicket), 126 (rolling), 127 (Law 41), 128 (l.b.w.), 129–138 and the unnumbered 1947 entries (Pitch, Special Regulation, Dead Ball Law, l.b.w. full pitch, umpires no longer pitch wickets) are all matched to the right events, by date and subject. The quotes match the text: ch.4 "unwittingly provided an admirable trial of a smaller ball, which in 1927 was legalised" (l.2900), "twenty-eight inches by nine inches" (l.2911), "primarily directed towards reducing the number of drawn matches" (l.2997), the direct-attack passage (l.2921–2975); ch.5 terms of reference (l.3211), "Bradford Central Cricket League in 1943" (l.3206), last over and bail disturbance (l.3271–3290), "Sixty old Laws ... condensed into forty-seven" (l.3324), "enabled several of the old Notes to be dropped" (l.3329), "The only alterations in the conduct of the game ..." (l.3332).
- **S12** (Chandler) was re-fetched. It contains "simply to tilt the delicate balance between bat and ball back in favour of the bowler" and says the change was experimental in 1935 and made permanent two years later. So the E019 (1932_1939) citation is correct.
- **1939 dating tags.** All of them are in `1939a_raw.txt` (l.150, 179, 194, 213, 249, 260, 312, 352, 493, 565, 608, 697, 875, 916, 926, 946). The tag-only events are correctly labelled `notes_revision`/derived. E050 rightly notes the tag's "10th July, 1894" against Rait Kerr's "June 10th 1894".
- **1923/1932 instruction sections.** The "Notice to Umpires" in `1923_raw.txt` (l.725–735) has the over and two-minute paragraphs with "should" (E007 1923_1932 correct). The 1923 Umpires section has "extra ten minutes" (l.893/896) and 1932 has "seven" (l.612/615) (E036 correct). The 1932 Umpires section has "one hour" and 1923 has "half an hour" (l.796 / l.849), so E026 1932_1939 is correct. 1932 has "Law 13" for Law 43 (l.772; 1923 has 43), so E044 is correct. 1932 has "seven minutes between the innings" (l.805), so E042 is correct.
- **25+ "moves" in 1932→1939 checked** (most well over 25). All of these are found verbatim or near-verbatim in the 1932 book's unsegmented sections (3-gram overlap ≥0.7, then confirmed by eye):
  - E008: the "Over" call, "Time" before the over is finished, round/over the wicket, over/underarm.
  - E026: where the umpire stands, the off-side permission, watch or clock, no interference except on appeal, report to the ground manager, scorers.
  - E034: retired innings counted "Not out".
  - E035: a side that fielded with ten may bat with full strength.
  - E038: 200-run new ball, informing the batsmen, balls approved by the captains.
  - E040: tricks, sole judges, attention to Law 48, the seam (1932 OCR "scam"), resin, ground fitness, inspection after rain, unfit ground, appeals at the start of a match.
  - E041: call a boundary, ball touching the boundary is dead, umpire not a boundary, umpire decides, six runs, Law 2 prevails, wilful act of a fieldsman.
  - E042: luncheon 40 minutes.
  - E043: the "Out" signal, call distinctly, batsman understands the decision, alter a decision.
  - E044: appeal to the other umpire.
  - E047: short run, batsmen do not cross.
  - E056: rolling supervision, foot-holes, overseas Law 9*.

  The text flagged as new really is absent from the 1932 raw text. The new items are: the no-ball for throwing at the striker, the slipped ball, the customary "Over" call, bails blown off, no-ball for changing the mode of delivery, the tie definition, remaking the wicket, kicked on to the wicket, "hugged" catch extended to pads/clothing, the bat-or-hand l.b.w. note, a piece of bat breaking the wicket, the score-book entries, "spirit of this Law", the lost-ball replacement, the bowler throwing at the wicket, intervening without appeal, the bodyline procedure, consultation on light, grounding over the boundary, sight screens, involuntary boundary, boundary overthrow, "Not out" call, walking batsman, appeals after "Time", metal stumps, no bails in high wind, ground executive, Law 9* supervising officer.

  The hidden real changes are described and carry a secondary UNCATEGORISED: reporting time one hour→30 min, Minor Counties added to the new-ball rule and the rule made optional elsewhere, the dissent procedure, light consultation.
- **The 21 "removed old Law merged" events in 1939_1947** (E005, E008, E013, E015, E039, E041, E043, E046, E047, E052, E057, E063, E069, E079, E080, E083, E084, E088, plus E001/E002 sections). E003 and E082 are separately UNCATEGORISED. Each destination was confirmed in the 1947 processed text and ACS 1947:
  - Law 26 "bowled, not thrown or jerked"
  - Law 40 "wilfully obstruct the opposite side"
  - Law 41 crossing sentence verbatim
  - Law 2 "may indicate positions in which the Substitute shall not field"
  - Law 2 Note 2 "Laws 36, 40 or 41" (covers every way a runner can infringe; no loss)
  - Law 3 "consent of both Captains"
  - Law 16
  - Law 9

  Absence was also confirmed: no Single Wicket Laws and no betting clause in the 1947 raw or ACS text (E003, E082 correctly UNCATEGORISED).
- **The 18 restructures with a secondary UNCATEGORISED** (E002, E004, E006, E019, E023, E024, E026, E032, E034, E040, E048, E049, E051, E062, E064, E065, E070, E089) describe their real changes correctly, with the exceptions noted below. Checked:
  - luncheon 40→45 (1947 raw)
  - "luncheon or tea"
  - "Retired, Out"
  - both feet inside the field for a catch
  - "spirit of this Law" hardened to an infringement
  - penalty credited to striker/extras, cap Note
  - toss 15 minutes before play, decision irrevocable
  - tie narrowed to played-out matches
  - wax/towel, pitch damage and run-stealing Notes
  - MCC Secretary reporting and the tricks Note dropped (absent from 1947)
- **E081 integrity is confirmed.** `1947_raw.txt` l.146–148: "not less than inches, nor more than 9 inches in circumference" (lower figure missing). Processed text: "not less than 9 inches, nor more than 9⅛ inches". ACS 1947 l.73: "not less than 8 13/16 inches, nor more than 9 inches". 1939 raw l.146–148: "eight and thirteen-sixteenths ... nine inches". So nothing changed, and the clean-up invented both figures (it also moved the upper limit to 9⅛). Secondary NOT_A_CHANGE/cleaning_artefact_numeric with `integrity=suspect` is correct.
- **E089 figures are confirmed** by `1947_raw.txt` l.177–190 and ACS l.122/125: 9 in., 28 in., bails 4 3/8 in., ½ in. projection, dome-shaped stump tops.
- **E013 (1923_1932).** The 15 June 1931 Committee insert is at `1923_raw.txt` l.350–359 and is correctly treated as an interpretation first printed in the Laws in 1932.
- **Mechanical/NOT_A_CHANGE/SEMANTIC_WORDING sample: 42 rows read in full.** These were all 19 NOT_A_CHANGE rows in 1923_1932 plus its 5 mechanical rows, 3 NOT_A_CHANGE and 4 SEMANTIC_WORDING rows in 1932_1939, and 7 NOT_A_CHANGE rows (including mechanical E056) and 4 SEMANTIC_WORDING rows (E044, E066, E067, E006/E011 of 1923) in 1939_1947. No hidden real change was found among the NOT_A_CHANGE rows. E085 (bat 4¼ in./38 in.) matches ACS l.92. The SEMANTIC_WORDING rows are reasonable. E066's "change the ball for one which has had similar wear" is a small real change, but it is described in `what`.

## Problems

| # | Event | Severity | Evidence | Correct reading |
|---|---|---|---|---|
| 1 | 1939_1947 **E028** (and E027) | **Wrong** (medium) | 1939 Over Note (f): "If a bowler is injured so that he cannot finish the over he has begun, the over shall be regarded as completed." 1947 Law 24: "A Bowler shall finish an 'Over' in progress unless he be incapacitated or be suspended for unfair play." "regarded as completed" appears in 1947 only in Law 46 Note 4(vi)(i), for the unfair-bowling case (processed l.471; ACS l.837). E027 says "injured bowler -> Law 24"; E028 is `consolidation_merge`, high, with no secondary. | The rule that an injured bowler's unfinished over counts as complete is **dropped**, not moved. Law 24 now only says when a bowler need not finish, which implies another bowler completes the over. This is a real change with no stated cause: add `sec=UNCATEGORISED/no_cause_stated` to E028 and correct the E027 wording. |
| 2 | 1939_1947 **E002** (and E026) | Minor | 1939 One-day note (b): "If the captains are unable to agree, the umpires shall decide if there is sufficient time left ...". 1947 Law 22 Note 2: "a one-day match shall not be regarded as finished on the result of the first innings if the umpires consider there is a prospect of carrying the game to a further issue" (ACS l.382). | The label says the umpires' decision simply moves to Law 22 Note 2. In fact the captains' first say is removed (umpires alone decide). This is a hidden real change. Mention it in `what`; the existing secondary UNCATEGORISED covers it. |
| 3 | 1939_1947 **E002, E014** | Minor | Both have basis `stated` on "Sixty old Laws, including three for one-day matches, were condensed into forty-seven" (ch.5 l.3324). | That sentence describes the outcome of the whole revision, not the cause of these merges. Under the guide's own rule ("a preface that states the aim of a whole revision ... use inferred"), and to match the TOR-based labels, the basis should be `inferred`. |
| 4 | 1939_1947 **E054** | Minor | 1939 Law 24: ball "shall have been pitched in a straight line ...". 1947 Law 39: "shall have, or would have, pitched" and "even though the point of impact be above the level of the bails". | On the face of the text, l.b.w. is extended to full tosses and to impacts above the bails. Rait Kerr calls it "more closely defined" but gives no cause. Under the restructure rule, a `codification_definition` label should carry `sec=UNCATEGORISED`. |
| 5 | 1939_1947 **E009** | Minor | 1939 Law 9 Note (c): the ground "shall be protected every night during the continuation of a match ... removed each morning, if fine, at 7 o'clock". 1947 Law 11 Note 1: "It is usual ... to protect the bowlers' run up ... both at night and ..."; "removed early each morning, if fine". | Mandatory nightly covering ("shall") becomes customary ("usual"). This is a modal/real change with no secondary category; add `SW/modal_strength` or UNCATEGORISED. |
| 6 | 1939_1947 **E023 / E004** | Minor | E023 lists "'A side should not field with more than eleven players' added" under Law 2. Processed 1947 l.5 and ACS l.5 have it as **Law 1 Note 2**. E004 (Law 1) omits it. E023 also omits serial 129's "N.B. Subject to consent a substitute may keep wicket". | Move the Note to the Law 1 label and mention the wicket-keeping N.B. in E023. |
| 7 | 1939_1947 **E080, E022** | Minor | E080: "with a new 'One short' signal". The signal is in the 1932 signal code (`1932_raw.txt` l.824–826) and in the 1939 Notes for Scorers. | Not new: the existing signal is restated inside Law 19. |
| 8 | 1939_1947 **E042** | Minor | 1939 (f): "the umpires are not justified in remaking the wicket until the ball has become 'dead'". 1947: "it is not the umpire's duty to remake the wicket until the ball has become 'dead'" (processed l.290). | A prohibition becomes "not a duty". This is a small semantic change that the label does not mention. |
| 9 | 1939_1947 **E089** | Minor (acceptable as low/inferred) | The cause rests on S39-01. That page still returns empty content: my own WebFetch on 2026-10-27 got "content ... empty", and the source was never read. Rait Kerr does not mention the bail length or the dome-shaped tops anywhere (searched ch.4–6 and the chronology). | Low/inferred is acceptable only if the rationale stands without the unread source. Add the arithmetic: two 4½ in. bails exactly fill the 9 in. wicket (they can jam), while two 4⅜ in. bails leave ¼ in. This supports "prevent jamming" as an inference tied to serial 135. Otherwise fall back to UNCATEGORISED. The bail-length change (First-class 4½→4⅜) is a real change missing from Rait Kerr's chronology; say so. |
| 10 | 1939_1947 **E021** | Minor | S39-02 (unread; only search-snippet content) is listed in `evidence`. | The cause is fully stated by Rait Kerr ch.5 l.3271–3276, so S39-02 adds nothing verifiable. Keep it out of the evidence list, or leave it in the rationale only, marked unverified. |
| 11 | 1939_1947 **E081** | Minor | Real changes (Minor Counties dropped from the 200-run new ball; balls approved "by the umpires and captains"; replacement "should have had similar wear") have no UNCATEGORISED secondary, because the single secondary slot holds the NOT_A_CHANGE artefact. | Acceptable given the schema, but `notes` should state that these changes have no stated cause. |
| 12 | 1939_1947 **E036** | Trivial | The 1939 Wide note (c) ("When only one run has been made from a 'Wide Ball' the batsmen do not cross over ...") is dropped in 1947 and not mentioned. | Mention it as a dropped Note. |
| 13 | 1923_1932 **E028** | Minor | The rationale says seam-lifting "moves to the Bowlers instructions". The 1923 book already had the seam paragraph in THE BOWLERS (`1923_raw.txt` l.742–745). | The Law 4 note is simply dropped and its seam clause duplicated an existing Bowlers paragraph. Nothing moved. |
| 14 | 1932_1939 **E039** | Minor | 1932 Law 41: "five runs added to the score; whatever runs may have been made, five only shall be added". 1939: "five runs added to the run or runs already made". | On the face of the Law this is a real scoring change (Rait Kerr: "It is made clear"). STRUCTURAL `codification_definition` plus secondary UNCATEGORISED is defensible because the 1923 note gave that interpretation, but `what` should call it a change to the Law text, not only a clarification. |

## Sources S38/S39
- **S38-01** (`1939a_raw.txt`): the preface (l.67–75) matches the note ("rendered necessary by changes in the Laws of the game, in the Rules governing International and County Cricket, and by additions to the notes ..."; "lettering and sub-division of the notes"; Index). The first-class-fixture Note is under Classification of Counties (l.1379–1380), which confirms 1932_1939 E003.
- **S38-02** (`1932_raw.txt`): the preface (l.10–25: "Hundreds of cases are sent to the M.C.C. ..."), the title page (l.30–32: "... 1927, 1928 & 1931"), the slip "ALTERATIONS OF LAWS 24 AND 41" (l.377–396, 5 May 1937 / 6 May 1936) and the overseas section (l.131–152) all match. Correct.
- **S38-03** (`1923_raw.txt`): "1920 & 1922" (l.138) and the 1931 Note on Law 21 (l.350–359) match. Correct.
- **S38-04** (`data_appendix.xlsx`): the 1923 row confirms the removed 1931 note and the dropped signalling headers. I did not inspect the 1932/1939 rows cell by cell.
- **S39-01, S39-02**: correctly flagged LOW/UNVERIFIED. My WebFetch of S39-01 also returned an empty page. They cannot support any `stated` basis, and they currently support none. They are used only as secondary supporting cites in E021 and E089 (see problems 9–10).

## What I could not verify
- The text of S39-01 and S39-02 (Papers Past returns empty pages).
- The 1932/1939 rows of S38-04, cell by cell.
- Whether the 1923→1932 "first-class fixture" note was printed in the 1923 book's county rules. It is not in the 1923 raw Laws text, and I did not read the 1923 county section in full.
- The 1939b raw OCR (only 1939a was used).
- ACS pages carry later amendments. All 1947 wordings relied on here were also confirmed in `1947_raw.txt`/processed, except the ACS-only ball circumference, which is the point of E081.
