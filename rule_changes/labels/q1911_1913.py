"""Labels for 1911 -> 1913. Evidence: Rait Kerr (S16; serial 120, 1 May 1912), ACS 1912 Law text (S37-02; Laws only),
raw OCR of both editions, project checks (S17, S18). There is no 1912 edition in the dataset, so the May 1912 Law 28
amendment first appears in the 1913 text."""
from _h import make
PAIR = "1911_1913"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"

L("E001", "Single-wicket Law 2: a trailing '16' (page number) appears in the 1913 text.", NC, "format_artefact", "high", "derived",
  "Page number picked up by OCR at a page break; the wording is identical.", ["S17", "S18"])
L("E002", "Law 10: 'either Umpires shall call “No Ball.”' becomes 'either Umpire shall call “No-ball.”'",
  ST, "wording_only", "high", "derived",
  "Raw OCR confirms 'either Umpires' in 1910/1911 and 'either Umpire' in 1913: a printer's grammatical correction plus hyphenation of 'No-ball'. Who may call a throw (either umpire) is unchanged.",
  ["S18"])
L("E003", "Law 11: '“No Ball”' printed '“No-Ball”'.", NC, "format_artefact", "high", "derived", "Hyphenation only.", ["S18"])
L("E004", "New Note on Law 11: 'The Umpire in this law refers to the Umpire at the bowlers wicket.'",
  ST, "clarification_umpire_workability", "medium", "inferred",
  "Genuine new Note (absent from 1911 raw, present in 1913 raw l.168). Law 10 lets 'either Umpire' call a throw; the Note makes clear that a foot-fault No-ball under Law 11 is called by the bowler's-end umpire only. Inferred from the text; no source gives a reason (nothing in Rait Kerr, S16).",
  ["S16", "S18"], date="First printed in the 1913 edition.")
L("E005", "Law 13: '“No Ball”' printed '“No-Ball”'.", NC, "format_artefact", "high", "derived", "Hyphenation only.", ["S18"])
L("E006", "Note on Law 19 removed: 'If the batsman is in the act of jumping in the air and the bat is also off the ground he would be “out of his ground.”'",
  UN, "no_cause_stated", "medium", "none",
  "Genuine removal: the sentence is in the 1908, 1910 and 1911 raw texts and absent from the 1913 raw Notes on Law 19 (which keep the two foot-on-the-line sentences) and from every later edition. The Law itself ('grounded within the line') still implies the same result, so the removal may be tidying, but no source says so; Rait Kerr (S16) has nothing on it.",
  ["S16", "S18"], date="Present in 1911, absent in 1913 (raw OCR of both).")
L("E007", "Heading 'Either Batsman is Out—' (1911) / 'Either Batsman is Out-' (1913) treated as a new provision.", NC, "segmentation_artefact", "high", "derived",
  "The heading is present in both editions' raw text; only the dash differs, so the segmenter failed to match it.", ["S18"])
L("E008", "Law 28 (Run out) gains a proviso: 'But the Striker may not be out thus, unless the ball has touched the bat or hand, when, in playing at a No-ball he be out of his ground and the wicket be put down by the wicket-keeper with the ball, or with hand or arm with ball in hand.'",
  UN, "no_cause_stated", "high", "none",
  "Rait Kerr serial 120 (1 May 1912): 'The striker cannot be out stumped off a “No ball,” but may be run out—this change was destined to cause much difficulty in interpretation' (S16); the ACS says the 1912 revision's only change was this Law 28 proviso (S37-02). Neither gives a reason; Rait Kerr (ch.5) says only that an enquiry about a run out off a No ball 'arising from an obscure amendment' led to the 1947 Code, and serial 136 (1947) reverted the Laws to remove the difficulty.",
  ["S16", "S37-02"], date="Adopted 1 May 1912 (S16 serial 120; ACS 1912 revision S37-02); first visible in the 1913 edition (no 1912 edition in the dataset).")
L("E009", "Note on Law 32: 'oft’' read correctly as 'off'; a page number '12' appended.", NC, "ocr_noise", "high", "derived", "OCR misreading of 'off' in 1911 and a page number in 1913.", ["S17", "S18"])
L("E010", "Law 34: 'boon' read correctly as 'been'.", NC, "ocr_noise", "high", "derived", "OCR misreading in 1911.", ["S18"])
L("E011", "Note on Law 35: 'oft’' read correctly as 'off'.", NC, "ocr_noise", "high", "derived", "OCR misreading in 1911.", ["S18"])
L("E012", "Law 37: final full stop and a page number '13' appear in 1913.", NC, "format_artefact", "high", "derived", "Punctuation and a page number only.", ["S17", "S18"])
L("E013", "Note on Law 39 (runners): 'When the injured Batsman is not the Striker he is subject to no penalty under this Law' becomes '... he is subject only to such penalty under this Law as is incurred by his runner.'",
  UN, "no_cause_stated", "high", "none",
  "A genuine reversal of the ruling in the Note (raw 1911 l.420-421 'subject to no penalty'; raw 1913 l.457-458 'subject only to such penalty ... as is incurred by his runner'): an injured non-striker can now suffer the consequence of his runner being out of his ground. The Law 39 text itself is unchanged. No source gives a reason; not in Rait Kerr's chronology (S16).",
  ["S16", "S18"], date="Present from the 1913 edition (between 1911 and 1913 printings).")
L("E014", "Law 50: a page number '15' appended in 1913.", NC, "format_artefact", "high", "derived", "Page number only.", ["S17", "S18"])
L("E015", "Law 6: 'to prevent the ball from passing through' read as 'bail' in 1913.", NC, "ocr_noise", "high", "derived",
  "Raw 1913 OCR has 'bail' (misreading); ACS Law 6 reads 'ball' in every revision (S37-02) and 1914 reads 'ball' again.", ["S18", "S37-02"])
