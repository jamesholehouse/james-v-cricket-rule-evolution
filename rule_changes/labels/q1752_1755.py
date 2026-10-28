"""Labels for 1752 -> 1755 (1744 code as printed in The New Universal Magazine, Nov 1752 -> the 1755 booklet printed for M. Read)."""
from _h import make
PAIR = "1752_1755"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"

L("E001",
  "Whole-code modernisation with no change of rule. Mostly capitalisation of nouns (1755 capitalises 'Wicket', 'Ball' and so on) and spelling "
  "('in' -> 'inn'). The wording changes are: the ball stops being 'she'/'her' and becomes 'it' ('though she be struck' -> 'tho' it be struck'; "
  "'before she touches ground' -> 'before it touches the Ground'); 'cast of a piece of money' -> 'Toss of a Piece of Money'; 'the either "
  "popping-crease' -> 'the other Popping-Crease'; 'then it's out' -> 'or else it's not out'; 'no person shall have the right to ask him' -> "
  "'no Person shall have any Right to question him'; 'which design must be determined by the umpires' -> 'the same must be determined by the "
  "Umpires'. 'awing the game' in 1752 is an OCR misreading of 'giving'. Measurements are the same (3 ft 10 in, 22 yards, 22 in stumps, "
  "6 in bail, 5-6 oz ball).",
  SW, "pronoun_gender", "high", "stated",
  "Rait Kerr (App. III) says the 1755 Laws 'are essentially the 1752 version in a slightly modernised form' and that the common code "
  "'had not varied materially since 1744'. In ch.1 he names, as signs of 'gradual modernisation', 'Ye' becoming 'The' and 'the ball "
  "ceasing to be referred to as \"She\" or \"Her\"'. This event shows exactly that. No Rait Kerr serial falls between 1744 and 1771 (serials "
  "1-21 are the 1744 baseline). The ACS transcription of 1755 matches the dataset's 1755 wording. The pronoun change has no effect on the "
  "rule; nor does 'question' for 'ask' (in both, no-one may challenge the umpire's no-ball call).",
  ["S16", "S31-01"], date="1752 printing of the 1744 code vs 1755 booklet (advertised 15 May 1755, Rait Kerr App. III)",
  note="1752 OCR also has 'awing' for 'giving'; capitalisation differences are format only")
L("E002",
  "'These laws are to the umpires jointly.' appears to be removed. It is still in the 1755 text, where it was printed together with the next "
  "sentence ('These Laws are to the Umpires jointly. ___ Each Umpire is the sole Judge...'). The segmenter treated it as part of that record.",
  NC, "segmentation_artefact", "high", "derived",
  "The sentence is in the 1755 processed text and in the ACS 1755 transcription, so the removal is a sentence-splitting artefact.",
  ["S18", "S31-01"])
