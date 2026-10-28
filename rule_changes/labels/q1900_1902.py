"""Labels for 1900 -> 1902.

Context: the project's 1900 text is a Wright & Co. printing headed 'As Revised by the Marylebone Cricket Club, May, 1900' that does
not reproduce the official May 1900 revision faithfully (ACS transcription S36-02): it keeps the old compulsory follow-on wording,
prints the declaration Law as an unnumbered sub-clause of Law 53, omits Law 33b (1899) and has several printer's wording variants.
The 1902 text is Sir Francis Lacey's first annotated edition ('an edition of the Laws with full notes and interpretations', Rait Kerr
ch. 5), so most events here are new Notes, plus the May 1900 follow-on/declaration changes appearing one edition late.
"""
from _h import make
PAIR = "1900_1902"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
EN = "ENJOYMENT"

NOTES_WHY = ("Rait Kerr (ch. 5) states that the growth of cricket after 1884 and the M.C.C.'s readiness to answer enquiries 'led to a "
             "considerable increase in the number of interpretations and definitions, and in 1902, the then Secretary, the late Sir Francis "
             "Lacey, published an edition of the Laws with full notes and interpretations', all approved by the M.C.C. Committee. "
             "That explains the edition as a whole, not this Note individually, so the reason is inferred.")
NOTES_DATE = "First appears in the 1902 Lacey annotated edition (Rait Kerr ch. 5); interpretations approved by the M.C.C. Committee 'from time to time' before that."

# --- Single wicket / one-day segmentation and printing noise -------------------------------------------------------------
L("E001", "The whole Laws of Single Wicket block (1900, segmented as one Law '*') is 'removed'; the same ten Laws reappear in 1902 "
  "split into numbered Laws (see the matching new-Law event for the 1902 single-wicket block). Not a change.",
  NC, "segmentation_artefact", "high", "derived",
  "The 1900 single-wicket section was segmented as one block and the 1902 one as numbered Laws; the wording is the same apart from "
  "capitalisation and the clean-up errors labelled separately in the per-Law single-wicket events.", ["S18"])
L("E006", "The Single Wicket block appears as a 'new Law' in 1902 because of how the 1900 single-wicket section was segmented; the "
  "same ten Laws were already in the 1900 (and 1896) texts. Not a change.",
  NC, "segmentation_artefact", "high", "derived",
  "Pair of the removed 1900 single-wicket block; the text is the same rule set, only segmented differently.", ["S18"])
L("E003", "One-day matches: 'Prior to the commencement of a match it may be agreed that the over consist of five or six balls' (1900, "
  "numbered 3.) becomes unnumbered ':—that the Over consist of 5 or 6 balls' in 1902. Same rule.",
  NC, "segmentation_artefact", "high", "derived",
  "Same provision; only its list number, the number words/numerals and capitals differ. The official 1900 one-day text (ACS) already "
  "has it as part of one-day Law 2.", ["S18", "S36-03"])
L("E005", "Duplicate record of the one-day 5-or-6-ball-over agreement (old Law 3 of the one-day section) 'removed'; the provision is "
  "still in 1902 (see the relocated one-day over agreement). Not a change.",
  NC, "segmentation_artefact", "high", "derived",
  "The provision continues in the 1902 one-day section; the removal is a segmentation artefact of the lost list number.", ["S18", "S36-03"])
L("E007", "Single wicket Law 1: '22 yards' -> 'twenty-two yards', capitals, 'in line' -> 'in a line'. Same rule.",
  NC, "format_artefact", "high", "derived",
  "Numerals versus number words (same value; the 1896 text also has 'in a line'), capitalisation and punctuation only.", ["S18"])
L("E008", "Single wicket Law 10: 'overs' -> 'Overs'. Same rule.", NC, "format_artefact", "high", "derived",
  "Capitalisation only.", ["S18"])
L("E009", "Single wicket Law 2: '22 yards' -> 'twenty-two yards', 'bounds' -> 'Bounds', plus a stray page number '16'. Same rule.",
  NC, "format_artefact", "high", "derived",
  "Numerals versus words (same value), capitalisation and a printed page number caught in the text.", ["S18"])
L("E010", "Single wicket Law 3: capitalisation ('Bounds', 'Striker'). Same rule.", NC, "format_artefact", "high", "derived",
  "Capitalisation only.", ["S18"])
L("E011", "Single wicket Law 4: capitalisation and a comma ('“no hit,”' -> '“No Hit,”'). Same rule.", NC, "format_artefact", "high", "derived",
  "Capitalisation and punctuation only.", ["S18"])
L("E012", "Single wicket Law 5: 'byes, leg-byes' -> 'Byes, Leg Byes', capitals. Same rule.", NC, "format_artefact", "high", "derived",
  "Capitalisation and hyphenation only.", ["S18"])
L("E013", "Single wicket Law 6: the clause 'the Striker may run till the ball be so returned' is joined to the sentence in 1902; in "
  "the 1900 text it is a separate sentence ('The striker may run till the ball be so returned.') that was segmented apart. Same rule.",
  NC, "segmentation_artefact", "high", "derived",
  "The clause is present in the 1900 text (as its own sentence) and in the 1896 text (joined with a semicolon, as in 1902).", ["S18"])
L("E014", "Single wicket Law 7: 1900 processed text reads 'must touch the middle stump or crease'; 1902 (and 1896) read 'bowling "
  "stump'. The 1900 raw OCR is illegible here ('the iu«ii>io ntump'), so 'middle' is an AI clean-up guess. Same rule; also 'starts' -> 'start'.",
  NC, "ocr_noise", "high", "derived",
  "Raw OCR of the 1900 page is garbled at this word; 1896 and 1902 both read 'bowling stump'. The 1900 processed word is an "
  "invention of the clean-up step, not a printed variant.", ["S18"], integrity="suspect",
  note="1900 processed text 'middle stump' is unsupported by raw OCR.")
L("E015", "Single wicket Law 8: 'field-man' (1900 printing) -> 'fieldsman' (1902, as in 1896); capitals. Same rule.",
  NC, "format_artefact", "high", "derived",
  "Spelling variant of the same word in the 1900 printing; 1896 and 1902 read 'fieldsman'.", ["S18"])
L("E016", "Single wicket Law 9: 1900 processed 'All runs, byes, leg byes, and overthrows' -> 1902 'All Hits, Byes, Leg Byes, and "
  "Overthrows'. 1900 raw OCR reads 'All hus, byes' (i.e. 'hits'), and 1896 reads 'All hits'; 'runs' is a clean-up error. Same rule.",
  NC, "ocr_noise", "high", "derived",
  "Raw OCR 'hus' is a misread of 'hits'; the 1896 and 1902 texts read 'hits'. The 1900 processed 'runs' was introduced by the "
  "clean-up step.", ["S18"], integrity="suspect", note="1900 processed text 'runs' is unsupported by raw OCR ('hus').")
L("E017", "Law 1: the two sentences 'A match is played between two sides of 11 players each, unless otherwise agreed to.' and "
  "'Each side has two innings...' are joined with a semicolon in 1902 and '11' becomes 'eleven'. Same rule.",
  NC, "segmentation_artefact", "high", "derived",
  "Sentence joining and numeral/word only; the official 1900 text (ACS) has the 1902 form.", ["S18", "S36-02"])

# --- Follow-on and declaration (Rait Kerr serials 114, 115), first visible in 1902 -------------------------------------
L("E002", "One-day matches, follow-on: 'The side which goes in second shall follow their innings if they have scored 75 runs less than "
  "the opposite side' (compulsory) -> 'The side which bats first and leads by 75 runs shall have the option of requiring the other side "
  "to follow their innings' (optional).",
  EN, "avoid_draws", "high", "stated",
  "Rait Kerr serial 114 (May 2nd 1900): enforcement of the follow-on becomes optional; one-day limit 75 runs. In ch. 5 he says the "
  "follow-on and declaration changes of the period 'were primarily directed towards reducing the number of drawn matches', that the "
  "compulsory rule forced a side 'to field for two consecutive innings on the improved pitches of the day, and then possibly to have to "
  "bat last on a crumbling pitch', and that pressure from Australia and the failure to win the 1899 Old Trafford Test after Australia "
  "had automatically followed on brought 'the change to an optional rule in the following year'.",
  ["S16", "S36-03"], sec="NOVEL_EVENT", secsub="single_incident",
  date="May 2nd 1900 (Rait Kerr serial 114; official 1900 one-day text, ACS). The project's 1900 printing already shows 75 runs but "
       "the old compulsory wording, so the option first appears in the 1902 text (edition lag / faithless 1900 printing).",
  integrity="ok")
L("E057", "Law 53, follow-on: 'The side which goes in second shall follow their innings if they have scored 150 runs less than the "
  "opposite side' (compulsory) -> 'The side which bats first and leads by 150 runs in a three days' match, or by 100 runs in a two days' "
  "match, shall have the option of requiring the other side to follow their innings'. The declaration clause that the 1900 printing "
  "attached to Law 53 ('1.—On the last day of a match...') leaves Law 53 and becomes Law 54 (see the new declaration Law).",
  EN, "avoid_draws", "high", "stated",
  "Rait Kerr serial 114 (May 2nd 1900): follow-on optional, limits 150 (three-day) and 100 (two-day). Ch. 5 gives the cause: the "
  "follow-on/declaration changes 'were primarily directed towards reducing the number of drawn matches'; the compulsory rule was "
  "absurd on improved pitches, and pressure from Australia plus the failure to win the 1899 Old Trafford Test after Australia had "
  "automatically followed on brought the optional rule 'in the following year'.",
  ["S16", "S36-02"], sec="NOVEL_EVENT", secsub="single_incident",
  date="May 2nd 1900 (Rait Kerr serial 114; ACS 1900 revision lists Law 53 as changed). The project's 1900 printing shows 150 runs "
       "but the old compulsory wording and no two-day figure; the option first appears in the 1902 text.",
  note="The 1900 text merges the declaration Law into Law 53 (raw OCR '1.—Ou the last day...'), so part of this event is segmentation.")
L("E058", "New Law 54 (declaration): 'The In-side may declare their innings at an end in a three days' match, at or after the "
  "luncheon interval on the second day; in a two days' match on the second day, at any time; in a one day match at any time', "
  "replacing 'On the last day of a match, or if a one day match at any time, the in-side shall be empowered to declare the innings at "
  "an end'. Notes added: a first-innings declaration does not preclude a second innings; a declared innings counts as completed and a "
  "win is in runs.",
  EN, "avoid_draws", "medium", "stated",
  "Rait Kerr serial 115 (May 2nd 1900): declaration allowed in a three-day match after the start of the luncheon interval on the "
  "second day. Ch. 5: the follow-on and declaration alterations of the period 'were primarily directed towards reducing the number of "
  "drawn matches, which resulted from the huge scores following on the improvement of pitches and batting technique'. He states this "
  "for the declaration changes as a group, hence medium confidence. The Notes are interpretations of the 1902 Lacey edition.",
  ["S16", "S36-02"], sec=ST, secsub="notes_revision",
  date="May 2nd 1900 (Rait Kerr serial 115; ACS 1900 revision). Absent from the project's 1900 printing, first appears in 1902.")
L("E004", "One-day matches: new 'N.B.—A tie is included in the words “played out.”'",
  ST, "codification_definition", "high", "inferred",
  "Defines 'played out' in the one-day rule that an unfinished match is decided on the first innings. It is already a Note in the "
  "official 1900 one-day text (ACS), so it is an interpretation that the project's 1900 printing omitted.",
  ["S36-03", "S16"], date="Note present in the official 1900 one-day text (ACS); first visible in the project's 1902 text.")

# --- Law 33b (1899) first appears ----------------------------------------------------------------------------------
L("E040", "New Law 33b: 'If the Ball, whether struck with the bat or not, lodges in a Batsman's Clothing, the ball shall become “Dead.”' "
  "(old Law 33 becomes 33a), with Notes: the ball is not dead when the bails are off or after an unsuccessful appeal; 'lodging' "
  "covers practically all ways a ball can lodge in or against clothing; it is not dead on hitting the umpire; it ceases to be dead when "
  "the bowler begins his run.",
  EN, "fairness_spirit", "low", "inferred",
  "Rait Kerr serial 112 (May 3rd 1899) records the change but gives no reason. A contemporary commentary (Cricket, 28 Feb 1901) says "
  "that before 1899 a ball lodged in the top of the batsman's leg-guard left an absurd dilemma (removing it infringed Law 29; if a "
  "fieldsman secured it the batsman was caught) and calls the earlier omission 'unaccountable'. That the Law was made to remove this "
  "unfair outcome is my inference from that commentary, not an M.C.C. statement.",
  ["S16", "S36-07", "S36-01"], sec=ST, secsub="notes_revision",
  date="May 3rd 1899 (Rait Kerr serial 112; ACS 1899 revision adds it as Law 33A, renumbered 33B in 1900). Omitted by the project's "
       "1900 printing; first appears in the 1902 text (edition lag).")

# --- Notes of the 1902 Lacey edition --------------------------------------------------------------------------------
L("E018", "Notes on Law 11 (bowler's feet) added: a bowler may bowl with both feet behind the bowling crease if one foot is within "
  "the return crease; knocking the wicket with the foot does not in itself justify 'No Ball'; part of the foot grounded on or outside "
  "the return crease is a 'No Ball'; heel-over-the-return-crease cases explained.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E019", "Notes on Law 12 (wide) added: the test is whether the ball is within reach of the Striker; a call of 'Wide' is ignored if "
  "the striker hits the ball; batsmen do not cross back after one run from a wide.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E020", "Notes on Law 13 (over) added: read with Law 16; no-balls and wides are not counted in the over but recorded on the score "
  "sheet; 'It is Umpire's and not the Scorer's duty to call over.'",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E021", "Law 14: 'The bowler may change ends as often as he pleases, provided that he shall not bowl two overs in succession in the "
  "same innings' (1900 printing) -> 'The Bowler shall be allowed to change ends as often as he pleases, provided only that he does not "
  "bowl two Overs consecutively in one innings'. Same permission and limit.",
  SW, "modal_strength", "medium", "derived",
  "The official text in 1899 and 1900 (ACS) and the 1896 text already read 'shall be allowed ... provided only that he does not bowl "
  "two overs consecutively in one innings'; the 1900 wording is a printer's paraphrase in the Wright & Co. edition (raw OCR confirms "
  "it), not an M.C.C. change. 'may' versus 'shall be allowed' carries the same permission.", ["S18", "S36-01", "S36-02"],
  note="Printing variant of the 1900 source, not an MCC change; candidate for NOT_A_CHANGE if source variants are to be excluded.")
L("E022", "Law 16: 'added to that score as “wide balls,” and if no runs be otherwise obtained' -> 'added to the score as “Wide Balls,” "
  "and if no run be otherwise obtained' (same rule; the official text has 'the score' and 'no run'). Notes added: a run off a no-ball "
  "by the bat is scored to the batsman and not as a no-ball; if one run is attempted and the batsman is run out the no-ball alone "
  "counts; the bowler gets another delivery; byes/overthrows from a wide are scored as wides; a batsman may be out hit wicket "
  "striking at a wide.",
  ST, "clarification_umpire_workability", "high", "inferred",
  NOTES_WHY + " The wording differences in the Law itself are a 1900 printer's variant (official 1900 text, ACS, reads as 1902).",
  ["S16", "S36-02"], date=NOTES_DATE)
L("E023", "Law 17: capitals and hyphens ('“no-ball,”' -> '“No Ball,”', 'leg-bye' -> 'Leg Bye'), one comma. Same rule.",
  NC, "format_artefact", "high", "derived", "Capitalisation, hyphenation and punctuation only.", ["S18"])
L("E024", "Law 18: 1900 'the umpire at the bowler's wicket shall call “play” from that time. No trial ball shall be allowed...' -> "
  "1902 'the Umpire at the Bowler's wicket shall call “Play”; from that time no trial ball shall be allowed...'. The punctuation "
  "moves 'from that time' from the call of Play to the ban on trial balls.",
  NC, "format_artefact", "medium", "derived",
  "The official text in 1899 and 1900 (ACS) already reads '“Play;” from that time no trial ball shall be allowed'; the 1896 and 1900 "
  "printings misplace the full stop. Not an M.C.C. change, though the misprinted version reads differently.",
  ["S18", "S36-01", "S36-02"], note="Punctuation changes the reading (when the trial-ball ban starts) but the official text never changed.")
L("E025", "Notes on Law 19 (out of his ground) added: part of the foot within the line suffices; a foot on the line with no part "
  "within is out of his ground; a batsman jumping with bat off the ground is out of his ground.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E026", "Law 2: '1.—So often as the batsman...' -> '1st—So often as the Batsmen...'; '2.—For penalties under Laws 16, 34, 41, and "
  "allowances under 41' -> '...allowances under 44'. The 1900 '41' is a misprint/OCR error (raw '411, and allowances under 41'); 1896 "
  "and the official text read 44 and 'batsmen'. Same rule.",
  NC, "ocr_noise", "high", "derived",
  "1896 and the official 1900 text (ACS) read 'batsmen' and 'allowances under 44' (Law 44 covers boundary allowances); the 1900 "
  "reading comes from a corrupted print/OCR line. List markers differ only in style.", ["S17", "S18", "S36-02"])
L("E027", "Notes on Law 2 added: runs actually completed beyond the boundary allowance are scored; neither side can be compelled to "
  "continue after the match is finished; in a one-day match the umpires decide if there is time to carry the game to a further issue.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E028", "Notes on Law 20 (wicket down) added: with one bail off, removing the other suffices; pulling a stump out with the ball in "
  "hand is customary when the bails are off.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E029", "Law 21: 'The striker is out if the wicket be bowled down...' -> heading 'The Striker is Out—' then 'If the wicket be bowled "
  "down...—“Bowled.”' (same rule; the official text has the heading). New Note: an umpire would be justified in giving 'Bowled' if a "
  "stump were bowled down but the bails by mischance stayed in place.",
  ST, "clarification_umpire_workability", "high", "inferred",
  NOTES_WHY + " The change in the Law's opening is only the heading being segmented differently (ACS 1900 prints 'The STRIKER is out -').",
  ["S16", "S36-02"], date=NOTES_DATE)
L("E030", "Notes on Law 22 (caught) added: the ball must not touch the ground, though the hand holding it may; falling catches are a "
  "question of fact; a ball struck again after touching the ground then caught is not out, but out if struck twice before touching the "
  "ground; out if caught off a ball that hit the pad first; with no boundaries arranged a hit can be caught off a tree, hedge or building.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E031", "Notes on Law 23 (stumped) added: a rebound off the wicket-keeper's pads/person with the Striker out of his ground is "
  "'Stumped' not 'Run Out'; removing one bail suffices; not out if the bails are knocked off with the foot or the hand not holding the ball.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E032", "Law 24 (l.b.w.): 'if with any part of his person he stop the ball' -> 'if with part of his person he stops the ball'. "
  "Notes added: l.b.w. possible with the bowler bowling round the wicket; three considerations for the umpire (would the ball have hit "
  "the wicket; did it pitch in a straight line between wicket and wicket; was it part of the batsman's person that intercepted it); "
  "'It is immaterial whether the ball breaks or not.'",
  ST, "clarification_umpire_workability", "high", "inferred",
  NOTES_WHY + " The Notes came while l.b.w. reform was being debated (Rait Kerr ch. 5: M.C.C. consulted in 1900; the proposed change "
  "failed at the 1902 Special General Meeting), but they interpret the existing Law. Dropping 'any' is in the Lacey printing only: the "
  "official Law in 1902-1910 (ACS) keeps 'any part of his person', so it is not an M.C.C. change.",
  ["S16", "S36-04"], sec=SW, secsub="qualifier_scope", date=NOTES_DATE,
  note="'any part' -> 'part' is a Lacey-edition printing variant (ACS keeps 'any'); kept as secondary SEMANTIC_WORDING.")
L("E033", "Notes on Law 25 (hit wicket) added: out if the wicket is hit down while making a second stroke to keep the ball out; not "
  "out for breaking the wicket while running; out if the hat or cap falls on the wicket while playing at the ball.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E034", "Note on Law 26 added: 'It should be noted that it is the Striker who is out if this Law is infringed.'",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E035", "Notes on Law 27 (hit the ball twice) added: the umpire decides whether the second strike was 'wilful'; an attempted run "
  "may be evidence but is not conclusive; runs from overthrows after a lawful second strike count; out even if no run is attempted.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E036", "Law 28 (run out): 'Either batsman is out if in running... while the ball is in play...' -> heading 'Either Batsman is Out—' "
  "then 'If in running... when the ball is in play...'. Notes added: not out if the striker hits the ball into the opposite wicket "
  "untouched by a fieldsman; either batsman can be run out by any fieldsman including the bowler; see Law 19 for 'out of his ground'.",
  ST, "clarification_umpire_workability", "high", "inferred",
  NOTES_WHY + " The opening is a heading segmented differently; 'while' -> 'when' is a Lacey-printing variant (ACS keeps 'while').",
  ["S16", "S36-04"], date=NOTES_DATE)
L("E037", "Note on Law 3 added: 'It should be noted, especially in League and Saturday Matches, that Umpires are appointed “one for "
  "each end” and not one for each side.'",
  ST, "clarification_umpire_workability", "high", "inferred",
  NOTES_WHY + " Rait Kerr also ties the rise in interpretations to the rapid expansion of league and club cricket after 1884, which this "
  "Note addresses directly; the 'one for each end' rule itself dates from 1884 (serial 104).", ["S16"], date=NOTES_DATE)
L("E038", "Note on Law 30 added: 'The Umpire must decide on the facts before him if the obstruction was “wilful.”'",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E039", "Notes on Law 32 added: cross-reference to the Notes on Law 22 (printed 'Sec' for 'See'); the remaining batsman does not "
  "go back if the batsmen had crossed on the run-out run.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E041", "Law 34 (lost ball): capitals and hyphen ('“lost-ball,”' -> '“Lost Ball”'), one comma; new Note listing when a ball can "
  "become dead ('under Laws 33a, 33b, 34, 35, 41 & 50, or on the call of a boundary hit').",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E042", "Law 35: 'if the bowler throw at the wicket' (1900 printing) -> 'if the Bowler throw at that wicket' (as in the official "
  "text), capitals. Notes added: whether the ball is 'finally settled' is for the umpire; a bowler may run a batsman out without "
  "delivering, after passing the crease or changing hands; bails may be knocked off from either side.",
  ST, "clarification_umpire_workability", "high", "inferred",
  NOTES_WHY + " 'the wicket' versus 'that wicket' is a 1900 printer's variant: 1896 and the official 1900 text (ACS) read 'that wicket'.",
  ["S16", "S36-02"], date=NOTES_DATE)
L("E043", "Law 37 (substitute): punctuation and a stray page number '13'; Notes added: a substitute for illness/injury during the "
  "match is a right, otherwise consent depends on the opposing captain's courtesy; captains should exchange lists before tossing; a "
  "player who had a runner may still bowl; a side short in the field may bat with its full number.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E044", "Note on Law 39 added: the distinction between 'Striker' and 'Batsman'; an injured batsman who is not the Striker is under "
  "no penalty under this Law.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E045", "Law 4 (ball): 'one quarter' -> 'one-quarter' (same size). New Note: 'It has become the practice to call for a new ball at "
  "any time, with the Umpire's consent, if the old one has become damaged or if the bowler has lifted the seam to obtain a better hold.'",
  ST, "codification_definition", "high", "inferred",
  NOTES_WHY + " The Note records an existing practice ('It has become the practice'), going beyond the Law's new ball only at the start "
  "of an innings. The new-ball-after-200-runs rule followed in 1907 (Rait Kerr ch. 5).", ["S16"], date=NOTES_DATE)
L("E046", "Law 40: 'A batsman is liable to be put out for any infringe ment of the laws by his substitute' (1900 printing, split word "
  "'infringe ment') -> 'A Batsman is liable to be out for any infringement of the Laws by his substitute'. Same rule.",
  NC, "format_artefact", "high", "derived",
  "'be put out' is a 1900 printer's variant: 1896 and the official 1900 text (ACS) read 'liable to be out'. 'infringe ment' is a "
  "line-break hyphenation artefact.", ["S18", "S36-02"])
L("E047", "Note on Law 41 added: the five penalty runs are added to the runs already made when the fieldsman wilfully stopped the ball.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E048", "Note on Law 42 added: a wicket-keeper may run a batsman out by going in front of the wicket; the umpire decides from the "
  "facts if the act is legal.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E049", "Law 43: cross-reference '(See also Instructions to Umpires.)' added (with a stray page number '14').",
  ST, "notes_revision", "high", "inferred",
  "A cross-reference to the Instructions to Umpires section, which the 1902 edition prints as 'a special section containing "
  "instructions to the umpires' (Rait Kerr ch. 5). No rule change.", ["S16"], date=NOTES_DATE)
L("E050", "Law 45: 'When they call “play”' (1900 printing) -> 'When they shall call “Play”' (as in 1896 and the official text); new "
  "Note: 'It is the duty of the Captains to see that this Law is strictly observed.'",
  ST, "clarification_umpire_workability", "high", "inferred",
  NOTES_WHY + " The dropped 'shall' is a 1900 printer's variant (official 1900 text, ACS: 'When they shall call \"Play,\"').",
  ["S16", "S36-02"], date=NOTES_DATE)
L("E051", "Law 46: 'N.B.—An appeal, “How's that?” covers all ways of being out (within the jurisdiction of the Umpire appealed to), "
  "unless a specific way of getting out is stated by the person asking.'",
  ST, "clarification_umpire_workability", "high", "inferred",
  "This Note was added to Law 46 in the 1899 revision (ACS 1899 header: 'Laws 46 (addition of a note)'); the project's 1900 printing "
  "omits it, so it first appears in 1902. It interprets the existing appeal rule.", ["S36-01", "S36-02", "S16"],
  date="1899 revision (ACS); omitted by the 1900 printing; first visible in 1902.")
L("E052", "Note on Law 47 added: when the bowler's-end umpire has given 'not out' the other umpire may answer any appeal within his "
  "jurisdiction, subject to Law 50.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E053", "Law 48b -> 48a: 'The umpire shall take special care to call “no ball” instantly upon delivery' -> 'The Umpires shall take "
  "especial care...' (renumbered after 48a -> 48). New Note: an umpire who calls 'No Ball' when the ball has not been delivered should "
  "revoke the call.",
  ST, "clarification_umpire_workability", "medium", "inferred",
  NOTES_WHY + " The renumbering (48a/48b -> 48/48a) matches the official 1900 revision ('Laws 33 and 48 being renumbered', ACS). "
  "'special' is a 1900 printer's variant (1896 and ACS: 'especial'). 'Umpires' (plural) is in the Lacey printing only; the official "
  "Law 48A (ACS 1900-1910) keeps 'The umpire', though plural fits the 1899 rule that either umpire may call No ball (Rait Kerr serial 113).",
  ["S16", "S36-02", "S36-04"], sec=SW, secsub="qualifier_scope", date=NOTES_DATE,
  note="Plural 'Umpires' is a Lacey-edition variant; ACS official text singular.")
L("E054", "Law 5 (bat): '38 inches' -> 'thirty-eight inches'. Same size.", NC, "format_artefact", "high", "derived",
  "Numeral versus number words; same value (official text, ACS: 'thirty-eight inches').", ["S17", "S18", "S36-02"])
L("E055", "Note on Law 50 added: nothing the fielding side does after 'Over' is called can put a batsman out, but an appeal may be made "
  "within the allotted time (with a stray page number '15').",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E056", "Law 52: '..., when either side may dismiss him' (1900 printing) -> '...; then either side may dismiss him'. Same rule.",
  NC, "format_artefact", "high", "derived",
  "'when' is a 1900 printer's variant (raw OCR confirms); 1896 and the official 1900 text (ACS) read 'then either side may dismiss him'.",
  ["S18", "S36-02"])
L("E059", "Law 6 (wickets): '22 yards' -> 'twenty-two yards', '27 inches' -> 'twenty-seven inches', 'of equal and sufficient size to "
  "prevent the ball passing through' -> 'of equal and of sufficient size to prevent the ball from passing through'. Same rule.",
  NC, "format_artefact", "high", "derived",
  "Numerals versus words with the same values (official 1900 text, ACS: 'twenty-two yards', 'twenty-seven inches') and two "
  "grammatical words with no change of meaning.", ["S17", "S18", "S36-02"])
L("E060", "Law 7 (bowling crease): '6 feet 8 inches' -> 'six feet eight inches' (same length). Notes added: 'The Return Crease is "
  "shortened for convenience. It must be deemed unlimited in length.' and 'A proposal will come before the General Meeting of the "
  "M.C.C. in 1902, to increase the Bowling Crease to 8ft. 8in.'",
  ST, "clarification_umpire_workability", "high", "inferred",
  NOTES_WHY + " The second Note announces the change adopted on May 7th 1902 (Rait Kerr serial 117), which reaches the Law text only "
  "in the next edition.", ["S16", "S36-02"], date=NOTES_DATE + " Proposal note: before the May 1902 meeting.")
L("E061", "Note on Law 9 added: the batting side has a right to have the ground swept and rolled 'for not more than 10 minutes' "
  "before each innings and each day's play, and the captain should see that his side obtains it.",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
