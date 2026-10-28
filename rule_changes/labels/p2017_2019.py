"""Labels for the 2017 -> 2019 edition pair (2017 Code, 2nd edition effective 1 April 2019). MCC's own change list with an
explanation for each of the 22 changes is source S04 (also S14)."""
from _h import make
PAIR = "2017_2019"
L, LABELS = make(PAIR)
ST, UN, NC, EN, NE = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "ENJOYMENT", "NOVEL_EVENT"
D19 = "MCC 2017 Code 2nd edition, in force 1 April 2019 (S04)."


def art(eid, what, why, sub="segmentation_artefact", ev=None, conf="medium", integrity="ok", note=""):
    L(eid, what, NC, sub, conf, "derived", why, ev or ["S18"], integrity=integrity, note=note)


L("E001", "Appendix A: a definition of 'waist height' is added for the first time (A.6.7), alongside notation fixes and re-segmentation of Appendix A.",
  ST, "clarification_umpire_workability", "high", "stated",
  "MCC: 'at the behest of umpires, MCC has for the first time put into the Laws a definition of the waist – something that has long-since been a point of contention, particularly in the recreational game' (it supports the reworked Law 41.7 on full-pitch deliveries above waist height).",
  ["S04", "S14"], date=D19, note="The rest of the event (A.1-A.6 re-ordering) is segmentation.")
art("E002", "Appendix A.4: cross-reference notation 'A4.3' corrected to 'A.4.3' and the 'bowler's end' definition moved between units; no change of definition.",
    "The word-level differences are notation ('A4.3'->'A.4.3'), apostrophes and sentence boundaries; the definitions are present in both editions.")
art("E003", "Appendix A.5/A.6: notation fixes and re-segmentation (e.g. 'Each umpire will be bowler's end umpire and striker's end umpire in alternate overs' moved); no change of definition.",
    "The sentences concerned (including 'alternate overs') occur in both the 2017 and 2019 texts; only unit boundaries and cross-reference notation differ.")
art("E004", "Appendix A: the delivery-stride definition ('It starts when the bowler's back foot lands for that stride and ends when the front foot lands in the same stride') is in both editions; only its position in the text unit differs.",
    "The sentence occurs once in each of the 2017 and 2019 texts.")
art("E005", "Appendix A.12: the sentence about the loss of an attempted run not being a disallowance is attached to a different unit; no change of rule.",
    "Text-unit boundary shift; the sentence about batsmen not being returned to their original ends is in both texts.", conf="low")
art("E006", "Appendix B (bat): B.1.2 Adhesives and B.2 handle wording re-segmented; no change of specification.",
    "'Adhesives - Throughout...' and 'This lower portion is used purely for joining the blade and the handle together' occur once in each text.")
art("E007", "Appendix B (bat): B.1.2/B.3 re-segmented and trailing full stops dropped; no change of specification.",
    "The same clauses are present in both editions; differences are punctuation and unit boundaries.")
art("E008", "Appendix B: clause number 'B.4.1.' typed 'B.41.' in the 2019 text.", "A one-character typographical difference in a clause number.", sub="format_artefact", conf="high")
art("E009", "Appendix B: bat-covering thickness appears to change from 0.04 in. (0.1 cm) to 0.004 in. (0.1 cm): not real. 0.04 in = 0.1 cm.",
    "The 2019 text's '0.004 in/0.1 cm' is internally inconsistent (0.004 in is 0.01 cm); the 2017 text and MCC's own 2026 text both give 0.04 in/0.1 cm in total thickness.",
    sub="cleaning_artefact_numeric", ev=["S17", "S02"], conf="high", integrity="suspect")
art("E010", "Appendix B.7: 'coloured, providing Law 5.5 is not contravened' is split off from the laminated-blade clause; no change.",
    "The wording 'providing Law 5.5 is not contravened' still occurs in both editions.")
L("E015", "Law 15.1: the sentence 'A declared innings shall be considered to be a completed innings' is added.",
  ST, "codification_definition", "high", "stated", "MCC: a forfeited innings is already described as a completed innings and this is 'also true of a declared innings (importantly for Law 16), but the Law does not currently state it'.",
  ["S04"], date=D19)
L("E017", "Law 16.3.3 reworded: playing time is counted as lost from the call of Time to the call of Play, excluding intervals (Law 11) and suspensions of play (Law 2.8).",
  ST, "consequential", "high", "stated", "MCC: in writing Law 42.1.5 'some minor amendments were made to the procedure for adding time on. As this Law had borrowed from Law 16.3.3, it was felt that these amendments should be made in both Laws.'",
  ["S04"], date=D19)
art("E018", "Law 16: the heading 'Winning hit or extras' moves to the next clause; no change.", "Heading position only; the text is found elsewhere in both editions.", ev=["S18"])
L("E021", "Law 18.6 (Runs awarded for penalties): the list of Laws under which penalty runs are awarded/restricted is completed and put in Law order.",
  ST, "codification_definition", "high", "stated", "MCC: 'Law 18.6 makes reference to four occasions when an umpire must disallow runs. However, there are actually eight such occasions. All eight are now be included in this Law [sic], and they have been re-ordered to be in Laws order.'",
  ["S04"], date=D19)
art("E027", "Law 2/3: umpires' consultation and decision paragraphs appear under the other Law's heading in the 2019 text segmentation.", "The same paragraphs ('Umpire's decision An umpire may alter any decision provided that such alteration is made promptly') exist in both editions; the Law boundary in the digitised text moved.", conf="medium")
art("E028", "Law 20: the lead-in 'The ball becomes dead when' sits in a different unit; no change.", "Found elsewhere in the old edition.")
L("E029", "Law 21.6 (Bowler breaking wicket in delivering ball): the concept of 'attempting' to run out the non-striker is removed; it now reads 'If the ball is delivered and if the non-striker is not dismissed under Law 41.16 ...'.",
  ST, "consequential", "high", "stated", "MCC: 'The change to Law 41.16 ... which allows for an accidental run-out of the non-striker by the bowler, required a similar change to Law 21.6.'",
  ["S04"], date=D19, sec="EXTERNAL_FORCE", secsub="", note="The underlying reason for 41.16 is described by MCC as 'principally on the back of TV replays' of accidental run-outs of the non-striker.")
L("E030", "Law 21.12 (Revoking a call of No ball): Dead ball under Law 20.4.2.7 (deliberate distraction) no longer revokes a No ball call.",
  EN, "fairness_spirit", "high", "stated", "MCC: the 2017 Code revoked a No ball call if there was a deliberate attempt to distract the striker; 'It was felt that this was unfair and that the batting side should still get the run for the No ball.'",
  ["S04"], date=D19)
art("E032", "Law 25: a clause fragment ('that this occurred during the match') is attached to the next sentence; no change.", "Same words, different unit.")
art("E033", "Law 25.7: the heading 'Restriction on the striker's runner' moves into the clause; no change.", "Heading position only.")
art("E034", "Law 28.2: the sentence 'A fielder may field the ball with any part of his/her person (see Appendix A.12), except as in 28.2.1.2' appears in a different unit.", "The sentence is in both editions; only its unit differs.")
art("E035", "Law 28.2: the penalty paragraph ('In addition the umpire shall award 5 Penalty runs ...') moves between units; no change.", "Re-ordering of units around the same sentences.", conf="low")
art("E036", "Law 28.4: 'A fielder will be considered to be behind the popping crease unless the whole of his/her person ... is in front of this line' attached to the preceding sentence; no change.", "Same sentence, different unit boundary.")
art("E038", "Law 3: the scorers' Law is cut at a different place in the 2019 digitised text (umpire-decision and signals paragraphs fall under Law 2 or 3).", "The 4,089 characters 'removed' from Law 3 reappear under Law 2 in the other edition: a Law-boundary shift in the digitised text.", conf="medium")
art("E039", "Law 3 (The scorers): cross-references and 'Appointment of scorers' paragraph begin the Law in 2019's segmentation.", "Counterpart of E038: the Law boundary differs in the digitised text.", conf="medium")
art("E040", "Law 3: scorers' paragraphs (Correctness of scores; Appointment) re-ordered within the Law.", "Same paragraphs, moved.", conf="medium")
L("E043", "Law 34.3: new sentence 'The striker may guard his/her wicket even if the delivery is a No ball.'",
  EN, "fairness_spirit", "medium", "inferred", "MCC's stated reasons are instinctive defence and that the call of No ball may not have been heard; the text does not itself say 'fair'. MCC: the striker could not be out bowled off a No ball, so some questioned a lawful second strike; 'As the call of No ball may not have been heard by the striker (or indeed may not even have been made by the umpire), and as the defence may well be instinctive, it was felt that the striker should still be permitted to defend his/her wicket.'",
  ["S04"], date=D19)
L("E044", "Law 37.3 (Obstructing a ball from being caught): if the delivery is a No ball the striker is no longer necessarily out; the striker is out only if the delivery is not a No ball.",
  EN, "fairness_spirit", "medium", "inferred", "MCC's stated reason is consistency with 'cannot be out Caught off a No ball'; also new 37.3.3/37.3.4 (whoever causes the obstruction is out). MCC: as the striker cannot be out Caught off a No ball, 'it should not be the striker who is necessarily out in this scenario. As in 34.3, ... whether the batsmen knew it was a No ball is not deemed to be relevant.'",
  ["S04"], date=D19)
L("E047", "Law 39.3.1 (Stumped): the striker is protected only if he/she left the ground to avoid injury 'after having received the delivery'; the reference to Law 25.6.5 in 39.3.2 is corrected.",
  ST, "clarification_umpire_workability", "high", "stated", "MCC: the Law 'did not clarify that such avoidance of injury could only be a defence if it happened after receiving the delivery and not as a result of it' (e.g. falling out of the ground ducking a bouncer); 39.3.2 'incorrectly included a reference to Law 25.6.5'.",
  ["S04"], date=D19)
art("E048", "Law 4 (The ball): circumference limits read '8.81 m/22.4 cm ... 9 m/22.9 cm' in the 2017 text and '8.81 in ... 9 in' in the 2019 text: an OCR unit misread, not a rule change.",
    "A ball circumference in metres is impossible; the centimetre equivalents are identical in both texts. The raw OCR of both 2017 and 2019 reads 'm' for 'in'; the 2019 clean-up corrected it and the 2017 one did not. MCC's own text gives 8.81 in/22.4 cm (S02).", sub="cleaning_artefact_numeric", ev=["S17", "S02"], conf="high", integrity="suspect", note="Mechanism: OCR unit misread (raw reads 'm'), not an invented number.")
art("E049", "Law 4: junior-ball circumference limits (raw OCR '8.25 m', '8 88 m') read 'm' in the 2017 text and 'in' in the 2019 text: OCR unit misread.", "Same mechanism as E048; the raw 2019 OCR also has 'm'.", sub="cleaning_artefact_numeric", ev=["S17", "S02"], conf="high", integrity="suspect")
L("E050", "Law 41.2 'Unfair actions' rewritten to incorporate the whole of former Law 41.19; 41.19 is removed and the sentence telling umpires not to intervene when the Laws do not direct them to is dropped.",
  ST, "consolidation_merge", "high", "stated", "MCC: 'Law 41.19 has been removed from the Laws. It was also decided to remove the final sentence of Law 41.2 (stating that umpires should not intervene when the Laws do not direct them to) which was determined to be more umpire guidance than Laws.' 41.19 duplicated content after changes to 41.2.",
  ["S04"], date=D19)
art("E052", "Law 41: 'Neither batsman shall be dismissed from that delivery and the ball shall not count as one of the over' shown as added; it occurs in the same Law in both editions.", "The sentence occurs twice in each edition's text; the difference is where a line break fell.")
L("E053", "Law 41.7 (dangerous and unfair non-pitching deliveries) reworked: a delivery passing above waist height without pitching is 'unfair' (any speed); it is also 'dangerous' if the bowler's end umpire considers there is a risk of injury to the striker, judged with regard to speed, height, direction, the striker's skill and repetition, disregarding protective equipment.",
  EN, "fairness_spirit", "high", "stated", "MCC (S04): the 2017 rule was 'overly harsh, particularly on younger bowlers'; MCC wants a 'better and fairer Law, while still maintaining the core aim of improving player safety and enjoyment'; the first edition of the 2017 Code imposed stricter penalties than before for full tosses over waist height; 'MCC listened to significant feedback and has handed more control to umpires to determine whether a delivery is dangerous.'",
  ["S04", "S14"], date=D19, sec="EXTERNAL_FORCE", secsub="medical_safety")
L("E054", "Law 41.7: warning and action sequences renumbered/reworded (41.7.3 and 41.7.4 independent of 41.6; 'dangerous and' dropped from the deliberate non-pitching delivery clause).",
  ST, "consequential", "high", "stated", "Follows from the rework of Law 41.7, described by MCC in the same change.", ["S04"], date=D19)
L("E055", "Law 41.2/41.19: the removal of Law 41.19.1 (duplicated by the rewritten Law 41.2); the apparent move of the time-wasting paragraph is an alignment mismatch (41.9.3 stays in Law 41.9).",
  ST, "consolidation_merge", "medium", "stated", "Alignment artefact: the time-wasting paragraph (41.9.3) stays in Law 41.9 in both editions; the apparent 41.19-to-41.9.3 move is a mismatch. The real change here is the removal of 41.19.1, part of the rewrite of Law 41.2.", ["S04"], date=D19, integrity="suspect")
art("E056", "Law 41.15: the definition of the protected area is split across two text units ('5 ft/' then '1.52 m ...'); no change.", "The measurements (5 ft/1.52 m and 1 ft/30.48 cm) are identical in both editions.")
L("E057", "Law 41.16 (Non-striker leaving his ground early) rewritten: 'the bowler is permitted to attempt to run him/her out' becomes 'the non-striker is liable to be Run out', 'whether or not the ball is subsequently delivered', with new clauses 41.16.2 and 41.16.3; also the dropped last sentence of 41.2. The Law 41.15 records in this event are segmentation only.",
  ST, "clarification_umpire_workability", "high", "stated",
  "MCC (S04): 'This new change clarifies MCC's interpretation of the Law', made 'principally on the back of TV replays' of accidental run-outs of the non-striker by the bowler.",
  ["S04"], date=D19, sec="EXTERNAL_FORCE", secsub="", note="Event mixes the 41.16 rewrite with 41.15 segmentation records; the label describes the substantive part.")
L("E058", "Law 42.1.5 added: for each Level 1 to 4 offence, playing time lost between the call of Time and the call of Play is added on and the close of play extended.",
  EN, "fairness_spirit", "high", "stated", "MCC: as originally written Law 42.1 allowed no time to be added on if lost to umpires dealing with player behaviour, so 'a side could risk committing an offence under Law 42, knowing that the time taken out of the game to deal with it would work in their favour. It was felt that this was unfair'.",
  ["S04"], date=D19)
L("E060", "Law 42.4.2.3.1/42.4.2.3.2: the part-over sentence ('any balls remaining in the over ...') is inserted into 42.4.2.3.1, so it now appears twice in 2019 (once in 2017); MCC change 42.4.2.3.2.",
  ST, "clarification_umpire_workability", "high", "stated", "MCC (S04): 'There was a lack of clarity over the suspension of a player for 10 overs in a match limited by time.'", ["S04"], date=D19)
L("E061", "Law 42.7: if a batsman's runner is removed under Level 4, the batsman is removed only from the ongoing innings (not the whole match); a nominated player with a substitute or runner suffers the penalty for Level 3/4 offences by that substitute or runner.",
  EN, "fairness_spirit", "high", "stated", "MCC: the batting side were left 'two players down because of the actions of one player'; 'It was decided that this was unfair', so the batsman may play in later innings (not so for a substitute, who 'is the embodiment of the player he/she is replacing').",
  ["S04"], date=D19)
art("E062", "Law 5.6: 'any part of a glove worn on the batsman's hand holding the bat' appears in a different unit; no change.", "Same clause, different unit.", ev=["S18"])
