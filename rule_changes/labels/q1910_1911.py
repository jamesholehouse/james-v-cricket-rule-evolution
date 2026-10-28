"""Labels for 1910 -> 1911. Evidence: Rait Kerr (S16), ACS 1910/1912 Law texts (S37-01, S37-02; Laws only, no Notes),
raw OCR of both editions, project checks (S17, S18). No Law (as opposed to Note) changed between these editions: the ACS
records no revision between 1910 (Law 54) and 1912 (Law 28)."""
from _h import make
PAIR = "1910_1911"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"

L("E001", "Single-wicket Law 2: 'When there shall be less than five players on a side, Bounds shall be placed ...' is one sentence in both editions; the 1910 printing/OCR has a full stop after 'side' ('on a side. Bounds'), so the clause was split into two records.",
  NC, "segmentation_artefact", "high", "derived", "Raw 1910 OCR reads 'less than five players on a side. Bounds shall be'; 1911 raw reads 'on a side, Bounds shall be'. Same words; only the sentence split differs.", ["S18"])
L("E003", "New Note on Law 18 (trial balls): 'In 1911 an agreement was arrived at between the Counties that “Trial balls, if both batsmen are at the wickets, be not allowed in First Class Matches.” This arrangement was approved and adopted by the M.C.C.'",
  UN, "no_cause_stated", "medium", "none", "A genuine new Note (absent from 1910 raw, present in 1911 raw). The Note itself records the origin (an agreement of the Counties adopted by MCC); a contemporary cable report says it was Surrey's proposal adopted by the Advisory County Cricket Committee (S37-07), but no source seen gives the reason. Searched Rait Kerr's chronology and chapters (S16; nothing for 1911 on trial balls, serial 84 concerns 1838) and the web.",
  ["S16", "S37-07"], date="County agreement 1911 (stated in the Note); Advisory County Cricket Committee meeting reported 25 Feb 1911 (S37-07); first printed in the 1911 edition.",
  note="Not part of the Law text (ACS 1910/1912 Law 18 unchanged), a first-class playing regulation printed as a Note.")
L("E005", "Note on Law 24: 'lbw' printed as 'l b w'.", NC, "format_artefact", "high", "derived",
  "Abbreviation spacing/punctuation only (the editions print 'l.b.w.' variants); the words are the same.", ["S18"])
L("E006", "Note on Law 24: 'an lbw' printed as 'an l b w'.", NC, "format_artefact", "high", "derived",
  "Abbreviation spacing/punctuation only; same wording.", ["S18"])
L("E007", "Law 27: a trailing '11' (page number/footnote marker carried into the 1910 text) is absent in 1911.", NC, "format_artefact", "high", "derived",
  "The digit is a page number picked up by OCR at a page break, not part of the Law; the Law wording is identical.", ["S17", "S18"])
L("E008", "Note on Law 28: 1910 'unless the bail had been touched' vs 1911 'unless the ball had been touched'.", NC, "ocr_noise", "high", "derived",
  "Raw 1910 OCR reads 'unless the nail had been', which the clean-up turned into 'bail'; 1911 raw reads 'ball'. OCR misreading of 'ball'.", ["S18"])
L("E009", "Note on Law 32: 'off a no-ball' read as 'oft’ a no-ball' in 1911.", NC, "ocr_noise", "high", "derived", "OCR misreading of 'off'.", ["S18"])
L("E010", "Law 34: 'have been run' read as 'have boon run' in 1911.", NC, "ocr_noise", "high", "derived", "OCR misreading of 'been'.", ["S18"])
L("E011", "Note on Law 35: 'knocking off the bails' read as 'knocking oft’ the bails' in 1911.", NC, "ocr_noise", "high", "derived", "OCR misreading of 'off'.", ["S18"])
L("E012", "New Note on Law 9: 'The responsibility of supervising the rolling of the pitch before play will, in the first place, rest with the Umpires.' (Also a stray page number '--2 7' removed from the covering paragraph.)",
  ST, "clarification_umpire_workability", "medium", "inferred",
  "Genuine new Note (absent from 1910 raw and processed text, present in 1911 raw l.111). It allocates a supervisory duty to the umpires for the existing 10-minute rolling right; read as a clarification of who enforces Law 9, inferred from the text. No source gives a reason (Rait Kerr's chronology has nothing on rolling between serials 102 and 126, S16). The page-number fragment is an OCR artefact.",
  ["S16", "S18"], sec=UN, secsub="no_cause_stated", date="First printed in the 1911 edition.")
