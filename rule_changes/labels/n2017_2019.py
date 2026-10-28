"""Labels for events added after the first labelling pass (authored against the pipeline output of the verification-fix run)."""
from _h import make
PAIR = "2017_2019"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
SW = "SEMANTIC_WORDING"
D19 = "MCC 2017 Code 2nd edition, in force 1 April 2019 (S04)."


def art(eid, what, why, sub="segmentation_artefact", conf="high"):
    L(eid, what, NC, sub, conf, "derived", why, ["S18"])


L("E002", "Appendix A.2: the 'Implements' and 'protective helmet' definitions (A.2.1, A.2.3) are re-segmented across units, and A.2.4 gains a sentence defining a fielder's equipment ('any external protective equipment that he/she is wearing').",
  UN, "no_cause_stated", "low", "none", "Mostly re-segmentation of Appendix A.2; the added fielder's-equipment sentence is not on MCC's list of 2019 changes (S04) and no source states a reason.", ["S04"], date=D19)
art("E004", "Appendix A.4: cross-reference notation 'See A4.2' corrected to 'See A.4.2', and a 'See A.4.1' pointer added to A.4.8.", "Cross-reference notation only; the definition is unchanged.", sub="format_artefact")
L("E013", "Law 11.2.2: cross-references 'See, however, 11.4, 11.6 and 11.7' corrected to '11.3, 11.5 and 11.6'.",
  ST, "clarification_umpire_workability", "high", "stated", "MCC: 'there was a slight error in the cross-references in Law 11. Law 11.2.2 currently makes reference to Laws 11.4, 11.6 and 11.7. It should be 11.3, 11.5 and 11.6.' This error has been fixed.", ["S04"], date=D19)
L("E014", "Law 11 (changing agreed times of intervals): a cross-reference number is updated (to 11.8).", ST, "consequential", "medium", "derived", "Only a Law-11 sub-clause cross-reference number changes.", ["S18"], date=D19)
L("E015", "Law 11 (lunch or tea interval, 9 wickets down): 'at a time up to and including...' becomes 'at any time up to and including...'.", ST, "wording_only", "medium", "derived", "One article becomes 'any'; the rule is unchanged in effect.", ["S18"], date=D19)
L("E020", "Law 16.7: 'the side batting last has lost all its wickets' becomes 'the innings of the side batting last has been completed' (win by Penalty runs).",
  ST, "clarification_umpire_workability", "high", "stated", "MCC: Law 16.7 'makes reference to a side losing all wickets. This is just one way an innings can be completed, and thus suggests that, if a side has players suspended/retired, they cannot win by Penalty runs.' The wording now refers to the innings being completed.", ["S04"], date=D19)
L("E021", "Law 17 (miscounted over): the umpire who allowed an over to continue after 6 valid balls 'may' subsequently call Over becomes 'must' subsequently call Over.",
  SW, "modal_strength", "low", "inferred", "A permissive 'may' becomes mandatory 'must' (strength word). Doubtful source text: the raw 2019 OCR reads 'he/she rr' and raw 2017 reads 'ma>', so the AI clean-up may have invented the modal; the change is not on MCC's list of 2019 changes (S04), and the 2026 4th edition reads 'shall'. Check against an MCC copy of the 2019 Laws before relying on it.", ["S04"], date=D19, integrity="suspect")
art("E025", "Law 18.11: cross-reference spacing ('18.11.2. 1') and a stray OCR fragment ('lawigTboundaries'); same rule.", "The only difference is spacing in a cross-reference and OCR garbage at the end of the sentence.", sub="ocr_noise")
art("E030", "Law 24: 'extratakes' (OCR) for 'either takes'; same rule.", "An OCR error in the old text.", sub="ocr_noise")
L("E033", "Law 26: 'any further contravention by any player of that team' becomes '... by a player of that team'; bullet punctuation changes.", ST, "wording_only", "medium", "derived", "One word changed ('any' to 'a'); the penalty for repeated contravention is unchanged.", ["S18"], date=D19)
L("E037", "Law 29.1.1.6: 'strikes or pulls a stump out of the ground in the same manner' becomes '... as in 29.1.1.5'.",
  ST, "clarification_umpire_workability", "high", "stated", "MCC: 'Law 29.1.1.6 in its previous form was slightly unclear, as it referred to Law 29.1.1.5 by saying \u2018in the same manner\u2019, when all of the above clauses are about how the wicket is put down.' The amendment makes clear that it refers back only to 29.1.1.5.", ["S04"], date=D19)
L("E041", "Law 30.1.2: the final proviso 'provided that the batsman has continued movement in the same direction' is removed.",
  ST, "clarification_umpire_workability", "high", "stated", "MCC: the previous Law 'contained a duplication of wording, which stemmed from an amendment to this Law in the 2017 changes'; the proviso 'was not felt to be necessary given the requirement to be \u201crunning or diving towards his/her ground and beyond\u201d'.", ["S04"], date=D19)
art("E052", "Law 41: the sentence 'the umpire shall' is cut off in the old text ('the ump'); same rule.", "An OCR truncation in the old text; the rule is the same.", sub="ocr_noise")
L("E054", "Law 41.7: 'The warning sequence in 41.7.1 and 41.7.2 is independent of the warning and action sequence in 41.6' becomes 'The warning and action sequences in 41.7.3 and 41.7.4 are independent of those in 41.6'.",
  ST, "consequential", "high", "stated", "Follows from the rework of Law 41.7 that MCC describes as handing 'more control to umpires to determine whether a delivery is dangerous' (S04).", ["S04"], date=D19)
L("E026", "Law 19: OCR errors in the 2019 text ('consider', 'cont^-\'', 'bal'); same rule.", NC, "ocr_noise", "high", "derived", "The only differences are mis-recognised words (OCR errors); the rule is identical.", ["S18"])
