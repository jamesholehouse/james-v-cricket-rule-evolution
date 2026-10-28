"""Labels for 1890 -> 1892.

No MCC change to the Laws falls in this interval (Rait Kerr ch.6 has nothing between serial 110, May 1889, and serial 111,
June 1894; ACS lists revisions in 1889 and then 1894, S35-02/S35-03). The 1890 text is a pocket printing ('As revised by the
Committee of the Marylebone Cricket Club, 1884 and 1889') with printer's variants; the 1892 text (Frank Bryan advertiser
printing, 'As Revised by the Marylebone Cricket Club, May 1890') agrees with the ACS transcription of the 1889 revision.
So every event here is a printing, OCR or segmentation difference.
"""
from _h import make
PAIR = "1890_1892"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
PRINT90 = "Reverts a variant of the 1890 pocket printing; the 1892 wording matches the 1884 text and ACS 1889 (S35-02)."

L("E001", "One-day matches Law 3 ('Prior to the commencement of a match it may be agreed that the over consists of 5 or 6 balls') appears as a new Law.",
  NC, "segmentation_artefact", "high", "derived",
  "Not new: the sentence was already in the 1884 text and is in the 1890 text, run into one-day Law 2 because the 1890 printing omits the number '3.'; the 1892 printing numbers it 3 again.",
  ["S18"], note=PRINT90)
L("E002", "Same one-day sentence moves from Law 2 back to Law 3 ('consist' -> 'consists').", NC, "segmentation_artefact", "high", "derived",
  "Numbering restored by the 1892 printing; 'consist'/'consists' is a printing variant. Same rule.", ["S18"], note=PRINT90)
L("E003", "Single wicket Law 1: 'twenty-two yards' printed '22 yards'.", NC, "format_artefact", "high", "derived", "Words vs. numeral; same distance.", ["S18"], note=PRINT90)
L("E004", "Single wicket Law 2: bounds 'twentytwo yards' printed '22 yards'.", NC, "format_artefact", "high", "derived", "Words vs. numeral; same distance.", ["S18"], note=PRINT90)
L("E005", "Single wicket Law 5: 'other throws' (1890 misprint 'otherthrows') back to 'overthrows'.", NC, "ocr_noise", "high", "derived",
  "The 1890 printing's 'otherthrows' is a misprint for 'overthrows' (1884 and 1892 both read 'overthrows').", ["S18"], note=PRINT90)
L("E006", "Single wicket Law 7: 'before the bail cross the ground' back to 'before the ball cross the ground'.", NC, "ocr_noise", "high", "derived",
  "'bail' was a misprint/misread in the 1890 printing; 1884 and 1892 read 'ball'.", ["S18"], note=PRINT90)
L("E007", "Law 10: call printed 'No-ball' -> 'No ball'.", NC, "format_artefact", "high", "derived", "Hyphenation only.", ["S18"])
L("E008", "Law 13: 'Wide-ball' -> 'Wide ball', quote marks.", NC, "format_artefact", "high", "derived", "Hyphenation and quote marks only.", ["S18"])
L("E009", "Law 16: 'no ball'/'noball' -> 'no-ball'; 'Laws' -> 'laws'.", NC, "format_artefact", "high", "derived", "Hyphenation and capitals only.", ["S18"])
L("E010", "Law 17 (Bye): 'no ball' -> 'no-ball', 'Leg bye' -> 'leg-bye', punctuation.", NC, "format_artefact", "high", "derived", "Hyphenation, capitals and punctuation only.", ["S18"])
L("E011", "Law 21: dismissal name '“Bowled.”' present in 1892 but split off in 1890.", NC, "segmentation_artefact", "high", "derived",
  "The 1890 segment lost the dismissal name to the next line; the Law is the same.", ["S18"])
L("E012", "Law 22: dismissal name '“Caught.”' present in 1892 but split off in 1890.", NC, "segmentation_artefact", "high", "derived",
  "The 1890 raw OCR has 'Caught.' on the next line; segmentation only.", ["S18"])
L("E013", "Law 23: 'providing it be not touched' -> 'provided it be not touched'; 'with the hand or arm' -> 'with hand or arm'; 'Stumped.' restored to the segment.",
  NC, "segmentation_artefact", "high", "derived",
  "'Stumped.' was split off the 1890 segment; 'provided' and 'with hand or arm' are the 1892 printing's readings and match ACS 1889 (S35-02), so 'providing'/'the hand' were 1890 printing variants. No change of rule.",
  ["S18", "S35-02"], note=PRINT90)
L("E014", "Law 27: 'or be struck by any part of his person' back to 'or be stopped by any part of his person'.", NC, "ocr_noise", "high", "derived",
  "The 1890 printing's 'struck by' was a misprint; 1884, 1892 and ACS 1889 (S35-02) read 'stopped by'.", ["S18", "S35-02"], note=PRINT90)
L("E015", "Law 35: punctuation and 'No ball' -> 'No-Ball', 'wicketkeeper' -> 'wicket-keeper'.", NC, "format_artefact", "high", "derived", "Punctuation/hyphenation only.", ["S18"])
L("E016", "Law 4: 'weigh no less than 5½oz.' back to 'weigh not less than 5½oz.'", NC, "ocr_noise", "high", "derived",
  "1890 printing variant; same limit; 1892 matches ACS 1889 (S35-02).", ["S18", "S35-02"], note=PRINT90)
L("E018", "Law 48 (umpire at bowler's end to call no ball if not satisfied of fairness): the 1892 segment ends with a stray '48*.'", NC, "segmentation_artefact", "high", "derived",
  "'48*.' is the next Law's number '48a' (raw OCR '485.') attached to this Law's text; the Law's wording is unchanged.", ["S18"])
L("E019", "'Especial care' Law (call no ball instantly, wide when past the striker) moves from Law 48a into Law 48 ('No ball' -> 'No-ball').", NC, "segmentation_artefact", "high", "derived",
  "The 1892 printing still numbers it 48a (raw OCR '485.', misread), so the segmenter folded it into Law 48. Same Law and wording.", ["S18"])
L("E020", "Law 48a listed as removed.", NC, "segmentation_artefact", "high", "derived",
  "Not removed: its text is still in the 1892 printing under the misread number '485.' (48a) and was merged into Law 48 by segmentation (see the relocation of the 'especial care' sentence in this pair).", ["S18"])
L("E021", "Law 5: bat width '4¼in.' becomes '4½ in.' in the processed texts.", NC, "cleaning_artefact_numeric", "high", "derived",
  "The 1892 raw OCR is illegible ('If in.'); the 1890, 1896 and 1900 printings and ACS 1889 (S35-02: 'four inches and one-quarter') all give 4¼ in., and Rait Kerr (ch.4) notes the bat width 'has remained at four and a quarter inches ever since 1771'. The ½ is an AI clean-up invention.",
  ["S17", "S16", "S35-02"], integrity="suspect")
L("E022", "Law 54 (declaration): 'On the last day of a match and in a one day match at any time, the in-side may declare their innings at any end' becomes 'On the last day of a match, or if a one- day match, at any time, the in-side shall be empowered to declare the innings at an end.'",
  NC, "format_artefact", "medium", "derived",
  "No MCC change between 1889 and 1894 (ACS S35-02/S35-03, Rait Kerr ch.6). The 1892 wording is the official 1889 wording as transcribed by ACS (S35-02: 'That on the last day of a match, or if a one day match, at any time, the in-side shall be empowered to declare the innings at an end'); the 1890 pocket printing paraphrased it and misprinted 'at an end' as 'at any end'. 'may declare' vs. 'shall be empowered to declare' grants the same permission.",
  ["S35-02", "S18"], note="Printing variant, not a semantic rewrite by MCC; flagged to the owner (no 'printing_variant' subtype exists).")
L("E023", "Law 6: bail length '4½in.' becomes '4⅚in.' in the processed texts.", NC, "cleaning_artefact_numeric", "high", "derived",
  "Raw OCR reads '4m.' (1890) and 'din,' (1892) - i.e. 4in.; ACS 1889 (S35-02) gives 'four inches' and a projection of 'half-an-inch'. Both fractions are AI clean-up inventions.",
  ["S17", "S35-02"], integrity="suspect")
L("E024", "Law 9: 'the batsmen from beating the ground ... nor the batsman or bowler' printed 'the batsman from beating ... nor the batsman nor bowler'.", NC, "ocr_noise", "medium", "derived",
  "Printing variants (each confirmed in raw OCR); same permission to beat the ground and use sawdust.", ["S18"], note=PRINT90)
