# Verification B: event labels 1947 -> 2000 (pairs 1947_1952 ... 1992_2000)

Reviewer scope: every label in `data/categories/post1947_event_labels.csv` for pairs 1947_1952, 1952_1962, 1962_1968,
1968_1980, 1980_1992 and 1992_2000. That is 191 labels; another 17 events were triaged `wording_only` and never labelled. Each
label was checked against its change records (`data/changes/*.jsonl`), the processed and raw edition texts, and the saved
evidence texts (`data/evidence/text/`, Rait Kerr 1950 txt). Where a source has no local copy (S08 index page, S12, S13), I
fetched the live page once and say so below. Read-only: no file other than this report was changed.

## Verdict summary

| | count |
|---|---|
| Labels checked | 191 (1947_1952: 30, 1952_1962: 14, 1962_1968: 13, 1968_1980: 63, 1980_1992: 15, 1992_2000: 56) |
| OK (no issue found beyond the systematic `basis` point below) | 134 |
| Minor issue (MEDIUM/LOW: incomplete or partly wrong description, weak basis, imprecise date) | 47 |
| Wrong (HIGH: wrong date/cause, false claim, or a real policy change labelled as structure/wording) | 10 |
| Real changes missing from any labelled event (unlabelled `wording_only` triage or records grouped into no event) | 5 important ones, 2 of them HIGH |

The numeric-artefact (NOT_A_CHANGE / cleaning_artefact_numeric) labels are **all confirmed** in substance. The problems are
mostly in three places: (1) the 1947-1962 dating of the Law 30/31 amendments; (2) STRUCTURAL/consolidation_merge labels
in the 1980 and 2000 rewrites that hide real policy changes; (3) a few factual misstatements (Law 39 = LBW, Lost ball is
still Law 20, practice was in Law 15).

## Problem labels

| pair:event | sev. | What is wrong | Evidence | Proposed correction |
|---|---|---|---|---|
| 1947_1952:E011 | HIGH | Dates the kicking/"kneeing" Note and the raised-knee signal to the **5 May 1954** amendment and doubts the 1952 text's printing date. Both are **original 2nd-edition (1952)** wording. The 1954 amendment changed only the Law body ("except his hand" -> "except his hand holding the bat"). | ACS 2nd ed. (S08) "Original Law 30 ... except his hand ... Notes on Law 30: The umpire shall regard the deliberate kicking or "kneeing" ... shall immediately call "Dead Ball" ... "Leg Bye" by touching a raised knee", under "Law amended May 5th 1954 [see original]". Dataset 1952 Law 30 body still reads "dress or person except his hand," (processed l.256), and Law 19 and Law 46 (vi) are still pre-1953 there, so the 1952 text is a genuine 1952 printing. | date_evidence: "Wording of the 2nd edition as adopted 7 May 1952 (ACS 'Original Law 30')". Delete the printing-date speculation. Category UNCATEGORISED is fine. |
| 1947_1952:E026 | HIGH | Same error: "Part of the 5 May 1954 amendment of Law 30". | As above: the raised-knee signal is in ACS "Original Law 30" Notes. | Date = 2nd edition 1952. |
| 1947_1952:E005 | HIGH | Says "The reason for dropping it is not stated". The cited source S09 states it. | acs_1947.txt: "In September 1951 the Australian Cricket Board of Control agreed that the follow-on margin should be 150 rather than 200. Subsequent to that date, the Note was no longer published with the Laws." | basis `stated`, date Sept 1951 (S09). Cause: Australian Board aligned its margin with the Law, so the local variation was abolished (STRUCTURAL/consequential, or EXTERNAL_FORCE; the cause is stated either way). |
| 1947_1952:E010 | MEDIUM | Rationale: "Laws 30 and 31 as amended on 5 May 1954 refer to it". The Law 31 Note 5 reference to "Law 25, Note 4" is already in the original 2nd edition. | ACS "Original Law 31 ... Note 5: ... as defined in Law 25, Note 4". | Drop the 1954 clause. |
| 1947_1952:E013 | MEDIUM | date_evidence "Law 31 amended 5 May 1954". That amendment is the body change (both bails) that first appears in 1962 (1952_1962:E009). The Note change here is 1952. | ACS Original vs. amended Law 31. | Date = 2nd edition 1952. (Note also that ACS gives "dress and equipment as defined"; the dataset/raw 1952 gives "dress as defined" (raw l.635). The difference is unresolved, so flag it.) |
| 1947_1952:E012 | LOW | note: "Law 31 was genuinely amended on 5 May 1954 (ACS) but that wording is in both editions' text here". False: the 1954 wording ("if both bails be off") is in neither. | 1952 processed l.269-270 "if either or both of the bails be previously off"; 1962 l.301 "if both bails be off". | Remove the note. |
| 1947_1952:E031 | LOW | "raw 1947 OCR has no digits for the lower and upper limits". The upper limit is present. | raw 1947 l.147-148 "not less than inches, nor more than 9 inches". | "No digits for the lower limit". The conclusion stands. |
| 1947_1952:E006 | LOW | "removed from the Law text". In 1947 it was Note 2 on Law 1. | acs_1947: "Notes on Law 1 ... 2. A side should not field with more than eleven players." | "Note 2 on Law 1 replaced by the new Note (E001)". |
| 1952_1962:E002 | MEDIUM | ENJOYMENT/avoid_draws, basis `inferred` from Rait Kerr (1950). Rait Kerr predates 1957 and is describing the 1889 declaration Law. The quote is accurate ("Both were primarily directed towards reducing the number of drawn matches"), but it cannot be evidence for 1957. S13 (verified online) says only "It was not until 1957 that a declaration on the first day was authorised." | Rait Kerr txt l.2996-2998. | basis `conjecture` with confidence low, or UNCATEGORISED with the Rait Kerr context in notes. |
| 1952_1962:E004 | MEDIUM | Says "the old rule that only one run is deducted on 'One short' is removed". It is restated ("One run only is deducted if both batsmen are short in one and the same run"). Omits the new anti-abuse provision on deliberate short running, which is ACS Note 3(3), late 1962/early 1963. | change records 0077, 0079; ACS 2nd ed. l.168. | Describe: short run defined; one run deducted for the same run; deliberate short running -> Dead ball, runs disallowed (new, 1962/63). |
| 1952_1962:E008 | MEDIUM | "the 1954 provision treating deliberate kicking". The 1952 text carries the original 1952 wording ("shall immediately call Dead Ball"). | 1952_1962_0072 OLD text; ACS "Original Law 30". | "the 1952 provision". |
| 1952_1962:E010 | MEDIUM | Wrong Law title: "New Note 1 on Law 39 (Stumped)". Law 39 is L.B.W. | ACS 2nd ed. "Law 39 - L.B.W. ... Note 1 was added ... late 1955 or early 1956". | "(L.B.W.)". |
| 1952_1962:E011 | MEDIUM | Puts all of E011 under the 15 Apr 1953 MCC statement. "Request" -> "Direct", the new "The captain shall take the bowler off as directed" and "justified in preventing" -> "duty ... to intervene" are later and undated. Basis `stated` for notes_revision is also questionable: the source states the trial outcome, not a structural reason. | ACS 2nd ed. (which already has the 1953 revision) still reads "Request the captain ..." and "The umpires are justified in preventing players from causing damage". | Split: 1953 intimidation wording (dated, stated) vs. later undated changes (UNCATEGORISED). Consider the primary category for the 1953 change (intimidatory bowling). |
| 1952_1962:E003 | LOW | "ACS: Note added 1 May 1957". The 1957 Note was a narrower version (last over of match, weather/bad light), amended late 1959/early 1960 to the form in 1962. | ACS l.145-152. | Add the 1959/60 amendment. |
| 1952_1962:E013 | LOW | Lists "umpires empowered to have the pitch dried without reference to the captains" as new. It was already in the 1952 text. | 0064 old: "umpires who shall be empowered to have the pitch dried, without reference to the Captains". | Remove it from the list of changes. |
| 1952_1962:E014 | LOW | "the 1962 text has the correct 8.8125". The value is correct, but it was also produced by the AI clean-up from garbled OCR. | raw 1962 l.153 "not less than 8-$- inches". | Mark 8.8125 as unsupported by the raw OCR (correct by luck). |
| 1952_1962:E016 | LOW | "the AI clean-up ... also changed the 1/2-inch projection to 1 inch". The raw OCR itself reads "1". | raw 1962 l.197 "project more than 1 inch above them". | "OCR misread 1/2 as 1". |
| 1962_1968:E014 | LOW | Called notation only. The 1968 '8 13/16' and '5 1/2' were supplied by the AI clean-up from garbled or missing OCR (correct values). | raw 1968 l.153-154 "not less than ounces ... not less than 8\|i". | Note the integrity point. Also note the 1968 bat '4 1/2' comes from a blank in raw ("not exceed inches"). |
| 1968_1980:E014 | HIGH | Described as restating the last-over Notes. It omits the major new **last-hour minimum of 20 six-ball (15 eight-ball) overs** with its deduction formula. | records 0379-0391; ACS 1980 l.303. | Add it to what_changed. UNCATEGORISED (no source) but substantive. |
| 1968_1980:E028 | HIGH | No-ball: omits the switch from the back-foot/bowling-crease rule to the **front-foot rule** ("some part of the front foot ... behind the popping crease"), the new definition of a throw, and the bowler attempting to run out the non-striker. | 0116/0445/0446/0464/0449; ACS 1980 l.464. Old 1968: "some part of one foot behind the Bowling crease". | Rewrite what_changed. Front-foot law: UNCATEGORISED unless a source is found. |
| 1968_1980:E030 | HIGH | Labelled STRUCTURAL consolidation "restructured under headings". It is a real change: leg-byes are now allowed when the striker "tried to avoid being hit by the ball" (1968: only an attempt to play with the bat). | 0482-0484; ACS 1980 l.521. | UNCATEGORISED (possible medical_safety, unsourced) + secondary consolidation. |
| 1968_1980:E036 | HIGH | "Law 3 restructured under headings". It hides a policy change: the umpires become sole judges of ground/weather/light (1968: the captains decided unless agreed otherwise), only the batting side may continue in poor light, appeals against light, and "Exceptional Circumstances". | 0318-0324 vs. 1968 Law 46 Note 5(a). | UNCATEGORISED, with the restructure as secondary. |
| 1968_1980:E043 | HIGH | "Caught restructured". It omits the new protective-helmet rules (no catch if the ball lodges in or has touched a fielder's helmet), an equipment-driven change, plus new boundary-catch rules. | 0498, 0500; ACS 1980 l.598, 601. | Primary EXTERNAL_FORCE/equipment (helmets): inferred at best, else UNCATEGORISED. |
| 1968_1980:E017 | MEDIUM | Restructure `stated`, but real changes are listed: no right of objection to substitutes; runner must be a team member who has batted if possible, with pads/gloves; a fielder absent >15 min may not bowl until back for that long. | 0006-0007, 0294-0296, 0305. | Primary UNCATEGORISED, with the restructure as secondary. |
| 1968_1980:E020 | MEDIUM | `wording_only` for a 12-record event that adds umpire-miscount, incomplete-over-on-resumption, bowler-incapacitated-during-over and non-striker-position provisions, and drops the UK 6-ball Note. | 0436, 0441-0443, 0234. | Split. The rest is consolidation/UNCATEGORISED. |
| 1968_1980:E056 | MEDIUM | "moves into the new Law 42". The test is loosened ("persistent ... systematic attempt at intimidation" -> "an attempt to intimidate"), and the caution goes to the captain. | 0287, 0288. | Flag it as substantive. |
| 1968_1980:E029, E032, E053, E063, E015, E047, E050 | MEDIUM | Restructure `stated` while new rules are added. Wide: striker moving in or out of reach (0468-0469). Appeals: timing now "before the bowler begins his run-up", and new withdrawal of an appeal (0194, 0535). Keeper: contravention now a no-ball (0520). Wickets: bails dispensed with by umpires, not captains; junior wickets (0031, 0346). Scoring: injured striker run out = no runs; obstruction runs (0402, 0405). Hit wicket: avoiding a throw-in (0507). Run out: leaving ground to avoid injury (0512). | change ids given. | Add `secondary UNCATEGORISED/no_cause_stated` and mention the substantive items. |
| 1968_1980:E002 | LOW | "watering sentence replaced by 'the pitch shall not otherwise be rolled'". The diff aligned the two sentences, but the watering ban remains. | 1980 processed l.228 "The pitch shall not be watered during a match." | Remove that clause. |
| 1968_1980:E013, E033 | LOW | E013 omits the tea-interval/9-wickets-down, drinks-interval and changed-interval-time rules. E033 omits "All the Stumps Out of the Ground". | 0368-0375; 0489. | Extend what_changed. |
| 1968_1980:E048 | MEDIUM | "out LBW, even if the ball pitched outside the off-stump line". Wrong: pitching outside off was already allowed. The 1972/1980 change is a ball **intercepted** outside the line of off stump with no genuine attempt to play. The label also quotes S13 as "'long, heated'"; the live S13 reads "long and heated controversy". S12's 15.2% is confirmed online. | ACS 1980 l.656 "even if the ball is intercepted outside the line of the off stump". | Fix what_changed and the quote. basis `stated` acceptable. |
| 1968_1980:E061 | MEDIUM | Primary NOVEL_EVENT/equipment_exploit although the label itself says the order is unresolved (Code approved 21 Nov 1979, ComBat in Dec 1979). S20's own registry note says sources "differ on the exact Law 6 change". S13 (live) only says "the Laws have provided that the blade of the bat must be made of wood". | sources.csv S20; S01 preface. | Primary UNCATEGORISED, with NOVEL_EVENT (attributed) as secondary, until the chronology is fixed. |
| 1980_1992:E012 | HIGH | `wording_only`, "treated as before". This is a real LBW change: a ball intercepted full pitch no longer has to "would have pitched in a straight line". | 0036 old: "or in the case of a ball intercepted full pitch would have pitched in a straight line between wicket and wicket" -> new "or was intercepted full pitch". | UNCATEGORISED (substantive LBW change). |
| 1980_1992:E007 | MEDIUM | Omits that a substitute may no longer keep wicket (1980: the opposing captain could object). | 0002. | Add it. |
| 1980_1992:E014, E016 | MEDIUM | EXTERNAL_FORCE/medical_safety with basis `inferred`, while the rationale admits "no source states the reason". S05 gives no reasons, and E016 is about where helmets are placed (a fielding advantage), not safety. This breaks the stated rule. | Rationale text; bop_2017 file (no reasons). | UNCATEGORISED, with a note on the helmet context. |
| 1980_1992:E010 | LOW | "tied to a new provision on running out the non-striker". Law 24.5 already existed in 1980. Cites S06 in the rationale but not in the evidence. | 1968_1980_0449. | Reword. |
| 1980_1992:E017 | LOW | Calls Law 42.10 the "over-rate procedure". 42.10 is Time Wasting. | ACS 1980 l.753-754. | Fix the name. |
| 1992_2000:E018 | HIGH | "Lost ball is no longer a separate Law". False: the 2000 text has "LAW 20 LOST BALL". The real changes are: the ball becomes dead on the call, a replacement ball, and runs = the greater of 6 or completed runs plus the run in progress. | 2000 processed l.1249-1251. | Rewrite what_changed. UNCATEGORISED secondary is fine. |
| 1992_2000:E014 | MEDIUM | "instead of a paragraph under Unfair play (Law 42, section 2)". In 1992 it was Law 15.2 (Start of Play). | 1992 processed l.534-538; 1992_2000_0398. | "formerly Law 15.2". |
| 1992_2000:E006 | MEDIUM | Covers "change in metric/imperial figures". It is a real change from 4 ft/1.22 m to **5 ft/1.52 m**, confirmed by the MCC 2010 text. | 0110; thapos l.822. | State 4 ft -> 5 ft. |
| 1992_2000:E016, E021, E024, E032, E035, E036, E037, E041 | MEDIUM | Unflagged `rewrite` (stated, no secondary) although each adds substantive rules. Boundaries: sight-screens outside the field, scoring "greater of". Dead ball: ball trapped, striker distracted. Leg byes: off a No ball scored as No-ball extras. Bowled: not out if the ball touched another player or umpire. Caught: catch precedence, catching beyond the boundary in the air. Handled ball: not out if avoiding injury. Hit twice: new run rules. Obstructing: returning the ball now obstruction. | records 0716/0742, 0790/0796, 0834, 0862, 0864/0870, 0881, 0894-0904, 0919. | Add `flagged=` (secondary UNCATEGORISED) like the other rewrite labels. |
| 1992_2000:E047 | LOW | Omits the new "Movement by wicket-keeper" unfairness and the glove-webbing rule. | 0938-0943. | Extend what_changed. |
| 1992_2000:E050 | LOW | The old record is only a cross-reference fragment "(The Bowling of Fast Short Pitched Balls), 42.9." in Law 22, not the bowling rule moving. | 0450. | NOT_A_CHANGE/segmentation_artefact. |

### Real changes not covered by any label (overlooked)

| where | sev. | change | evidence |
|---|---|---|---|
| 1952_1962 record 0034 (in no event) | HIGH | Law 30 body "except his hand" -> "except his hand holding the bat". This is the actual **5 May 1954** amendment. | ACS "Law amended May 5th 1954"; Original vs. amended Law 30. |
| 1952_1962:E001 (triaged wording_only, unlabelled) | HIGH | After-rain rolling Note extended from "Australia, South Africa, the West Indies, and New Zealand" to "Except in the United Kingdom". | ACS l.82-84 "It was changed sometime late 1962 or early 1963." |
| 1947_1952 record 0016 (in no event) | MEDIUM | "the West Indies" added to the same Note. | ACS 1947 vs. 2nd-ed. "Previous Version of Note 4". |
| 1952_1962 record 0011 (in no event) | MEDIUM | Law 16 "Laws 14 and 15" -> "Law 14" (consequential on the 1 May 1957 declaration change). | ACS "Law 16 ... Law amended May 1st 1957". |
| 1980_1992:E015 (unlabelled) | MEDIUM | Stumped rebound "other than a protective helmet" (a helmet rule). | 1980_1992_0040. |
| 1962_1968:E013, 1947_1952 record 0078 | LOW | Drying-regulation scope "in the United Kingdom" deleted; cross-reference Law 27 -> 25 corrected. | records 0127, 0078. |

Root cause: change records with `substantive=false` are never grouped into events (68/117 records in 1947_1952, 49/89 in
1952_1962, 118/144 in 1962_1968), and `wording_only` triage events are never labelled. Short insertions such as "holding
the bat" or "the West Indies" therefore disappear.

## Systematic patterns

1. **`basis = stated` for consolidation_merge is overstated (≈101 labels: the `restructure`/`rewrite` helpers).** The S01
   preface (verified verbatim: "to remove certain anomalies, consolidate various Amendments and Notes, and to achieve greater
   clarity and simplicity"; "to dispense with the Notes, to incorporate all the points into the Laws and to remove, where
   possible, any ambiguities") states the aim of the whole revision. It does not say that a particular provision was
   consolidation. Per provision, the honest basis is `inferred`.
2. **Restructure labels hide policy changes** (the issue in brief point f). This happens in 1968_1980 (E014, E028, E030, E036, E043 HIGH; ~10 MEDIUM)
   and in 1992_2000 (8 unflagged rewrites). The 1992_2000 module has a `flagged=` mechanism; 1968_1980 only uses it via `policy()`.
   Many restructure labels describe the first one or two records of a 10-30 record event.
3. **S11 (ACS "1980 Code") is not the 1980 printing.** It contains later amendments: helmet placement Law 41.4,
   "may request to have the pitch rolled", and stumped "other than a protective helmet". All of these are absent from the dataset's 1980
   text and appear in 1992. So "confirmed in the ACS transcription of the 1980 Code" does not confirm 1980 wording. The same
   applies to S08/S10, whose pages show amended text with the originals inset. The 1947_1952 dating errors come from reading
   the amended text as the 1952 text.
4. **"No source states a cause" was sometimes asserted without reading the whole cited source** (E005: the cause is in S09).
5. **Medical/equipment categories assigned on topic, not evidence** (1980_1992 E014, E016), contrary to the "no claim without
   evidence" rule.
6. Wrong Law names or numbers in what_changed: 1952_1962:E010 (LBW, not Stumped), 1992_2000:E014 (Law 15, not 42),
   1992_2000:E018 (Law 20 exists), 1980_1992:E017 (Time wasting, not over-rate).

## Verified OK

- **Numeric artefacts confirmed against raw OCR and the ACS/MCC texts:** 1947 ball (raw lower limit blank; ACS 8 13/16-9);
  1952 ball "8ti?", bat "42", bails "42" (ACS 8 13/16, 4 1/4, 4 3/8); 1962 bails "4|" (ACS 4 3/8, 1/2 in); 1968 covers
  "distance than feet" (ACS 1st/2nd/4th all 3 1/2 ft); 1968 bails "4-J" -> 4 5/16 (wrong; 4 3/8); 1968_1980 real covers change
  3 1/2 -> 4 ft (ACS 1980 l.217); 2000 ball raw "8'K>" -> processed 8 3/4 (MCC 2010: 8 13/16 in/22.4 cm). Format-artefact labels
  spot-checked (1947_1952 E004/E009/E014/E025/E027, 1980_1992 E019/E021/E022): correct.
- **Quotes verified verbatim:** S01 preface (1947/1979/1992/2000 entries, the Spirit of Cricket passage). Rait Kerr: "OTHER
  MEASURES ADOPTED TO ASSIST THE BOWLER", "most certainly did encourage seam bowling ... altered experimentally ... after a
  fixed number of overs", "primarily directed towards reducing the number of drawn matches", "nine ways", and "Wicket" confined
  to stumps and bails (E028 terminology). ACS 15 Apr 1953 statement. S08's "contained no alterations to the Laws but
  corrections and a few additions to the Notes" is **not in the saved local text**, but is on the live ACS index page (checked).
- **ACS dates verified:** Law 15/16 1 May 1957; Law 18 Note 2 late 1962/63 and amended 1968/69; Law 28 Note late 1962/63; Law 30
  Notes late 1955/56 and May 1965; Law 39 Note 1955/56; Law 5 65 -> 85 overs late 1966/67; Law 10 late 1966/67; forfeiture Note
  1968/69; Law 31 5 May 1954 (1952_1962:E009 correct).
- Online checks (no local copy): S13 does state the 1957 first-day declaration, the six-ball over worldwide from 1979, the
  1972 "played no stroke" change, and the wood blade. S12 gives the 1969 11.2%, 1970-71 8.0/8.2% and 1972 15.2% figures.
- Correctly cautious labels: 1962_1968:E011 (keeper Note absent from ACS 4th), 1992_2000:E051 (ball artefact), 1968_1980:E006,
  E009, E054, E060 and E062 (UNCATEGORISED with accurate descriptions), 1992_2000:E002 (Spirit of Cricket, stated).

## Residual risks

- S06, S19 and S21 have no saved text and were not checked. Labels resting on them (Timed out 1968_1980:E041, 1992_2000:E033)
  depend on unverified secondary claims, though their categories are UNCATEGORISED.
- For the 1952-1968 printings, ACS dates "to the nearest winter" sit near edition boundaries (e.g. 1968/69 provisions are in
  the "1968" text), so edition labels and printing dates can disagree.
- The ComBat chronology (1968_1980:E061) and the wood-blade clause's first printing are unresolved. It needs an original 1980
  printing.
- I read the 1992_2000 rewrite events at the record level only for the events listed. Very large events (E049 Law 42, 173
  records; E031 Law 3) were checked only against their flagged summaries.
- `DATA_INTEGRITY_FINDINGS.md` repeats the wrong claim that the 1952 text carries 1954 Law 30 wording. It should be corrected
  together with 1947_1952:E011/E026.
