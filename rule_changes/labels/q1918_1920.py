"""Labels for 1918 -> 1920. Evidence: Rait Kerr (S16; serial 121, second date 7 May 1919), ACS 1919 Law text (S37-04;
Laws only), 1919 two-day County Championship context (S37-06), raw OCR, project checks (S17, S18).
The 1920 OCR is poor ('howler', 'hall', 'he' for 'be'); most events are noise."""
from _h import make
PAIR = "1918_1920"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"

def ocr(e, what):
    L(e, what, NC, "ocr_noise", "high", "derived", "OCR misreading(s) in one edition; same wording otherwise.", ["S18"])

ocr("E001", "Single-wicket Law 1: 'Law 6' read as 'Law G' in 1920.")
ocr("E002", "Single-wicket Law 2: 'off' read as 'oft' in 1920.")
ocr("E003", "Single-wicket Law 3: 'to'/'be' read as 'io'/'he' in 1920.")
ocr("E004", "Single-wicket Law 4: 'poppin\"'/'run-shall' (1918 OCR) vs 'popping'/'run shall he' (1920 OCR).")
ocr("E005", "Single-wicket Law 8: 'lost ball' read as 'lost hall' in 1920.")
L("E006", "Notes on Law 11: 'A bowler may bowl' read as '/V howler may howl', 'act' as 'net', and the heading 'Notes on Law 11.' attached to the first Note in 1920.",
  NC, "ocr_noise", "high", "derived", "OCR misreadings plus a heading merged into the record; same Notes.", ["S18"])
ocr("E007", "Note on Law 11: 'part' read as 'jwirt' (and 1918 'ciease' as 'crease').")
ocr("E008", "Notes on Law 12: 'run' read as 'rim', 'not on' as 'noton' in 1920.")
ocr("E009", "Note on Law 13: 'be'/'time' read as 'he'/'lime' in 1920.")
ocr("E010", "Note on Law 16: 'clearly' read as ', dearly' in 1920.")
ocr("E011", "Note on Law 16: 'off' read as 'oft’' in 1920.")
L("E012", "Note on Law 18 (1911 trial-balls agreement): heading attached, 'In'/'be' read as 'lu'/'bo', and its two sentences merged in 1920.",
  NC, "segmentation_artefact", "high", "derived", "Same Note; heading merge, sentence merge and OCR only.", ["S18"])
ocr("E014", "Notes on Law 22: 'Law 32' read as 'Law !J2', 'ball' as 'hall' in 1920.")
L("E015", "Notes on Law 23: heading attached; '“Run Out.”' cut off and the 'one bail' Note split off; 'off' read as 'oft' in 1920.",
  NC, "segmentation_artefact", "high", "derived", "Same Notes; record boundaries and OCR only (raw 1920 l.94 area).", ["S17", "S18"])
ocr("E016", "Note on Law 25: 'Sec' (1918 OCR) vs 'See'.")
L("E017", "Law 27 and Notes: 'it'/'be'/'take'/'If'/'See' misread, a stray '5' for ';', and a heading fragment 'Either Batsman is' as a new record in 1920.",
  NC, "ocr_noise", "high", "derived", "OCR misreadings; the heading 'Either Batsman is Out-' is present in raw 1920 l.349, so the fragment is a segmentation artefact.", ["S17", "S18"])
L("E019", "Note on Law 32: stray '(' gone, page number '12' appended.", NC, "format_artefact", "high", "derived", "Punctuation and page number only.", ["S17", "S18"])
L("E021", "Notes on Law 35: two sentences ('... authorized by the Laws. He may have passed ...') joined as '... authorized by the Laws, i.e. he may have passed ...' in the 1920 processed text.",
  NC, "ocr_noise", "high", "derived",
  "Raw 1920 l.421 reads 'authorized by the Laws, l ie may have passed', an OCR garble of '. He may'; the clean-up invented 'i.e.'. 1918 and 1923 raw both read 'Laws. He may'. Same Note.", ["S18"])
L("E022", "Law 37: page number '13' appended.", NC, "format_artefact", "high", "derived", "Page number only.", ["S17", "S18"])
L("E025", "Law 43 cross-reference '(See also Instructions to Umpires.)' becomes '(See “Umpires”.)' (with a page number '11').",
  ST, "wording_only", "high", "derived",
  "Raw 1920 l.482 confirms. All cross-references in the 1920 edition now point to the section headed 'UMPIRES.' (the heading itself is 'UMPIRES.' in both 1918 and 1920 raw); the instructions are unchanged in substance. Re-labelling of a cross-reference.",
  ["S18"])
L("E026", "Law 50: page number '15' appended.", NC, "format_artefact", "high", "derived", "Page number only.", ["S17", "S18"])
L("E027", "Note on Law 54: '(See also Instructions to Umpires as to “declaring.”)' becomes '(See also under Umpires as to “declaring.”)'; 'prechide' (1918 OCR) back to 'preclude'.",
  ST, "wording_only", "high", "derived", "Same cross-reference re-labelling as for Law 43 in this edition, plus an OCR fix.", ["S18"])
L("E028", "Law 55 amended: new sentence 'Where there is no play on the first day of a two-day match, Law ‘one day matches’ shall apply as if the match were a one-day match'; in the three-day clause 'Laws 53, 54 and Law 1' becomes 'Law 54 and Law 1' (raw); typo 'there in' corrected to 'there is'.",
  "ENJOYMENT", "avoid_draws", "medium", "inferred",
  "Rait Kerr serial 121 is dated 'May 6th 1914 and May 7th 1919' (S16); the ACS says the 1919 revision's only change was the two-day sentence in Law 55 (S37-04). Rait Kerr says the follow-on and declaration Laws were 'primarily directed towards reducing the number of drawn matches' (S16, ch.4) - stated for that family of Laws, so the cause here is inferred. Context: in February 1919 the counties restricted Championship matches to two days (S37-06), which made a two-day weather rule immediately relevant, but no source links the two.",
  ["S16", "S37-04", "S37-06"], sec=ST, secsub="consequential",
  date="Adopted 7 May 1919 (S16 serial 121; S37-04); first in the 1920 edition.",
  note="Raw 1920 l.553 reads 'Law 54 and Law 1' in the three-day clause, whereas the ACS 1919-1927 texts keep 'Laws 53, 54 and Law 1': a printing difference not confirmed independently. The processed 1920 text dropped the '1' of 'Law 1' (raw has it): a clean-up artefact.")
L("E029", "Notes on Law 9: 'The ground in this law means “the pitch.”' and the covering-size sentence merged into the preceding sentences; '6in' read as 'Gin' in 1920.",
  NC, "segmentation_artefact", "high", "derived", "Same Notes; raw 1920 l.139 has 'Gin' (OCR for '6in'; 1923 raw has '6in'). Record boundaries and OCR only.", ["S17", "S18"])
