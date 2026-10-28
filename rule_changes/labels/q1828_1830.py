"""Labels for 1828 -> 1830.

Context for every label in this module (checked against the texts and sources, not assumed):
- The dataset's 1828 text is the pre-May-1828 MCC code from The Sporting Magazine of 1828 (via Haygarth); the raw OCR
  (data/datasets/rule_texts/raw/1828_raw.txt) ends with the 19 May 1828 resolutions that the clean-up removed.
- The dataset's 1830 text is NOT an official MCC code. It is a pocket booklet with an instructional preamble ("for the
  information of young beginners") whose Laws reproduce, almost word for word, the 1819/1820 MCC wording (compare the 1820
  Craft broadsheet reproduced in Rait Kerr, S16 ch.2 p.25): three-foot bowling crease, wickets "pitched within thirty yards
  of a centre, by the adversaries", LBW "with his foot or leg ... pitched in a straight line", wicket-keeper "hands, knees,
  feet or head", the Single-wicket bail sentence, no single-wicket/bets numbering. Only the 1823 wicket size, six-run lost
  ball and the 1828 "wide ball" entry were updated. Rait Kerr App. III (S16) lists such an 1830 booklet ("Laws of the Manly
  and Noble Game of Cricket as revised by the Mary-le-bone Club in 1830", Lewis & Co.) as "nothing more than a reprint with
  a few alterations of the Farnham editions" in which "Many of the changes known from official records to have been made in
  1828 and 1829 are omitted"; the data appendix (S33-01) says the 1830 rulebook "does not have the changes recorded as
  having been made for 1830". The ACS transcription of the official 1829 Code (S33-02) confirms the official wording.
  So most differences here are source-edition artefacts, not rule changes. NOT_A_CHANGE has no subtype for "unreliable
  edition"; such rows use subtype "" and the phrase "source-edition artefact" (question raised in the report).
- The raw 1830 OCR jumps from page 9 to page 11 in the middle of the ground law ("when the"), so the end of that law and
  the after-rain law are lost with a missing page.
"""
from _h import make
PAIR = "1828_1830"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"

BOOK = ("The 1830 text is an unofficial booklet reprinting the 1819/1820 MCC wording (Rait Kerr App. III, S16: an 1830 booklet "
        "'nothing more than a reprint with a few alterations of the Farnham editions', omitting changes of 1828-29; data "
        "appendix S33-01). ")
SEG = "Segmentation artefact: the provision is still in the 1830 text, matched to a different event (pre-1884 texts are segmented as heading blocks). "
EV_B = ["S16", "S33-01", "S33-02"]

L("E001", "Added: the booklet's instructional preamble 'The particulars necessary to be attended to when a Game of Cricket is to be "
  "played, are-1. The number of players.-2. The selection of the ground.-3. The choice of Umpires. First, then, for the information "
  "of young beginners...'. Not a Law.", NC, "", "high", "derived",
  BOOK + "This is the booklet's own editorial introduction, not part of any MCC code (absent from the 1828 code and the official 1829 "
  "Code, S33-02). Source-edition artefact.", EV_B, note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E002", "1830 Wickets text 'must be opposite to each other, at the distance of twenty-two yards; which shall be pitched within thirty "
  "yards of a centre, by the adversaries' (the 1828 code has the umpires pitch them); ground law loses '&c.' and is cut off at 'when the'.",
  NC, "", "high", "derived",
  BOOK + "The 'thirty yards of a centre' wording is Rait Kerr serial 52 (before 1811), superseded by serial 63 (before May 1823: pitch "
  "left entirely to the umpires); the 1828 code and the official 1829 Code (S33-02, Law 6) have the umpires pitch the wickets, and the "
  "1835 text again has 'pitched ... by the umpires'. The ground-law truncation comes from a missing page in the 1830 scan (raw OCR "
  "jumps from p.9 to p.11). Source-edition artefact, not a rule change.", EV_B,
  date="Wording superseded before May 1823 (serial 63)", integrity="suspect", note="source-edition artefact + missing page")
L("E003", "Removed (at old Law 11 position): 'He may order the striker at his wicket to stand on which side of it he pleases.'",
  NC, "segmentation_artefact", "high", "derived", SEG + "The same sentence appears in the 1830 Bowler block (relocation event "
  "'He may order the striker, at his wicket, to stand on which side of it he please').", ["S18"])
L("E004", "Wides: 1828 'shall adjudge one run to the striker ... which shall be put down to the byes' becomes 1830 'the party that is "
  "in shall be allowed one notch, to be put down as a wide ball'; i.e. a wide is scored as a wide, no longer as a bye. (Same event: "
  "the Bowler law 'which he shall be permitted to do but once' -> 'which he shall do but once', 1820 booklet wording.)",
  UN, "no_cause_stated", "medium", "none",
  "Real change: Rait Kerr serial 71 (May 19th 1828): 'The allowance for a Wide is to be entered as such and no longer as a Bye'; the "
  "raw 1828 OCR records the 19 May 1828 resolution 'that the 12th Law should be altered by erasing the word \"byes\"', and the "
  "official 1829 Code (S33-02, Law 12) records the run as a wide. Neither Rait Kerr (ch.2, ch.6) nor S33-02 gives a reason. The rest "
  "of the 1830 wording ('so wide that the striker cannot play at it', no mention of the umpire or appeal) is the older 1820 wording "
  "reprinted by the booklet, not a change.", ["S16", "S33-02"], date="Resolved 19 May 1828 (Rait Kerr serial 71)",
  note="Only the 'wide ball' entry is a real change; other wording differences are source-edition artefacts.")
L("E005", "Relocated 'He may order the striker at his wicket to stand on which side of it he pleases' -> '..., at his wicket, ... he "
  "please'. Same rule.", NC, "format_artefact", "high", "derived",
  "Only punctuation and the subjunctive spelling 'please'/'pleases' differ; the move reflects the booklet's arrangement. " + BOOK, ["S18", "S16"])
L("E006", "Relocated No-ball law: 'If the bowler bowl a \"no ball\" the striker may play at it ...' -> 'If the bowler bowls a no ball, ...'. "
  "Same rule.", NC, "format_artefact", "high", "derived",
  "Verb form and quote marks only. Note the official 1829 Code (S33-02, Law 13) already adds the one-run no-ball penalty (Rait Kerr "
  "serial 72, July 1829), which this booklet omits: the omission is a source-edition artefact, not a repeal.", ["S18", "S16", "S33-02"])
L("E007", "Removed: the 1828 wide law ('If the bowler toss the ball over the striker's head, or bowl it so wide that it shall be out of "
  "distance to be played at, the umpire ... shall adjudge one run to the striker ... put down to the byes ...').", NC,
  "segmentation_artefact", "high", "derived",
  SEG + "The wide law is present in the 1830 Bowler block (event that adds 'to be put down as a wide ball'), where the real 1828 change "
  "is labelled.", ["S18"])
L("E008", "No-ball law: 1828 'The ball must be bowled (not thrown nor jerked), and delivered underhand with the hand below the elbow. But "
  "if the ball be jerked or the arm extended from the body horizontally, and any part of the back of the hand be uppermost, or the hand "
  "horizontally extended ..., the umpire shall call \"No Ball.\"' -> 1830 'The ball must be bowled underhand, and delivered with the hand "
  "below the elbow.' (Second record pairs the 1816 sentence with the unchanged two-practice-balls rule.)", "NOVEL_EVENT",
  "bowling_innovation", "medium", "stated",
  "A real change occurred to this law in the period: Rait Kerr serial 70 (May 19th 1828) 'As a sequel to the experimental round-arm "
  "matches played in 1827 ... the No ball Law was adopted in a simplified form leaving it crystal clear that the bowler must keep his hand "
  "and arm below the elbow'; ch.2 (S16) says George Knight proposed latitude for round-arm and William Ward's amendment simplified 'the "
  "previous difficult Law' while continuing to bar the hand or arm above the elbow. But the 1830 booklet does not print the 1828 text "
  "('The ball shall be bowled. If it be thrown or jerked, or if any part of the hand or arm be above the elbow ...', raw 1828 OCR and "
  "S33-02 Law 10); it prints the older c.1811 form (Rait Kerr serial 55). The dropped 1816 complicated sentence matches the 1828 "
  "simplification in effect only.", ["S16", "S33-02"], sec=ST, secsub="clarification_umpire_workability",
  date="Adopted 19 May 1828 (Rait Kerr serial 70); 1830 wording is the c.1811 form, not the official 1828 text",
  integrity="suspect", note="1830 source is unreliable; label describes the real 1828 change that this event coincides with")
L("E009", "Removed: 1828 law 13 'If the bowler bowl a \"no ball\" the striker may play at it ...'.", NC, "segmentation_artefact", "high",
  "derived", SEG + "Present in the 1830 Bowler block (relocation event 'If the bowler bowls a no ball ...').", ["S18"])
L("E010", "Mis-paired block: 1828 law 43 (umpires not changed) + the whole Single-wicket and Bets sections against the 1830 'Striker is Out' "
  "block (1820 wording: 'upon his hand, (but not wrist,)', '-if they are not crossed, he that has left the wicket which is put down, is "
  "out', no hit-wicket-by-dress); fieldsman-return rule paired with the 1820 LBW 'If with his foot or leg he stops the ball, which the "
  "bowler ... shall have pitched in a straight line to the wicket'. Single-wicket laws (except one sentence) absent from 1830.",
  NC, "", "high", "derived",
  BOOK + "Every wording difference matches the 1820 MCC text reproduced by Rait Kerr (S16 ch.2 p.25); the LBW 'pitched'/'foot or leg' "
  "form had been replaced before May 1823 (serial 67) and the official 1829 Code (S33-02, Law 25) has 'delivered' and 'any part of his "
  "person'. The booklet simply omits most single-wicket laws; they reappear in 1835. Source-edition and segmentation artefact.", EV_B,
  integrity="suspect", note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E011", "Mis-paired: single-wicket 'After the striker shall have run one notch, if he start again ...' vs 1830 lost-ball law 'If a lost "
  "ball is called, the striker shall be allowed six ...'.", NC, "segmentation_artefact", "high", "derived",
  SEG + "The lost-ball allowance is six in both editions (1828 law 29); the single-wicket sentence is omitted by the 1830 booklet "
  "(source-edition artefact).", ["S18", "S16"])
L("E012", "Removed: 1828 law 14 'In the event of a change of bowling, no more than two balls shall be allowed in practice.'", NC,
  "segmentation_artefact", "high", "derived", SEG + "Present in 1830 ('no more than two balls to be allowed in practice'), matched to the "
  "No-ball event.", ["S18"])
L("E013", "Wicket-keeper: 1828 'if any part of his person be over or before the wicket ... the striker shall not be out' -> 1830 'if his "
  "hands, knees, feet or head, be over or before the wicket though the ball hit it, it shall not be out'; Bets laws relocated after it.",
  NC, "", "high", "derived",
  BOOK + "'hands, knees, feet or head' is the 1820 wording (S16 ch.2 p.25); the official 1829 Code (S33-02, Law 36) and the 1835 code "
  "have 'any part of his person'. The Bets move is the booklet's arrangement. Source-edition artefact.", EV_B,
  note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E014", "Removed: 1828 law 15 'The bowler who takes the two balls shall be obliged to bowl four balls.'", NC, "segmentation_artefact",
  "high", "derived", SEG + "Present in 1830 ('The bowler who takes the two balls to be obliged to bowl four balls').", ["S18"])
L("E015", "Removed: 1828 law 16 'The Striker is out if the bail be bowled off ...'.", NC, "segmentation_artefact", "high", "derived",
  SEG + "Present at the start of the 1830 'Striker is Out' block.", ["S18"])
L("E016", "Removed: 1828 law 17 (caught).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Present in the 1830 out block ('upon his hand, (but not wrist,)' - 1820 wording, source-edition artefact).", ["S18"])
L("E017", "Removed: 1828 law 18 (stumped / out of ground).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Present in the 1830 out block.", ["S18"])
L("E018", "Removed: 1828 law 19 (hit wicket in striking).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Present in the 1830 out block.", ["S18"])
L("E019", "Added: booklet commentary 'Number of Players, In a regular and full game, consists of twenty-two, viz. eleven on each side; but "
  "merely for the purpose of practice, a less number may be sufficient.'", NC, "", "high", "derived",
  BOOK + "Editorial advice of the booklet's preamble, not an MCC Law (no number of players appears in the 1828 code, the official 1829 "
  "Code S33-02 or the 1835 code; Rait Kerr's chronology has no such serial before 1884). Source-edition artefact.", EV_B,
  note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E020", "Removed: 1828 law 20 (preventing a catch).", NC, "segmentation_artefact", "high", "derived", SEG + "Present in the 1830 out block.", ["S18"])
L("E021", "Removed: 1828 law 21 (hitting the ball twice).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Present in the 1830 out block ('if the ball is struck up, and he wilfully strikes it again').", ["S18"])
L("E022", "Removed: 1828 law 22 (run out).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Present in the 1830 out block (1820 wording 'or with the ball in hand').", ["S18"])
L("E023", "Removed: 'Or, if any part of the striker's dress knock down the wicket.' (no counterpart in 1830).", NC, "", "high", "derived",
  BOOK + "Hit wicket by dress was added before 1821 (Rait Kerr serial 61) and is in the official 1829 Code (S33-02, Law 23) and in the "
  "1835 code; the booklet reprints a pre-1821 text without it. Source-edition artefact, not a repeal.", EV_B,
  note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E024", "Removed: 1828 law 24 (touching/taking up the ball).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Present in the 1830 out block.", ["S18"])
L("E025", "Removed: 1828 LBW law 25 ('with any part of his person ... delivered in a straight line to the striker's wicket').", NC, "",
  "high", "derived",
  SEG + "An LBW law is present in 1830 but in the pre-1823 form ('with his foot or leg ... pitched in a straight line'), Rait Kerr "
  "serial 67 having replaced that form before May 1823; the official 1829 Code (S33-02) keeps 'delivered'. " + BOOK, EV_B,
  note="segmentation + source-edition artefact")
L("E026", "Removed: 1828 law 26 (players crossed).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Present in the 1830 out block, with the 1820 addition '-if they are not crossed, he that has left the wicket ... is out' "
  "(source-edition artefact).", ["S18", "S16"])
L("E027", "Removed: 1828 law 27 (no notch when caught).", NC, "segmentation_artefact", "high", "derived", SEG + "Present in 1830.", ["S18"])
L("E028", "Removed: 1828 law 28 (no notch when run out).", NC, "segmentation_artefact", "high", "derived", SEG + "Present in 1830.", ["S18"])
L("E029", "Removed: 1828 law 29 (lost ball six).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Present in 1830 ('the striker shall be allowed six').", ["S18"])
L("E030", "Added: booklet commentary 'Choice of Ground. It will be scarcely necessary to direct the attention of players to the choice of a "
  "smooth piece ... place the Wickets as near the centre as convenient ... provision is made for their immediate settlement by "
  "appointing, at the outset, two [Umpires]'.", NC, "", "high", "derived",
  BOOK + "Editorial advice of the booklet's preamble, not an MCC Law. Source-edition artefact.", EV_B,
  note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E031", "Removed: 1828 law 30 (ball no longer in play in bowler's or wicket-keeper's hands).", NC, "segmentation_artefact", "high",
  "derived", SEG + "Present in 1830 ('When the ball has been in the bowler's or wicket-keeper's hands ...').", ["S18"])
L("E032", "Removed: 1828 law 31 'If the striker be hurt, he may retire from his wicket and return to it at any time in that innings.'",
  NC, "segmentation_artefact", "high", "derived",
  SEG + "Present in 1830 in the 1820 wording '... and have his innings any time in that innings' (same effect).", ["S18", "S16"])
L("E033", "Removed: 1828 law 32 (hurt striker's runner).", NC, "segmentation_artefact", "high", "derived", SEG + "Present in 1830.", ["S18"])
L("E034", "Removed: 'No substitute in the field shall be allowed to bowl, keep wicket, stand at the point or middle-wicket, or stop behind "
  "to a fast bowler, unless with the consent of the adverse party.' (no counterpart in 1830).", NC, "", "high", "derived",
  BOOK + "This law (Rait Kerr serial 62, before May 1823) is in the official 1829 Code (S33-02, Law 33), and Rait Kerr says its "
  "umpire-enforcement direction 'was restored by 1830'; the booklet omits it. Source-edition artefact, not a repeal.", EV_B,
  note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E035", "Removed: 1828 law 34 (ball stopped with hat).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Present in 1830 ('If any player stops the ball with his hat ...'; 'person' -> 'player' is 1820 wording).", ["S18"])
L("E036", "Removed: 1828 law 35 'If the ball be struck, the striker may guard his wicket either with his bat or his body.'", NC,
  "segmentation_artefact", "high", "derived", SEG + "Present in 1830 ('If the ball is struck up ...').", ["S18"])
L("E037", "Removed: 1828 law 38 (umpires pitch fair wickets; toss).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Relocated to the 1830 Umpires block.", ["S18"])
L("E038", "Removed: 1828 law 39 (two minutes; fifteen minutes; refusing to play).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Relocated to the 1830 Umpires block with the same numbers.", ["S18"])
L("E039", "Removed: 1828 law 4 'The Bowling-crease must be in a line with the stumps, six feet eight inches in length ...'.", NC,
  "segmentation_artefact", "high", "derived",
  SEG + "The 1830 bowling-crease law (three feet) is matched to another event, where the source-edition reversion is labelled.", ["S18"])
L("E040", "Umpires: 1828 'The Umpires are sole judges ... but in case of a catch, which the umpire at the wicket bowled from cannot see "
  "...' -> 1830 'Who are to be sole judges ... but in a Catch, which the Umpire, at the Bowler's Wicket, cannot see ...'.", NC, "",
  "high", "derived",
  BOOK + "Same rule; 'at the Bowler's Wicket' and 'at the wicket bowled from' are the same umpire. Wording follows the booklet's "
  "preamble style. Source-edition artefact.", EV_B, note="source-edition artefact")
L("E041", "Relocated 'The umpires in all matches shall pitch fair wickets, and the parties shall toss ...' -> 'The Umpires, in all Matches, "
  "to pitch fair wickets, and the parties to toss ...'.", NC, "", "high", "derived",
  "Same rule; capitalisation and 'shall'->'to' infinitive style of the 1820 text reprinted by the booklet; relocation is the booklet's "
  "arrangement. " + BOOK, EV_B, note="source-edition artefact")
L("E042", "Relocated 'They shall allow two minutes ... fifteen minutes between each innings ...' (same numbers).", NC, "format_artefact",
  "high", "derived", "Punctuation/capitalisation only; relocation is the booklet's arrangement. " + BOOK, ["S18", "S16"])
L("E043", "Relocated 'They are not to order a player out unless appealed to by their adversaries' -> '... by the adversaries'.", NC,
  "format_artefact", "high", "derived", "'their'->'the' only; relocation is the booklet's arrangement. " + BOOK, ["S18", "S16"])
L("E044", "Relocated bowler's-foot no-ball: 'be not ... when he shall deliver' -> 'is not ... when he delivers' (same rule).", NC,
  "format_artefact", "high", "derived", "Verb mood only; relocation is the booklet's arrangement. " + BOOK, ["S18", "S16"])
L("E045", "Relocated 'If the striker run a short notch, the umpire must call \"No Notch.\"' -> 'runs ... \"no notch.\"'.", NC,
  "format_artefact", "high", "derived", "Verb form/capitalisation only; relocation is the booklet's arrangement. " + BOOK, ["S18", "S16"])
L("E046", "Added: 'The umpires are not to be changed during the match, but by the consent of both parties:'", NC, "segmentation_artefact",
  "high", "derived", SEG + "1828 law 43 has the same sentence; it was absorbed into a mis-paired block event.", ["S18"])
L("E047", "Removed: 1828 law 40 (no order out unless appealed to).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Relocated to the 1830 Umpires block.", ["S18"])
L("E048", "Removed: 1828 law 41 (bowler's foot no-ball).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Relocated to the 1830 Umpires block.", ["S18"])
L("E049", "Removed: 1828 law 42 (short notch).", NC, "segmentation_artefact", "high", "derived",
  SEG + "Relocated to the 1830 Umpires block.", ["S18"])
L("E050", "Ball: 'The Ball must not weigh less than five ounces and a half ...' -> heading 'The Ball' + 'must weigh not less than five "
  "ounces and a half ...'. Same limits.", NC, "format_artefact", "high", "derived",
  "Heading split and word order only; limits identical (raw OCR 1830 confirms 'five ounces and a half ... five ounces and three "
  "quarters').", ["S18"])
L("E051", "Removed: 1828 law 6 'The Wickets must be pitched opposite to each other by the umpires at the distance of twenty-two yards.'",
  NC, "segmentation_artefact", "high", "derived",
  SEG + "The 1830 Wickets law is matched to another event, where its pre-1823 'by the adversaries' wording is labelled as a "
  "source-edition artefact.", ["S18"])
L("E052", "Bat: 'The Bat must not exceed four inches and one quarter ...' -> heading 'The Bat' + 'must not exceed ...'. Same rule.", NC,
  "format_artefact", "high", "derived", "Heading split only.", ["S18"])
L("E053", "Stumps: 1830 drops 'the stumps of sufficient thickness to prevent the ball from passing through' (27 in / 8 in unchanged).",
  NC, "", "high", "derived",
  BOOK + "The thickness clause dates from Rait Kerr serial 68 (after May 1823, before 1825) and is in the official 1829 Code (S33-02, "
  "Law 3) and the 1835 code; the booklet updated the 1820 numbers but not the clause. Source-edition artefact.", EV_B,
  note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E054", "Mis-paired: 1828 'After rain the wickets may be changed with the consent of both parties' vs 1830 Bowling-crease law 'must be "
  "in a line with the stumps, three feet in length, with a return-crease' (1828: six feet eight inches, return-crease at each end).", NC,
  "", "high", "derived",
  BOOK + "Three feet is the pre-1823 bowling crease (Rait Kerr serial 28; lengthened by serials 65 and 69 to 6 ft 8 in before 1828); the "
  "official 1829 Code (S33-02, Law 4) and the 1835 code have 6 ft 8 in. Raw 1830 OCR does read 'three feet', so the number is the "
  "booklet's, not a clean-up invention. The after-rain law was probably on the missing p.10 of the 1830 scan. Not a rule change.",
  EV_B, integrity="suspect", note="source-edition artefact + missing page")
L("E055", "Popping crease: heading split only ('The Popping-crease must be four feet ...' -> 'must be four feet ...').", NC,
  "format_artefact", "high", "derived", "Heading split only; four feet in both.", ["S18"])
