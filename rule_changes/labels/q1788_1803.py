"""Labels for 1788 -> 1803.

Edition note: the dataset's '1803' text is R. Pocock's Gravesend printing (raw OCR title page; misdated '1903' by OCR). Rait Kerr (App.
III) says it agrees with Britcher's reliable 1798-1803 texts 'except for one divergence in sequence' (the wicket-keeper Law placed
earlier). The real changes in this pair are the 1798 revision, Rait Kerr serials 45-49."""
from _h import make
PAIR = "1788_1803"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
EN, EF = "ENJOYMENT", "EXTERNAL_FORCE"
BAL = ("Rait Kerr serial 48: 'The benefits granted to the bowler by Serial Numbers 47 and 48 are particularly interesting as the first "
       "evidence of a set policy to maintain an even balance between the bowler and the batsman'. In ch.2 he says the early M.C.C.'s major "
       "alterations were 'confined to giving assistance to the bowler by increasing the size of the wicket, and by allowing a new ball at the "
       "start of each innings'.")

L("E001",
  "Ball: new 'At the beginning of each innings either party may call for a new ball.' The 1788 clause 'it cannot be changed during the Game, "
  "but by the consent of both Parties' is dropped, and 'nor more than' -> 'and not more than'.",
  EN, "bowler_batsman_balance", "high", "stated",
  BAL + " Serial 47: 'A new ball may be demanded by either side at the start of each innings.'",
  ["S16"], date="1798 (Rait Kerr serial 47); first in the dataset in the 1803 Pocock printing")
L("E002",
  "Striker-out list re-segmented (Pocock prints it as one ';or,' chain). Three new provisions are attached here: 'If the striker is hurt, he "
  "may retire from his wicket, and have his innings at any time in that innings' (replacing the umpires' 'the person hurt shall have his "
  "hands in any part of the Innings'); 'If a striker is hurt, some person may be allowed to stand out for him, but not go in' (a substitute "
  "fielder for an injured player); and 'If any person stops the ball with his hat, the ball is to be considered as dead, and the opposite "
  "party to add five notches to their score: if any are run, they are to have five in all.' Variants: 'and either wilfully strike it again' "
  "(was 'he wilfully strikes'), 'takes up his ball' (was 'the Ball').",
  EF, "dress_fashion", "medium", "inferred",
  "Rait Kerr serial 49a (1798): 'A new Law provides a penalty of 5 runs if the fieldsman stops a ball with his hat. No doubt the adoption of "
  "the top hat as part of the usual attire of the players led to this introduction.' Serial 49b: 'Dead ball' is used for the first time in "
  "this Law. 'No doubt' marks his own inference. Serial 45 (1798, 'substitutes in the field is recognised without restriction') covers the "
  "stand-out rule and gives no cause, hence secondary UNCATEGORISED. 'either' and 'his ball' are Pocock's variants (ACS's 1809 Wallis text "
  "has 'he' and 'the Ball').",
  ["S16", "S31-03"], sec=UN, secsub="no_cause_stated", date="1798 (Rait Kerr serials 45, 49)")
L("E003",
  "'If If the ball is struck up' (duplicated word from the page catchword) and single wicket 'to strike at the Ball' -> 'to strike the ball'.",
  NC, "format_artefact", "high", "derived",
  "The doubled 'If' is the printer's catchword repeated at a page break. 'strike the ball' is Pocock's variant; the reliable Wallis 1809 "
  "text (ACS) still reads 'to strike at the Ball'. No change.",
  ["S18", "S31-03"])
L("E004",
  "Umpires: sentences re-split and the hurt-striker rule moved to the strikers' list. New: 'The Umpires are not to be changed during the "
  "match, but by the consent of both parties.'",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 46 (1798): 'Permission to change umpires by mutual consent is again granted', restoring a 1744/1755 point dropped in 1774 "
  "(serial 24). He gives no cause for the 1798 restoration.",
  ["S16"], date="1798 (Rait Kerr serial 46)")
L("E005",
  "Stumps: 'must be twenty-two Inches out of the Ground, the Bail six Inches' -> 'Which are three, must be twenty-four inches out of the "
  "ground, the BAIL seven inches in length'. The wicket is now 24 x 7 in (bail 7 in). 'Which are three' restates the three stumps.",
  EN, "bowler_batsman_balance", "high", "stated",
  BAL + " Serial 48 (1798): 'The wicket is increased to measure 24 by 7 inches, with the bail 7 inches long.' Numbers confirmed in raw OCR "
  "1803 ('twenty-four ... seven'). 'Which are three' is Pocock's wording: the Wallis 1809 text (ACS) does not have it, and Rait Kerr serial "
  "39 says the number was not officially specified until 1838.",
  ["S16", "S31-03", "S31-04"], date="1798 (Rait Kerr serial 48)")
L("E007",
  "Visiting side and ground-alteration rules: heading words 'FROM HOME' moved into the text, the long sentence split in two, 'a Striker' -> "
  "'the striker', 'holes' -> 'the holes'.",
  NC, "segmentation_artefact", "high", "derived", "Same provisions; sentence/heading split differs.", ["S18"])
L("E008",
  "The 1788 striker-out pseudo-Law is removed; its provisions are in the re-segmented strikers' list.",
  NC, "segmentation_artefact", "high", "derived", "Provisions present in 1803; segmentation artefact.", ["S18"])
L("E009",
  "Bowler: 'returnreturn-crease' (page catchword 'return-' repeated across a page break) and hyphenation.",
  NC, "format_artefact", "high", "derived",
  "The raw OCR shows 'return-' / 'CRICKET.' / 'return-crease' at a page break; the wording is otherwise unchanged.", ["S18", "S31-04"])
