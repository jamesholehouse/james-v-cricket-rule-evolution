"""Labels for 1908 -> 1910. Official Law change (ACS): Law 54 (May 1910). Plus the M.C.C. covering advice of April 1910 as a Note."""
from _h import make
PAIR = "1908_1910"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
EN = "ENJOYMENT"

L("E013", "Law 54: three-day match declaration 'at or after the luncheon interval on the second day' -> 'at any time on the second day'.",
  EN, "avoid_draws", "medium", "stated",
  "Rait Kerr serial 119 (May 4th 1910): a declaration is allowed at any time on the second day of a three-day match. Ch. 5: the "
  "follow-on and declaration alterations of the period 'were primarily directed towards reducing the number of drawn matches' (stated "
  "for these Laws as a group, hence medium).",
  ["S16", "S36-06"], date="May 4th 1910 (Rait Kerr serial 119; ACS: 'The change in the 1910 revision was to Law 54').")
L("E014", "Notes on Law 9 added: 'Pending an alteration to this Law the M.C.C. have advised the County Cricket Clubs to concur in the "
  "following procedure to adopt any covering to protect the ground against rain at any time after 7 o'clock a.m. on the morning of the "
  "first day of a match.' The ground may be covered again after play starts and every night, removed each morning if fine at 7 a.m.; "
  "covering 'must not protect a larger area than 18ft by 12ft at each end, and must not protect more than 3ft 6in in front of the "
  "popping crease'. Law 9 itself still forbids covering during a match.",
  "EXTERNAL_FORCE", "pitch_technology", "low", "inferred",
  "Cricket (28 Apr 1910) reports that the M.C.C. Committee adopted, 'with certain verbal alterations', Surrey's proposal that county "
  "grounds cover the pitch ends against rain, but gives no reason beyond protecting the ground against rain. Rait Kerr does not discuss "
  "it. I infer the cause is protecting prepared pitches from weather (pitch-care practice), not a stated aim. It is a real relaxation "
  "of Law 9 for county cricket, issued as advice 'pending an alteration to this Law'.",
  ["S36-10", "S16"], date="M.C.C. Committee resolution reported 28 Apr 1910 (S36-10); first appears in the 1910 text. Numbers "
       "(7 a.m., 18ft by 12ft, 3ft 6in) match raw OCR and the Cricket report.",
  note="Text ends with stray characters '--2 7' (page layout).")
L("E002", "Note on Law 12: 'When a wide is called the ball does not become “dead”' -> 'does not on that account become “dead”'.",
  SW, "qualifier_scope", "medium", "derived",
  "'on that account' limits the Note: the call of wide does not itself make the ball dead, leaving room for it to become dead for other "
  "reasons (e.g. Law 33b, boundary). Clarifies reading; no rule change.", ["S18"])
L("E001", "Single wicket Law 2: 'When there shall be less than five players on a side, Bounds shall be placed...' segmented into two "
  "records, and the stray page number '16' dropped. Same rule.",
  NC, "segmentation_artefact", "high", "derived", "Same words split differently; page number is layout.", ["S18"])
L("E003", "Notes on Law 16 cross-reference: '(See Laws 13, 23, 23 and 32 and Notes.)' -> '(See Laws 13, 23, 28 and 32 and Notes.)'.",
  NC, "ocr_noise", "medium", "derived",
  "The 1908 '23, 23' (present in raw OCR) is a misprint or OCR misreading of '28' (run out), which the same Notes cite alongside "
  "Law 23; 1910 reads 28. No change.", ["S18"])
L("E004", "Notes on Law 16: 'If one run is attempted and the batsman is run out the “No Ball” alone counts' joined to the next sentence "
  "(missing full stop in 1910). Same notes.", NC, "segmentation_artefact", "high", "derived", "Same words, sentence split differs.", ["S18"])
L("E005", "Notes on Law 23: heading 'Notes on Law 23' joined to the first Note, page number '10' dropped, second Note split off. Same notes.",
  NC, "segmentation_artefact", "high", "derived", "Same words, segmentation and page number only.", ["S18"])
L("E006", "Note on Law 24: 'l b w' -> 'lbw'. Same note.", NC, "format_artefact", "high", "derived", "Abbreviation spacing only.", ["S18"])
L("E007", "Note on Law 24: 'an l b w' -> 'an lbw'. Same note.", NC, "format_artefact", "high", "derived", "Abbreviation spacing only.", ["S18"])
L("E008", "Law 28 and Note: 1908 OCR errors ('bis', 'hall', 'nail') corrected. Same text.", NC, "ocr_noise", "high", "derived",
  "Raw OCR 1908 has these misreadings.", ["S18"])
L("E010", "Note on Law 32: stray page number '12' dropped. Same note.", NC, "format_artefact", "high", "derived", "Page number only.", ["S18"])
L("E012", "Note on Law 50: stray page number '15' dropped. Same note.", NC, "format_artefact", "high", "derived", "Page number only.", ["S18"])
