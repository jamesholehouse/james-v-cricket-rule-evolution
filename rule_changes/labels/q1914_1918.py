"""Labels for 1914 -> 1918. Every event is OCR/segmentation noise: the ACS records no revision between 1914 (Law 55) and
1919 (S37-03, S37-04), the 1918 edition predates the May 1919 change, and the Notes compared below have the same wording."""
from _h import make
PAIR = "1914_1918"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
NOREV = "No Law revision between 1914 and 1919 (S37-03, S37-04)."

L("E001", "Single-wicket Law 2: 'oft' (1914 OCR) back to 'off'.", NC, "ocr_noise", "high", "derived", "OCR misreading.", ["S18"])
L("E002", "Single-wicket Law 4: 'popping' read as 'poppin\"' and 'run shall' as 'run-shall' in 1918.", NC, "ocr_noise", "high", "derived", "OCR misreadings.", ["S18"])
L("E003", "Notes on Law 13: the sentence split at '(see. Law 45)' rejoined; page number '8' gone.", NC, "segmentation_artefact", "high", "derived", "Same words; record boundaries and page number differ.", ["S17", "S18"])
L("E004", "Law 16: 'No Bail' / 'be’scored' (1914 OCR) back to 'No Ball' / 'be scored'.", NC, "ocr_noise", "high", "derived", "OCR misreadings. " + NOREV, ["S18", "S37-04"])
L("E006", "Law 2 enumerated clauses ('A run is scored: 1st ... 2nd ...') segmented differently.", NC, "segmentation_artefact", "high", "derived", "Same words.", ["S18"])
L("E007", "Notes on Law 23: the heading 'Notes on Law 23' no longer attached to the first Note.", NC, "segmentation_artefact", "high", "derived", "Heading/record boundary only.", ["S18"])
L("E008", "Note on Law 24: 'lbw' read as '1 b w'.", NC, "ocr_noise", "high", "derived", "OCR read 'l' as '1'.", ["S17", "S18"])
L("E009", "Note on Law 24: 'an lbw' read as 'an 1 b w'.", NC, "ocr_noise", "high", "derived", "OCR read 'l' as '1'.", ["S17", "S18"])
L("E010", "Note on Law 25: 'See' read as 'Sec'.", NC, "ocr_noise", "high", "derived", "OCR misreading.", ["S18"])
L("E012", "Note on Law 32: page number '12' gone, a stray '(' appears.", NC, "format_artefact", "high", "derived", "Page number and stray character only.", ["S17", "S18"])
L("E013", "Law 33b: 'Bail' (1914 OCR) back to 'Ball'.", NC, "ocr_noise", "high", "derived", "OCR misreading.", ["S18"])
L("E014", "Notes on Law 35: 'any way'/'anyway', 'in his run, may change' / 'in his run or may change', 'throwing' read as 'th owing'.", NC, "ocr_noise", "high", "derived",
  "Raw 1914 l.409 reads 'in his run may change' (the 'or' lost in a damaged scan line, cf. 1913 raw 'in his inn or may'); the rest is spacing and OCR. Same Note.", ["S18"])
L("E015", "Law 37: page number '13' gone.", NC, "format_artefact", "high", "derived", "Page number only.", ["S17", "S18"])
L("E016", "Law 42: first sentence 'The Wicket-keeper shall stand behind the wicket.' merged into the next sentence (full stop missing in 1918).", NC, "segmentation_artefact", "high", "derived",
  "Raw 1918 l.468 reads 'behind the wicket If he' (no full stop), so the segmenter merged two sentences; words identical.", ["S18"])
L("E017", "Law 43: page number '14' gone.", NC, "format_artefact", "high", "derived", "Page number only.", ["S17", "S18"])
L("E018", "Note on Law 45: 'out coming' vs 'out-coming'.", NC, "format_artefact", "high", "derived", "Hyphenation only.", ["S18"])
L("E019", "Law 50: page number '15' gone.", NC, "format_artefact", "high", "derived", "Page number only.", ["S17", "S18"])
L("E020", "Note on Law 54: 'preclude' read as 'prechide'.", NC, "ocr_noise", "high", "derived", "OCR misreading.", ["S18"])
