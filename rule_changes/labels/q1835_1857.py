"""Labels for 1835 -> 1857.

Dating notes that apply to the whole pair:
- The dataset's "1835" main text is the second ruleset in the 1835 PDF (data_appendix.xlsx). It already contains the 1838-1845
  changes (three stumps, no trial balls, l.b.w. pitched straight, all runs from a Wide, the 1845 Wide definition and No-ball
  wording, umpires changing ends: Rait Kerr serials 83-92) but not the 1849 rolling change (serial 93), so it is a printing of
  c.1845-1849, not the 1835 code. Its Single Wicket and Bets sections come from the first (1835) ruleset in the same PDF.
- The "1857" text is a Toronto reprint (Henry Rowsell) printed before May 1858 (its own addendum, S34-04). Its pp.10-11 are
  missing in the scan; old Laws 44-47 and Single Wicket 1-5 were imputed from the 1835 text by the data team.
So the real changes here are those of 1849-1854 (Rait Kerr serials 93-96, plus the 1850 leg-bye decision).
"""
from _h import make
PAIR = "1835_1857"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
EN, EC = "ENJOYMENT", "ECONOMY"

L("E001", "The Ball: the heading 'The Ball' is folded into the sentence ('The ball must weigh ...'); 'five ounces and a half' becomes "
  "'five ounces and a-half' and 'nine inches and one quarter' becomes 'nine and a-quarter inches'. The limits (5½-5¾ oz, 9-9¼ in) are unchanged.",
  NC, "format_artefact", "high", "derived",
  "Same weights and circumference in both texts (raw OCR of both editions agrees); only the heading layout and the way the fractions are written differ. "
  "The circumference limits date from 1838 (Rait Kerr serial 82).", ["S18", "S16"])
L("E002", "Law 12 (Wide): 'adjudge one run to the parties receiving the innings' becomes 'to the party receiving the innings' (plus a comma).",
  SW, "terminology_term", "low", "derived",
  "Plural 'parties' becomes singular 'party' for the side receiving the innings; it names the same side and cannot change how a Wide is scored.",
  ["S18"], date="Printing variation between a c.1845-1849 MCC printing and the 1857 Toronto reprint; no MCC decision recorded.")
L("E003", "Law 13: a new sentence 'If the ball shall first touch any part of the striker’s dress or person (except his hands), the umpire shall call “leg bye.”' "
  "is added after the No-ball/Wide scoring provisions.",
  ST, "codification_definition", "medium", "stated",
  "Taylor (1901) states that on May 2nd 1850 the M.C.C. settled that leg byes should be marked down as such in the score 'so that it could be seen "
  "how much in fault the long stop might be'; before that they were scored as byes. Leg byes were already a recognised means of scoring "
  "(Rait Kerr serials 17 and 105), so the sentence records an existing practice separately rather than creating a new way to score.",
  ["S34-01", "S16"],
  date="M.C.C. decision of 2 May 1850 (Taylor 1901). Rait Kerr serial 105 dates the first formal definition of byes and leg byes to the 1884 code and does not mention this 1850s wording.",
  note="Sources disagree on when leg byes first entered the Laws; the 1857 Toronto text shows a 'leg bye' call before 1884.")
L("E004", "The heading 'The Striker is Out' (a separate block in 1835) disappears; in 1857 the words open Law 15 ('The striker is out if ...').",
  NC, "segmentation_artefact", "high", "derived",
  "The heading text is not lost but moved into the first sentence of Law 15; the segmenter treated the 1835 heading as its own provision.", ["S18"])
L("E005", "Law 15 (Bowled): 'If either of the bails be bowled off ...' becomes 'The striker is out if either of the bails be bowled off ...' - the old heading is folded in.",
  NC, "segmentation_artefact", "high", "derived",
  "Only the 1835 heading 'The Striker is Out' is moved into the sentence; the rule is identical.", ["S18"])
L("E006", "Law 17: 'at any other time while the ball shall be in play' becomes 'at any other time when the ball shall be in play'; 'popping crease' hyphenated.",
  SW, "clarifying_rewrite", "low", "derived",
  "'While' and 'when' are interchangeable here; the wording swap cannot change when a batsman out of his ground can be put out.", ["S18"])
L("E007", "Law 2 (The Bat): heading folded into the sentence ('The bat must not exceed ...'); 'four inches and one quarter' becomes 'four and a-quarter inches'. "
  "Limits (4¼ in wide, 38 in long) unchanged.",
  NC, "format_artefact", "high", "derived",
  "Same width and length in both texts; only the heading layout and the wording of the fraction differ.", ["S18"])
L("E008", "Law 21 (Run out): 'the wicket be struck down by a throw' becomes 'struck down with a throw'; commas moved; 'popping crease' hyphenated.",
  SW, "clarifying_rewrite", "low", "derived",
  "A preposition swap and punctuation; the meaning of the run-out rule is unchanged.", ["S18"])
L("E009", "Law 29: apostrophe added ('wicket keepers' -> 'wicket keeper’s'), colon to semicolon, hyphenation of 'popping-crease', a comma moved.",
  NC, "format_artefact", "high", "derived", "Punctuation and hyphenation only; same words.", ["S18"])
L("E010", "Law 3 (The Stumps): heading folded into the sentence ('The stumps must be three in number ...'); punctuation changes. Dimensions unchanged.",
  NC, "format_artefact", "high", "derived",
  "Same dimensions (27 in out of the ground, 8 in bails); heading layout and punctuation only.", ["S18"])
L("E011", "Law 30: 'If the striker be hurt he may retire from his wicket, and return to it any time during that innings' is replaced by 'The striker shall not "
  "retire from his wicket and return to it to complete his innings after another has been in, without the consent of the opposite party.'",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 96 (May 15th 1854): a batsman who retires may only resume his innings by consent of the fielding side. Neither his chronology "
  "nor chapter 3, nor Taylor 1901 (who notes the right to return without appeal lasted to 1844), gives a reason.",
  ["S16", "S34-02"], date="Rait Kerr serial 96, 15 May 1854; first visible in the 1857 Toronto printing.",
  note="The new text also drops the condition 'be hurt': the consent rule applies to any retirement.")
L("E012", "Old Law 31 'If the striker be hurt, some other person may stand out for him, but not go in.' is deleted; it is replaced by the new consent-based "
  "substitute/runner law (the provision beginning 'No substitute shall in any case be allowed to stand out, or run between wickets').",
  UN, "no_cause_stated", "medium", "none",
  "Part of the 1854 revision of substitutes and runners (Rait Kerr serial 94): standing out for a hurt striker now needs the opponents' consent. "
  "No source found gives a reason.", ["S16"], date="Rait Kerr serial 94, 15 May 1854.")
L("E013", "New Law 31: 'No substitute shall in any case be allowed to stand out, or run between wickets for another person, without the consent of the opposite "
  "party; and in case any person shall be allowed to run for another, the striker shall be out if either he or his substitute be off the ground in manner "
  "mentioned in laws 17 and 21, while the ball is in play.' - first runner provision.",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 94b (May 15th 1854): a runner may be allowed for an injured striker, who is liable to be run out if either he or his runner is out of "
  "ground. Rait Kerr gives no reason; an injury context is implicit in the text but not stated as the cause by any source found.",
  ["S16"], date="Rait Kerr serial 94, 15 May 1854.")
L("E014", "Law 32: 'No substitute in the field shall be allowed to bowl, keep wicket, stand at the point, cover the point, or stop behind in any case.' is replaced by "
  "'In all cases where a substitute shall be allowed, the consent of the opposite party shall also be obtained as to the person to act as substitute, and the "
  "place in the field which he shall take.' The fixed list of forbidden positions is dropped in favour of consent.",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 94a (May 15th 1854): consent of the opposite side is required to the particular player and the place he fields; this ends the 1835 "
  "embargo (serial 75). Taylor 1901 gives the end of the embargo as 'May 15th, 1845' (same day and month, probably a misprint for 1854). No cause is given by either.",
  ["S16", "S34-02"], date="Rait Kerr serial 94a, 15 May 1854.")
L("E015", "Law 33: 'If any fieldsman stop the ball with his hat' becomes 'If any fieldsman stop the ball with his bat' in the 1857 text.",
  NC, "ocr_noise", "medium", "derived",
  "The raw 1857 OCR reads 'bat' here and again in Single Wicket rule 7, but the M.C.C. Law concerned the hat until 1884 (Taylor 1901: before 1884 the "
  "penalty was for stopping the ball with the hat; Rait Kerr serial 49 on the origin of the hat law). This is either an OCR h/b confusion or a misprint "
  "in the Toronto reprint, not a change to the Laws.",
  ["S34-02", "S16", "S18"], integrity="suspect",
  note="Cannot be settled without the page image; either way not an MCC change.")
L("E016", "Law 34: 'that the twenty-third law may not be disobeyed' becomes 'that the 23d law may not be disobeyed'.",
  NC, "format_artefact", "high", "derived", "Same law number written as an ordinal numeral; no change.", ["S18"])
L("E017", "Law 35 (Wicket-keeper): 'until it have passed the wicket' becomes 'until it has passed the wicket'; 'till' becomes 'until'; 'wicket keeper' hyphenated.",
  SW, "clarifying_rewrite", "low", "derived",
  "Subjunctive to indicative and 'till' to 'until': grammar modernisation that cannot change what the wicket-keeper may do.", ["S18"])
L("E018", "Law 37: 'the parties shall toss up for the choice of innings' becomes 'the parties shall toss-up for choice of innings' (article dropped, hyphen, semicolon).",
  SW, "clarifying_rewrite", "low", "derived",
  "Dropping 'the' before 'choice' is a printing variant; the toss rule is unchanged.", ["S18"])
L("E019", "Law 4 (Bowling crease): heading folded into the sentence ('The bowling-crease must be ...'), hyphenation and commas. Length (6 ft 8 in) unchanged.",
  NC, "format_artefact", "high", "derived", "Heading layout, hyphenation and punctuation only.", ["S18"])
L("E020", "Law 40 (No ball, foot): hyphenation ('bowling-crease', 'return-crease'), commas around 'unasked', and 'No Ball' printed as 'no ball'.",
  NC, "format_artefact", "high", "derived", "Punctuation, hyphenation and capitalisation only.", ["S18"])
L("E021", "Law 43: 'except in case of a violation of the 42nd law' becomes 'except in case of violation of the 42d law'.",
  NC, "format_artefact", "high", "derived",
  "Ordinal written '42d' instead of '42nd' and the article 'a' dropped; same cross-reference and same rule.", ["S18"])
L("E022", "Single Wicket rule 1: the heading 'Laws for Single Wicket. 1.' is split from or merged into the first rule differently in the two texts.",
  NC, "segmentation_artefact", "high", "derived",
  "The rule text ('When there shall be less than five players on a side, bounds shall be placed twenty-two yards ...') is identical; only where the "
  "heading and number fall differs. In the 1857 dataset text this rule is imputed from the 1835 text (missing pp.10-11).", ["S18"])
L("E023", "Single Wicket and Bets: (a) the whole 'Bets' section of the 1835 text ('No bet is payable on any match unless it be played out, or given up.' "
  "and three rules on settling bets on players' runs and on innings) is absent in 1857; (b) in Single Wicket rules 6-10 small wording changes: "
  "'before the ball shall cross the play' -> 'before the ball cross the play'; 'ball stopped with hat' -> 'ball stopped with bat'; cross-reference "
  "'29th & 34th law of double wicket' -> '28th and 33rd laws'; 'All hits; byes, and overthrows shall then be allowed' -> 'all “hits,” “byes,” and "
  "“overthrows” will then be allowed'; 'Not more than one minute shall be allowed between each ball' -> 'No more than one minute shall be allowed between each two balls'.",
  EC, "betting_stakes", "low", "inferred",
  "Rait Kerr (ch.3) says betting was 'finally stamped out' during the early part of 1835-1884 and that 'the first step taken in the revision of the code "
  "in 1884 was to delete these [rules on bets] in toto'; the end of cricket betting is therefore the inferred reason for dropping the Bets rules. "
  "The single-wicket changes are wording only: the corrected cross-reference matches the double-wicket numbering (lost ball Law 28, fieldsman Law 33 "
  "after the trial-ball laws were merged), 'bat' for 'hat' is the same misreading/misprint as in Law 33, and 'each two balls' clarifies the interval.",
  ["S16", "S18"], sec=ST, secsub="consequential", integrity="suspect",
  date="Rait Kerr dates the M.C.C. deletion of the betting rules to the 1884 code. Their absence from the 1857 Toronto reprint may be the publisher's choice "
  "or a loss in the missing pp.10-11 (the data team judged they were not on those pages); the dataset shows the removal 27 years early.",
  note="The 1835 'Single Wicket'/'Bets' sections come from the first (1835) ruleset in the PDF, hence the stale cross-references 29th/34th.")
L("E024", "Law 5 (Popping crease): heading folded into the sentence ('The popping-crease must be ...'); 'paralleled to it' corrected to 'parallel to it'; punctuation.",
  NC, "format_artefact", "high", "derived",
  "'paralleled' is a misprint in the 1835 printing; distance (4 ft) and length rule are unchanged.", ["S18"])
L("E025", "Law 6 (The Wickets): heading folded into the sentence ('The wickets must be pitched ...'); 'twenty-two' printed 'twentytwo'; comma added.",
  NC, "format_artefact", "high", "derived", "Same distance (22 yards); heading layout and punctuation only.", ["S18"])
L("E026", "Law 7: the ban on altering the ground during a match gains an exception: 'except at the commencement of each innings, when the ground may be swept "
  "and rolled at the request of either party, such request to be made to one of the umpires within one minute after the conclusion of the former innings.' "
  "Also 'saw dust' -> 'sawdust', 'when the ground shall be wet' -> 'when the ground is wet'.",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 93 (May 3rd 1849) records this permission without a reason; chapter 3 does not discuss it, and his later link between pitch "
  "preparation and the batsman's advantage concerns the 1870s onward. No other source found gives a cause.",
  ["S16"], date="Rait Kerr serial 93, 3 May 1849; first visible in the 1857 printing because the dataset's 1835 text predates 1849.")
L("E027", "Law 9 (The Bowler): heading folded into the sentence ('The bowler shall deliver ...'); 'which he shall be permitted to do once only' becomes "
  "'only once'; hyphenation.",
  SW, "clarifying_rewrite", "low", "derived",
  "Word order 'once only' -> 'only once' and heading layout; the limit of one change of ends per innings is unchanged.", ["S18"])
