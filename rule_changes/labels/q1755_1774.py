"""Labels for 1755 -> 1774.

Edition note: the dataset's '1774' text is not the Ridley printing of the 25 Feb 1774 code. Its raw OCR is titled 'New LAWS &c. Of
The Game of Cricket'. It mentions two bails in two places ('either of the bails are bowled off'; 'the two bails not to exceed six
inches'), it keeps the Hit wicket law, and it adds 'unless he returns to his ground after he has struck the ball' to the single-wicket
rule. These are the marks that Rait Kerr (App. III) uses to describe J. Blake's undated Maidstone edition (c.1786), and none of them is
in the ACS transcription of the 1774 code (S31-02). So this pair contains the 1774 revision (Rait Kerr serials 23-33) plus the
post-1774 changes up to c.1786 (serials 34, 36, 37)."""
from _h import make
PAIR = "1755_1774"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
EN, NE, EC = "ENJOYMENT", "NOVEL_EVENT", "ECONOMY"
ED = "Dataset '1774' text is a later printing (Blake's Maidstone edition c.1786 by Rait Kerr's App. III description); the 1774 code was adopted 25 Feb 1774."

L("E001",
  "The 1755 opening block is dropped as a unit and its contents are reorganised under separate headings ('The BOWLING-CREASE', 'The "
  "POPPING-CREASE', 'The Party which goes from Home'). The block contained: the toss for pitching the first wicket ('determined by the Toss "
  "of a Piece of Money'), the popping-crease distance (3 ft 10 in), the 22-yard distance between wickets, and 'The Bowling-Creases must be "
  "cut in a direct Line from each Stump'. The measurements carry over unchanged. Two real policy changes are hidden in the removal: the "
  "toss for the pitch gives way to the visiting side's choice, and the bowling crease is redefined. Each is labelled in the event that adds "
  "the new heading.",
  ST, "reorganisation", "high", "inferred",
  "Rait Kerr App. III states that the 1774 revision 'included radical modifications to both the sequence and the wording of the 1755 "
  "version'. The policy content is Rait Kerr serials 27 (choice of pitch and innings) and 28 (bowling crease 3 ft), for which he gives no cause.",
  ["S16", "S31-02"], sec=UN, secsub="no_cause_stated", date="25 Feb 1774 (Rait Kerr serials 27, 28)")
L("E002",
  "Ball: 'must weigh between Five & Six Ounces' -> 'MUST not weigh less than five ounces and a half, nor more than five ounces and three "
  "quarters' (tolerance narrowed to 5.5-5.75 oz). New: 'It cannot be changed during the game, but with consent of both parties'. This "
  "replaces the umpires' duty 'To mark the Ball that it may not be changed', and the ball may now be changed by consent. The old record "
  "also carried the toss-up for choice of innings, which moved to the visiting-side rule.",
  ST, "codification_definition", "medium", "inferred",
  "Rait Kerr serial 25: 'The tolerance for the weight of the ball is reduced to be between 5½ and 5¾ ounces'. He gives no reason for this "
  "item. He says the 1774 changes overall 'were mainly directed towards the closer definition necessary for the more serious game in course "
  "of development' (ch.2), so the closer-definition reading is inferred. Numbers are confirmed by raw OCR ('five ounces and a half ... five "
  "ounces and three quarters') and by the ACS 1774 transcription.",
  ["S16", "S31-02"], sec=UN, secsub="no_cause_stated", date="25 Feb 1774 (Rait Kerr serial 25)")
L("E003",
  "Umpires' Laws rewritten. (1) 'Ten Minutes between each Hand' -> 'fifteen minutes between each innings'. (2) 'When both Umpires call "
  "Play three Times, 'tis at the Peril of giving the Game' -> 'when the umpire shall call play, the party refusing to play shall lose the "
  "match'. (3) 'are not to allow a fresh Man to play, on either Side, on any Account' dropped, and the hurt man now 'shall have his place in "
  "any part of that innings'. (4) Dropped: umpires' sole judgement of 'frivolous Delays' and 'Hurts', of 'Hindrances' (with the power to "
  "order a notch for hindrance), 'Each Umpire is the sole Judge ... at his own Wicket', 'he shall not be changed for another Umpire, without "
  "the Consent of both Sides', and 'When the four Balls are bowl'd, he is to call over'. (5) New: umpires are 'sole judges of fair and "
  "unfair play, and all disputes'; 'appealed to by one of the Players' -> 'by the adversaries'; the no-ball call moved here from the "
  "bowlers' Law ('the umpire, unasked, must call no ball'); and new 'If the strikers run a short notch, the umpire must call no notch'.",
  UN, "no_cause_stated", "medium", "none",
  "Rait Kerr serials 29 (interval 10 -> 15 minutes; 'Play' called once), 30 ('Short runs' specially referred to for the first time) and 23 "
  "(substitutes no longer prohibited) give no cause. Serials 24 (umpires changed by consent), 31 (call of 'Over') and 33 (each umpire at his "
  "own wicket) are among the 'five omissions from the previous code which may well have resulted from careless drafting' (ch.2; Rait Kerr's "
  "conjecture). The secondary label records that conjecture.",
  ["S16", "S31-02"], sec=ST, secsub="drafting_omission", date="25 Feb 1774 (Rait Kerr serials 23, 24, 29, 30, 31, 33)")
L("E004",
  "New BETS section: 'If the notches of one player are laid against another, the bet depends on both innings, unless otherwise specified. "
  "If one party beats the other in one innings, the notches in the first innings shall determine the bet. But if the party goes in a second "
  "time, then the bet must be determined by the number on the score.'",
  EC, "betting_stakes", "high", "stated",
  "Rait Kerr ch.2: 'The 1774 Laws for betting were introduced to meet the changing requirements of the gamblers'. He quotes these three "
  "rules and links them to the growth of high-stakes matches and to a 1774 Chelmsford Chronicle attack on 'excessive gaming'.",
  ["S16", "S31-02"], date="25 Feb 1774", note="Blake text omits 'other' in 'if the other party goes in'; ACS 1774 has 'the other party'")
L("E005",
  "New SINGLE WICKET rule: 'If the striker moves out of his ground to strike at the ball, he shall be allowed no notch for such stroke, unless "
  "he returns to his ground after he has struck the ball.'",
  UN, "no_cause_stated", "medium", "none",
  "The single-wicket rule first appears in the 1774 code (ACS 1774: '...he shall be allowed no notch for such stroke'). The 'unless he returns "
  "...' clause is not in the 1774 code. It matches Rait Kerr's note that Blake's c.1786 edition has 'a minor alteration ... in a rule for "
  "the Single Wicket game' (App. III). Rait Kerr's chronology has no serial for this and gives no cause.",
  ["S16", "S31-02"], date="Rule from 25 Feb 1774; 'unless he returns' clause c.1786 (Blake). " + ED, integrity="suspect",
  note="The qualifying clause comes from a later, unofficial printing")
L("E006",
  "New BAT Law: 'Must not exceed four inches and one quarter in the widest part.' (no width limit before)",
  NE, "equipment_exploit", "high", "stated",
  "Rait Kerr serials 22 and 26: the Hambledon committee limited the width to 4¼ in on 25 Sept 1771, and the 1774 code confirms it. In ch.2 he quotes "
  "Nyren: a player named White, of Ryegate, 'brought a bat to a match, which being the width of the stumps, effectually defended his wicket "
  "from the bowler: and in consequence, a law was passed limiting the future width of the bat to four and a quarter inches'.",
  ["S16", "S31-02"], date="Hambledon decision 25 Sept 1771; in the code 25 Feb 1774")
L("E007",
  "Stumps: 'must be Twenty-Two Inches long, and the Bail Six Inches' -> 'Must be twenty-two inches, and the bail six inches long; but by a "
  "subsequent meeting it is settled for to use three stumps instead of two, to each wicket, and the two bails not to exceed six inches.' "
  "This introduces the three-stump wicket and two bails.",
  NE, "single_incident", "high", "stated",
  "Rait Kerr serial 34 (c.1775): the three-stump wicket followed the Hambledon v Kent single-wicket match of 22-23 May 1775, where Lumpy's "
  "balls passed three times between Small's two stumps. He quotes Nyren: 'it was considered to be a hard thing upon the bowler that his "
  "straightest balls should be thus sacrificed; the number of the stumps was in consequence increased from two to three'. Two bails are "
  "serial 36: first referred to in the Maidstone edition c.1786, no cause given. The 1774 code itself (ACS) has two stumps and one bail.",
  ["S16", "S31-02", "S31-04"], sec=EN, secsub="bowler_batsman_balance",
  date="Third stump c.1775 (serial 34; first in a dated edition in Wallis 1785, serial 35); two bails c.1786 (serial 36). " + ED,
  note="22 in / 6 in confirmed in raw OCR")
L("E008",
  "Bowling crease redefined: 'The Bowling-Creases must be cut in a direct Line from each Stump' -> 'Must be parallel with the stumps, three "
  "feet in length, with a return-crease.' The crease gets a fixed length and a return crease appears for the first time.",
  ST, "codification_definition", "medium", "inferred",
  "Rait Kerr serial 28: 'The Bowling Crease is defined as being 3 feet long on either side of the wicket'. He gives no cause for this "
  "item. His general statement that the 1774 changes were 'mainly directed towards the closer definition necessary for the more serious "
  "game' supports the closer-definition reading by inference.",
  ["S16", "S31-02"], date="25 Feb 1774 (Rait Kerr serial 28)",
  note="Rait Kerr's wording ('on either side of the wicket') differs from the printed 'three feet in length'; the number is not doubted")
L("E009",
  "New heading 'The POPPING-CREASE': 'Must be three feet ten inches from the wickets; and the wickets must be opposite to each other, at the "
  "distance of twenty-two yards.' The values are those of the 1755 opening block (3 ft 10 in; 22 yards), now under their own heading.",
  ST, "reorganisation", "high", "derived",
  "Values and requirement unchanged; only the position and heading are new. This is part of the 1774 'radical modifications to both the "
  "sequence and the wording' (Rait Kerr App. III).",
  ["S16", "S31-02"], date="25 Feb 1774")
L("E010",
  "Strikers' Laws rewritten as a list 'The STRIKER is out ... Or if ...'. The main change is the first L.B.W. law: 'Or if the striker puts his "
  "leg before the wicket with a design to stop the ball, and actually prevents the ball from hitting his wicket by it.' Other changes: "
  "'(but not Arms)' -> '(but not wrists)' in the catch rule and 'of the catcher' added. 'nipp'd up ... before it came to the Wicket' -> 'struck "
  "up, and he wilfully strike it again'. Run out may now be made 'with the ball in hand', and if the bail is off 'a stump must be struck out "
  "of the ground by the ball'. 'he that returns' -> 'he that has left the wicket'. 'unless ask'd by the Bowler, or Wicket-Keeper' -> 'unless "
  "at the request of the opposite party'. The old 'he may go where he pleases till the next Ball' becomes 'the strikers need not keep within "
  "their ground till the umpire has called play; but if the player goes out of his ground, with an intent to run before the ball is "
  "delivered, the bowler may put him out'. Dropped: the striker's partner placing 'his Body any where within the Swing of the Bat' to hinder a "
  "catch, the umpires ordering a notch for designed crossing, and 'The Bail hanging on one Stump ... it's not out'. The text also says 'either "
  "of the bails' (two bails).",
  EN, "bowler_batsman_balance", "medium", "attributed",
  "Rait Kerr serial 32b: 'The first specific \"L.B.W.\" Law is introduced'. He reports that 'Silver Billy' Beldham remembered it 'as a cure for "
  "the \"shabby\" methods adopted by the batsmen', and notes that the 1744 Laws already let umpires judge 'standing unfair to strike'. So the "
  "cause is Beldham's claim, reported by Rait Kerr. The other rewrites have no stated cause (Rait Kerr gives only the general 'closer "
  "definition' aim of 1774), hence the secondary UNCATEGORISED.",
  ["S16", "S31-02"], sec=UN, secsub="no_cause_stated", date="25 Feb 1774 (serial 32b); 'either of the bails' wording c.1786 (serial 36). " + ED)
L("E011",
  "New rule 'The Party which goes from Home Shall have the choice of the innings and the pitching of the wickets, which shall be pitched "
  "within thirty yards of a centre fixed by the adversaries. When the parties meet at a third place, the bowlers shall toss up for the "
  "pitching of the first wicket, and the choice of going in.' Before, a toss decided the pitching of the wicket, and the winner of the toss-up "
  "chose innings.",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 27 records the change (visiting team has choice of pitch and innings; toss at a 'Third Place') without giving a cause.",
  ["S16", "S31-02"], date="25 Feb 1774 (Rait Kerr serial 27)")
L("E012",
  "Bowler: 'with one Foot behind the Crease, even with the Wicket' -> 'with one foot behind the bowling-crease, and within the "
  "return-crease' (new lateral limit from the return crease). 'when he has bowl'd one Ball, or more, shall bowl to the Number of Four' -> "
  "'shall bowl four balls'. 'at a reasonable Distance' dropped from the bowler's right to place the striker. The no-ball rule ('hinder Foot "
  "over the Bowling-Crease ... no Person shall have any Right to question him') moves to the umpires' Law in a new form.",
  ST, "codification_definition", "medium", "inferred",
  "The return-crease limit follows from the new crease definition (Rait Kerr serial 28). Rait Kerr gives no specific cause. The 'closer "
  "definition' aim he gives for the 1774 revision supports this reading by inference. The moved no-ball rule is part of the event that "
  "rewrites the umpires' Laws.",
  ["S16", "S31-02"], sec=UN, secsub="no_cause_stated", date="25 Feb 1774")
L("E013",
  "Wicket-keeper: same wording apart from capitalisation, the heading's plural 'Wicket-Keepers', a stray 'for the' at the end of the 1755 "
  "record (OCR/page residue), and a comma.",
  NC, "format_artefact", "high", "derived",
  "Word-for-word the provision is the same in the 1755 and 1774 texts (ACS 1755 and 1774 agree).",
  ["S18", "S31-01", "S31-02"])
