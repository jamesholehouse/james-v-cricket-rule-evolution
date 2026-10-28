"""Labels for 1906 -> 1908. Both Lacey annotated editions; the official Laws did not change between them (ACS has no 1908
revision: 1906 then 1910). All events are Notes or noise."""
from _h import make
PAIR = "1906_1908"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"

NOTES_WHY = ("Rait Kerr (ch. 5): interpretations approved by the M.C.C. Committee were 'promulgated in the form of public "
             "pronouncements, instructions to umpires, or as Notes added to the Laws' in Lacey's annotated edition. That explains the "
             "Notes generally, not this one, so the reason is inferred.")
NOTES_DATE = "First appears in the 1908 text (a later Lacey annotated edition); no official Law change 1906-1910 (ACS)."

L("E001", "Single wicket Law 2: 'oft' -> 'off' (1906 OCR error corrected) plus a stray page number '16'. Same rule.",
  NC, "ocr_noise", "high", "derived", "Raw OCR 1906 'oft'; the word is 'off'. Page number is layout.", ["S18"])
L("E002", "Note on Law 11: '“NoBall.”' -> '“No Ball.”'. Same note.", NC, "ocr_noise", "high", "derived", "Spacing only.", ["S18"])
L("E003", "Note on Law 12 added: 'When a wide is called the ball does not become “dead” and the batsman may be out stumped or run out.'",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E004", "Note on Law 13 added: 'An over should always be finished, unless a wicket fall within two minutes of time (see Law 45), or "
  "unless there is a local rule extending the time.' The general UMPIRES note 'Umpires should not call “Time” before the Over is "
  "finished unless a wicket fall within two minutes of “Time.”' (present since 1902) remains; the new Note adds the local-rule exception.",
  ST, "notes_revision", "medium", "inferred",
  NOTES_WHY + " This restates an existing umpires' note under Law 13 and adds 'or unless there is a local rule extending the time', "
  "acknowledging local playing conditions.", ["S16"], date=NOTES_DATE)
L("E005", "Notes on Law 16: cross-reference '(See Law 13 and Note.)' -> '(See Laws 13, 23, 23 and 32 and Notes.)'; Notes added: 'A "
  "Batsman cannot be stumped off a No Ball (Law 16).', the Laws distinguish wicket-keeper from fieldsmen and stumping from run out, and "
  "when a No Ball has been called the umpire decides whether the case is 'stumping' (Law 23) or 'run out' (Law 28).",
  ST, "clarification_umpire_workability", "high", "inferred",
  NOTES_WHY + " Law 16 already allowed no dismissal off a no-ball except run out (and Laws 26, 27, 29, 30); the Note spells out that "
  "stumping is excluded. The Law itself was reworded to say so on May 1st 1912 (Rait Kerr serial 120, 'destined to cause much "
  "difficulty in interpretation'), so this Note anticipates that change.", ["S16"], date=NOTES_DATE)
L("E006", "Note on Law 24: 'lbw' -> 'l b w'. Same note.", NC, "format_artefact", "high", "derived", "Abbreviation spacing only.", ["S18"])
L("E007", "Notes on Law 24: third l.b.w. consideration 'Was it part of the batsman's person which intercepted the ball?' -> 'Was it part "
  "of the batsman's person, other than the hand, which intercepted the ball?'; 'lbw' -> 'l b w'.",
  SW, "qualifier_scope", "medium", "inferred",
  "The qualifier 'other than the hand' narrows the Note's test: a ball stopped by the hand cannot give l.b.w. This is consistent with "
  "Law 22 treating the hand as part of the bat for catches, and the Law 24 wording itself is unchanged (ACS 1906, 1910: 'any part of "
  "his person'), so it changes how the Law is read/applied rather than the Law. No source gives a reason.",
  ["S18", "S36-05", "S36-06", "S16"], date=NOTES_DATE)
L("E008", "Law 28 and its Note: OCR errors in 1908 ('bis' for 'his', 'hall' for 'ball', 'nail' for 'ball'). Same text.",
  NC, "ocr_noise", "high", "derived", "Raw OCR 1908 has these misreadings; meaning unchanged.", ["S18"])
L("E009", "Notes on Law 32: OCR apostrophe removed ('Law' 22' -> 'Law 22'), page number moves; new Note: 'When a run has been made off a "
  "no-ball the no-ball should be scored although the ball has been caught.'",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E010", "Notes on Law 35: 'A bowler may run a Batsman out, without having delivered the ball, in anyway authorized by the Laws' and "
  "'He may have passed the bowling crease...' (two sentences in 1906, 'howling' OCR error) are one sentence in 1908. Same Note.",
  NC, "segmentation_artefact", "high", "derived", "Same words, split differently; 'howling' is an OCR error.", ["S18"])
L("E011", "Law 37: stray page number '13' dropped. Same rule.", NC, "format_artefact", "high", "derived", "Page number only.", ["S18"])
L("E012", "Notes on Law 39 added: 'The intention of this Law is that the injured striker's ground, when he has a substitute to run for "
  "him, is at the wicket keeper's end. He himself can only be run out at that end as provided for in the latter part of the Law.'",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
L("E013", "Notes on Law 45 added: 'The effect of this Law is that the Umpire shall decide whether the delay of the individual amounts to "
  "a refusal of the batting side to play. It provides a specific penalty in such a case but none for the individual.'",
  ST, "clarification_umpire_workability", "high", "inferred", NOTES_WHY, ["S16"], date=NOTES_DATE)
