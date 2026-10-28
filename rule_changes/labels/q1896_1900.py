"""Labels for 1896 -> 1900.

MCC changes in this interval (Rait Kerr ch.6; ACS S35-04/S35-05): serial 112 (3 May 1899, ball lodging in clothing - NOT in the
dataset's 1900 text), serial 113 (30 Oct 1899, either umpire may call no ball), serials 114-116 (2 May 1900: optional follow-on at
150/100/75, declaration after lunch on day two of a three-day match, six-ball over). The dataset's 1900 text is a Wright & Co.
pamphlet ('As Revised by the Marylebone Cricket Club, May, 1900') that carries the six-ball over, 'either umpire' and the 150/75
figures but still prints the follow-on as compulsory and the old last-day declaration Law, omits Law 33B (lodging in clothing)
and has many paraphrases/misprints ('may change ends', 'put out', 'allowances under 41', 'special care', 'when either side',
'throw at the wicket') that the 1902 text and ACS 1900 (S35-05) do not have. Those are labelled as printing noise.
"""
from _h import make
PAIR = "1896_1900"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
EN, EC, NE = "ENJOYMENT", "ECONOMY", "NOVEL_EVENT"
P00 = "Variant of the 1900 Wright & Co. pamphlet; the 1902 text and ACS 1900 (S35-05) keep the 1896 wording."
D1900 = "Rait Kerr: May 2nd 1900; ACS S35-05: 'The changes in the 1900 revision were to Laws 13, 53 and 54'."
D1899 = "Rait Kerr serial 113: Oct. 30th 1899; ACS S35-04 (1899 revisions, Law 48A 'umpire at either end')."

L("E001", "Single wicket Laws appear as one new block ('Law *') in 1900.", NC, "segmentation_artefact", "high", "derived",
  "The single-wicket Laws were already present in 1896 (each also matched as a relocation in this pair); the 1900 printing's heading 'THE LAWS OF SINGLE WICKET.' made the segmenter treat them as one new block. Wording differences inside it are labelled on the relocation events.",
  ["S18"])
L("E002", "Single wicket Laws 1-2 relocated; 'in a line with the bowling stump' printed 'in line with the bowling stump'.", NC, "segmentation_artefact", "high", "derived",
  "Same Laws, matched across a block-segmentation change; 'in line'/'in a line' is a printing variant (1902 reads 'in a line').", ["S18"], note=P00)
L("E003", "Single wicket Law 10 (no restriction on overs, one minute between balls) relocated.", NC, "segmentation_artefact", "high", "derived", "Identical wording; segmentation only.", ["S18"])
L("E004", "Single wicket Law 2 (bounds 22 yards when fewer than five a side) relocated.", NC, "segmentation_artefact", "high", "derived", "Identical wording; segmentation only.", ["S18"])
L("E005", "Single wicket Law 3 (ball must be hit before the bounds) relocated.", NC, "segmentation_artefact", "high", "derived", "Identical wording; segmentation only.", ["S18"])
L("E006", "Single wicket Law 4 ('No hit') relocated; comma and capital only.", NC, "segmentation_artefact", "high", "derived", "Same wording apart from punctuation; segmentation only.", ["S18"])
L("E007", "Single wicket Law 5 (no byes/overthrows, no caught behind or stumped when fewer than five a side) relocated.", NC, "segmentation_artefact", "high", "derived", "Identical wording; segmentation only.", ["S18"])
L("E008", "Single wicket Law 6: the clause 'the striker may run till the ball be so returned' is a separate sentence in 1900.", NC, "segmentation_artefact", "high", "derived",
  "1900 prints the clause as its own sentence ('The striker may run till the ball be so returned.'); it is still there, so nothing is removed.", ["S18"])
L("E009", "Single wicket Law 7: 'he must touch the bowling stump or crease' becomes 'he must touch the middle stump or crease'; 'start' -> 'starts'.",
  NC, "ocr_noise", "high", "derived",
  "The 1900 raw OCR is garbled at this point ('touch the iu«ii>io ntump «»r crease'); 'middle' is an AI clean-up guess. The run is completed at the bowling stump (single-wicket Law 3), and the 1902 text reads 'touch the bowling stump or crease'. No change.",
  ["S17", "S18"], integrity="suspect")
L("E010", "Single wicket Law 8: 'fieldsman' printed 'field-man'.", NC, "ocr_noise", "high", "derived", "OCR/printing slip; same rule.", ["S18"])
L("E011", "Single wicket Law 9: 'All hits, byes, leg-byes, and overthrows shall then be allowed' becomes 'All runs, byes, leg byes, and overthrows ...'.",
  NC, "ocr_noise", "high", "derived",
  "1900 raw OCR reads 'All hus, byes, Kg byes' - 'hits' garbled and 'cleaned' to 'runs'; the 1902 text reads 'All Hits, Byes, Leg Byes, and Overthrows'.", ["S17", "S18"], integrity="suspect")
L("E012", "One-day matches Law 1: follow-on 'if they have scored 60 runs less than the opposite side' becomes '75 runs less'.",
  EN, "avoid_draws", "medium", "inferred",
  "Rait Kerr serial 114 (May 2nd 1900): the follow-on 'becomes optional for the side in the lead. The limits are altered to: ... for a one-day match 75 runs.' Ch.4 says the alterations to the follow-on and declaration Laws 'were primarily directed towards reducing the number of drawn matches'; for the 1900 change he cites 'considerable pressure from Australia, and the failure to win a Test match after Australia had automatically followed on in 1899 at Old Trafford' (that reason concerns making it optional; the new figure is part of the same revision, hence inferred).",
  ["S16", "S35-08"], sec=NE, secsub="single_incident", date=D1900, integrity="suspect",
  note="The 1900 printing still says 'shall follow their innings' (compulsory); the 1902 text has the optional form ('shall have the option of requiring'). 75 itself is in the raw OCR.")
L("E013", "One-day Law 3: 'the over consists of 5 or 6 balls' printed 'the over consist of five or six balls'.", NC, "format_artefact", "high", "derived",
  "Numerals vs. words and 'consist'/'consists' printing variant; same option.", ["S18"], note=P00)
L("E014", "Single wicket Laws block ('Law *') listed as removed.", NC, "segmentation_artefact", "high", "derived",
  "Not removed: the same single-wicket Laws are in the 1900 text (see the relocations and the new block in this pair).", ["S18"])
L("E015", "Law 1: 'two sides of eleven players each' printed '11 players'; the sentence split into two segments.", NC, "format_artefact", "high", "derived",
  "Numeral vs. word and sentence splitting; 1902 reads 'eleven players'. Same Law.", ["S18"], note=P00)
L("E016", "Law 10: 'if thrown or jerked, the umpire shall call “No ball.”' becomes 'if thrown or jerked either umpire shall call “no ball.”'",
  NE, "tactic_abuse", "medium", "stated",
  "Rait Kerr serial 113 (Oct. 30th 1899): 'Either umpire may call “No ball” if not satisfied with the absolute fairness of any delivery.' Ch.4 ('Throwing'): the throwing scandal 'by 1896 had spread from England to Australia', and 'The M.C.C. decided to deal with the matter by empowering either umpire to call “No ball”'. He attributes the throwing itself to bowlers' frustration on improved pitches (secondary).",
  ["S16", "S35-04"], sec="EXTERNAL_FORCE", secsub="pitch_technology", date=D1899,
  note="ACS S35-04/S35-05 change only Law 48A ('umpire at either end') and still print Law 10 as 'the umpire'; the dataset's 1900 and 1902 texts both have 'either umpire' in Law 10. Confidence medium because the Law 10 wording is not confirmed by ACS.")
L("E017", "Law 13: the over increased from five to six balls ('overs of five balls' -> 'overs of six balls'; 'When five balls' -> 'When six balls'); third record hyphenation only.",
  EC, "time_saving", "high", "stated",
  "Rait Kerr serial 116 (May 2nd 1900): 'The Over is increased from five balls to six.' Ch.4: the 1889 increase and 'a further increase to six balls ... in 1900. These changes were designed to save time during play'.",
  ["S16", "S35-05"], date=D1900)
L("E018", "Law 14: 'The bowler shall be allowed to change ends as often as he pleases, provided only that he does not bowl two overs consecutively in one innings' printed 'The bowler may change ends as often as he pleases, provided that he shall not bowl two overs in succession in the same innings.'",
  NC, "format_artefact", "medium", "derived",
  "Paraphrase in the 1900 pamphlet (raw OCR confirms it), not an MCC rewording: ACS 1900 (S35-05) and the 1902 text both keep 'shall be allowed to change ends ... provided only that he does not bowl two overs consecutively in one innings'. The permission and restriction are the same.",
  ["S35-05", "S18"], note=P00 + " Flagged to owner: would be SEMANTIC_WORDING (modal_strength) if it were an official rewording.")
L("E019", "Law 16: 'no-ball' -> 'no ball' throughout; 'Laws 26, 27, 29, 30' -> 'Laws 26, 27, 29 and 30'; 'added to the score as “wide balls”' -> 'added to that score'.",
  NC, "format_artefact", "high", "derived", "Hyphenation, punctuation and a 'the'/'that' printing variant (1902 reads 'the score'); same rule.", ["S18"], note=P00)
L("E020", "Law 2: '1st'/'2nd' clauses printed '1.—'/'2.—'; 'the batsmen after a hit' printed 'the batsman'; 'allowances under 44' printed 'allowances under 41'.",
  NC, "ocr_noise", "high", "derived",
  "Numbering style plus two misprints in the 1900 pamphlet (both in raw OCR): 'batsman ... their ground' is ungrammatical, and allowances for boundaries are under Law 44 (umpires 'arrange boundaries ... and the allowances to be made for them'), as the 1896 and 1902 texts and ACS S35-05 say. No change.",
  ["S18", "S35-05"], integrity="suspect", note=P00)
L("E021", "Law 21: the heading 'The striker is out—' is printed inside Law 21 in 1900 ('The striker is out if the wicket be bowled down ...'); 'Bowled.' split off.",
  NC, "segmentation_artefact", "high", "derived",
  "Same Law: 1896 has 'The striker is out—' as a heading before Law 21; the 1900 raw OCR still has '“ Bowled.”' on the next line.", ["S18"])
L("E022", "Law 28: the heading 'Either batsman is out—' is printed inside Law 28 in 1900; brackets round '(with ball in hand)'.", NC, "segmentation_artefact", "high", "derived",
  "Heading text moved into the Law by the printing/segmentation; the run-out rule is unchanged.", ["S18"])
L("E023", "Law 34: 'lost ball' printed 'lost-ball'; punctuation.", NC, "format_artefact", "high", "derived", "Hyphenation and punctuation only.", ["S18"])
L("E024", "Law 35: 'if the bowler throw at that wicket' printed 'throw at the wicket'; 'no-ball' -> 'no ball'.", NC, "ocr_noise", "medium", "derived",
  "'the'/'that' is a 1900 pamphlet variant (raw OCR 'at the wicket'); 1902 and ACS S35-05 read 'that wicket'. Same rule.", ["S18", "S35-05"], note=P00)
L("E025", "Law 4: ball weight and circumference written in words ('five ounces and a half ... five ounces and three-quarters'; 'nine inches, nor more than nine inches and one quarter'); the 1896 processed circumference '9½in.' becomes 'nine inches and one quarter'.",
  NC, "cleaning_artefact_numeric", "high", "derived",
  "Words vs. figures; the apparent ½ -> ¼ change only reverses an AI clean-up invention in the 1896 processed text (raw '9|in.'); ACS S35-04/S35-05 give 'nine inches and one-quarter'.",
  ["S17", "S35-05"], integrity="suspect")
L("E026", "Law 40: 'A batsman is liable to be out for any infringement' printed 'liable to be put out for any infringe ment'.", NC, "ocr_noise", "medium", "derived",
  "1900 pamphlet variant plus a line-break hyphen; 1902 reads 'liable to be out'. Same rule.", ["S18"], note=P00)
L("E028", "Law 45: 'When they shall call “Play,”' printed 'When they call “play”'.", NC, "format_artefact", "high", "derived",
  "1900 pamphlet variant; 1902 reads 'When they shall call “Play”'. Same rule.", ["S18"], note=P00)
L("E029", "Law 48 (48a in 1900): 'If the umpire at the bowler's end be not satisfied of the absolute fairness of the delivery of any ball, he shall call “No ball.”' becomes 'If either umpire be not satisfied ...'.",
  NE, "tactic_abuse", "high", "stated",
  "Rait Kerr serial 113 (Oct. 30th 1899): 'Either umpire may call “No ball” if not satisfied with the absolute fairness of any delivery.' Ch.4: 'The M.C.C. decided to deal with the matter [the throwing scandal] by empowering either umpire to call “No ball”'. ACS S35-04 shows Law 48A changed to 'the umpire at either end' in the 1899 revisions. The stray '48½.' in the 1896 text is a misread Law number.",
  ["S16", "S35-04"], sec="EXTERNAL_FORCE", secsub="pitch_technology", date=D1899)
L("E030", "'Especial care' Law appears as new Law 48b ('The umpire shall take special care to call “no ball” instantly upon delivery ...').", NC, "segmentation_artefact", "high", "derived",
  "Not new: the same Law existed as 48a in 1896 (relocation event in this pair). The 1900 pamphlet's numbering (raw OCR '48/7.' and '48ft.') was read as 48a/48b; ACS S35-05 says 48 was renumbered in 1900 (to 48/48A, as in 1902). 'special' for 'especial' is a pamphlet variant.",
  ["S18", "S35-05"])
L("E031", "'Especial care' Law relocated from 48 (merged in 1896 segmentation) to 48b; 'especial' printed 'special'.", NC, "segmentation_artefact", "high", "derived",
  "Same Law; numbering artefact (see the new-Law event for 48b) and a printing variant (1902: 'especial care').", ["S18", "S35-05"], note=P00)
L("E032", "Law 5: bat '4¼in.' and '38in.' written as 'four inches and one-quarter' and '38 inches'.", NC, "format_artefact", "high", "derived", "Figures vs. words; same dimensions.", ["S18"])
L("E033", "Law 52: '..., then either side may dismiss him' printed '..., when either side may dismiss him'.", NC, "format_artefact", "high", "derived",
  "1900 pamphlet variant; 1902 reads 'then'. Same rule.", ["S18"], note=P00)
L("E034", "Law 53 (follow-on): 'if they have scored 120 runs less than the opposite side in a threedays match, or 80 runs in a two-days match' becomes 'if they have scored 150 runs less than the opposite side' (still printed as compulsory); the declaration Law is appended to the segment as '1.—On the last day of a match ...'.",
  EN, "avoid_draws", "medium", "inferred",
  "Rait Kerr serial 114 (May 2nd 1900): 'The enforcement of a “Follow on” becomes optional for the side in the lead. The limits are altered to: for a three-day match 150 runs, for a two-day match 100 runs'. Ch.4: follow-on and declaration alterations were 'primarily directed towards reducing the number of drawn matches'; the 1900 change came after 'considerable pressure from Australia, and the failure to win a Test match after Australia had automatically followed on in 1899 at Old Trafford' and the University matches of 1891, 1893 and 1896. The 1900 pamphlet shows only the new three-day figure; the optional form and 100-run two-day limit appear in ACS S35-05 and the 1902 text. Inferred because his stated reasons concern optionality, not the figure.",
  ["S16", "S35-05", "S35-08"], sec=NE, secsub="single_incident", date=D1900, integrity="suspect",
  note="The appended declaration text is a segmentation artefact (Law number '54' read as 'o 1.'). The 1900 printing omits the optional wording, the two-day limit and the new 1900 declaration Law (serial 115); these first show in 1902.")
L("E035", "Law 54 (declaration on the last day) listed as removed.", NC, "segmentation_artefact", "high", "derived",
  "Not removed: the 1900 pamphlet still prints the old last-day declaration Law, but its number was read as 'o 1.' and the text was attached to Law 53 (see the follow-on event in this pair). Note the pamphlet does NOT show the May 1900 declaration change (Rait Kerr serial 115: declaration after luncheon on the second day of a three-day match), which first appears in the 1902 text.",
  ["S18", "S35-05"], integrity="suspect")
L("E036", "Law 6: '8in.' written 'eight inches'; bail length '4¼in.' (1896 processed) becomes 'four inches' and projection '¾in.' becomes 'half-an-inch'.",
  NC, "cleaning_artefact_numeric", "high", "derived",
  "1896 raw OCR reads 'The bails shall be each 4in.' and 'more than gin.' (½); ACS S35-04/S35-05 give 'four inches' and 'half-an-inch'. The apparent changes only reverse AI clean-up inventions in the 1896 processed text.",
  ["S17", "S35-05"], integrity="suspect")
L("E037", "Law 7: '6ft. 8in.' written '6 feet 8 inches'; punctuation.", NC, "format_artefact", "high", "derived",
  "Abbreviation vs. full units; the bowling crease stays 6 ft 8 in. (lengthened only in 1902, Rait Kerr serial 117).", ["S18", "S16"])
L("E038", "Law 8: '4ft.' written 'four feet'; 'and be deemed unlimited' -> 'and deemed unlimited'.", NC, "format_artefact", "high", "derived", "Figures vs. words and a dropped 'be'; same rule.", ["S18"])
