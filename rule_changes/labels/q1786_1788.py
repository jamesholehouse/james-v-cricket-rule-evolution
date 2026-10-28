"""Labels for 1786 -> 1788.

Edition note: the dataset's '1786' text is the Turpin 1786 reprint of the 1774 code (Rait Kerr App. III; it matches the ACS 1774
transcription S31-02). So this pair is effectively the 1774 code -> the first M.C.C. code of 30 May 1788 (as in Britcher), Rait Kerr
serials 38-44. The reintroduction of Hit wicket (serial 37, c.1786) and the c.1787 obstruction law (serial 38) also show up here."""
from _h import make
PAIR = "1786_1788"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
EN, EC = "ENJOYMENT", "ECONOMY"
D88 = "First M.C.C. code, 30 May 1788 (Britcher; Rait Kerr App. III notes Britcher may have included later changes)."
CL = ("Rait Kerr ch.2 on the 1788 code: 'The new code contained only four new provisions—of these, three were closer definitions of the "
      "Laws dealing with \"L.B.W.,\" the obstruction of a catch, and for the disallowance of runs in the case of a catch or a run out—all in "
      "strict keeping with Hambledon's established conception of the game as one deserving more detailed legislation than had hitherto been provided.'")

L("E001",
  "Ball: 'MUST not weigh less than ... nor more than ...' -> 'must weigh not less than ... nor more than ...'; the no-change sentence is "
  "merged in, with 'but with Consent of both Parties' -> 'but by the consent of both Parties'. Same limits (5.5-5.75 oz).",
  ST, "wording_only", "high", "derived",
  "Same requirement and numbers in both texts; only word order and sentence joining differ.", ["S18", "S31-02"], date=D88)
L("E002",
  "A block of strikers' provisions counted as a new pseudo-Law. It contains three new 1788 provisions. (1) Obstruction: 'Or, if under pretence "
  "of running a Notch, or otherwise, either of the Strikers prevent a Ball from being caught, the Striker of the Ball is out.' This replaces "
  "'Or if he runs out of his ground to hinder a catch' and the old licence that 'it is lawful for the strikers to hinder its being catched'. "
  "(2) L.B.W. rewritten: 'If with his foot or leg he stops the Ball, which the Bowler in the opinion of the Umpire at the Bowler's Wicket "
  "shall have pitched in straight line to the Wicket, and would have hit it' (old: 'puts his leg before the wicket with a design to stop the "
  "ball'). (3) 'When a Ball is caught, no Notch to be reckoned. When a Striker is run out, the Notch they were running for is not to be "
  "reckoned.' Also 'before it has lain still' -> 'while in play' for handling the ball, and the ball in the bowler's or keeper's hands 'is "
  "considered as no longer in Play'.",
  ST, "codification_definition", "high", "stated",
  CL + " Serials 41 (runs on a catch/run out), 43 (L.B.W. restricted to a ball 'pitched in a straight line to the wicket') and 38 (obstruction "
  "law, first in the second Maidstone edition c.1787 'in identical wording to that later used in the first M.C.C. Code'). Rait Kerr states "
  "the purpose of these specific provisions (closer definition). L.B.W. now turns on where the ball pitched rather than the batsman's design.",
  ["S16"], date="30 May 1788 (serials 41, 43); obstruction wording c.1787 (serial 38). " + D88)
L("E003",
  "Six strikers' provisions relocated. Substantive wording changes: handling the ball 'before it has lain still' -> 'while in play'. The "
  "bowler/keeper clause adds 'it is considered as no longer in Play' (first statement of when the ball becomes dead between deliveries). "
  "'that is put down' -> 'which is put down'; 'Single-Wicket' -> 'single Wicket'.",
  ST, "codification_definition", "medium", "inferred",
  "Rait Kerr has no serial for the 'in play' wording. It belongs to the 1788 code, whose new provisions he describes as closer definitions "
  "giving the game 'more detailed legislation'. Applied to these clauses, that is an inference. The 'in play' concept replaces a vaguer "
  "test ('lain still') without changing the rule's purpose.",
  ["S16"], date=D88)
L("E004",
  "Wicket-keeper: 'Boot' (OCR in 1786 for 'Foot') -> 'feet'; otherwise identical.",
  NC, "ocr_noise", "high", "derived",
  "'Boot' is an OCR misreading of 'Foot' (ACS 1774: 'foot'); 'foot' -> 'feet' does not change the rule.", ["S18", "S31-02"])
L("E005",
  "Umpires: 'They are the sole Judges of fair and unfair Play, and all Disputes shall be determined by them' gains '; each at his own Wicket'. "
  "New: 'But in case of a Catch, which the Umpire at the Wicket cannot see sufficiently to decide upon, he may apply to the other Umpire "
  "whose opinion is conclusive' and 'That the Umpire at the Bowler's Wicket shall be first applied to decide on all Catches'. Also 'allow' "
  "-> 'permit' (hurt striker), 'the Umpire unasked must call' -> 'they must, unasked, call No Ball', 'If the Strikers run' -> 'If the Striker "
  "runs'.",
  ST, "drafting_omission", "medium", "inferred",
  "Rait Kerr serial 44 (1788): 'The jurisdiction of the umpires in respect of an appeal for a catch is again introduced', restoring the "
  "1744/1755 'each at his own wicket' dropped in 1774 (serial 33). He conjectures that this 1774 omission 'may well have resulted from careless "
  "drafting'. Reading the 1788 restoration as a correction of that omission is an inference. The new mechanism (refer an unseen catch to the "
  "other umpire; the bowler's-end umpire first) has no stated cause, hence secondary UNCATEGORISED.",
  ["S16"], sec=UN, secsub="no_cause_stated", date="30 May 1788 (serial 44)")
L("E006",
  "Bets: 'the Bet depends on both Innings, unless otherwise specified' -> 'the Bets depend on the first Innings, unless otherwise "
  "specified' (default reversed). The second rule now starts 'If the Bets are made upon both Innings, and one party beat the other in one "
  "Innings...'.",
  EC, "betting_stakes", "low", "inferred",
  "Rait Kerr gives no serial or cause for this change. He says the betting Laws themselves 'were introduced to meet the changing requirements "
  "of the gamblers' (1774) and describes stakes rising up to 1790. Attributing the 1788 change of default settlement to the same purpose is "
  "an inference. The provision only concerns how bets are settled, so ECONOMY is the only plausible domain.",
  ["S16"], date=D88)
L("E007",
  "Stumps: 'MUST be Twenty-two Inches, the Bail Six Inches long' -> 'must be twenty-two Inches out of the Ground, the Bail six Inches, in "
  "length'. The height is now measured above ground. The number of stumps is not stated in either text.",
  ST, "codification_definition", "medium", "inferred",
  "Rait Kerr serial 39 (1788): 'The number of stumps is not specified ... It would seem that the three-stump wicket had been so commonly "
  "accepted by this year that no special reference to it was thought necessary', and the bail is 6 inches. 'out of the Ground' is a closer "
  "definition in line with his account of the 1788 code; there is no serial for it, so this is inferred. Numbers confirmed in raw OCR.",
  ["S16"], date="30 May 1788 (serial 39)")
L("E008",
  "Bowling crease: 'MUST be parallel with the Stumps' -> 'must be in a line with the Stumps'; same length (3 ft) and return crease. Page "
  "number '( 3 )' removed.",
  SW, "clarifying_rewrite", "low", "derived",
  "Both phrasings place the crease along the line of the stumps, so the requirement is unchanged. 'in a line with' is the more exact "
  "statement. Neither Rait Kerr nor the 1788 text indicates a change of position.",
  ["S16", "S18"], date=D88)
L("E009",
  "Popping crease: 'from the Wickets; and the Wickets must be opposite to each other at the Distance of Twenty-two Yards' -> 'from the "
  "Wicket, and parallel to it'. The 22-yard clause moves to a new 'THE WICKETS' heading, and the crease is now required to be parallel "
  "to the wicket. The distance is unchanged at 3 ft 10 in.",
  ST, "codification_definition", "medium", "inferred",
  "There is no Rait Kerr serial for 'parallel to it'. It is a closer definition of the kind he says the 1788 code made (inferred). Numbers are "
  "confirmed in raw OCR.",
  ["S16"], date=D88)
L("E010",
  "New heading 'THE WICKETS: must be opposite to each other, at the distance of twenty-two yards' (wording previously in the popping-crease Law).",
  ST, "reorganisation", "high", "derived", "Same requirement under its own heading.", ["S18"], date=D88)
L("E011",
  "Visiting side: wording the same, but the third-place toss is now 'for the pitching of the Wickets' (was 'of the First Wicket'). New rule: "
  "'It shall not be lawful for either Party during a Match without the consent of the other to alter the Ground, by rolling, watering, "
  "covering, mowing, or beating; this rule is not meant to prevent a Striker from beating the ground with his Bat near where he stands "
  "during the Innings, or to prevent the Bowler from filling up holes, watering his ground, or using Sawdust, &c. when the ground is wet.'",
  EN, "quality_of_play", "medium", "inferred",
  "Rait Kerr serial 40 (30 May 1788): 'For the first time a Law provides for rolling, watering, covering, mowing and beating of the pitch "
  "during a match by mutual consent'. In ch.2 he calls it 'surely the earliest sign of the now accepted principle that bad conditions make for "
  "bad cricket; doubtless it reflected the tremendous advance made in bowling technique, and thereby in batting, by such players as David "
  "Harris'. That is his own inference ('surely', 'doubtless'), so the basis is inferred.",
  ["S16"], date="30 May 1788 (serial 40)")
L("E012",
  "Bowler: 'MUST deliver the Ball' -> 'shall deliver the Ball'. 'He may order the Player at his Wicket to [stand]' -> 'He may order the "
  "Striker, at his Wicket, to stand'. 'Hand' in 1786 is OCR for 'stand'.",
  SW, "modal_strength", "low", "derived",
  "'must' -> 'shall' is a change of modal verb in a mandatory rule. Both are mandatory, so enforcement is unaffected. 'Player' -> 'Striker' "
  "names the person more exactly. No source treats either as a rule change.",
  ["S18"], date=D88)
L("E013",
  "Striker-out list. Hit wicket reintroduced in new words: 'Or if in striking at the Ball he hits down his [Wicket]'. Stumping extended: "
  "'if, in Striking, both his Feet are over the Popping-Crease' -> 'if in striking, or at any other time while the Ball is in play, both his "
  "feet are over the Popping Crease'. Catch rule 'upon his Hands' -> 'upon his hand', 'though if he hugged' (OCR) -> 'although it be "
  "hugged'. The old L.B.W. rule, 'it is lawful for the strikers to hinder its being catched', and the old run-out wording leave this list; "
  "their replacements are in the new block (see the event adding the obstruction law).",
  ST, "drafting_omission", "medium", "conjecture",
  "Rait Kerr serial 42 (1788): 'The reintroduction of the \"Hit wicket\" Law is confirmed in a new form of words' (it first reappeared c.1786, "
  "serial 37). It had disappeared in 1774 (serial 32a), which he conjectures 'may well have resulted from careless drafting', so restoring it "
  "corrects a drafting omission (conjecture). The 'at any other time while the Ball is in play' extension of stumping has no serial or "
  "stated cause, hence secondary UNCATEGORISED.",
  ["S16"], sec=UN, secsub="no_cause_stated", date="30 May 1788 (serial 42); c.1786 in the Maidstone edition (serial 37)")
