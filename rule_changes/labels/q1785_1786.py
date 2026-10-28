"""Labels for 1785 -> 1786.

Edition note: the dataset's '1786' text begins 'LAWS, &c' and ends 'END of the NEW LAWS', followed by the 1755 code, which the project
removed. This matches Rait Kerr's account (App. III) of the 'New Articles of the Game of Cricket' printed for H. Turpin in 1786. He says
these 'are identical with the version given in the Ridley edition of 1774, and contain none of the alterations noted in the Wallis
broadsheet', that 'there is no reference to the introduction of the third stump', and that the 1755 code is printed 'immediately after
the one for 1774', calling the booklet unreliable for lax editorship. The text agrees with the ACS transcription of the 1774 code
(S31-02). So this pair compares the Wallis 1785 broadsheet with a reprint of the 1774 code. Nothing in it is a change to the Laws."""
from _h import make
PAIR = "1785_1786"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
ED = "Dataset '1786' = Turpin 'New Articles' 1786, a reprint of the 1774 code (Rait Kerr App. III); '1785' = Wallis broadsheet 1 Sept 1785."

L("E001",
  "The strikers' block that the 1785 segmentation treated as its own pseudo-Law (L.B.W., crossing, running before delivery, hindering a "
  "catch, guarding the wicket, single wicket) is removed. All of it reappears under 'STRIKER' in 1786.",
  NC, "segmentation_artefact", "high", "derived",
  "Every provision is in the 1786 text (the matching relocation event). Heading-based segmentation produced the removal.", ["S18"], date=ED)
L("E002",
  "No-ball call: 'the Umpires unasked must call No Ball' -> 'the Umpire unasked must call No Ball'; page number '( 6 )' added.",
  NC, "", "medium", "derived",
  "'Umpire' is the 1774 code's reading (ACS 1774) and 'Umpires' is the Wallis variant. The page number is OCR layout. No change.",
  ["S31-02", "S31-04"], date=ED, note="Printer variant + page number (proposed subtype edition_artefact)")
L("E003",
  "Stumps: the Wallis note 'It is lately settled to use three Stumps instead of two to each Wicket, the Ball [Bail] the same Length as "
  "above' is absent in 1786, which gives only 'MUST be Twenty-two Inches, the Bail Six Inches long'.",
  NC, "", "high", "derived",
  "The three-stump wicket was not abolished. Rait Kerr says the 1786 Turpin booklet reproduces the 1774 Ridley text and 'there is no "
  "reference to the introduction of the third stump, although an engraving is inserted depicting the three-stump wicket in use'. The note is "
  "missing because this unreliable reprint copied the pre-1775 code.",
  ["S16", "S31-02", "S31-04"], date=ED + " Third stump c.1775 (serial 34).", integrity="suspect",
  note="Edition artefact (proposed subtype edition_artefact)")
L("E004",
  "Bowling crease: 'parallal' -> 'parallel', hyphenation, page number '( 3 )'.",
  NC, "format_artefact", "high", "derived", "Same words.", ["S18"])
L("E005",
  "Bowler: capitalisation/punctuation, and 'to stand' -> 'to Hand' (OCR misreading of 'stand'; raw OCR 1786 line 42 'Hand on which Side').",
  NC, "ocr_noise", "high", "derived",
  "'Hand' is an OCR misreading (the long-s 'ſtand' read as 'Hand'), and the 1788 text again reads 'stand'.", ["S18", "S31-04"])
L("E006",
  "Striker out: 'Wrists' -> 'Wrist' (raw 'Wrift', long-s), 'though it be hugged' -> 'though if he hugged' (OCR), page number '( 4 )', "
  "'the Ball' -> 'a Ball', 'strikes' -> 'strike', and the run-out record completed with 'by the Ball'.",
  NC, "ocr_noise", "high", "derived",
  "All differences are OCR misreadings or printer's variants of identical provisions (ACS 1774: '(but not wrists)', 'though it be hugged').",
  ["S18", "S31-02"])
L("E007",
  "Handling-the-ball provision moved back into the striker list; wording identical.",
  NC, "segmentation_artefact", "high", "derived", "Relocation produced by segmentation.", ["S18"])
L("E008",
  "Six strikers' provisions moved back under 'STRIKER'. 'Legs' -> 'Leg', 'the Wicket' -> 'his Wicket', 'out of the Ground' -> 'out of "
  "his Ground', otherwise capitalisation.",
  NC, "segmentation_artefact", "high", "derived",
  "Relocation only. The small word differences are Wallis's variants against the 1774 code's 'leg', 'his wicket', 'his ground' (ACS 1774).",
  ["S18", "S31-02"])
L("E010",
  "A duplicate truncated segment of the handling-the-ball provision ('...unless at the Request of the Opposite') is removed.",
  NC, "segmentation_artefact", "high", "derived", "The provision is still present in 1786; only the duplicate segment goes.", ["S18"])
L("E011",
  "Wicket-keeper: 'Foot' -> 'Boot' (OCR) and 'touch' -> 'hit'.",
  NC, "ocr_noise", "high", "derived",
  "'Boot' is an OCR misreading (raw 1786 line 101). 'hit' is the 1774 code's reading (ACS) and 'touch' was a Wallis variant.",
  ["S18", "S31-02"])
