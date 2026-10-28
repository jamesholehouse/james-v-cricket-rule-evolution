"""Labels for the 2008 -> 2010 edition pair (2000 Code 4th edition, in force 1 October 2010). Evidence: MCC preface (S01: 'several
necessary amendments arising from experience and practical application of the Code around the world since October 2000'); NZC (S15):
eight key changes including ground/weather/light, the toss, no balls and practice on the field, and 'MCC have also modernised the Laws to
make them easier to understand'; MCC 2013 explanation (S03) referring back to the 2010 practice change."""
from _h import make
PAIR = "2008_2010"
L, LABELS = make(PAIR)
ST, UN, NC = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE"
D = "2000 Code 4th edition, effective 1 October 2010 (S01, S15)."


import re as _re


def wd(eid, what):
    if _re.search(r"'(will|must|may|shall|should)' (becomes|replaced by) '(will|must|may|shall|should)'|\bonly\b.*becomes.*\bonly\b", what):
        # strength word / qualifier position changed: semantic wording (user category), not plain wording_only
        return L(eid, what, "SEMANTIC_WORDING", "modal_strength" if not _re.search(r"\bonly\b", what) else "qualifier_scope", "medium", "inferred",
                 "A strength word or qualifier changes ('will'/'must'/'shall'/'only'); the rule is probably unchanged in effect, but the stronger or repositioned wording may change how it is enforced. NZC's general remark that MCC 'modernised the Laws' (S15) is not a stated cause.", ["S15"], date=D)
    L(eid, what, ST, "wording_only", "medium", "inferred", "NZC reports in general terms that for the 4th edition MCC 'modernised the Laws to make them easier to understand' (S15); that general remark is not a stated cause for this particular edit. This change is a rewording that leaves the rule as it was.", ["S15"], date=D)


HIDDEN = {
    "E012": "the toss must now take place in the presence of one or both umpires; the decision is notified 'as soon as the toss is completed' (previously 10 minutes before the start); a limited-innings agreement must include criteria for determining the result; a completed innings now includes the retirement of a batsman. (The toss is one of NZC's eight key changes, S15.)",
    "E036": "adds a new Law 19.4 'Ball beyond the boundary' (fielding or catching after the ball has crossed the boundary; airborne fielder).",
    "E084": "adds a new defence: the striker is not out Stumped if he has left his ground to avoid injury; stumping now requires a delivered ball that is not a No ball and no attempted run.",
    "E011": "when time is short the batting captain may still have the 7 minutes of rolling, with the delay taken out of playing time; the debris-clearance regime is rewritten (before each day, between innings, at meal intervals; by hand if sweeping would harm the pitch).",
    "E021": "new 15.8: retirement of a batsman is not equivalent to the fall of a wicket; drinks are taken if a wicket falls or a batsman retires.",
    "E025": "new 16.9(c) on the conclusion of a match under a 12.1(b) agreement; the reference becomes 5(a).",
    "E031": "for deliberate short runs the warning goes to both batsmen and all runs except any runs awarded for penalties are disallowed (previously only the No ball/Wide penalty and two named penalties survived).",
    "E039": "the bar on a substitute acting as captain on the field is removed from Law 2.3; the 15-minute absence becomes 15 minutes of playing time; a player returning without permission has completed runs scored.",
    "E040": "runner rules: an injured striker out of his ground is Run out notwithstanding Law 38.2(e); he is Stumped only off a ball that is not a No ball; runs are disallowed.",
    "E046": "new Law 21.4: a match under a 12.1(b) agreement takes its result from the agreement; 21.6(b) redefined.",
    "E047": "mistakes in scoring now cover limited-overs innings, with times taken at the call of Time.",
    "E052": "a Dead ball for a striker not ready no longer needs 'adequate reason' for the call itself, but the ball counts in the over unless there was adequate reason; new Dead ball 23.4(b)(vii) for deliberate distraction under 42.4/42.5.",
    "E053": "the validity-of-ball rule (23.6) is rewritten with new exceptions (2.6, 41.2, 42.5).",
    "E059": "new leg-bye rule on subsequent inadvertent contact; runs credited to the striker after later contact with his bat; the 'wilful lawful second strike' condition.",
    "E090": "illegal fielding: completed runs are now credited and the No ball/Wide penalty stands; ball hitting a helmet: completed runs are scored and the penalty is added to the No ball/Wide.",
    "E092": "the ball-condition test changes to 'deterioration ... greater than is consistent with the use it has received' (overlaps E093).",
    "E094": "'Both the above caution and final warning shall continue to apply even though the bowler may later change ends' is removed; the time-wasting trigger becomes 'either umpire considers'.",
    "E072": "the catch off an obstruction within the boundary now requires that the obstruction 'had not been designated a boundary by the umpires before the toss' (previously 'not previously decided to regard the obstruction as a boundary'); a ball that has touched a fielder's helmet is not a fair catch but 'remains in play' wording is dropped; Note also Law 19.4 added.",
}


def hid(eid, what):
    """A change first triaged as a rewording that in fact alters the rule (Opus verification): UNCATEGORISED, real change stated."""
    L(eid, what + " ALSO a real rule change: " + HIDDEN[eid], UN, "no_cause_stated", "low", "none",
      "The wording change hides substantive rule changes (found by direct comparison of old and new text); NZC's general remark that MCC 'modernised the Laws' (S15) does not explain them and no source states a reason.",
      ["S01", "S15"], date=D, sec=ST, secsub="wording_only")


def pol(eid, what, key=None, note=""):
    ev = ["S01"] + (["S15"] if key else [])
    why = "An amendment in the 4th edition of the 2000 Code; no source states a reason."
    if key:
        why = f"{key} is one of the eight key changes NZC lists for the 4th edition (S15), but no source states the reason for the change."
    L(eid, what, UN, "no_cause_stated", "low", "none", why, ev, date=D, note=note)


def defi(eid, what, why):
    L(eid, what, ST, "codification_definition", "low", "inferred", why, ["S01"], date=D)


def art(eid, what, why, sub="format_artefact", ev=None, conf="medium", integrity="ok"):
    L(eid, what, NC, sub, conf, "derived", why, ev or ["S18"], integrity=integrity)


defi("E001", "New definition in Appendix A: 'The outfield is that part of the field of play between the square and the boundary edge.'", "Supports the new practice-on-the-outfield provisions of Law 17.")
defi("E002", "Appendix A: striker's end defined more fully ('only insofar as it identifies, independently of where the striker may subsequently move, one half of the field of play'; also called the wicket-keeper's end in certain situations).", "Definitions are expanded; no source states a reason.")
defi("E003", "Appendix A: definitions of 'protective helmet' and of 'rebounds directly/strikes directly' (without contact with any fielder but not excluding contact with the ground) added.", "Definitions are expanded; no source states a reason.")
pol("E004", "Appendix E (bat): 'Grades' A, B and C renamed 'Types' A, B and C, with a reference note that all Law references are to sections of Law 6.", note="Follows the 2008 re-write of Law 6 (see 2000-2008 labels, S22).")
L("E005", "Appendix E (bat): 'Grades' become 'Types' in the handle-materials clause; the one-tenth (Types A and B) / one-fifth (Type C) volume restriction on other handle materials is already in the 2008 text.", ST, "terminology", "medium", "inferred", "Vocabulary change only (Grades -> Types); the restriction itself was already present in 2008 (old record 0587). No source states a reason.", ["S01"], date=D)
L("E006", "Appendix E (bat): the commercial-identification thickness changes from '0.08 in/0.2 mm' (2008; raw OCR '0.08 m/0.2 mm', internally inconsistent) to '0.008 in/0.2 mm' (2010, matching MCC's text): a correction of a printed error, not a policy change. The toe-insert limit (2.5 in/6.35 cm) and side-insert limit are already in the 2008 text.", ST, "wording_only", "medium", "inferred", "Correction of a unit/decimal inconsistency in the earlier printing (2010 value confirmed by S01 l.3050); no source states a reason.", ["S01"], date=D, integrity="suspect")
pol("E010", "Law 1: 'At any time after the toss, the deputy must be one of the nominated players' becomes 'At any time after the nomination of the players, only a nominated player can act as deputy in discharging the duties of the captain'.")
hid("E011", "Law 10: 'the captain of the batting side shall have the choice' of roller becomes 'shall choose which one is to be used', and other rewording throughout the rolling provisions.")
hid("E012", "Law 12: 'in a one innings match it shall apply to both innings' becomes 'a similar agreement shall apply to both innings'.")
pol("E019", "Law 15 (Intervals): 'Changing agreed times for intervals' rewritten: if, at any time during the match, playing time is lost through adverse conditions of ground, weather or light, or in exceptional circumstances, the agreed times may be changed.", key="Ground, weather and light")
hid("E021", "Law 15: 'when 30 minutes remain before the time agreed for tea' reworded (singular/plural slips corrected).")
pol("E022", "Law 15: new provision that, when play is in progress, the batsmen at the wicket may deputise for their captain in agreeing to forgo a drinks interval in that session.")
wd("E023", "Law 16: 'The umpire at the bowler's end shall call Play' becomes 'The bowler's end umpire shall call Play'.")
hid("E025", "Law 16: 'Three overs to be deducted from the result for the interval' reworded ('Three overs, for the interval, to be deducted from the resulting number').")
pol("E026", "Law 16: new sentence 'The separate parts of such an over shall count as one over of the minimum to be bowled.'")
pol("E027", "Law 17 (Practice on the field) rewritten: no practice of any kind on the pitch or the two adjacent parallel strips at any time on any day; no practice of any kind on the rest of the square except before or after play; practice on the outfield permitted before/after play, at intervals and between innings if the umpires are satisfied it will not damage the outfield (and other restrictions).",
    key="Practice on the field",
    note="MCC's 2013 explanation (S03) records that 'the change made in 2010 to outlaw this practice' (practice deliveries by a bowler to a fielder) was 'over-written by playing regulations in all professional and most amateur cricket'.")
hid("E031", "Law 18: 'the number of runs scored' becomes 'the number of runs to be recorded' for multiple short runs.")
wd("E032", "Law 18: 'Runs scored when a batsman is dismissed': 'In addition to any penalties ... if...' replaced by 'When a batsman is dismissed, any runs for penalties awarded to either side shall stand'.")
pol("E033", "Law 18: 'Notwithstanding any agreement under 12.1(b)'; when a batsman is dismissed Run out the batting side scores the runs completed 'before the wicket was put down' (previously 'before the dismissal').")
hid("E036", "Law 19: the definition of 'grounded beyond the boundary' reworded ('a line or solid object marking the boundary except its boundary edge').")
pol("E037", "Law 19: provisions about the penalty for a No ball or Wide standing together with other penalties when a boundary is scored are reworded and a cross-reference added.")
hid("E039", "Law 2: 'A substitute shall not be allowed to bat or bowl nor to act as wicket-keeper' becomes 'to bat, bowl or act as wicketkeeper'.")
hid("E040", "Law 2: 'A batsman with a runner' becomes 'A batsman who has a runner' and equivalent rewording.")
pol("E041", "Law 2: the rule that after a run-out or similar event 'the batsmen shall return to their original ends' becomes 'the non-striker shall return to his original end' in the runner provisions.")
pol("E042", "Law 2: 'A batsman may retire at any time during his innings' becomes 'A batsman may retire at any time during his innings when the ball is dead'.")
wd("E044", "Law 20 (Lost ball): 'If any other penalties have been awarded to either side, they shall be scored as penalty extras' becomes 'Any runs for penalties awarded to either side shall be scored'.")
wd("E045", "Law 21: cross-reference 'See Law 12.3 (Completed innings)' added to the forfeited-innings clause.")
hid("E046", "Law 21: wording of the extension of close of play subject to Law 3.9 clarified.")
hid("E047", "Law 21: 'umpires and players' becomes 'players and umpires' in the mistakes-in-scoring clause (the clause also appears elsewhere).")
wd("E048", "Law 22: 'from each wicket alternately' becomes 'from each end alternately'.")
defi("E049", "Law 22: new definition 'Any deliveries other than those listed in (a) and (b) above shall be known as valid balls' (balls that do not count in the over are listed in (a) and (b)).", "Introduces the term 'valid balls'; no source states a reason.")
pol("E050", "Law 22: the bowler change rule restated: another bowler completes the over provided he does not bowl 'two overs consecutively, nor bowl parts of each of two consecutive overs'.")
pol("E051", "Law 23: new sentence 'The ball will be deemed to be dead from the instant of the incident causing the dismissal'; 'member of the fielding side' becomes 'fielder'; cross-reference to Law 41.2 added.")
hid("E052", "Law 23: 'before he has the opportunity' becomes 'before the striker has had the opportunity'.")
hid("E053", "Law 23: 'under any of the Laws' becomes 'under any of the Laws not included above'.")
pol("E054", "Law 24 (No ball): the primary responsibility of the striker's end umpire 'to ensure' the fairness of a delivery becomes 'to assess' it, with 'See 3 below' and a reference that nothing prevents the bowler's end umpire from calling No ball.", key="No balls")
pol("E055", "Law 24: the front-foot rule now has 'three conditions' (24.5); the caution procedure for a thrown delivery restated ('If, after such caution, either umpire considers that, in that innings, a further delivery by the same bowler is thrown, the procedure set out in (a) above shall be repeated').", key="No balls")
pol("E058", "Law 25 (Wide ball): cross-reference '(see 3 above)' becomes '(see 3(b) and (c) above)'; AND the wide test gains a second condition: the ball passes wide of the striker 'where he is and which also would have passed wide of him standing in a normal guard position' (previously 'where he is standing and would also have passed wide of him standing in a normal guard position').", "Cross-reference changes and a rewritten wide test; no source states a reason.")
hid("E059", "Law 26: 'If the ball, delivered by the bowler, not being a No ball or a Wide' (words added for clarity).")
wd("E060", "Law 26: 'no other penalties shall be awarded to the batting side when the ball is dead' becomes 'no other penalties arising from that delivery shall be awarded'.")
pol("E062", "Law 27 (Appeals): the striker's end umpire, not the bowler's end umpire, answers appeals under Laws 35 (Hit wicket), 39 (Stumped) or 38 (Run out) when this occurs at the wicket-keeper's end.")
wd("E063", "Law 27: withdrawal of an appeal reworded ('only if he obtains the consent of the umpire within whose jurisdiction the appeal falls').")
pol("E064", "Law 28 (Wicket put down): rewritten to specify that the wicket is put down by the ball, by the striker's bat if he is holding it or any part of the bat he is holding, or (notwithstanding Law 6.8(a)) by the bat in falling; replacement of the wicket 'by an umpire' wording.")
pol("E065", "Law 29: new provision (a): notwithstanding the general rule, if a running batsman having grounded some part of his foot behind the popping crease continues running towards the wicket at that end and beyond, any subsequent total loss of contact with the ground is ignored.")
pol("E067", "Law 3 (The umpires): pre-match checks restated (boundary complies with Laws 19.1 and 19.2; implements conform to Laws 5 onwards); AND the ground/weather/light change: the captains' option to play on in unsuitable conditions is removed, the umpires alone decide whether conditions are 'dangerous or unreasonable', and both terms are defined.", key="Ground, weather and light")
wd("E068", "Law 3: 'the signals above ... shall be repeated to the scorers' becomes 'the bowler's end umpire shall repeat the signals above ... to the scorers'.")
pol("E069", "Law 31 (Timed out): 'After the fall of a wicket or the retirement of a batsman, the incoming batsman must, unless Time has been called, be in position to take guard ... within 3 minutes' (retirement added to the trigger).")
wd("E070", "Law 32 (Caught): 'any member of the fielding side' becomes 'any fielder'.")
pol("E071", "Law 32: the act of making a catch now starts when 'the ball in flight comes into contact with some part of a fielder's person other than a protective helmet' (previously when a fielder first handles the ball).",
    note="Concerns catches off fielders' protective helmets; the 2017 Code changed the treatment again (S05).")
hid("E072", "Law 32: 'but only if the ball has not been grounded since first being struck' reworded.")
pol("E074", "Law 33 (Handled the ball): the heading 'Out Handled the ball' is re-segmented, but the offence of returning the ball now excludes 'a hand not holding the bat' and adds 'while the ball is in play'; 'consent of the opposing side' becomes 'consent of a fielder'.")
wd("E076", "Law 34: 'only subsequent completed runs or a boundary shall be allowed' becomes '... shall be scored'.")
wd("E078", "Law 35 (Hit wicket): 'for his first run' wording tidied.")
wd("E081", "Law 37: 'obstructs or distracts the opposing side' becomes 'the fielding side'.")
wd("E082", "Law 38: 'his wicket is fairly put down by the opposing side' becomes 'by the action of a fielder'.")
wd("E083", "Law 38: the 'No ball has been called' provision for a striker out of his ground restated.")
hid("E084", "Law 39 (Stumped): 'except as in 3 below' added.")
wd("E086", "Law 39: 'liable to be out Run out' becomes 'may ... be out Run out' with a Law 38.2(e) exception.")
wd("E087", "Law 40: 'member of the fielding side' becomes 'fielder'.")
hid("E090", "Law 41: 'No member of the fielding side other than the wicket-keeper' becomes 'No fielder other than the wicket-keeper'.")
hid("E092", "Law 42: 'dry a wet ball on a towel' becomes 'on a piece of cloth'.")
pol("E093", "Law 42: reporting of unfair play now 'together with the other umpire ... after the match'; the match-ball condition is described as 'a greater deterioration in' the condition of the ball (previously 'unfairly changing'); umpires must together agree.")
hid("E094", "Law 42: 'the umpire at the bowler's end' becomes 'the bowler's end umpire' throughout the unfair-play procedures.")
pol("E095", "Law 42 (Fair and unfair play): new definitions that a player is deemed to cause avoidable damage to the pitch if either umpire considers his presence on the pitch to be without reasonable cause, and that a bowler contravenes the protected-area rule if he runs on to it after delivery; the umpire 'seeing the contravention' informs the other umpire; warnings and procedures under the dangerous/fast short-pitched provisions are directed at 'both batsmen' where they previously referred to 'the batsman'; the umpire need not inform the other batsman and fielding captain at that stage.")
art("E096", "Ball size appears to change from 8 13/16 to 8 15/16 inches: not real. The 2010 text's '8 15/16 in/22.4 cm' is internally inconsistent (22.4 cm is 8 13/16 in) and MCC's own 2010 text reads 8 13/16.",
    "MCC's published 4th edition (2010) text (S01) gives 'not less than 813/16 in/22.4 cm'; the raw 2010 OCR already reads '815/16 in/22.4cm' (raw/2010_raw.txt l.587), so this is an OCR misread carried into the dataset text, not an AI clean-up slip.", sub="cleaning_artefact_numeric", ev=["S17", "S01"], conf="high", integrity="suspect")
art("E098", "Junior (under 13) ball circumference upper limit appears to change from 8 11/16 to 8 5/8 inches, and the women's lower limit from 8 1/4 to 8 1/2: neither is real. MCC's 2010 text reads 8 11/16 in/22.0 cm (junior) and 8 1/4 in (women's; 21.0 cm = 8.27 in).",
    "The 2010 dataset text '8 5/8' does not match MCC's own 4th edition text (S01) nor its 22.0 cm figure (raw OCR '8\u201c/i6', i.e. 8 11/16: clean-up error); the women's '8 1/2' (raw '8V2') is a second artefact in the same event.", sub="cleaning_artefact_numeric", ev=["S17", "S01"], conf="high", integrity="suspect")
wd("E100", "Law 7: 'The umpires shall be the final judges of the fitness of the pitch' becomes 'the sole judges'.")
art("E103", "Junior wicket table: '8 in/20.32 cm' written '8 in/20.3 cm' and the table's columns are laid out differently; no change.", "Rounding of a metric equivalent and table layout.", sub="format_artefact", conf="high")
art("E104", "Popping crease '6ft/1.83m' typed '6 ft/1.83 m': spacing only.", "Same figures.", conf="high")
