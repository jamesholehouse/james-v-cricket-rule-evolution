"""Labels for 1820 -> 1823.

1820 = Craft broadsheet 'as revised ... 1820' (typescript transcription; Rait Kerr reproduces the broadsheet in facsimile, S32-02).
1823 = Carpenter broadsheet 'Revised by the Marylebone Club in the year 1823' (typescript of the Sloane-Stanley copy).
Rait Kerr (S16) dates serials 62-67 'Before May 1823'; serials 54b/4 put the general change 'notch' -> 'run' at 1823.
Both editions are segmented as heading blocks, so many events are a block 'add' that duplicates individually moved
sentences; the add is labelled segmentation_artefact when its content is labelled on the matching move/remove event.
The ACS transcription of the official 1829 code (S32-01) confirms which 1823 wordings persisted.
"""
from _h import make
PAIR = "1820_1823"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
D23 = "Rait Kerr dates serials 62-67 'Before May 1823'; first seen in the dataset's 1823 broadsheet."

L("E001", "Ball law word order only: 'must weigh not less than Five Ounces and a Half' -> 'MUST not weigh less than five Ounces and a half'. "
  "Same limits (5 1/2 - 5 3/4 oz).", ST, "wording_only", "high", "derived",
  "Token comparison shows only a reordering of 'not'; the weight limits are identical in the 1820 facsimile (S32-02) and the 1823 text.",
  ["S18", "S32-02"])

L("E002", "Heading-block add for the 1823 run/scoring/substitute block. Content genuinely new in 1823: 'No Substitute in the field shall be allowed to "
  "bowl, keep Wicket, stand at the point, or middle Wicket, or stop behind to a fast Bowler, unless with the Consent of the adverse party. "
  "The umpires shall enforce this Law.' (the rest of the block duplicates sentences labelled on the move/remove events).", UN, "no_cause_stated",
  "medium", "none",
  "Matches Rait Kerr serial 62 (substitutes not to bowl, keep wicket, field at point, middle wicket or long stop, except by agreement). "
  "Rait Kerr ch.2 counts substitutes among the 'general points' of 1810-1835 and gives no cause; nothing else found.", ["S16"],
  date=D23 + " ACS 1829 code (S32-01) keeps the same law.",
  note="Block add also contains the 1823 lost-ball (six runs) wording, labelled on the removal of the 1820 'Four' sentence.")

L("E003", "LBW rewritten: 'If with his foot or leg he stops the Ball, which the Bowler ... shall pitch [facsimile: shall have pitched] in a straight "
  "line to the Wicket' -> 'Or, if with any Part of his Person he stop the Ball, which ... shall have been delivered in a straight line to the "
  "Striker's Wicket'. Other moved sentences only reworded (hurt striker 'have his Innings' -> 'return to it'; 'struck up' -> 'struck'; "
  "hat-ball penalty 'Notches' -> 'Runs').", "ENJOYMENT", "bowler_batsman_balance", "high", "stated",
  "Rait Kerr serial 67: the LBW Law altered to require the ball delivered in a straight line and to have struck any part of the person; "
  "'This alteration was certainly designed to assist the bowler.' Ch.2 also lists 'extending the L.B.W. Law' among changes designed to help the bowler.",
  ["S16", "S32-02"], sec=SW, secsub="terminology_term", date=D23,
  note="The 1823 processed text reads 'stop the Ball with his Bat' in the hat-penalty sentence: raw OCR has 'his pat' (OCR p for H, cf. 'pall', "
  "'pun') and the single-wicket law refers to 'Ball stopped with Hat'; ACS 1829 has 'hat'. A cleaning artefact, not a change.")

L("E004", "Heading-block add of the Wicket Keeper law; duplicates the moved sentence (labelled on the relocation event).", NC,
  "segmentation_artefact", "high", "derived",
  "The added text is identical to the new text of the moved wicket-keeper sentence; the add/move split is a heading-block segmentation artefact.", ["S18"])

L("E005", "Wicket-keeper: 'if his hands, knees feet, or head, be over or before the Wicket, though the Ball hit it, it shall not be out' -> "
  "'if any part of his Person be over or before the Wicket, although the Ball hit it, the striker shall not be out'.", SW, "qualifier_scope",
  "medium", "derived",
  "The list of body parts is replaced by 'any part of his Person' (same phrase introduced in the LBW law in this edition), so a keeper's "
  "elbow or body before the wicket now also voids the dismissal; 'it' is made explicit as 'the striker'. No source records it as a rule change. "
  "Wording persists in the ACS 1829 code.", ["S18", "S32-01", "S32-02"], date=D23)

L("E006", "Heading-block add of the Umpires block; duplicates the moved sentences (labelled on the relocation event).", NC,
  "segmentation_artefact", "high", "derived",
  "Added text equals the new text of the umpire sentences moved in this pair; heading-block segmentation artefact.", ["S18"])

L("E007", "Umpires block reworded: catch referral now by 'the Umpire at the Wicket bowled from' (absorbing the separate 1820 sentence 'That the Umpire "
  "at the Bowler's Wicket shall be first applied to, to decide on all Catches'); 'to pitch'/'to toss' -> 'shall pitch'/'shall toss'; "
  "short run: 'If the Striker runs a Short Notch, the Umpire must call \"No Notch.\"' -> 'If the Striker run a short run the umpire must call \"One Short\"'.",
  ST, "consolidation_merge", "medium", "derived",
  "Two 1820 sentences on catch decisions are combined into one with the same effect. The 'No Notch' -> 'One Short' call follows the general "
  "notch -> run change Rait Kerr places in 1823 (serials 4 and 54b). Wording persists in ACS 1829 code.", ["S18", "S16", "S32-01"],
  sec=SW, secsub="terminology_term", date=D23)

L("E008", "New section 'LAWS FOR SINGLE WICKET' first sentence: 'When there shall be less than five players on a Side, Bounds shall be placed "
  "twenty-two yards each in a Line from the Off, and Leg stump.' (1820 had only one single-wicket sentence).", ST,
  "documentary_first_appearance", "medium", "inferred",
  "Rait Kerr's chronology has no serial for single-wicket laws in 1823, and Appendix III notes 'five new and crudely worded rules' for single "
  "wicket in an unofficial c.1805 edition, so such rules existed earlier; this is their first appearance in an official broadsheet in the dataset. Cause not stated.",
  ["S16"], date="First in the dataset's 1823 broadsheet; same section in the 1835 code.")

L("E009", "Single-wicket section rules (bounds, run requires touching the bowling stump 'or crease in a line with it', 'No Hit' if not one foot "
  "behind the popping crease, no byes/overthrows and no caught-behind or stumping with fewer than five a side, return of ball across the play, "
  "three runs for lost ball or ball stopped with hat, no bounds with more than four a side, one minute between balls).", ST,
  "documentary_first_appearance", "medium", "inferred",
  "As for the first single-wicket sentence: no chronology serial, earlier unofficial single-wicket rules noted in Rait Kerr Appendix III; first "
  "appearance in an official text in this dataset. No cause found.", ["S16"], date="First in the dataset's 1823 broadsheet.")

L("E010", "Bets: 'If the Notches of one Player are laid against another' -> 'If the Runs of one Player be laid against those of another'; "
  "'the Notches in the First Innings' -> 'the Runs in the first innings'.", SW, "terminology_term", "high", "derived",
  "Pure terminology: Rait Kerr serial 54b says 'run' instead of 'notch' became general by 1823 and serial 4 that 'notch' finally disappeared from "
  "the Laws in 1823. Betting effect unchanged.", ["S16", "S18"], date=D23)

L("E011", "Transcriber's note added in the 1823 text: '( This Law is altered in contemporary ink to read \"must be twenty-seven inches out of the "
  "Ground; the BAILS eight Inches in Length: and of sufficient thickness ...\" )'. Not printed Law text.", NC, "format_artefact", "high",
  "derived",
  "The printed 1823 stumps law (26 in, bails 7 in) is unchanged from 1820; the note records a hand alteration by the copy's owner (Rait Kerr "
  "Appendix III). The alteration itself is serial 68 (after May 1823) and is labelled in the 1823->1828 pair.", ["S16", "S18"],
  date="Serial 68: 'After May 1823 but before 1825'; Bell's Life 27 June 1823 'newly adopted'.")

L("E012", "Bowling crease: 'Three Feet in length, with a RETURN CREASE' -> 'six Feet seven inches in Length, (the Stumps in the centre) with a "
  "RETURN CREASE at each end towards the Bowler at right Angles'.", UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 65 (bowling crease increased to 6 ft 7 in with return creases at each end at right angles); no cause given. 6 ft 7 in = 3 ft "
  "either side (serial 28, 1774) plus the 7-in wicket, so it may partly restate existing practice; Rait Kerr calls it an increase.", ["S16"],
  date=D23, note="Numbers checked against raw OCR of both editions ('Three Feetin lengtn'; 'six Feet seven inches').")

L("E013", "Removed: wickets 'shall be pitched within Thirty Yards of a centre fixed by the Adversaries'; 1823 has the wickets 'pitched opposite "
  "to each other by the Umpires'.", UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 63: selection of the pitch left entirely to the umpires, the opponents no longer fixing a centre. Ch.2 counts pitching "
  "wickets among 'general points'; no cause given.", ["S16", "S32-02"], date=D23)

L("E014", "Heading-block add for 'The wickets' block. New content: 'After Rain the wickets may be changed with the Consent of both Parties.' "
  "(also the new 'pitched ... by the Umpires' wording and the ground-alteration rule, labelled elsewhere).", UN, "no_cause_stated",
  "high", "none",
  "Rait Kerr serial 64 (after rain the pitch may be changed by mutual consent); no cause given in the chronology or ch.2.", ["S16"], date=D23)

L("E015", "Ground-alteration rule: the dataset's 1820 text reads 'by watering, covering, mowing, or beating: this rule is to prevent the "
  "Striker...' but the 1820 broadsheet reads 'by rolling, watering, covering, mowing, or beating: This rule is not meant to prevent...', as does 1823.",
  NC, "ocr_noise", "high", "derived",
  "Raw 1820 OCR is illegible here ('by ro', '..his ru . i- - - to prevent'); the AI clean-up dropped 'rolling' and 'not meant', inverting the "
  "sense. The facsimile of the 1820 broadsheet in Rait Kerr (S32-02) has the same wording as 1823 apart from trivial words.", ["S32-02", "S18"],
  integrity="suspect", note="1820 processed text is wrong here; needs correcting at source.")

L("E016", "Removed 1820 wording, replaced in 1823 by: 'Or, if the Ball is struck up, and he wilfully strikes it again' -> 'Or, if the Ball be "
  "struck, and he wilfully strike it again'; run out 'if in running a Notch, the Wicket is struck down by a throw, or with the Ball in Hand' -> "
  "'if in running the wicket be struck down by a Throw, or by the Hand, or Arm (with Ball in Hand)'.", SW, "qualifier_scope", "medium",
  "derived",
  "Dropping 'up' widens hitting-twice from a ball struck in the air to any struck ball; 'by the Hand, or Arm (with Ball in Hand)' spells out a "
  "run out by hand or arm holding the ball. No source records either as a rule change; both wordings persist in ACS 1829 and the 1835 code.",
  ["S18", "S32-01"], date=D23)

L("E017", "Removed 1820 sentences, replaced in 1823: lost ball 'the Striker shall be allowed Four' -> 'six Runs'; crossed-batsmen rule loses "
  "its second half 'if they are not crossed, he that has left the Wicket which is put down, is out'; 'no Notch' -> 'no run'.", UN,
  "no_cause_stated", "high", "none",
  "Rait Kerr serial 66 (lost-ball allowance increased from four to six runs); no cause given. The dropped not-crossed clause is not in his "
  "chronology; it is also absent from ACS 1829 and the 1835 code, so it is a real omission without stated cause.", ["S16", "S32-01"], date=D23)

L("E018", "Removed the 1820 single sentence 'In SINGLE-WICKET MATCHES, if the Striker moves out of his ground to strike at the Ball, he shall be "
  "allowed no Notch for such Stroke'; 1823's new single-wicket section has instead 'one of his Feet must be on the Ground, and behind the popping "
  "crease; otherwise the umpire shall call \"No Hit\"'.", ST, "reorganisation", "medium", "inferred",
  "The rule moves into the new Laws for Single Wicket section and is reworded with a named call ('No Hit'); the effect (no run from such a "
  "stroke) appears the same. No source discusses it.", ["S18", "S16"], date=D23)

L("E019", "Removed 1820 sentence 'That the Umpire at the Bowler's Wicket shall be first applied to, to decide on all Catches.'", ST,
  "consolidation_merge", "high", "derived",
  "Its content is folded into the 1823 catch sentence ('the Umpire at the Wicket bowled from'); no change of effect.", ["S18"], date=D23)

L("E020", "Heading-block add of The Bowler law; duplicates the moved sentence (labelled on the relocation event).", NC,
  "segmentation_artefact", "high", "derived", "Added text equals the moved sentence's new text; heading-block segmentation artefact.", ["S18"])

L("E021", "Bowler: 'which he shall do but once in the same Innings' -> 'which he shall be permitted to do but once in the same innings'.", SW,
  "modal_strength", "medium", "derived",
  "Framed as a permission rather than a duty; the limit (one change of ends per innings) is unchanged. Wording kept in ACS 1829.",
  ["S18", "S32-01"], date=D23)

L("E022", "Wide law rewritten: 'bowls it so wide that the Striker cannot play at it, the Party that is in shall be allowed One Notch, to be put "
  "down to the Byes' -> 'bowl it so wide that it shall be out of Distance to be played at, the umpire (either with or without an Appeal from the "
  "Party receiving the innings) shall adjudge one Run to the striker, even although he attempt to hit it; which shall be put down to the Byes'. "
  "Also practice balls 'to be allowed' -> 'shall be allowed'.", UN, "no_cause_stated", "medium", "none",
  "A real change: the umpire now awards the wide with or without appeal, and the wide stands even if the striker attempts to hit it. Rait Kerr's "
  "chronology has no serial for it (serial 56 is the first Wides law, serial 71 the 1828 change to scoring as 'wide'); ch.2 gives the 1810 Lambert "
  "incident only for the first Wides law. ACS 1829 has the new wording.", ["S16", "S32-01"], date=D23,
  note="The No-ball record in this event ('when the Ball shall be delivered') is an 1820 cleaning artefact: the 1820 broadsheet already has "
  "'when the Ball is delivered' (raw OCR 'then the Ball is delivered'; S32-02).")

L("E023", "Heading-block add of the 'Striker is Out' block; duplicates moved sentences and the reworded hit-twice/run-out sentences (labelled on "
  "the removal event).", NC, "segmentation_artefact", "high", "derived",
  "Every sentence of the added block is the new text of a moved or removed/re-added sentence labelled elsewhere in this pair.", ["S18"])

L("E024", "Striker-out sentences reworded: catch 'from a stroke over or under the Bat, or on [facsimile: upon] his hand (but not wrists)' -> "
  "'from a Stroke of the Bat, or Hand, (but not wrist)'; 'under pretence of running a Notch' -> 'under Pretence of running'; verbs to subjunctive.",
  SW, "clarifying_rewrite", "medium", "derived",
  "Shorter catch wording with the same intent (a catch off bat or hand, not wrist); 'notch' dropped per the 1823 terminology change (Rait Kerr "
  "serials 4, 54b). Wording persists in ACS 1829.", ["S18", "S16", "S32-01"], sec=SW, secsub="terminology_term", date=D23)
