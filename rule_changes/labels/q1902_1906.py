"""Labels for 1902 -> 1906. Both texts are Lacey annotated editions (Laws + Notes). Official Law changes in between (ACS): Law 7 (1902)
and Law 54 (1906)."""
from _h import make
PAIR = "1902_1906"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
EN = "ENJOYMENT"

NOTES_WHY = ("Rait Kerr (ch. 5): interpretations approved by the M.C.C. Committee were 'promulgated in the form of public "
             "pronouncements, instructions to umpires, or as Notes added to the Laws', and Lacey's annotated edition (first 1902) went "
             "through many editions. That explains the Notes generally, not this one, so the reason is inferred.")
NOTES_DATE = "First appears in the 1906 text (a later Lacey annotated edition); no date for the interpretation itself found."

L("E016", "Law 7: the Bowling Crease 'six feet eight inches in length' -> 'eight feet eight inches in length'.",
  EN, "bowler_batsman_balance", "high", "stated",
  "Rait Kerr serial 117 (May 7th 1902): the bowling crease is lengthened to 8 feet 8 inches. In ch. 5, under 'Other measures adopted "
  "to assist the bowler' (measures showing 'the restoration of the balance of power between the bowler and the batsman'), he says "
  "'In 1902 on the recommendation of the County captains the length of the Bowling crease was increased by two feet to eight feet "
  "eight inches', a change first proposed by the umpire Thoms in 1888.",
  ["S16", "S36-04"],
  date="May 7th 1902 (Rait Kerr serial 117; ACS: 'The change in the 1902 revision was to Law 7'). The project's 1902 text predates "
       "the meeting (its Note announces the proposal), so the change first appears in the 1906 text. Raw OCR 1902 'six feet', 1906 'eight feet'.")
L("E017", "Note on Law 7 removed: 'A proposal will come before the General Meeting of the M.C.C. in 1902, to increase the Bowling "
  "Crease to 8ft. 8in.'",
  ST, "consequential", "high", "inferred",
  "The announced proposal was adopted on May 7th 1902 (Rait Kerr serial 117) and is now in the Law itself, so the Note is obsolete.",
  ["S16", "S36-04"], date="After May 7th 1902.")
L("E015", "Law 54, two-day match declaration: 'in a two days' match on the second day, at any time' -> 'in a two days' match the "
  "Captain of the batting side has power to declare his innings at a close at any time; but such declaration may not be made on the "
  "first day later than 1 hour and 40 minutes before the hour agreed on for drawing stumps'.",
  EN, "avoid_draws", "medium", "stated",
  "Rait Kerr serial 118 (May 2nd 1906): in a two-day match a declaration on the first day is allowed provided 100 minutes remain. Ch. 5: "
  "the follow-on and declaration alterations of the period 'were primarily directed towards reducing the number of drawn matches' "
  "(stated for these Laws as a group, hence medium). Cricket (29 Mar and 3 May 1906) reports that F. B. May proposed the adopted "
  "wording at the M.C.C. meeting and that the time limit was inserted to prevent the batting side securing an unfair advantage in a "
  "failing light.",
  ["S16", "S36-05", "S36-08", "S36-09"], sec=EN, secsub="fairness_spirit",
  date="May 2nd 1906 (Rait Kerr serial 118; ACS: 'The change in the 1906 revision was to Law 54'). Raw OCR '1 hour and 40 minutes' "
       "matches ACS 'one hour and forty minutes'.")
L("E001", "Single wicket Law 2: 'off and leg stump' -> 'oft and leg stump' (OCR error in 1906) and a stray page number '16' dropped. Same rule.",
  NC, "ocr_noise", "high", "derived", "Raw OCR 1906 reads 'oft'; the word is 'off' in every other edition. Page number is layout.", ["S18"])
L("E002", "Note on Law 11: '“No Ball.”' -> '“NoBall.”' (missing space). Same note.", NC, "ocr_noise", "high", "derived",
  "Spacing error only.", ["S18"])
L("E004", "Note on Law 16: '“NoBall”' -> '“No Ball”' (missing space restored). Same note.", NC, "ocr_noise", "high", "derived",
  "Spacing error only.", ["S18"])
L("E003", "Notes on Law 12 added: 'When the ball has been delivered but remains stationary before reaching the striker no runs can be "
  "added to the score, unless it has been struck by the striker. The striker has a right to hit the ball without interference by the "
  "field. The Umpire must decide if the ball has been “delivered.”'",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E006", "Notes on Law 23: two Notes ('If the ball rebounds off the pads...' and 'It is sufficient for the wicket-keeper to remove one "
  "bail...') run together with a stray page number '10'. Same Notes.",
  NC, "segmentation_artefact", "high", "derived", "Both sentences are present in both editions; only line joining and a page number differ.", ["S18"])
L("E007", "Note on Law 24: 'l.b.w.' -> 'lbw'. Same note.", NC, "format_artefact", "high", "derived", "Abbreviation punctuation only.", ["S18"])
L("E008", "Note on Law 24: 'an l.b.w.' -> 'an lbw'. Same note.", NC, "format_artefact", "high", "derived", "Abbreviation punctuation only.", ["S18"])
L("E009", "Law 27: a stray page number '11' after '“Hit the ball twice.”'. Same rule.", NC, "format_artefact", "high", "derived",
  "Printed page number caught in the text.", ["S18"])
L("E011", "Notes on Law 32: '(Sec Notes on Law 22.)' -> '(See Notes on Law' 22.)' and a stray page number '12'. Same notes.",
  NC, "ocr_noise", "high", "derived", "OCR errors ('Sec', stray apostrophe) and a page number.", ["S18"])
L("E013", "Law 43: stray page number '14' after '(See also Instructions to Umpires.)' dropped. Same text.",
  NC, "format_artefact", "high", "derived", "Printed page number only.", ["S18"])
L("E014", "Note on Law 45 added: 'The In going Batsman should meet the out-coming batsman before he enters the Pavilion.'",
  ST, "clarification_umpire_workability", "medium", "inferred",
  NOTES_WHY + " The Note sits under the Law allowing two minutes for each striker to come in, and its evident effect is to save time "
  "between wickets; no source states that aim.", ["S16"], date=NOTES_DATE)
L("E018", "Note on Law 9 added: 'The ground in this law means “the pitch.”'",
  ST, "codification_definition", "high", "inferred",
  NOTES_WHY + " It defines the term 'ground' in the rolling/covering Law as the pitch, narrowing what the ban on rolling, watering, "
  "covering, mowing or beating applies to.", ["S16"], date=NOTES_DATE)
