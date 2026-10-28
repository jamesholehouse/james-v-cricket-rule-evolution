"""Labels for 1884 -> 1890.

Sources of the two texts: 1884 = W. J. Pile printing 'Passed by the Marylebone Cricket Club April 21, 1884' (54 numbered Laws,
umpire Laws numbered 48/49); 1890 = a pocket printing 'As revised by the Committee of the Marylebone Cricket Club, 1884 and 1889'
with several printer's variants ('no less', 'providing', 'struck by', 'bail cross', 'otherthrows', 'at any end') that the 1892
printing and the ACS transcription of the 1889 revision (S35-02) do not have. The only MCC changes in this interval are the
1 May 1889 amendments (Rait Kerr serials 108-110; ACS: 'The changes to the 1884 code were to Laws 13 and 14 and the addition of Law 54').
"""
from _h import make
PAIR = "1884_1890"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
EN, EC, NE = "ENJOYMENT", "ECONOMY", "NOVEL_EVENT"
D1889 = "Rait Kerr ch.6 dates the 1889 amendments to May 1st 1889; first printed edition in the dataset is 1890."
PRINT90 = "1890 text is a different printing (pocket edition, 'As revised ... 1884 and 1889'); the 1892 printing and ACS 1889 (S35-02) have the 1884 wording."

L("E001", "One-day matches Law 2: 'The match, when not played out, shall be decided by the first innings' becomes 'The match, unless played out, shall be decided by the first innings.'",
  SW, "clarifying_rewrite", "medium", "derived",
  "Same rule in other words ('when not' = 'unless'); the new wording persists in the 1892, 1896, 1900 and 1902 texts, so it is not a one-off misprint, but nothing in it changes when a one-day match is decided on first innings. No source mentions it (ACS S35-02 covers only the main Laws, not the one-day Laws).",
  ["S18", "S35-02"], date="Between the 1884 Pile printing and the 1890 printing; undated.")
L("E002", "One-day matches Law 3 ('Prior to the commencement of a match it may be agreed that the over consists of 5 or 6 balls') appears attached to Law 2 in 1890 ('consist' for 'consists').",
  NC, "segmentation_artefact", "high", "derived",
  "In the 1890 raw OCR the sentence follows Law 2 without its number '3.' (the printing ran the two together); the 1892 printing numbers it 3 again. Same rule; 'consist'/'consists' is a printing variant.",
  ["S18"], note=PRINT90)
L("E003", "One-day matches Law 3 (agreed 5- or 6-ball over) listed as removed.", NC, "segmentation_artefact", "high", "derived",
  "Not removed: the sentence is still in the 1890 text, run into one-day Law 2 because the printing omits the number '3.' (see the relocation of the same sentence in this pair); restored as Law 3 in 1892.",
  ["S18"], note=PRINT90)
L("E004", "Single wicket Law 1: '22 yards' printed as 'twenty-two yards'.", NC, "format_artefact", "high", "derived",
  "Numeral vs. words in a different printing; the distance is unchanged (the 1892 printing has '22 yards' again).", ["S18"], note=PRINT90)
L("E005", "Single wicket Law 2: bounds '22 yards' printed as 'twentytwo yards'.", NC, "format_artefact", "high", "derived",
  "Numeral vs. words in a different printing; unchanged distance (1892 has '22 yards').", ["S18"], note=PRINT90)
L("E006", "Single wicket Law 5: 'nor overthrows' printed 'nor otherthrows' (processed as 'other throws'); the 1884 text also carried a stray page marker 'xi.'.",
  NC, "ocr_noise", "high", "derived",
  "The 1890 raw OCR reads 'otherthrows' - a printer's misprint for 'overthrows' (1892 has 'overthrows' again); 'xi.' in 1884 is a page signature read into the text.",
  ["S18"], note=PRINT90)
L("E007", "Single wicket Law 7: 'turn before the ball cross the ground' printed 'turn before the bail cross the ground'.", NC, "ocr_noise", "high", "derived",
  "'bail' is in the 1890 raw OCR but makes no sense in the Law and reverts to 'ball' in 1892: a misprint (or OCR misread) in this printing, not a change.",
  ["S18"], note=PRINT90)
L("E008", "Law 1 cross-reference 'except in the case provided for in Law 54' becomes 'Law 53' (the follow-on Law).", NC, "format_artefact", "medium", "derived",
  "The follow-on Law is the same; its number differs because the 1884 Pile printing numbers the two no-ball umpire Laws 48 and 49 (54 Laws in all), whereas the ACS transcription of the 1884 Code (S35-01) numbers them 48A/48B with the follow-on as Law 53, as in 1890. A printing-numbering difference, not an MCC renumbering (the 1889 declaration Law was added as 54 after it).",
  ["S35-01", "S35-02"])
L("E009", "Law 10: 'No ball' printed 'No-ball' (and a stray page marker 'iii.' in 1884).", NC, "format_artefact", "high", "derived",
  "Hyphenation of the call and a page signature only; the throwing rule is unchanged.", ["S18"])
L("E010", "Law 11: 'No-Ball' printed 'No ball'; a comma dropped.", NC, "format_artefact", "high", "derived", "Hyphenation/punctuation only.", ["S18"])
L("E011", "Law 13: the over increased from four to five balls ('overs of four balls' -> 'overs of five balls'; 'When four balls have been bowled' -> 'When five balls ...'); third record only hyphenation of 'Wide-ball'.",
  EC, "time_saving", "high", "stated",
  "Rait Kerr serial 108 (May 1st 1889): 'The Over is increased from four balls to five.' Ch.4 ('Other measures adopted to assist the bowler'): the 1889 change of ends 'was off-set by another increasing the over from four to five balls; a further increase to six balls was made in 1900. These changes were designed to save time during play'. Ch.4 also records that an 1888 M.C.C. Committee proposal 'to even the balance between bowler and batsman' was referred back and 'completely accepted' when resubmitted the following year.",
  ["S16", "S35-02"], sec=EN, secsub="bowler_batsman_balance", date=D1889 + " ACS S35-02 confirms Law 13 changed in 1889.")
L("E012", "Law 14: 'The bowler may not change ends more than twice in the same innings nor bowl more than two overs in succession' becomes 'The bowler shall be allowed to change ends as often as he pleases, provided only that he does not bowl two overs consecutively in one innings.'",
  EN, "bowler_batsman_balance", "medium", "stated",
  "Rait Kerr serial 109 (May 1st 1889). Ch.4 lists it first under 'Other measures adopted to assist the bowler' ('The first change, made in 1889, permitted a bowler to change ends as often as he wished in any innings provided he did not bowl two overs in succession'), then says 'These changes were designed to save time during play' (that sentence may cover only the over-length changes, hence secondary time_saving). Background (ch.4): improved pitches made the bowler's lot the main concern of 1884-1947 legislation.",
  ["S16", "S35-02"], sec=EC, secsub="time_saving", date=D1889)
L("E013", "Law 16: 'no-ball' printed 'no ball'/'noball'; 'laws' capitalised.", NC, "format_artefact", "high", "derived", "Hyphenation/capitalisation only.", ["S18"])
L("E014", "Law 17 (Bye): 'no-ball' -> 'no ball', 'leg-bye' -> 'Leg bye', punctuation and capitals.", NC, "format_artefact", "high", "derived", "Hyphenation, quote and punctuation differences only.", ["S18"])
L("E015", "Law 22: the dismissal name '“Caught.”' is missing from the end of the 1890 processed text (and a page marker 'v.' from 1884).", NC, "segmentation_artefact", "high", "derived",
  "The 1890 raw OCR has '\" Caught.\"' on the following line; the segmenter split it off. Same Law.", ["S18"])
L("E016", "Law 23: 'provided it be not touched' printed 'providing it be not touched'; the dismissal name 'Stumped.' split off the 1890 text.",
  NC, "segmentation_artefact", "high", "derived",
  "'Stumped.' is in the 1890 raw OCR on the next line (segmentation); 'providing' is a printing variant of this pocket edition (1892 and ACS 1889 S35-02 read 'provided'). No change of rule.",
  ["S18", "S35-02"], note=PRINT90)
L("E017", "Law 27: 'if the ball be struck, or be stopped by any part of his person' printed 'or be struck by any part of his person'.", NC, "ocr_noise", "high", "derived",
  "'struck by' is in the 1890 raw OCR but is a misprint in this printing: the 1884 text, the 1892 printing and ACS 1889 (S35-02) all read 'be stopped by'. Not an MCC change.",
  ["S18", "S35-02"], note=PRINT90)
L("E018", "Law 35: 'No-Ball' -> 'No ball'; commas moved ('finally settled, in the', 'when the bowler, is').", NC, "format_artefact", "high", "derived", "Punctuation and hyphenation only.", ["S18"])
L("E019", "Law 4: 'The ball shall weigh not less than 5½oz.' printed 'shall weigh no less than 5½oz.'", NC, "ocr_noise", "high", "derived",
  "Printing variant of the 1890 pocket edition (raw OCR 'weigh no'); 1892 and ACS 1889 (S35-02) read 'not less'. Same limit.", ["S18", "S35-02"], note=PRINT90)
L("E021", "'Especial care' Law (call no ball on delivery, wide when past the striker) renumbered from 49 (1884 Pile printing) to 48A; 'No-ball' -> 'No ball'.", NC, "format_artefact", "high", "derived",
  "Same Law, same wording. ACS 1884 (S35-01) numbers the two no-ball umpire Laws 48A and 48B (this one 48B), so the 1884 Pile printing's 48/49 numbering and the 1890 printing's 48/48A are printing variants of one sub-numbered pair; hyphenation only otherwise.",
  ["S18", "S35-01"])
L("E022", "Law on changing umpires: cross-reference 'violation of Law 52' (no betting) becomes 'Law 51'.", NC, "format_artefact", "medium", "derived",
  "Same referenced Law (umpires not to bet); the number differs because the 1884 Pile printing counts the no-ball umpire Laws as 48 and 49, while the ACS transcription of the 1884 Code (S35-01) numbers them 48A/48B, making the betting Law 51 as in 1890.",
  ["S35-01", "S35-02"])
L("E023", "New Law 54: 'On the last day of a match and in a one day match at any time, the in-side may declare their innings at any end.' (first provision for declarations; 'at any end' is a misprint for 'at an end').",
  EN, "avoid_draws", "high", "stated",
  "Rait Kerr serial 110 (May 1st 1889): 'The batting side is allowed to declare its innings closed at any time on the last day of a match.' Ch.4 ('Legislation of a general nature'): the alterations to the 'follow on' and 'declaration' Laws 'were primarily directed towards reducing the number of drawn matches, which resulted from the huge scores following on the improvement of pitches and batting technique', and the inspiration for both 'can be traced to the desire to avoid the burlesque of batsmen knocking down their own wickets, or deliberately getting themselves out in other ways.'",
  ["S16", "S35-02"], sec="EXTERNAL_FORCE", secsub="pitch_technology", date=D1889 + " ACS S35-02: 'the addition of Law 54'.",
  note="The 1890 printing's wording ('may declare their innings at any end') differs from the official 1889 wording in ACS S35-02 ('the in-side shall be empowered to declare the innings at an end'), which the 1892 printing restores.")
L("E024", "Law 6: bail length '4¾in.' becomes '4½in.' in the processed texts (projection '¾in.' in both).", NC, "cleaning_artefact_numeric", "high", "derived",
  "Both raw OCR texts read 'The bails shall be each 4in. in length' (1884) / '4m. in length' (1890); ACS 1884 and 1889 (S35-01, S35-02) give 'four inches' and a projection of 'half-an-inch'. The fractions are AI clean-up inventions; no change.",
  ["S17", "S35-01", "S35-02"], integrity="suspect")
L("E025", "Law 9: 'This shall not prevent the batsman from beating the ground ... nor the batsman nor bowler' printed 'the batsmen from beating ... nor the batsman or bowler'.",
  NC, "ocr_noise", "medium", "derived",
  "Printing variants between the two printings (raw OCR confirms each); the permission (beating the ground, sawdust) is unchanged. ACS 1889 (S35-02) itself reads 'batsmen ... nor the batsman nor bowler', so 'batsman/batsmen' is a long-standing typographical wobble, not a rule change.",
  ["S18", "S35-02"], note=PRINT90)
