"""Labels for events added after the first labelling pass (authored against the pipeline output of the verification-fix run).
Evidence: MCC preface of the 4th edition (S01); NZC (S15) lists eight key changes and says MCC 'modernised the Laws to make them easier to
understand' in general terms, which is not a stated cause for any single edit, so wording-only labels carry basis 'inferred'."""
from _h import make
PAIR = "2008_2010"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"
D = "2000 Code 4th edition, effective 1 October 2010 (S01, S15)."


def wd(eid, what, sub="wording_only"):
    import re as _re
    if _re.search(r"'(will|must|may|shall|should)' becomes '(will|must|may|shall|should)'|'[^']*\bonly\b[^']*' becomes '[^']*\bonly\b", what):
        return L(eid, what, SW, "qualifier_scope" if _re.search(r"\bonly\b", what) else "modal_strength", "medium", "inferred",
                 "A strength word or qualifier changes or moves; the rule is probably unchanged in effect, but the wording may change how it is enforced. NZC's general remark that MCC 'modernised the Laws' (S15) is not a stated cause.", ["S15"], date=D)
    L(eid, what, ST, sub, "medium", "inferred", "NZC reports in general terms that for the 4th edition MCC 'modernised the Laws to make them easier to understand' (S15); that general remark is not a stated cause for this edit. Old and new text compared directly: the rule is unchanged in effect.", ["S15"], date=D)


def pol(eid, what, why="An amendment in the 4th edition of the 2000 Code; no source states a reason."):
    L(eid, what, UN, "no_cause_stated", "low", "none", why, ["S01"], date=D)


def art(eid, what, why, sub="segmentation_artefact", conf="high"):
    L(eid, what, NC, sub, conf, "derived", why, ["S18"])


wd("E001", "Appendix D (Before the toss): 'one day match' becomes 'one-day match' and 'on the day that match' becomes 'on the day the match'.")
L("E007", "Appendix E (bat), covering of blade: 'Grade C bats' becomes 'Type C bats'; the thickness unit '0.012 m/0.3 mm' (2008 raw OCR) is read '0.012 in/0.3mm' in 2010.", ST, "terminology", "medium", "inferred",
  "Grades are renamed Types; the 'm' to 'in' difference is an OCR unit misread in the 2008 text (0.012 m cannot equal 0.3 mm), not a rule change.", ["S01"], date=D, sec=NC, secsub="cleaning_artefact_numeric", integrity="suspect")
art("E009", "Preamble: the running title 'THE LAWS OF CRICKET' is dropped from the start of the unit; the Preamble text is unchanged.", "Only a heading unit differs.")
wd("E010", "Law 1: 'sides of more or less than eleven players' becomes 'sides of fewer than, or more than, eleven players'.")
pol("E015", "Law 14: a declaration may be made 'at any time during the innings' (previously 'at any time during a match'; 'the side batting' for 'the batting side'); a forfeiture may be made 'at any time before the commencement of that innings'.")
wd("E016", "Law 15: a 'Before the toss' heading unit appears in the Intervals section; no rule text is added.")
wd("E017", "Law 15 (interval between innings): 'to' becomes 'until'; 'will' becomes 'shall'; '10 minutes' becomes '10 minute interval'.")
pol("E019", "Law 15: when an interval between innings is already in progress 30 minutes before tea, play resumes after the 10 minute interval 'if conditions permit' (previously unconditionally).", "A conditional 'if conditions permit' is added; NZC lists ground, weather and light among the key changes (S15) but no source states the reason for this clause.")
wd("E022", "Law 16: 'The umpire at the bowler's end' becomes 'The bowler's end umpire'; 'to the scorers' for 'the scorers'.")
art("E026", "Law 3/17: a list marker '(i)' in the practice-on-the-field text is attributed to a different Law in the two texts; same text.", "The unit is identical in both editions; only the Law boundary of the digitised text moved.")
pol("E027", "Law 18 (Runs disallowed): the scoring of runs is 'subject to any provisions that may be applicable, for the disallowance of runs or for the non-award of penalties' (previously only 'any disallowance of runs provided for within the Laws').", "The caveat is extended to the non-award of penalties; no source states a reason.")
wd("E028", "Law 18: 'a striker taking stance in front of his popping crease' becomes 'a striker setting off for his first run from in front of his popping crease'; the short-run clause is re-ordered.")
art("E031", "Law 19: the cross-reference '(To inform captains and scorers)' gains 'See Law 3.4' and an adjacent 'See Law 3.4(ii)' is dropped; the same pointer.", "The same Law 3.4 pointer appears in both texts; only unit boundaries differ.", conf="medium")
wd("E032", "Law 19: 'that portion is to be removed' becomes 'that part shall be removed'; 'umpire at the bowler's end' becomes 'bowler's end umpire'; 'as soon as the ball becomes dead'.")
wd("E035", "Law 2: 'a player has been injured or become ill after the nomination' becomes 'a nominated player ... since the nomination'.")
wd("E036", "Law 2: the umpires' discretion to allow a substitute or runner is re-worded ('to allow, for other wholly acceptable reasons, a substitute fielder or a runner to act for a nominated player'); 'must leave the field' becomes 'shall leave'.")
pol("E037", "Law 2 (Restrictions on role of substitutes): the bar on a substitute acting 'as captain on the field of play' is dropped ('A substitute shall not be allowed to bat, bowl or act as wicket-keeper'); a pointer 'Note also Law 1.3(b)' is added.", "The substitute-as-captain bar is removed (the deputy-captain provision is in Law 1.3(b)); no source states a reason.")
wd("E042", "Law 2: 'he may only resume his innings' becomes 'he may resume his innings only'.")
wd("E046", "Law 21: the conditions on runs completed before a catch (or the obstruction of a catch) and on a win by Penalty runs are re-worded ('If, without having scored a total of runs in excess of the total scored by the opposing side, the side batting last has lost all its wickets, but ...').")
L("E048", "Law 22: a 'Validity of balls' heading is added, and the 'ball shall not count as one of the 6 balls' sentence cross-refers to Law 42.15 (Bowler attempting to run out non-striker before delivery).", ST, "clarification_umpire_workability", "low", "inferred", "A cross-reference to the non-striker run-out Law is added to the validity-of-balls sentence; the rule that a ball not delivered does not count is unchanged. No source states a reason.", ["S01"], date=D)
wd("E049", "Law 22: 'Note also the special provisions of Law 23.4(b)(v)' is added as a cross-reference.", "consequential")
wd("E057", "Law 24 (No ball): penalty wording is tidied ('any other penalties awarded' becomes 'any other runs awarded for penalties'; 'The one run penalty for a No ball' becomes 'The one run penalty'; 'a 5 run penalty' becomes '5 penalty runs').")
pol("E058", "Law 25 (Wide ball): the judging test is re-worded: the ball passes wide of the striker 'where he is and which also would have passed wide of him standing in a normal guard position' (previously 'where he is standing and would also have passed wide of him standing in a normal guard position'); it may change how a borderline wide is judged.", "Re-worded wide test; no source states a reason.")
wd("E061", "Law 27: 'unless appealed to by the fielding side' becomes 'unless appealed to by a fielder'.")
pol("E064", "Law 28 (The wicket is put down): the list is rewritten: by the ball, or (ii) by the striker's bat if he is holding it or any part of it he is holding, or (iii) notwithstanding Law 6.8(a), by the striker's bat in falling if he has let go of it, or by a part of the bat becoming detached, etc.", "The conditions under which the striker's bat (or a detached part) puts the wicket down are restated with a Law 6.8(a) exception; no source states a reason.")
pol("E066", "Law 29: new 'Notwithstanding (a) above' proviso: if a running batsman, having grounded some part of his foot behind the popping crease, continues running towards the wicket at that end and beyond, any subsequent total loss of contact with the ground is ignored (heading 'When out of his ground' re-segmented).", "A new protection for a running batsman; no source states a reason.")
art("E068", "Law 3: the list items '(i) the wickets are properly pitched' and the closing 'above.' of the scorers' agreement clause are re-segmented; no change.", "The same words occur in both editions; only unit boundaries differ.", conf="medium")
pol("E070", "Law 3: the sentence 'If they do so agree, then they shall implement the procedure in (b) or (d) above ... whether or not there had been any decision by the captains to continue, or any appeal against the conditions' is removed, and a new 'Informing the umpires' paragraph is added (it is sufficient for one umpire to be informed and to inform the other).", "The ground/weather/light procedure is simplified and a general 'Informing the umpires' rule is added; NZC lists ground, weather and light among the key changes (S15) but states no reason.")
pol("E072", "Law 3 (Signals): all signals are made by the bowler's end umpire except Short run (signalled by the umpire at the end where short running occurs); the bowler's end umpire reports the final Short run signal and number of runs to the scorers; 'throughout the match' is added to the umpires' duty on scores; the Boundary 6 signal line is no longer in this unit (it may be re-segmented).", "New allocation of signalling duties; no source states a reason.")
wd("E076", "Law 32 (No runs to be scored): 'any penalties awarded to either side when the ball is dead, if applicable, will stand' becomes 'any runs for penalties awarded to either side shall stand'; the cross-reference 'Law 18.12(a)' becomes 'Law 18.12'.")
wd("E078", "Law 34 (Not out Hit the ball twice): 'makes a second or subsequent stroke ... to any member of the fielding side' becomes 'strikes the ball a second or subsequent time ... to any fielder'.")
pol("E079", "Law 34 (Ball lawfully struck more than once): the clauses are restated ('a second or subsequent time' for 'more than once'; 'attempted to avoid being hit' for 'tried to avoid'; 'Runs scored' for 'Runs permitted'; the batting side 'shall be credited with ...' penalties); whether the credit of penalties changes is not established here.", "Several sentences are re-worded; no source states a reason, and the old and new penalty-credit wording was only compared in part.")
art("E081", "Law 34: 'The batsmen shall return to their original ends.' appears at the start of the next clause in the 2010 text; same rule.", "The sentence is at the end of the preceding unit in the 2008 text; only unit boundaries differ.", conf="medium")
wd("E083", "Law 35 (Hit wicket): 'while he is trying to avoid a throw-in' becomes 'when he is trying to avoid a throw in'.")
wd("E084", "Law 36 (LBW): the condition on the point of impact is re-ordered ('(ii) if the striker has made no genuine attempt to play the ball with his bat, is either between wicket and wicket or outside the line of the off stump'); same rule.")
wd("E089", "Law 39 (Stumped): 'any part of his person or equipment' becomes 'any part of the wicket-keeper's person or equipment'; 'any member of the fielding side' becomes 'any fielder'.")
wd("E092", "Law 40: 'the umpire at the striker's end' becomes 'the striker's end umpire'.")
pol("E093", "Law 40: wilful interference by the wicket-keeper: 'the umpire concerned considers' becomes 'either umpire considers', and Law 42.4 'shall also apply' (previously 'shall apply').", "Either umpire (not only the umpire concerned) may judge the interference wilful; no source states a reason.")
wd("E095", "Law 42: 'shall call and signal Dead ball' loses a repeated 'shall'; 'the umpires shall not interfere' becomes 'umpires shall not interfere with the progress of play without appeal'.")
pol("E100", "Law 42: the 5 'penalty extras' become '5 penalty runs ... added to the score in its next innings'; the players' conduct provision is extended to 'an unfair action not covered by the Laws, under 2 above'; offences are reported 'as soon as possible after the match' to the Executive and to any Governing Body.", "The penalty terminology, the conduct clause and the reporting time are all restated; no source states a reason.")
pol("E102", "Law 5 (The ball): 'The umpires shall indicate to the batsmen and the scorers whenever a new ball is taken into play' becomes 'The umpire shall inform the other umpire and indicate to the batsmen and the scorers ...'.", "The new-ball signalling duty is allocated to one umpire who also informs the other; no source states a reason.")
wd("E104", "Law 6 (The bat): 'Grade A and Grade B bats' becomes 'Type A and Type B bats'.", "terminology")
