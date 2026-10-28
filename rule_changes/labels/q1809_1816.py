"""Labels for 1809 -> 1816.

Edition note: '1809' = J. Baxter, Lewes (unreliable per Rait Kerr App. III, older Britcher-type text). '1816' = T. Craft broadsheet 'as
revised by the Cricket Club, at St. Mary-le-bone, 1816' (official M.C.C. printer; reliable). Many events are the c.1809-11 changes
(already in the dataset's Bailey '1806' text) reappearing after Baxter's omission. The genuinely new item is the 1816 'No ball' law
(Rait Kerr serial 58)."""
from _h import make
PAIR = "1809_1816"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
NE = "NOVEL_EVENT"
ED = ("Edition artefact: the provision was in force before 1811 (in the Bailey text) and only looks new because the dataset's 1809 text "
      "(Baxter) omits it. Proposed subtype: edition_artefact.")
EV = ["S16", "S31-03", "S31-04"]

L("E001",
  "Ball: 'and not more than' -> 'nor more than'; 'either party may call for a new ball' -> 'either may call for a new Ball' (Craft omits "
  "'party'; raw OCR 1816 line 10 confirms).",
  ST, "wording_only", "high", "derived",
  "Same limits and same new-ball right; 'either' still means either side (the 1820 Craft text restores 'Party').", ["S18", "S31-04"])
L("E002",
  "Wicket-keepers: 'Shall stand ... and shall not move ... and shall not by any noise, incommode the striker' -> 'must stand ... and must not "
  "move ... not incommode the Striker by any noise'.",
  SW, "modal_strength", "low", "derived",
  "'shall' -> 'must' (raw OCR 1816 lines 113-114). Both are mandatory, so the duty is unchanged. The 1820 Craft text returns to 'shall', so "
  "this looks like a drafting/printing variant of the 1816 broadsheet rather than a deliberate strengthening.",
  ["S18", "S31-04"], date="1816 Craft broadsheet")
L("E003",
  "'NOT OUT: If the striker hits the other wicket, and his partner off his guard.' disappears.",
  NC, "", "medium", "derived",
  "This provision was only in Baxter's unreliable 1809 printing. It is not in the Wallis 1809 text (ACS), and Rait Kerr's chronology does "
  "not record it. Its absence in 1816 is not a repeal.",
  EV, date="Baxter-only provision (proposed subtype edition_artefact)", integrity="suspect")
L("E004",
  "'The Umpires, in all matches, to pitch fair wickets, and the parties to toss for the choice of innings.' appears; no-ball call now in "
  "quote marks.",
  NC, "", "medium", "derived",
  "Rait Kerr serials 52-53 ('Before 1811'), already present in the Bailey text (dataset '1806') and labelled there.", EV, date=ED, integrity="suspect")
L("E005",
  "Bat: 'four inches and one quarter' -> 'four inches and a quarter'.",
  ST, "wording_only", "high", "derived", "Same 4¼ in limit (raw OCR 1816 line 12).", ["S18", "S31-04"])
L("E006",
  "Stumps: 'Which are three, must be twenty-four inches...' -> 'must be twenty-four inches...'.",
  NC, "", "high", "derived",
  "'Which are three' was Pocock/Baxter wording, absent from the Wallis 1809 text (ACS). Same 24 x 7 in wicket.", EV, date=ED)
L("E007",
  "Wickets: ', which shall be pitched within thirty yards, fixed by the adversaries' added; ground-alteration rule moved here, re-worded "
  "'It is not lawful...', 'This is not meant...', 'watering the ground', '&c.' dropped.",
  NC, "", "medium", "derived",
  "The pitching clause is the pre-1811 arrangement (serial 52) already in Bailey. 'of a centre' is lost in OCR (raw 1816: 'within thirty "
  "yarcis / fixed by the adversaries'), and the 1820 Craft text has 'within Thirty Yards of a centre fixed by the Adversaries'. 'rule' and "
  "'his' are also lost in OCR ('Tnis / not meant'; 'watering / ground'). Not a change to the Laws.",
  EV, date=ED, integrity="suspect", note="Edition artefact plus OCR loss in 1816")
L("E008",
  "Bowler: 'shall bowl four or six balls' -> 'must bowl four balls'; 'which he shall do but once' -> 'which he is to do but once'. 'He may "
  "order a striker ...' moves to after the no-ball rule.",
  NC, "", "medium", "derived",
  "'four or six' was Baxter's own wording; the Wallis 1809 text (ACS) and all other editions have four balls (four-ball over until 1889, "
  "Rait Kerr serial 108). 'must'/'is to' for 'shall' is a Craft 1816 wording variant (1820 Craft returns to 'shall') with no change of "
  "rule. The relocation is sequence only.",
  EV, date=ED, integrity="suspect", note="Baxter-only 'four or six'; must/shall variant (see also the wicket-keeper event)")
L("E009",
  "New 'No ball' law: 'The ball must be bowled (not thrown or jerked), and delivered underhand, with the hand below the elbow. But if the ball "
  "be jerked, or the arm extended from the body horizontally, and any part of the hand be uppermost, or the hand horizontally extended when "
  "the ball is delivered, the Umpire shall call \"No Ball\".' The same record also brings back the Bailey-era rules missing from Baxter: "
  "Wides (one notch 'to be put down to them' [sic]), the striker may play at a No Ball, and two practice balls for a change of bowling.",
  NE, "bowling_innovation", "high", "stated",
  "Rait Kerr serial 58 ('Before 1817'): 'The \"No ball\" Law was again modified with the object of curbing round-arm bowling.' In ch.2 he says "
  "'the practice of \"throwing\" was becoming general by 1816; William Ward ... pressed his views on the M.C.C. to such effect that they "
  "adopted a new version of the \"No ball\" Law', which he quotes. The other rules are Bailey-era (serials 54, 56, 57; trial balls first in an "
  "official version in 1816 per Rait Kerr), hence secondary UNCATEGORISED. Integrity: Rait Kerr's quotation reads 'any part of the back of "
  "the hand'. The dataset's 1816 text (and raw OCR line 42) has 'any part of the hand'. The wides clause 'put down to them' is an AI "
  "clean-up guess for illegible raw OCR 'to the/' (Bailey and 1820 read 'to the Byes').",
  ["S16", "S31-04"], sec=UN, secsub="no_cause_stated", date="Before 1817, in the 1816 Craft broadsheet (serial 58)", integrity="suspect",
  note="'back of' missing vs Rait Kerr's quotation; 'to them' is a cleaning artefact for 'to the Byes'")
L("E010",
  "Striker-out list: 'either wilfully strike' -> 'he wilfully strike'; 'his bat' -> 'the bat'; 'hall' (OCR) -> 'ball'; L.B.W. 'shall have "
  "pitched' -> 'has pitched'; capitalisation.",
  ST, "wording_only", "medium", "derived",
  "Printer's variants of identical provisions. 'has pitched' vs 'shall have pitched' does not alter the L.B.W. test (umpire's opinion that "
  "the ball pitched straight and would have hit).",
  ["S18"])
L("E011",
  "Lost-ball rule appears ('If a lost ball is called, the Striker shall be allowed four...'); 'some person' -> 'some other Person'.",
  NC, "", "medium", "derived",
  "The lost-ball law dates from before 25 May 1809 (Rait Kerr serial 51) and is in the Wallis 1809 text (ACS) and the Bailey text. It looks "
  "new here only because Baxter omitted it.",
  EV, date=ED, integrity="suspect")
