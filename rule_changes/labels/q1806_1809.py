"""Labels for 1806 -> 1809.

Edition note: the dataset's '1806' text is J. Bailey's undated printing (c.1809-11 per Rait Kerr App. III). The '1809' text is
J. Baxter's booklet (Sussex Press, Lewes, 1809; raw OCR colophon 'BAXTER, PRINTER, LEWES'). Rait Kerr says Baxter's text 'Both in
sequence and detail ... differ[s] from the more authentic Wallis print of the same year, and [it] must be regarded as unreliable'.
Baxter follows the older Britcher/Pocock text. So most events here are the Bailey changes (wides, no ball, underhand, trial balls,
umpires pitch, toss, lost ball) seeming to disappear, plus two Baxter-only oddities ('four or six balls', 'NOT OUT' if the striker
hits the other wicket). The authentic Wallis 1809 text (ACS, S31-03) has neither oddity and does have the lost-ball law. None of
these events is a change to the M.C.C. Laws."""
from _h import make
PAIR = "1806_1809"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
ED = ("Edition artefact: '1806' = Bailey c.1809-11 (Rait Kerr App. III); '1809' = Baxter, Lewes 1809, which Rait Kerr calls unreliable. "
      "Proposed subtype: edition_artefact.")
EV = ["S16", "S31-03", "S31-04"]

L("E001",
  "Ball: 'Must weigh not less than ... nor more than' -> 'Must not weigh less than ... and not more than'.",
  ST, "wording_only", "high", "derived", "Same limits; word order only.", ["S18"])
L("E002",
  "Striker-out list. The lost-ball rule ('If a lost Ball is called, the Striker shall be allowed four...') is absent in Baxter. 'in striking "
  "at any other time' -> 'in striking, or at any other time'. 'he wilfully strikes' -> 'either wilfully strike'. 'other party' -> "
  "'opposite party'. 'hall' is OCR for 'ball'.",
  NC, "", "medium", "derived",
  "The lost-ball law was in force by May 1809: Rait Kerr serial 51 dates it 'After 1803 but before May 25th 1809', and the Wallis broadsheet "
  "of 25 May 1809 (ACS) contains it. Baxter's text simply copies the older Britcher/Pocock wording ('either wilfully strike', 'his ball'), "
  "which also restores the 'or' that Bailey had dropped. Not a repeal.",
  EV, date=ED, integrity="suspect", note=ED)
L("E003",
  "Striker list re-segmented; 'some other person' -> 'some person' (stand-out substitute).",
  NC, "segmentation_artefact", "high", "derived", "Same provisions; printer's variant of one word.", ["S18"])
L("E004",
  "New pseudo-Law 'NOT OUT: If the striker hits the other wicket, and his partner off his guard.'",
  NC, "", "medium", "derived",
  "This rule is in no reliable edition. The authentic Wallis 1809 text (ACS) does not have it, nor do the Bailey, 1816 or 1820 Craft texts. "
  "Rait Kerr's chronology has no such change, and he regards Baxter's 1809 Laws as unreliable, differing from Wallis 'in sequence and "
  "detail'. Raw OCR confirms that Baxter printed it (raw 1809 lines 167-169). It is a Baxter-only provision, not an M.C.C. Law.",
  EV, date=ED, integrity="suspect", note="Baxter-only provision; ask owner whether unofficial-printing provisions should be kept as events")
L("E005",
  "'The Umpires, in all matches, to pitch fair Wickets, and the parties to toss for the choice of Innings.' is absent in Baxter.",
  NC, "", "medium", "derived",
  "This is Rait Kerr serials 52-53 ('Before 1811'), present in Bailey and in the official 1816 and 1820 texts. Baxter reprints the older rule "
  "(visiting side chooses). The absence reflects Baxter's out-of-date source, not a repeal.",
  EV, date=ED, integrity="suspect", note=ED)
L("E006",
  "'The Umpire at the Bowler's Wicket shall be first applied to' -> 'That the umpire at the bowler's wicket be first applied to'.",
  ST, "wording_only", "high", "derived",
  "Same rule. 'That ...' is the 1788 code's own form ('That the Umpire at the Bowler's Wicket shall be first applied to').", ["S18"])
L("E007",
  "Stumps: 'Must be twenty-four inches ... the BAILS seven inches' -> 'Which are three, must be twenty-four inches ... the bails seven inches'; "
  "page mark 'A2' removed.",
  NC, "", "high", "derived",
  "'Which are three' is the Pocock/Baxter wording; the Wallis 1809 text (ACS) does not have it. Dimensions are unchanged (raw OCR).",
  EV, date=ED, note=ED)
L("E008",
  "Wickets: ', which shall be pitched within thirty yards of a centre fixed by the adversaries' is dropped here (Baxter puts it back under "
  "the visiting side's choice).",
  NC, "", "medium", "derived",
  "This is the old (pre-serial-52) arrangement, which Baxter reprints. It is not a change to the Laws.", EV, date=ED, integrity="suspect", note=ED)
L("E009",
  "Removed in Baxter: 'The Ball must be bowled underhand, and delivered with the hand below the elbow' and the two practice (trial) balls "
  "for a change of bowling.",
  NC, "", "medium", "derived",
  "The underhand rule (serial 55, before 1811) and trial balls (serial 57, before 1817) are in Bailey and in the official 1816 Craft text. "
  "Their absence from Baxter reflects his out-of-date source; he can also predate their adoption. Not a repeal.",
  EV, date=ED, integrity="suspect", note=ED)
L("E010",
  "'THE PARTY WHICH GOES FROM HOME Shall have the choice of the innings, and the pitching of the wickets ... When the parties meet at a third "
  "place, the bowlers shall toss up...' reappears, followed by the ground-alteration rule.",
  NC, "", "medium", "derived",
  "This is the rule replaced by the umpires pitching and the toss (serials 52-53). It is in the Wallis 1809 text (ACS) but not in Bailey. "
  "Its reappearance here comes from the dataset ordering Bailey (c.1809-11) before Baxter (1809), not from a restoration.",
  EV, date=ED, integrity="suspect", note=ED)
L("E011",
  "Ground-alteration rule moved from 'THE WICKETS' to the visiting-side heading; 'holes' -> 'the holes', 'his saw-dust' -> 'sawdust'.",
  NC, "segmentation_artefact", "high", "derived", "Relocation with printer's variants.", ["S18"])
L("E012",
  "Bowler: 'shall bowl four Balls' -> 'shall bowl four or six balls'. Wides rule and 'the Striker may play at [a No Ball]' rule absent.",
  NC, "", "medium", "derived",
  "'four or six' is printed in Baxter (raw OCR 1809 lines 81-82). But the authentic Wallis 1809 text (ACS) and the official 1816/1820 texts all "
  "have 'four Balls'. Rait Kerr's chronology keeps the four-ball over until 1889 (serial 108) and treats Baxter as unreliable. The wides "
  "(serial 56) and no-ball (serial 54) rules are in Bailey and in 1816; their absence reflects Baxter's out-of-date source.",
  EV, date=ED, integrity="suspect", note="Baxter-only 'four or six balls'; " + ED)
