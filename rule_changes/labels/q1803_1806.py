"""Labels for 1803 -> 1806.

Edition note: the dataset's '1806' text is J. Bailey's undated printing (raw OCR: 'Printed and Sold by J. Bailey, 110 [116], Chancery
Lane'). Rait Kerr (App. III, c.1809) says the M.C.C. copies 'are dated 1806 on the modern leather binding. This may be a misprint for
1809 as the Laws are definitely later than those of the Wallis print', and that the text agrees with the Liverpool 1811 edition 'as
revised ... in 1809'. So the changes here are Rait Kerr's 'After 1803 but before May 25th 1809' and 'Before 1811' serials (50-56).
The two trial balls (serial 57, 'Before 1817') are also present. The '1806' date is too early: these changes date from c.1809-11."""
from _h import make
PAIR = "1803_1806"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
NE = "NOVEL_EVENT"
DB = "Dataset '1806' = J. Bailey undated printing, c.1809-11 per Rait Kerr App. III (binding date 1806 probably wrong)."

L("E001",
  "Ball: 'and not more than' -> 'nor more than'.",
  ST, "wording_only", "high", "derived", "Same limits and meaning; one conjunction differs between printings.", ["S18"])
L("E002",
  "Umpires: new 'The Umpires, in all matches, to pitch fair Wickets, and the parties to toss for the choice of Innings.' The no-ball, "
  "no-notch and catch-appeal sentences are re-split; 'no ball' loses its quote marks.",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serials 52 and 53 ('Before 1811'). The pitch is to be selected by the umpires (within 30 yards of a centre chosen by the sides), "
  "and 'Tossing is again to decide the choice of innings'. In ch.2 he counts such changes among five that 'dealt with general points, such "
  "as rules for fielding substitutes, tossing for innings, and pitching wickets', with no cause given. A handwritten annotation in the "
  "scanned copy (gold file, serial 52) suggests serials 52-56 may date from 1809.",
  ["S16"], date="Before 1811, possibly 1809 (serials 52-53). " + DB)
L("E003",
  "Stumps: 'Which are three, must be twenty-four inches out of the ground, the BAIL seven inches' -> 'Must be twenty-four inches out of the "
  "ground, the BAILS seven inches'. Bail becomes plural; 'Which are three' is dropped. Page mark 'A2' added.",
  ST, "documentary_first_appearance", "medium", "stated",
  "Rait Kerr serial 50 ('After 1803 but before May 25th 1809'): 'The bails are referred to in the plural for the first time in a reliable "
  "edition of the Laws'. Two bails had been in use since c.1786 (serial 36), so this is the official text catching up, not a new rule. 'Which "
  "are three' was Pocock's own wording (absent in the Wallis 1809 text, ACS). 24 in / 7 in unchanged (raw OCR).",
  ["S16", "S31-03"], date="After 1803, before 25 May 1809 (serial 50). " + DB)
L("E004",
  "Wickets: 'Must be opposite to each other, at the distance of twenty-two yards' gains ', which shall be pitched within thirty yards of a "
  "centre fixed by the adversaries'. The clause comes from the dropped visiting-side rule; the umpires now pitch the wickets (see the "
  "umpires' event).",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 52 ('Before 1811'): 'The pitch is to be selected by the umpires within 30 yards of a centre selected by the opposing "
  "sides'. Listed among 'general points' (ch.2) without a cause. The 22-yard and 30-yard figures are unchanged (raw OCR).",
  ["S16"], date="Before 1811 (serial 52). " + DB)
L("E005",
  "Ground-alteration rule moved under 'THE WICKETS'; wording identical except 'the holes' -> 'holes' and 'using sawdust' -> 'using his "
  "saw-dust'.",
  NC, "segmentation_artefact", "high", "derived", "Relocation with printer's variants; same rule.", ["S18"])
L("E006",
  "Two new bowling rules. Wides: 'If the Bowler tosses the Ball over the Striker's head, or bowls it so wide that the Striker cannot play at "
  "it, the party that is in shall be allowed one notch, to be put down to the Byes, and those Balls not to be reckoned as any of the four "
  "Balls.' No ball: 'If the Bowler bowls a No Ball, the Striker may play at it, and be allowed all the runs he can get, and shall not be put "
  "out, except by running out.'",
  NE, "single_incident", "low", "conjecture",
  "Rait Kerr serial 56 ('Before 1811'): 'A Law for \"Wides\" appears for the first time'. In ch.2 he writes that it 'probably resulted from a "
  "well-known incident which occurred at Lord's in 1810': Lambert, 'realizing he could bowl wide of the wicket without any penalty', did so "
  "against Lord Frederick Beauclerk. 'probably' makes this his conjecture. Conflict: if the Bailey text really reflects an 1809 revision, "
  "the 1810 incident cannot be its cause, so confidence is low. Serial 54a: the striker may play at a No ball. The handwritten annotation in "
  "the scanned copy calls serials 54-56 'the first evidence of the attack ... against the introduction of round-arm bowling', but its author "
  "is unknown. Recorded as secondary NOVEL_EVENT/bowling_innovation.",
  ["S16"], sec=NE, secsub="bowling_innovation", date="Before 1811 (serials 54, 56); Rait Kerr links Wides to an 1810 match. " + DB)
L("E007",
  "The visiting side's choice ('THE PARTY WHICH GOES FROM HOME Shall have the choice of the innings, and the pitching of the wickets ... "
  "When the parties meet at a third place, the bowlers shall toss up...') is removed. Its ground-alteration rule is kept under 'THE WICKETS'.",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 53 ('Before 1811'): 'Tossing is again to decide the choice of innings'. He adds that home-and-away matches may still have "
  "used the old rule as late as 1828. Serial 52 transfers pitch selection to the umpires. No cause given ('general points', ch.2).",
  ["S16"], date="Before 1811 (serials 52-53). " + DB)
L("E008",
  "New: 'The Ball must be bowled underhand, and delivered with the hand below the elbow.' And: 'In the event of a change of bowling, no "
  "more than two Balls are to be allowed in practice. The Bowler who takes the two Balls, to be obliged to bowl four Balls.'",
  NE, "bowling_innovation", "medium", "inferred",
  "Rait Kerr serial 55 ('Before 1811'): 'The ball is to be bowled under-hand and delivered with the hand below the elbow.' In ch.2 he says "
  "John Willes revived round-arm ('throwing') 'about 1802' until 'the matter became serious enough for the M.C.C. to take notice', and "
  "that 'restraint on the \"New style\" was insisted on by four changes in the \"No ball\" Law'. He does not name this provision as a "
  "response to Willes, so the link is inferred. Trial balls are serial 57 ('Before 1817'; ch.6 says first in the official 1816 version), "
  "no cause given, hence secondary UNCATEGORISED.",
  ["S16"], sec=UN, secsub="no_cause_stated", date="Before 1811 (serial 55); trial balls before 1817 (serial 57). " + DB)
L("E009",
  "Striker-out list. New: 'If a lost Ball is called, the Striker shall be allowed four, but if more than four are run before lost Ball is "
  "called, then the Striker to have all they have run.' Variants: 'in striking, or at any other time' printed as 'in striking at any other "
  "time' (Bailey omits 'or'); 'either wilfully strike' -> moved; 'his ball' -> 'the Ball'; 'opposite party' -> 'other party'.",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 51 ('After 1803 but before May 25th 1809'): 'A \"Lost ball\" Law is introduced—the striker to score all the runs he may have "
  "made, with a minimum allowance of four.' No cause given. The omitted 'or' is a printer's slip: the Wallis 1809 text (ACS) and the 1816/1820 "
  "texts keep 'in striking, or at any other time'.",
  ["S16", "S31-03"], date="After 1803, before 25 May 1809 (serial 51). " + DB, note="Bailey's dropped 'or' would narrow stumping; treated as a misprint")
L("E010",
  "Alignment pairs 'If If the ball is struck up, the striker may guard his wicket...' with 'Or, if the Ball is struck up, and he wilfully "
  "strikes it again'. Both provisions are present in both editions.",
  NC, "segmentation_artefact", "high", "derived", "Mis-alignment of two unchanged provisions.", ["S18"])
L("E011",
  "Striker list re-segmented. Variants: 'some person' -> 'some other person' (stand-out substitute), the 'When When' catchword fixed, "
  "'***' printer's mark before the single-wicket rule.",
  NC, "segmentation_artefact", "high", "derived",
  "Same provisions. 'some other person' does not change who may stand out.", ["S18"])
