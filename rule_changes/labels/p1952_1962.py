"""Labels for the 1952 -> 1962 edition pair. Dated amendments come from the ACS 2nd-edition page (S08), which annotates
Laws and Notes with the date of each later amendment (some only 'late 19xx or early 19xx')."""
from _h import make
PAIR = "1952_1962"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"

L("E002", "Law 15 (Declarations): the 1947 restrictions (declaration only on the second and later days of a match of three days or more; in a two-day match not on the first day later than 1 hour 40 minutes before close) are replaced by 'may declare an innings closed at any time during a match irrespective of its duration'.",
  UN, "no_cause_stated", "low", "none",
  "No source states why the 1957 restriction was lifted. Rait Kerr (1950) predates 1957 and only describes the earlier (1889) declaration Law, which he says was 'primarily directed towards reducing the number of drawn matches' (ch.4 p.55); that cannot be evidence for 1957. Wikipedia (S13) only records that first-day declarations were authorised in 1957. A draws-avoidance motive is plausible but conjecture.",
  ["S08", "S13", "S16"], date="ACS: Law 15 amended 1 May 1957 (Law 16, on weather-delayed starts, amended the same day).")
L("E003", "Two Notes added to Law 18: (1) if players leave the field during the last over of a period of play the umpires call Time, and in the last over of a match there is no resumption and the match ends; (2) the last over before an interval or close of play is started if the square-leg umpire has reached his place behind the bowler's stumps before time.",
  UN, "no_cause_stated", "low", "none", "ACS dates the first Note to 1 May 1957 (a narrower version: last over of the match, weather or bad light), amended late 1959 or early 1960 to the 1962 form, and the second to late 1962 or early 1963; no source gives a reason.",
  ["S08"], date="ACS: Note added 1 May 1957, amended late 1959/early 1960; Note 2 added late 1962 or early 1963.")
L("E004", "Law 19 (Scoring) Notes: 'a boundary from extras' added to the batsmen-do-not-return exception; new definition of a 'short' run (either or both batsmen fail to make good their ground in turning for a further run); a short run shortens the succeeding one but the latter counts if completed; one run only is deducted if both batsmen are short in one and the same run (restated, not removed); deliberate short running now makes the ball dead and the runs are disallowed (new, ACS Note 3(3), late 1962/early 1963).",
  UN, "no_cause_stated", "low", "none", "ACS records Note 3(3) added late 1962 or early 1963 and the scoring Notes changed in 1953 or early 1954; no source gives a reason.",
  ["S08"], date="ACS: Note 3(3) added late 1962 or early 1963; earlier Notes changed 1953 or early 1954.")
L("E006", "Law 23 Note on the over: 'In default of any agreement to the contrary, in the United Kingdom the over shall be 6 balls' becomes 'In the United Kingdom the over shall be 6 balls, unless an agreement to the contrary has been made.'",
  ST, "wording_only", "medium", "derived", "Same rule, clauses reordered.", ["S18"], note="ACS records a different later change to Law 23 (late 1967 or early 1968, to 'overs of either 8 or 6 balls according to the agreed conditions').")
L("E007", "New Note on Law 28 (Wide ball): should the fielding side interfere, the umpire may replace the ball where it came to rest and order the fielders back to the positions they held when the ball was delivered.",
  UN, "no_cause_stated", "low", "none", "ACS dates the change to late 1962 or early 1963; no reason given.", ["S08"], date="ACS: Law 28 note changed late 1962 or early 1963.")
L("E008", "Law 30 body: the striker's 'dress or person except his hand' becomes 'except his hand holding the bat' (the 5 May 1954 amendment, ACS). Law 30 Note replaced: the 1952 provision treating deliberate kicking or 'kneeing' of the ball by the striker as unfair is replaced by: leg byes from unintentional deflection are fair, and the umpire calls Dead ball if not entirely satisfied the act was unintentional.",
  UN, "no_cause_stated", "low", "none", "ACS dates the Law-body amendment to 5 May 1954 and the Note replacement to late 1955 or early 1956 (with a further change in May 1965); no source states a reason.",
  ["S08"], date="ACS: body amended 5 May 1954; Note changed late 1955 or early 1956 (and again May 1965).")
L("E009", "Law 31 (Wicket is down): wording changed from 'if either or both of the bails be previously off' to 'if both bails be off', and the Note adds that if one bail is off it suffices to dislodge the other or to strike any of the three stumps out of the ground.",
  UN, "no_cause_stated", "low", "none", "ACS records Law 31 as amended on 5 May 1954; no reason is given. (How the wicket is 'down' was also discussed during the 1947 revision, Rait Kerr ch.5 p.62, but that is the earlier change.)",
  ["S08", "S16"], date="ACS: Law 31 amended 5 May 1954.", note="Whether this hunk is the 1954 amendment is not certain; the dataset's 1952 text still has the earlier wording.")
L("E010", "New Note 1 on Law 39 (L.B.W.): the word 'hand' in this Law means the hand holding the bat.",
  ST, "codification_definition", "medium", "inferred", "A defining Note; ACS dates it to late 1955 or early 1956 (the previous Note 1 became Note 2). No further reason given.",
  ["S08"], date="ACS: Note 1 added late 1955 or early 1956.")
L("E011", "Note on persistent fast short-pitched bowling revised: 'persistent and systematic bowling... is unfair' becomes 'persistent bowling... is unfair if... it constitutes a systematic attempt at intimidation', with a fixed procedure (caution, final warning, direct the captain to take the bowler off); umpires' duty to intervene against damage to the pitch is also strengthened ('justified' becomes 'duty').",
  ST, "notes_revision", "medium", "inferred",
  "Two layers. (1) The 1953 intimidation wording: ACS records an M.C.C. statement of 15 April 1953 that, following an experiment in Australia, the Australian Board of Control found the new Note satisfactory, tried experimentally in England in 1953; the Note's lineage runs back to the 'direct attack' (bodyline) episode (Rait Kerr ch.4 p.53-54). (2) Later, undated changes ('Request' -> 'Direct' the captain, 'The captain shall take the bowler off as directed', umpires' 'justified in preventing' -> 'duty to intervene' on pitch damage): the ACS 2nd-edition text, which already has the 1953 revision, still reads 'Request' and 'justified', so these came later; no source dates or explains them.",
  ["S08", "S16"], sec="UNCATEGORISED", secsub="no_cause_stated", date="Intimidation wording: M.C.C. statement 15 April 1953 (ACS). Later wording changes: undated.")
L("E013", "Drying regulations for first-class matches in England (Law 47 appendix) revised: before the toss the groundsman may dry pitch and outfield; thereafter drying of the outfield by the groundsman but of the pitch only under the umpires' instructions; footholds may be dried as the umpires direct.",
  UN, "no_cause_stated", "low", "none", "A procedural change to who controls pitch drying; no source gives a reason or a date.", ["S08"])
L("E014", "Ball weight and size appear to change from '5 1/2, 5 3/4 ounces; 8 7/8 to 9 inches' to '5.5, 5.75 ounces; 8.8125 to 9 inches': only the size is a real difference, and it corrects an earlier mistake. The true limits were 8 13/16 (= 8.8125) to 9 inches in every edition.",
  NC, "cleaning_artefact_numeric", "high", "derived", "The 1952 text's '8 7/8' was an AI clean-up error (raw OCR '8ti?'); the 1962 text's 8.8125 is the correct value, but it too was produced by the AI clean-up from garbled raw OCR ('8-$- inches'), so it is correct by luck, not supported by the raw text. Decimal notation for the weights is a format change only.",
  ["S17", "S09", "S08"], integrity="suspect")
L("E015", "Sentence 'The latter may demand a new ball at the start of each innings' dropped from the Note on Law 5.",
  ST, "notes_revision", "low", "inferred", "The Law itself still says either captain may demand a new ball at the start of each innings, so the sentence duplicated it; no source states this was the reason.",
  ["S08"])
L("E016", "Bail dimensions appear to change from '4 1/2 inches; 1/2 inch projection' to '4.5 inches; 1 inch projection': not real. All independent transcriptions give bails 4 3/8 inches and a projection of not more than 1/2 inch.",
  NC, "cleaning_artefact_numeric", "high", "derived", "Raw OCR of the 1962 edition reads '4|' (a garbled fraction); the AI clean-up output 4.5; the raw OCR itself reads the projection as '1 inch' (a misread of 1/2). ACS texts of the 1st, 2nd and 4th editions say 4 3/8 inches and 1/2 inch.",
  ["S17", "S09", "S08", "S10"], integrity="suspect")
