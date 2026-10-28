"""Labels for 1816 -> 1820 (T. Craft broadsheets of 1816 and 1820; both reliable per Rait Kerr App. III).

Real changes: Rait Kerr serials 59 (wicket 26 x 7 in), 60 (popping crease 4 ft) and 61 (Hit wicket by dress), all 'Before 1821' and
'almost certainly made in 1819'. The 1820 text is reproduced in facsimile in Rait Kerr (p.25), which lets the AI clean-up of the
badly OCR'd 1820 text be checked."""
from _h import make
PAIR = "1816_1820"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
EN = "ENJOYMENT"
D19 = "Before 1821; 'almost certainly made in 1819' (Rait Kerr note to serials 59-61: a 29 June 1819 match 'with the wicket two inches higher than usual')."

L("E001",
  "Ball: 'must not weigh less than' -> 'must weigh not less than'; 'either may call' -> 'either Party may call'; capitalisation.",
  ST, "wording_only", "high", "derived", "Same limits and the same new-ball right.", ["S18"])
L("E002",
  "The 1816 wicket-keepers pseudo-Law is removed; the provision reappears inside a merged block in 1820 (one-paragraph layout).",
  NC, "segmentation_artefact", "high", "derived", "Provision present in 1820; heading-based segmentation lost it.", ["S18"])
L("E003",
  "The 1816 umpires pseudo-Law is removed; all eight provisions reappear in the merged block in 1820.",
  NC, "segmentation_artefact", "high", "derived", "Provisions present in 1820.", ["S18"])
L("E004",
  "Bat: 'four inches and a quarter' -> 'Four Inches and One Quarter, in the widest part'.",
  ST, "wording_only", "high", "derived", "Same 4¼ in limit.", ["S18"])
L("E005",
  "Stumps: 'twenty-four inches out of the ground' -> 'Twenty-six Inches out of the ground'; bails still seven inches. The wicket becomes 26 x 7 in.",
  EN, "bowler_batsman_balance", "high", "stated",
  "Rait Kerr serial 59 ('Before 1821'): 'The Wicket is increased to measure 26 by 7 inches.' In ch.2, of the major 1810-35 changes, 'three "
  "were designed to help the bowler by twice increasing the size of the wicket ... and by extending the \"L.B.W.\" Law'. The number is "
  "confirmed by raw OCR 1820 ('Twenty-six Inches') and by Rait Kerr's facsimile of the 1820 Craft broadsheet.",
  ["S16", "S31-04"], date=D19)
L("E006",
  "Popping crease: 'three feet ten inches from the wicket' -> 'Four Feet from the Wicket'. The ground-alteration rule is re-segmented into "
  "this block. The processed 1820 text reads 'by watering, covering, mowing, or beating: this rule is to prevent the Striker...', but this "
  "is a clean-up error. Rait Kerr's facsimile of the same 1820 broadsheet reads 'by rolling, watering, covering, mowing, or beating: This "
  "rule is not meant to prevent the Striker', and the raw OCR is illegible there ('by ro' / 'his ru . i- - -').",
  ST, "consequential", "high", "stated",
  "Rait Kerr serial 60 ('Before 1821'): 'The distance of the Popping crease from the wicket is increased to 4 feet as a result of the increase "
  "in the height of the wicket.' This states that the change follows from serial 59. 'Four Feet' is confirmed in raw OCR. The apparent removal "
  "of 'rolling' and inversion of 'not meant to' are AI clean-up artefacts, not rule changes.",
  ["S16", "S17", "S31-04"], date=D19, integrity="suspect",
  note="Popping-crease change is sound; the ground-alteration wording in processed 1820 is corrupted (missing 'rolling', 'not meant')")
L("E007",
  "Wickets provision relocated; 'within thirty yards, fixed by' (1816, OCR loss) -> 'within Thirty Yards of a centre fixed by the "
  "Adversaries'.",
  NC, "segmentation_artefact", "high", "derived",
  "Same rule. 'of a centre' was lost in the 1816 OCR (raw: 'yarcis / fixed by the adversaries').", ["S18", "S31-04"])
L("E008",
  "Bowler provision relocated; 'must bowl four balls ... which he is to do but once' -> 'shall bowl Four Balls ... which he shall do but "
  "once'.",
  SW, "modal_strength", "low", "derived",
  "Reverts the 1816 'must'/'is to' to 'shall'. Both are mandatory and the four-ball over is unchanged, so there is no effect on the rule.",
  ["S18"])
L("E009",
  "The 1816 'THE WICKETS' pseudo-Law (wickets + ground-alteration rule) is removed; both provisions reappear in the merged 1820 block.",
  NC, "segmentation_artefact", "high", "derived", "Provisions present in 1820.", ["S18"])
L("E010",
  "New striker-out rule: 'Or, if any part of the Striker's dress knocks down the Wicket.' The other records in the block differ only "
  "slightly. No-ball law 'any part of the hand' -> 'any part of the back of the hand' (1820 matches Rait Kerr's quotation of the 1816 "
  "law), and 1820 drops 'when the ball is delivered'. Wides 'put down to them' -> 'put down to the Byes'. L.B.W. 'has pitched' -> 'shall "
  "pitch'. Catch rule 'upon his hand' -> 'on his hand'.",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 61 ('Before 1821'): 'The striker is out \"Hit wicket\" if any part of his dress breaks the wicket.' He gives no cause. "
  "Integrity: the other differences are text artefacts. Rait Kerr's facsimile of the 1820 broadsheet includes 'when the Ball is delivered' "
  "(raw OCR 'then the Ball is delivered'), 'shall have pitched' (raw OCR 'shall ' si-tched') and 'upon his hand' (raw OCR 'son his hand'). "
  "The AI clean-up dropped or altered those words. 'to them' in 1816 was a clean-up guess for illegible 'to the/'. 'back of the hand' is in "
  "Rait Kerr's quotation of the 1816 law, so the 1816 omission is probably a text problem too.",
  ["S16", "S17", "S31-04"], date=D19, integrity="suspect",
  note="Only the dress-hit-wicket rule is a real change; other differences are clean-up/OCR artefacts")
L("E011",
  "Ten striker provisions relocated into the merged block; capitalisation and punctuation only ('running' -> 'running for' restores a word "
  "the 1816 text lacks).",
  NC, "segmentation_artefact", "high", "derived", "Same provisions.", ["S18"])
L("E012",
  "Wicket-keeper provision relocated; 'must stand ... must not move ... not incommode the Striker by any noise' -> 'shall stand ... shall not "
  "move ... shall not by any noise incommode the Striker'.",
  SW, "modal_strength", "low", "derived",
  "Reverts the 1816 'must' to 'shall' (the wording of 1788-1809). Both are mandatory; no effect on the duty.", ["S18"])
L("E013",
  "Eight umpires' provisions relocated into the merged block. Only difference: 'is to be first applied to' -> 'That the Umpire ... shall be "
  "first applied to'.",
  NC, "segmentation_artefact", "high", "derived", "Same provisions; the 'That ... shall' form is the 1788 wording.", ["S18"])
L("E014",
  "The 1816 'THE BOWLER' pseudo-Law is removed; its provision reappears in the merged 1820 block.",
  NC, "segmentation_artefact", "high", "derived", "Provision present in 1820.", ["S18"])
L("E015",
  "The 1816 'THE STRIKER IS OUT' pseudo-Law is removed; its provisions reappear in the merged 1820 block.",
  NC, "segmentation_artefact", "high", "derived", "Provisions present in 1820.", ["S18"])
