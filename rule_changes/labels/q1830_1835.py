"""Labels for 1830 -> 1835.

Context for every label in this module (checked against the texts and sources):
- OLD side: the dataset's 1830 text is an unofficial pocket booklet reprinting the 1819/1820 MCC wording with a few updates
  (see the docstring of q1828_1830.py; Rait Kerr App. III, S16; data appendix S33-01; official 1829 Code in ACS, S33-02).
  Differences that only undo the booklet's outdated wording are source-edition artefacts, not 1830-35 rule changes.
- NEW side: the dataset's "1835" Laws are the second of two versions in the 1835 scan (S33-01). They are the 1835 Code AS
  AMENDED TO c.1845: they already contain Rait Kerr serials 82-85 (10 May 1838), 86-87 (9 May 1839), 88 (14 May 1840), 89
  (17 June 1844) and 90-92 (2 June 1845), but not serial 93 (3 May 1849). The first version in the scan is the MCC Secretary's
  circular of 20 March 1835 with the proposed revision (S33-03), used here to date wording to the 1835 revision.
  So several "1835" changes below are dated 1838-1845 (edition lag; see each `date`).
"""
from _h import make
PAIR = "1830_1835"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"

BOOK = ("The old (1830) text is an unofficial booklet reprinting the 1819/1820 MCC wording (Rait Kerr App. III, S16; data appendix "
        "S33-01); the official 1829 Code (S33-02) already had the 1835 wording's substance. ")
SEG = "Segmentation artefact: the same provision is matched to another event of this pair (pre-1884 texts are segmented as heading blocks). "
LATE = "The dataset's 1835 text is the 1835 Code as amended to c.1845 (contains Rait Kerr serials 82-92, not 93), so this appears here, not in a later edition. "
EV_B = ["S16", "S33-01", "S33-02"]

L("E001", "Removed: the booklet's instructional preamble ('The particulars necessary to be attended to when a Game of Cricket is to be "
  "played ... for the information of young beginners ...').", NC, "", "high", "derived",
  BOOK + "Editorial text of the booklet, not an MCC Law. Source-edition artefact.", EV_B,
  note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E002", "Ball: added 'It must measure not less than nine inches, nor more than nine inches and one quarter in circumference.' (weight "
  "limits unchanged; 'must weigh not less' -> 'Must not weigh less').", ST, "codification_definition", "medium", "inferred",
  "Rait Kerr serial 82 (May 10th 1838): 'The size of the ball is specified for the first time; it must measure between 9 and 9 1/4 "
  "inches in circumference.' No cause given; ch.3 (S16) counts 'limitations for the dimensions of the bat and the ball' among "
  "alterations 'of an entirely general nature', so treated as a codification (inferred). The March 1835 proposal (S33-03) had a 9 1/8 in "
  "upper limit that was not adopted then. Raw 1835 OCR reads 'nine inches and one quarter', matching Rait Kerr.", ["S16", "S33-03"],
  date="10 May 1838 (Rait Kerr serial 82). " + LATE)
L("E003", "No-ball law (new): 'The ball must be bowled, not thrown or jerked, and the hand must not be above the shoulder in delivery; and "
  "whenever the bowler shall so closely infringe on this rule ... as to make it difficult for the umpire ... to judge ..., the umpire "
  "shall call \"No Ball.\"' (replaces the old requirement to bowl underhand with the hand below the elbow).", "NOVEL_EVENT",
  "bowling_innovation", "high", "stated",
  "Two real changes: Rait Kerr serial 74 (May 14th 1835) legalised round-arm bowling ('if the hand be above the shoulder in the "
  "delivery, the umpire must call No ball'); ch.2 (S16): the 'New style' campaign (Willes, Knight's 1827 experimental matches), "
  "umpires 'increasingly were turning a blind eye to the lifting of the arm, and matters finally came to a head in 1834', so 'the "
  "change was accepted on May 14th, 1835'. Then serial 90 (June 2nd 1845): ch.3 says 'It was not until 1845 that the M.C.C. launched "
  "their full assault on the increasing number of bowlers who ... were bowling over-arm', issuing the 'much more definite' law ending "
  "'whenever the bowler shall so closely infringe ...' - the wording printed here.", ["S16", "S33-03"],
  sec="ENJOYMENT", secsub="bowler_batsman_balance",
  date="14 May 1835 (serial 74, also in the March 1835 proposal S33-03); final wording 2 June 1845 (serial 90). " + LATE)
L("E004", "Added: 'He may require the striker at the wicket from which he is bowling to stand on that side of it which he may direct.' "
  "(old: 'He may order the striker, at his wicket, to stand on which side of it he please').", SW, "clarifying_rewrite", "medium",
  "inferred",
  "Re-wording in the 1835 revision (same sentence in the March 1835 proposal, S33-03). It specifies that the batsman concerned is the "
  "one at the bowler's own end ('at the wicket from which he is bowling'), where the old text said only 'at his wicket'; the bowler's "
  "power is unchanged, but the reading of which batsman it applies to may change. No source gives a reason; Rait Kerr has no serial "
  "for it.", ["S33-03"], date="1835 revision (S33-03)")
L("E005", "Removed: old 'must be bowled underhand, and delivered with the hand below the elbow' together with the two practice-balls "
  "sentences.", NC, "segmentation_artefact", "high", "derived",
  SEG + "The replacement No-ball law (round-arm legalised) and the replacement trial-ball rule are labelled at the events that add "
  "them.", ["S18"])
L("E006", "Wides (new): 'so wide that in the opinion of the umpire it shall not be fairly within the reach of the batsman, he shall adjudge "
  "one run ... either with or without an appeal, ... put down to the score of wide balls; ... but if the batsman shall by any means bring "
  "himself within reach of the ball the run shall not be adjudged' (old booklet: 'so wide that the striker cannot play at it').", ST,
  "clarification_umpire_workability", "high", "stated",
  "Rait Kerr serial 91 (June 2nd 1845): Wide defined as a ball not 'fairly within the reach of a batsman', and not a Wide if the striker "
  "moves to bring himself within reach. Ch.3 (S16): after Denison's protests about 'the liberal contribution of wide balls' the "
  "Committee was asked whether 'any regulation can be laid down by them by which the limit of bowling may be more easily defined and "
  "acted on'; the new definition 'satisfied both the umpires and the players by removing the uncertainty which had previously existed'. "
  "The umpire/appeal wording was already official before 1830 (S33-02), so it is not a change.", ["S16", "S33-02"],
  sec="ENJOYMENT", secsub="quality_of_play", date="2 June 1845 (Rait Kerr serial 91). " + LATE)
L("E007", "No ball / Wide (new law 13): 'If the bowler deliver a \"No Ball\" or a \"Wide Ball,\" the striker shall be allowed as many runs as "
  "he can get ... In the event of no run being obtained by any other means, then one run shall be added to the score, of \"No Balls\" or "
  "\"Wide Balls\" ... The names of the bowlers who bowl \"Wide Balls,\" or \"No Balls,\" in future to be placed on the score ...'.",
  "ENJOYMENT", "quality_of_play", "high", "stated",
  "Main new content is Rait Kerr serial 89 (June 17th 1844): batting side may reckon all runs from a Wide. Ch.3 (S16): wides were "
  "thrown away by bowlers emulating Alfred Mynn's speed, 'damaging the growth of scientific batsmanship' and hazarding results; after "
  "Denison's protests the Law was altered 'to allow the batsmen all the runs they could make' and the scorers' instruction on bowlers' "
  "names, which 'appeared quite improperly as part of the Law until the revision of 1884'. The one-run no-ball penalty is Rait Kerr "
  "serial 72 (July 27th 1829), official before 1830 (S33-02 Law 13) but omitted by the 1830 booklet.", ["S16", "S33-02"],
  date="Penalty 27 July 1829 (serial 72); wide runs 17 June 1844, confirmed 1845 (serial 89). " + LATE,
  note="The 1835 ball-dead-on-a-wide rule (serial 80b) never shows in the dataset: it was introduced and repealed between the two texts.")
L("E008", "Trial balls (new): 'At the beginning of each innings the umpire shall call \"Play,\" from that time to the end of each innings, "
  "no trial ball shall be allowed to any bowler.' (old: two practice balls allowed on a change of bowling).", "ENJOYMENT",
  "bowler_batsman_balance", "medium", "stated",
  "Rait Kerr serial 84 (May 10th 1838): 'Trial balls are no longer allowed to a fresh bowler.' Ch.3 (S16): 'the start of the struggle to "
  "restrain the bowler can be traced to a pin prick when the right of a fresh bowler to trial balls was taken away in 1838'. (The 1835 "
  "Code's intermediate form, serial 79a, two trial balls but the over must be finished after even one, is in the March 1835 proposal "
  "S33-03 and never shows in the dataset.)", ["S16", "S33-03"], sec="NOVEL_EVENT", secsub="bowling_innovation",
  date="10 May 1838 (serial 84). " + LATE)
L("E009", "Bowled: 'If either of the bails be bowled off, or if a stump be bowled out of the ground' (old: 'if the bail is bowled off, or the "
  "stump bowled out of the ground').", ST, "codification_definition", "medium", "inferred",
  "The wicket had two bails since c.1809 (Rait Kerr serial 50), so the old singular 'the bail' was outdated; the 1835 revision (March 1835 "
  "proposal, S33-03, has 'either of the bails') states that removing either bail bowls the striker. No source gives a reason; treated "
  "as bringing the wording into line with the two-bail wicket (inferred).", ["S16", "S33-03"], date="1835 revision (S33-03)")
L("E010", "Caught: 'if the ball from the stroke of the bat, or hand, but not the wrist, be held ...' (old booklet: 'from a stroke over or "
  "under the bat, or upon his hand, (but not wrist,) held ...').", SW, "clarifying_rewrite", "medium", "inferred",
  "Re-wording; the 1835 proposal (S33-03) has 'from a stroke of the bat, or hand, but not wrist'. 'over or under the bat' is the old "
  "1820 phrasing (S16 ch.2). Dropping it might read more widely (any stroke of the bat), but no source records a change of rule; no "
  "cause given.", ["S33-03", "S16"], date="1835 revision (S33-03)")
L("E011", "Out of ground: 'while the ball shall be in play, both his feet shall be over ... except his bat be grounded' vs 'is in play ... are "
  "over ... except his bat is grounded'. Same rule.", NC, "format_artefact", "high", "derived", "Verb mood only.", ["S18"])
L("E012", "Hit wicket: 'Or, if in striking at the ball he hit down his wicket' vs '..., he hits down his wicket'. Same rule.", NC,
  "format_artefact", "high", "derived", "Verb mood and punctuation only.", ["S18"])
L("E013", "Preventing a catch: 'under pretence of running a notch' -> 'under pretence of running'. Same rule.", SW, "terminology_term",
  "medium", "inferred",
  "Part of the 1835 revision's replacement of 'notch' by 'run' (the March 1835 proposal S33-03 uses 'running'); Rait Kerr serial 54b "
  "notes 'run' replacing 'notch'. Meaning unchanged.", ["S16", "S33-03"], date="1835 revision")
L("E014", "Removed: the booklet's commentary 'Number of Players ... eleven on each side ...'.", NC, "", "high", "derived",
  BOOK + "Editorial text, not a Law. Source-edition artefact.", EV_B, note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E015", "Bat: added 'it must not be more than thirty-eight inches in length.' (width 4 1/4 in unchanged).", ST, "codification_definition",
  "medium", "inferred",
  "Rait Kerr serial 77 (May 20th 1835): 'The limit of 38 inches for the length of the bat is introduced.' No cause given; ch.3 (S16) "
  "puts 'limitations for the dimensions of the bat and the ball' among alterations 'of an entirely general nature' (inferred "
  "codification). Raw OCR of both 1835 versions reads thirty-eight.", ["S16", "S33-03"], date="20 May 1835 (Rait Kerr serial 77)")
L("E016", "Hit twice: 'if the ball be struck and he wilfully strike it again' vs booklet 'if the ball is struck up, and he wilfully strikes "
  "it again'.", NC, "", "high", "derived",
  BOOK + "'struck up' is the booklet's 1820 wording; the 1828 code already has 'if the ball be struck'. Source-edition artefact.", EV_B,
  note="source-edition artefact")
L("E017", "Run out: 'by a throw, or by the hand or arm, (with ball in hand) before his bat (in hand) or some part of his person be grounded "
  "over the popping crease. But if both the bails be off, a stump must be struck out of the ground.' (old: 'before his foot, hand, or "
  "bat, is grounded ...; but if the bail is off, the stump must be struck out').", UN, "no_cause_stated", "medium", "none",
  "Two changes: (1) grounding by 'his bat (in hand) or some part of his person' - in the March 1835 proposal (S33-03), so 1835 revision; "
  "(2) Rait Kerr serial 85 (May 10th 1838): if one bail remains, removing it puts the wicket down for a run out; the text requires a "
  "stump to be struck out only if 'both the bails be off'. Rait Kerr (ch.3, ch.6) gives no reason for either; 'by the hand or arm' was "
  "already in the 1828 code (booklet artefact).", ["S16", "S33-03"], date="1835 revision (grounding); 10 May 1838 (serial 85). " + LATE)
L("E018", "Added: 'Or, if any part of the striker's dress knock down the wicket.'", NC, "", "high", "derived",
  BOOK + "Hit wicket by dress dates from before 1821 (Rait Kerr serial 61) and is in the 1828 code and official 1829 Code (S33-02 Law "
  "23); the 1830 booklet omitted it. Source-edition artefact, not a new rule.", EV_B,
  note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E019", "Handling: 'unless at the request of the other party' -> '... of the opposite party'. Same rule.", ST, "wording_only", "high",
  "derived", "Synonym only ('other'/'opposite' party); no change of meaning.", ["S18"])
L("E020", "LBW: 'Or, if with any part of his person he stop the ball which ... shall have been pitched in a straight line from it to the "
  "striker's wicket, and would have hit it.' (booklet: 'If with his foot or leg he stops the ball, which the bowler ... shall have "
  "pitched in a straight line to the wicket').", "ENJOYMENT", "bowler_batsman_balance", "medium", "stated",
  "Against the official code the real change is Rait Kerr serial 87 (May 9th 1839): 'The L.B.W. Law reverts to the 1788 version which "
  "required a ball to have been pitched straight irrespective of the line of its delivery' (the official 1829 Code, S33-02, and the "
  "March 1835 proposal, S33-03, say 'delivered'). Ch.3 (S16): within ten years of 1835 three changes, first 'a revised L.B.W. Law "
  "under which the ball must have pitched between wicket and wicket instead of having been delivered in a straight line from the "
  "bowler's hand', were 'all directed towards limiting [round-arm's] effect'. The booklet's 'pitched'/'foot or leg' is outdated 1820 "
  "wording, so the texts look closer than the official Laws were.", ["S16", "S33-02", "S33-03"], sec="NOVEL_EVENT",
  secsub="bowling_innovation", date="9 May 1839 (serial 87). " + LATE)
L("E021", "Crossed: booklet's extra clause '-if they are not crossed, he that has left the wicket which is put down, is out' not in 1835.",
  NC, "", "high", "derived",
  BOOK + "The clause is in the 1820 text (S16 ch.2) but not in the 1828 code or the official 1829 Code (S33-02 Law 26 'covers only "
  "crossed players'). Source-edition artefact, not a deletion in 1835.", EV_B, note="source-edition artefact")
L("E022", "'When a ball is caught, no notch to be reckoned' -> 'A ball being caught no run shall be reckoned.'", SW, "terminology_term",
  "medium", "inferred", "'notch' -> 'run' in the 1835 revision (Rait Kerr serial 54b on 'run' replacing 'notch'; the March 1835 "
  "proposal S33-03 has 'no run shall be reckoned'). Meaning unchanged.", ["S16", "S33-03"], date="1835 revision")
L("E023", "'When a striker is run out, the notch they were running for is not to be reckoned' -> 'A striker being run out, that run which he "
  "and his partner were attempting shall not be reckoned.'", SW, "terminology_term", "medium", "inferred",
  "'notch' -> 'run' and 'they' made explicit ('he and his partner') in the 1835 revision (S33-03). Meaning unchanged.",
  ["S16", "S33-03"], date="1835 revision")
L("E024", "Lost ball: 'allowed six: ... then the striker to have all they run' -> 'allowed six runs; ... then the striker shall have all "
  "which have been run'. Same rule.", ST, "wording_only", "high", "derived",
  "Allowance six in both (Rait Kerr serial 66, before 1823); only 'runs' added and grammar regularised.", ["S18", "S16"])
L("E025", "Dead ball / leaving crease: old 'When the ball has been in the bowler's or wicket-keeper's hands, it is considered as no longer in "
  "play; and the strikers need not keep within their ground till the umpires have called \"play:\" but if the player goes out of his "
  "ground with an intent to run, before the ball is delivered, the bowler may put him out' -> new 'After the ball shall have been finally "
  "settled in the wicket keepers or bowler's hand, it shall be considered dead: but when the bowler is about to deliver the ball, if the "
  "striker at his wicket go outside the popping crease before such actual delivery, the said bowler may put him out, unless ... his bat "
  "in hand, or some part of his person be within the popping crease.'", UN, "no_cause_stated", "medium", "none",
  "Real changes of the 1835 revision (March 1835 proposal S33-03: 'lodged & definitively settled ... dead', striker going outside the "
  "crease before actual delivery may be put out by the bowler): the ball becomes 'dead' only when 'finally settled', the 'with an intent "
  "to run' condition and the 'till the umpires have called play' allowance are gone, and the grounding exception refers to the run-out "
  "law. Rait Kerr's chronology has no serial for it and gives no cause; searched ch.2-3 and ch.6.", ["S33-03", "S16"],
  date="1835 revision (S33-03); the 'unless ... 21st law' exception is not in the proposal and was added by c.1845")
L("E026", "Removed: the booklet's commentary 'Choice of Ground ...'.", NC, "", "high", "derived",
  BOOK + "Editorial text, not a Law. Source-edition artefact.", EV_B, note="source-edition artefact; no fitting NOT_A_CHANGE subtype")
L("E027", "Stumps: 'Must be three in number, twenty-seven inches out of the ground, the bails eight inches in length; the stumps of equal and "
  "of sufficient thickness to prevent the ball from passing through.'", ST, "codification_definition", "high", "stated",
  "Rait Kerr serial 83 (May 10th 1838): 'Although often referred to in earlier unofficial editions of the Laws, it is specifically "
  "stated for the first time officially that each wicket consists of three stumps, of equal and sufficient thickness'. The 'sufficient "
  "thickness' clause itself was official since c.1823 (serial 68; S33-02 Law 3) and its absence in 1830 is a booklet artefact.",
  ["S16", "S33-02"], date="10 May 1838 (serial 83). " + LATE)
L("E028", "Hurt striker: 'may retire from his wicket, and have his innings any time in that innings' -> '... and return to it any time "
  "during that innings'. Same rule.", NC, "", "high", "derived",
  BOOK + "The 1828 code already says 'return to it at any time in that innings'; 'have his innings' is the booklet's 1820 wording.",
  EV_B, note="source-edition artefact")
L("E029", "Runner: 'some other person may be allowed to stand out for him, but not go in' -> 'some other person may stand out for him, but "
  "not go in'. Same rule.", ST, "wording_only", "high", "derived", "'be allowed to' dropped; permission unchanged.", ["S18"])
L("E030", "Substitutes (new): 'No substitute in the field shall be allowed to bowl, keep wicket, stand at the point, cover the point, or "
  "stop behind in any case.' (1828/1829 official: '... stand at the point or middle-wicket, or stop behind to a fast bowler, unless with "
  "the consent of the adverse party'; absent from the 1830 booklet).", UN, "no_cause_stated", "medium", "none",
  "Rait Kerr serial 75 (May 20th 1835): 'Substitutes, even with consent, may not bowl, keep wicket, field at point, cover point, or long "
  "stop - in the last-named position the embargo now applies to every type of bowling.' No reason given (ch.2 calls the 1810-35 "
  "substitute rules 'general points').", ["S16", "S33-02"], date="20 May 1835 (Rait Kerr serial 75)",
  note="The law's absence in 1830 is a booklet artefact; the substantive 1835 change is the removal of consent and the wider embargo.")
L("E031", "Hat: 'If any player stops the ball with his hat ... add five notches' -> 'If any fieldsman stop the ball with his hat ... add five "
  "runs ...'.", SW, "terminology_term", "medium", "inferred",
  "'notch' -> 'run' (1835 revision; S33-03 has 'five runs') and 'player' -> 'fieldsman', which makes explicit that the penalty concerns "
  "the fielding side, as the law's effect already implied (the 1828 code says 'any person'). Penalty unchanged (five). Rait Kerr serial "
  "49a dates the law to 1798; no later change before 1884.", ["S16", "S33-03"], date="1835 revision")
L("E032", "Guarding the wicket: 'the striker may guard his wicket either with his bat or body' -> 'The ball having been hit, the striker may "
  "guard his wicket with his bat, or with any part of his body except his hands; that the twenty-third law may not be disobeyed.'", ST,
  "consequential", "medium", "stated",
  "The Law itself states its purpose: the hands are excluded 'that the twenty-third law [touching or taking up the ball] may not be "
  "disobeyed'; the March 1835 proposal (S33-03) reads 'except his hand; that the twenty fourth law (by which he is forbidden to touch, "
  "or take up the ball) may not be disobeyed'. A consequential alignment with the handling law; Rait Kerr has no serial for it.",
  ["S33-03"], date="1835 revision (S33-03)")
L("E033", "Wicket-keeper: new 'The wicket keeper shall not take the ball for the purpose of stumping, until it have passed the wicket'; "
  "'any part of his person' (booklet: 'his hands, knees, feet or head'); the clause 'shall stand at a reasonable distance behind the "
  "wicket' is no longer printed; Bets moved to the end.", UN, "no_cause_stated", "medium", "none",
  "The stumping restriction is new in the 1835 revision (March 1835 proposal S33-03, which still keeps 'he shall stand at a reasonable "
  "distance behind the wicket'). Rait Kerr's chronology has no serial for it; his serial 137 (1947) says 'The old Laws were obscure on "
  "the point of the wicket-keeper taking the ball in front of the wicket'. No cause given. 'any part of his person' was already the "
  "official wording (S33-02), so that part is a booklet artefact.", ["S33-03", "S16", "S33-02"], date="1835 revision (S33-03)",
  integrity="suspect", note="Whether 'reasonable distance' was really dropped by c.1845 or lost in this printing is unverified.")
L("E034", "Umpires: 'sole judges of fair and unfair play' -> 'fair or unfair play'; 'whose opinion is conclusive' -> 'shall be conclusive'; "
  "'at the Bowler's Wicket' -> 'at the wicket bowled from'; the interval sentence moved to its own Law.", ST, "wording_only", "high",
  "derived", "Same powers and same catch procedure; 'and'/'or' and 'is'/'shall be' do not alter the rule. The interval sentence is "
  "labelled where it now stands.", ["S18"])
L("E035", "Added: 'The umpires shall change wickets, after each party has had one innings.' (with the pitch-and-toss sentence, also moved).",
  UN, "no_cause_stated", "medium", "none",
  "Rait Kerr serial 92 (June 2nd 1845): 'The umpires are required to change ends after each side has had one innings.' No reason given "
  "(ch.3, ch.6).", ["S16"], date="2 June 1845 (serial 92). " + LATE)
L("E036", "Relocated 'The Umpires, in all Matches, to pitch fair wickets, and the parties to toss ...' -> 'The umpires in all matches shall "
  "pitch fair wickets, and the parties shall toss up ...'.", NC, "", "high", "derived",
  BOOK + "The 1828 code already has 'shall pitch ... shall toss'; the infinitive style is the booklet's. Source-edition artefact.",
  EV_B, note="source-edition artefact")
L("E037", "Interval: 'two minutes for each man to come in, and fifteen minutes between each Innings' -> 'two minutes for each striker to "
  "come in, and ten minutes between each innings'.", UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 88 (May 14th 1840): 'The interval between innings reverts to 10 minutes' (serial 29, 1774, had raised it from 10 to "
  "15). No reason given. Raw 1835 OCR (second version) reads 'ten minutes'. 'each man' -> 'each striker' is terminology only.",
  ["S16"], date="14 May 1840 (serial 88). " + LATE)
L("E038", "Added: 'They are not to order a striker out unless appealed to by the adversaries.'", NC, "segmentation_artefact", "high",
  "derived", SEG + "The same sentence is also matched as a relocation of the old one, where the 'player'->'striker' wording is labelled.",
  ["S18"])
L("E039", "Relocated 'They are not to order a player out, unless appealed to by the adversaries' -> '... a striker out ...'.", SW,
  "terminology_term", "high", "inferred", "'player' -> 'striker': only a batsman can be ordered out, so the meaning is unchanged; part of "
  "the 1835 revision's tidier terminology.", ["S18"])
L("E040", "Bowling crease: booklet 'three feet in length, with a return-crease' -> 'six feet eight inches in length, the stumps in the "
  "centre; with a return crease at each end towards the bowler at right angles'.", SW, "clarifying_rewrite", "medium", "inferred",
  "The length is not a 1830-35 change: three feet is the pre-1823 crease reprinted by the booklet, and 6 ft 8 in was official since "
  "before 1828 (Rait Kerr serials 65 and 69; S33-02 Law 4). The only new words are 'towards the bowler' (also in the March 1835 "
  "proposal, S33-03), which fixes the direction in which the return creases are drawn.", ["S16", "S33-02", "S33-03"], sec=NC,
  secsub="", date="'towards the bowler': 1835 revision", note="length difference is a source-edition artefact")
L("E041", "Removed: 'The umpires are not to be changed during the match, but by the consent of both parties:'", NC, "segmentation_artefact",
  "high", "derived", SEG + "Re-appears in new law 43 with the umpire-betting exception, labelled there.", ["S18"])
L("E042", "Added: 'But if one of the bowler's feet be not on the ground behind the bowling crease ... the umpire at his wicket unasked must "
  "call \"No Ball.\"'", NC, "segmentation_artefact", "high", "derived",
  SEG + "The same sentence is also matched as a relocation of the old foot no-ball sentence, where the change is labelled.", ["S18"])
L("E043", "Bowler's foot: 'if the bowler's foot is not behind the bowling-crease ... they must, unasked, call no ball' -> 'if one of the "
  "bowler's feet be not on the ground behind the bowling crease, and within the return crease when he shall deliver the ball, the "
  "umpire at his wicket unasked must call \"No Ball.\"'", UN, "no_cause_stated", "medium", "none",
  "Real change: the delivery foot must be grounded behind the crease ('on the ground'), and the call is assigned to the bowler's-end "
  "umpire. 'on the ground' is not in the March 1835 proposal's Bowler law (S33-03), so it was added between 1835 and c.1845; Rait Kerr "
  "has no serial for it and no source gives a reason.", ["S33-03", "S16"], date="Between May 1835 and c.1845 (not dated by Rait Kerr)")
L("E044", "Added: 'If either of the strikers run a short run, the umpire must call \"One Short.\"'", NC, "segmentation_artefact", "high",
  "derived", SEG + "Also matched as a relocation of the old short-notch sentence, where the change is labelled.", ["S18"])
L("E045", "Short run: 'If the striker runs a short notch, the umpire must call \"no notch.\"' -> 'If either of the strikers run a short run, "
  "the umpire must call \"One Short.\"'", SW, "terminology_term", "high", "inferred",
  "'notch' -> 'run' and the call 'No Notch' -> 'One Short'; Rait Kerr serial 30 says the short-run Law 'has remained essentially "
  "unaltered' since c.1774 (a 1835 proposal to deduct two runs was considered but not adopted). 'either of the strikers' makes explicit "
  "that both batsmen are covered.", ["S16", "S33-03"], date="1835 revision")
L("E046", "Added: 'No umpire shall be allowed to bet.'", "ECONOMY", "betting_stakes", "medium", "inferred",
  "Rait Kerr serial 76 (May 20th 1835): 'A Law to prohibit umpires from betting appears later in the day than might be expected, since "
  "the selling of matches had become a scandal many years earlier.' He implies the cause (betting corruption) without stating that it "
  "prompted the 1835 law, so basis inferred.", ["S16"], date="20 May 1835 (Rait Kerr serial 76)")
L("E047", "Added: 'No umpire is to be changed during a match, unless with the consent of both parties, except in case of a violation of the "
  "42nd law; then either party may dismiss the transgressor.'", "ECONOMY", "betting_stakes", "medium", "inferred",
  "Rait Kerr serial 76 (May 20th 1835): 'Either side is given power to dismiss an offending umpire' - the sanction for the new umpire-"
  "betting ban, prompted (inferred) by match-selling scandals. The consent rule itself is old (serial 46, 1798).", ["S16"],
  date="20 May 1835 (Rait Kerr serial 76)")
L("E048", "Added: 'After the delivery of four balls, the umpire must call \"Over,\" but not until the ball shall be finally settled in the "
  "wicket keepers, or bowler's hand; the ball shall then be considered dead; nevertheless if an idea be entertained that either of the "
  "strikers is out, a question may be put previously to, but not after the delivery of the next ball.'", UN, "no_cause_stated",
  "medium", "none",
  "Rait Kerr serials 79b ('The umpire is again instructed to call Over after the four balls have been bowled') and 81 ('For an appeal to "
  "be entertained it must be made before the next ball is bowled'), both May 20th 1835. No reason given (ch.6; ch.2-3 searched).",
  ["S16", "S33-03"], date="20 May 1835 (serials 79b, 81)")
L("E049", "Added: 'The umpire must take especial care to call \"No Ball\" instantly upon delivery, \"Wide Ball\" as soon as ever it shall pass "
  "the striker.'", UN, "no_cause_stated", "medium", "none",
  "Rait Kerr serial 80a (May 20th 1835): umpire 'specially enjoined to call No ball immediately on delivery, and Wide as soon as the ball "
  "has passed the striker'. No reason given.", ["S16", "S33-03"], date="20 May 1835 (serial 80a)")
L("E050", "Added: 'The players who go in second shall follow their innings, if they have obtained one hundred runs less than their "
  "antagonist.'", "ENJOYMENT", "avoid_draws", "high", "stated",
  "Rait Kerr serial 78 (May 20th 1835): 'The first follow on Law appears obliging a side to bat again if 100 runs behind on the first "
  "innings.' Ch.4 (S16): the follow-on and declaration Laws 'were primarily directed towards reducing the number of drawn matches' and "
  "'the follow on Law dates from 1835'; ch.3 lists the follow-on rule as 'designed to reduce the number of undecided matches'.",
  ["S16"], date="20 May 1835 (Rait Kerr serial 78)")
L("E051", "Mis-paired block: old lost-ball/out/dead-ball text vs new law 47 'When one of the strikers shall have been put out, the use of "
  "the bat shall not be allowed to any person, until the next striker shall come in', plus the Single-wicket laws (new: run completed by "
  "touching 'the bowling stump or crease in a line with it ... or go beyond them'; 'nor shall the striker be caught out behind wicket, "
  "nor stumped out') and Bets ('No bet is payable on any match unless it be played out, or given up').", UN, "no_cause_stated", "medium",
  "none",
  "Law 47 is Rait Kerr serial 86 (May 9th 1839): 'Practice with the bat is prohibited during play'; no reason given. The single-wicket "
  "and bets additions are in the March 1835 proposal (S33-03), so 1835 revision; Rait Kerr does not list them. The booklet had dropped "
  "most single-wicket laws (source-edition artefact), so their reappearance is not itself a change.", ["S16", "S33-03"],
  date="Law 47: 9 May 1839 (serial 86), " + LATE + "Single wicket / bets: 1835 revision.",
  note="Several real changes in one mis-segmented event.")
L("E052", "Popping crease: added 'unlimited in length, but not shorter than the bowling crease' (four feet unchanged; 'paralleled' is a "
  "misprint of 'parallel').", ST, "codification_definition", "medium", "inferred",
  "New in the 1835 revision (March 1835 proposal S33-03, which also proposed 4 ft 4 in - not adopted; the adopted text keeps four feet, "
  "raw OCR confirms). Rait Kerr has no serial and no source gives a reason; treated as defining the marking (inferred).",
  ["S33-03"], date="1835 revision (S33-03)")
L("E053", "Wickets: booklet 'which shall be pitched within thirty yards of a centre, by the adversaries' -> 'Must be pitched opposite to "
  "each other by the umpires'.", NC, "", "high", "derived",
  BOOK + "Pitching by the umpires dates from before May 1823 (Rait Kerr serial 63) and is in the 1828 code and S33-02 Law 6. Source-"
  "edition artefact, not an 1830-35 change.", EV_B, note="source-edition artefact")
L("E054", "Added: the ground law 7 (alteration of the ground; striker may beat the ground; bowler may fill up holes with saw dust).", NC,
  "segmentation_artefact", "high", "derived", SEG + "The same law is also matched as a relocation of the old text, where the change is "
  "labelled.", ["S18"])
L("E055", "Ground law: old '... nor to prevent the bowler from filling up holes, watering his ground, or using saw-dust, when the' (cut off) "
  "-> '... near to the spot where he stands ..., nor to prevent the bowler from filling up holes with saw dust, &c. when the ground "
  "shall be wet.'", UN, "no_cause_stated", "medium", "none",
  "Real change: the bowler's permission to water his ground is gone - Rait Kerr serial 73 (before 1831): 'An old provision permitting "
  "the bowler to water his run up to the wicket is deleted'; the official 1829 Code (S33-02) already lacks it, so the 1830 booklet "
  "carries an obsolete clause. No reason given. The truncation of the old text is a missing page in the 1830 scan.", ["S16", "S33-02"],
  date="Before 1831 (serial 73); appears here because the 1830 source is an outdated booklet")
L("E056", "Added: 'After rain the wickets may be changed with the consent of both parties.'", NC, "", "high", "derived",
  "The law is in the 1828 code and the official 1829 Code (S33-02 Law 8); it is missing from the 1830 text because a page is missing "
  "from the 1830 scan (raw OCR jumps from p.9 to p.11 in the middle of the preceding ground law). Not a new rule.", ["S33-02", "S33-01"],
  note="scan (missing page) artefact; no fitting NOT_A_CHANGE subtype")
L("E057", "Bowler: 'shall deliver the ball with one foot behind the bowling-crease ... which he shall do but once in the same innings' -> "
  "'Shall deliver the ball with one foot on the ground behind the bowling crease ... which he shall be permitted to do once only in the "
  "same innings'; the booklet's side/wide/no-ball sentences leave this block.", UN, "no_cause_stated", "medium", "none",
  "Real change: delivery foot must be 'on the ground' behind the crease (not in the March 1835 proposal's Bowler law, S33-03, so added "
  "1835-c.1845; same change in the umpires' no-ball law). No source gives a reason; Rait Kerr has no serial. 'shall be permitted to "
  "do' was already the 1828 wording ('shall do' is the booklet's). The removed sentences are labelled where their replacements stand.",
  ["S33-03", "S16"], date="Between May 1835 and c.1845 (not dated by Rait Kerr)")
