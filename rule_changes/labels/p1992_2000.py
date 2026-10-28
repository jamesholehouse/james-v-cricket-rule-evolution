"""Labels for the 1992 -> 2000 edition pair (the 2000 Code). MCC (S01): 'In 2000, MCC revised and re-wrote the Laws for the new
Millennium. In this Code, the major innovation was the introduction of the Spirit of Cricket as a Preamble to the Laws ... The other
aims were to dispense with the Notes, to incorporate all the points into the Laws and to remove, where possible, any ambiguities.'
The wording below is the dataset's 2000 text; the 2010 4th edition (S01) provides an independent text of the same Code."""
from _h import make
PAIR = "1992_2000"
L, LABELS = make(PAIR)
ST, UN, NC, EN = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "ENJOYMENT"
CM = "consolidation_merge"
D00 = "2000 Code, approved 3 May 2000 (S01)."
REW = ("MCC states the 2000 Code was re-written with the aims 'to dispense with the Notes, to incorporate all the points into the Laws and to remove, "
       "where possible, any ambiguities' (S01 preface).")


def rewrite(eid, what, extra="", flagged=None, conf="medium", integrity="ok", note=""):
    """Law re-written under the 2000 Code. flagged: text describing substantive provisions that no source explains."""
    L(eid, what, ST, CM, conf, "inferred", REW + (" " + extra if extra else ""), ["S01"], sec=UN if flagged else "",
      secsub="no_cause_stated" if flagged else "", date=D00, integrity=integrity,
      note=("Contains substantive provisions with no documented reason: " + flagged) if flagged else note)


L("E001", "New Appendix A 'Definitions and explanations of words or phrases not defined in the text' (toss, before the toss, before the match, implements, playing time, ...), gathering definitions that had been scattered through the Laws and Notes.",
  ST, CM, "medium", "inferred", REW, ["S01"], date=D00)
L("E002", "New Preamble: 'The Spirit of Cricket' (cricket owes much of its unique appeal to the fact that it should be played not only within the Laws but also within the Spirit of Cricket; responsibilities of captains, umpires and players; respect for opponents, umpires, traditions).",
  EN, "fairness_spirit", "high", "stated",
  "MCC: 'the major innovation was the introduction of the Spirit of Cricket as a Preamble to the Laws. Whereas in the past it was assumed that the implicit Spirit of the Game was understood and accepted by all those involved, MCC felt it right to put into words some clear guidelines, which help to maintain the unique character and enjoyment of the game.'",
  ["S01"], date=D00)
rewrite("E003", "Law 1 rewritten in plain English: 'A match is played between two sides, each of eleven players, one of whom shall be captain. By agreement a match may be played between sides of more or less than eleven players, but not more than eleven players may field.'")
rewrite("E004", "Law 10 (rolling) rewritten as 'Rolling' (permitted rolling set out in (a), (b)), 'Frequency and duration of rolling', 'Rolling after a delayed start' (umpires must together agree the delay had no significant effect before refusing a request); several time limits restated (7, 10, 15, 30 minutes).",
        flagged="the restated rolling time limits and the 'umpires together agree' test")
rewrite("E005", "Law 10: outfield mowing rewritten ('the outfield shall be mown on each day of the match on which play is expected'); time limits restated.", flagged="the restated mowing/notification provisions")
rewrite("E006", "Law 11 (covering the pitch) rewritten: use of covers before the match is the Ground Authority's responsibility; run-up covers limits restated (the extent of covers in front of the popping crease grows from 4 ft/1.22 m to 5 ft/1.52 m); during-the-match covering rules recast.",
        flagged="the changed distance limit for covers in front of the popping crease (4 ft/1.22 m becomes 5 ft/1.52 m, confirmed by MCC's 2010 text)")
rewrite("E007", "Law 12 (Innings): 'A match shall be one or two innings of each side according to agreement before the match; it may be agreed to limit any innings by overs or by time'; toss and choice of innings restated (30 minute figures).",
        flagged="new agreement to limit innings by overs or time")
rewrite("E008", "Law 13 (Follow-on): thresholds restated ('In a two innings match of 5 days or more, the side which bats first and leads by at least 200 runs shall have the option...'; 150 for 3-4 days, 100 for 2 days, 75 for 1 day) with 'Day's play lost' wording.")
rewrite("E009", "Law 14 (Declaration and forfeiture): 'The captain of the batting side may declare an innings closed, when the ball is dead, at any time during a match'; forfeiture of an innings restated (the 7-minute rolling reference dropped).",
        flagged="declaration is now only 'when the ball is dead'")
rewrite("E010", "Old Law 15 'Start of Play' (Call of Play) is merged into the new Law 16 'Start of play; cessation of play'.")
rewrite("E011", "Law 15 (Intervals) rewritten as 'An interval' (what counts as an interval: end of day, between innings, meal, drinks) with lengths and the luncheon-interval adjustments restated (10, 30 minutes etc.), absorbing the Notes on intervals.",
        flagged="the restated interval lengths and extensions")
rewrite("E012", "Law 16 'Start of play; cessation of play': 'Call of Play' by the bowler's end umpire, call of Time, completion of the last over before an interval or close, restated with minute figures (5, 7, 10, 2).",
        flagged="the restated last-over and interval timing provisions")
rewrite("E013", "Law 16: 'Completion of last over of match' restated: the over in progress at close of play on the final day is completed unless a result has been reached or ...")
L("E014", "'Practice on the field' becomes a separate Law 17 (no bowling or batting practice on the pitch or the adjacent parallel area at any time on any day; on the rest of the square only before or after play; outfield provisions), instead of a paragraph under Start of Play (formerly Law 15.2).",
  ST, "reorganisation", "medium", "derived", "The 1992 text has 'Practice on the Field' as Law 15.2 (Start of Play); the 2000 text gives it its own Law with a fuller set of provisions. MCC's stated aim of incorporating all points into the Laws (S01) is consistent, but no source says why practice became a separate Law.",
  ["S01", "S18"], date=D00, sec=UN, secsub="no_cause_stated")
rewrite("E015", "Law 18 (Scoring runs) rewritten ('A run is scored so often as the batsmen, at any time while the ball is in play, have crossed and made good their ground'); short runs, runs scored, boundaries, penalty runs set out as numbered sections.",
        flagged="restated rules on short runs and penalty runs")
rewrite("E016", "Law 19 (Boundaries): 'The boundary of the field of play' agreed before the toss; marking, sight-screens, scoring a boundary and grounded/lost-ball provisions rewritten.", flagged="sight-screens outside the field of play and the 'greater of' boundary-scoring rule")
rewrite("E017", "Law 2 (Substitutes and runners): 'If the umpires are satisfied that a player has been injured or become ill after the nomination of the players, they shall allow that player to have a substitute and/or a runner'; objection, fielding, wicket-keeping substitutes and runner provisions rewritten.",
        flagged="restated substitute and runner entitlements")
L("E018", "Law 20 'Lost ball' rewritten (it remains a separate Law, 'LAW 20 LOST BALL'): the ball becomes dead on the call of Lost ball, a replacement ball is brought in, and the runs scored are the greater of 6 or the runs completed plus the run in progress.",
  ST, CM, "medium", "inferred", REW, ["S01"], date=D00, sec=UN, secsub="no_cause_stated",
  note="Contains substantive changes (dead on the call, replacement ball, 'greater of 6 or runs completed'); no source explains them.")
rewrite("E019", "Law 21 (The result) rewritten ('A Win - two innings match', one-innings matches, tie, draw, umpires awarding a match, correctness of result).", flagged="the restated provisions on awarding a match")
L("E020", "Law 22 (The over): 'overs of either 6 or 8 balls according to agreement' becomes 'overs of 6 balls'; new 'Start of an over' definition; 'Balls not to count in the over' set out.",
  ST, "codification_definition", "medium", "inferred",
  "The eight-ball option is removed. Wikipedia describes the six-ball over as having become standard worldwide from 1979 (S13), so the change codifies existing practice; no source states this was MCC's reason.",
  ["S13", "S01"], date=D00)
rewrite("E021", "Law 23 (Dead ball) rewritten as 'Ball is dead' ('The ball becomes dead when a boundary is scored; a batsman is dismissed; whether played or not it becomes lodged in ...') with 'Ball finally settled', 'Call of Dead ball' and 'Ball not dead' sections.", flagged="a ball trapped in the clothing or equipment of a batsman or umpire, and the striker being distracted")
rewrite("E022", "Law 24 (No ball) rewritten: 'The umpire shall ascertain whether the bowler intends to bowl right handed or left handed, over or round the wicket, and shall so inform the striker'; fair delivery (arm and foot), no-ball provisions restated as numbered sections.",
        flagged="restated mode-of-delivery and foot-fault provisions")
rewrite("E023", "Law 25 (Wide ball) rewritten with a definition in (b) of the area the ball must pass; 'Judging a wide' restated; metric figures introduced for the wide guidelines.", flagged="the restated definition of a Wide")
rewrite("E024", "Law 26 (Byes and leg byes) rewritten: 'Byes ... any runs completed by the batsmen or a boundary ...'; leg byes and 'leg byes not to be awarded' restated.", flagged="leg byes off a No ball are scored as No-ball extras")
rewrite("E025", "Law 27 (Appeals) rewritten: 'Neither umpire shall give a batsman out, even though he may be out under the Laws, unless appealed to'; time of appeals, withdrawal, consultation restated.")
rewrite("E026", "Law 28 (Wicket is down) rewritten: 'Wicket put down' by the ball, the striker's bat, person or clothing, or a fielder's hand or arm holding the ball.")
rewrite("E027", "Law 28: the rule about a fielder removing a bail with the hand while holding the ball restated in the new 'Wicket put down' list.")
rewrite("E028", "Law 28: 'All the stumps out of the ground' becomes 'Any fielder may replace a stump or stumps ... in order to have an opportunity of putting the wicket down'.")
rewrite("E029", "Law 29 (Batsman out of his ground) rewritten: 'a batsman shall be considered to be out of his ground unless his bat or some part of his person is grounded behind the popping crease'.")
rewrite("E030", "The rule on the non-striker's position (opposite side of the wicket to the striker) moves from the Law on the over to Law 29.")
rewrite("E031", "Law 3 (The umpires) rewritten and extended ('Appointment and attendance'; umpires' duties before and during the match: clocks, fitness of ground, signals, correctness of scores), absorbing the former Laws 45-46 content and Notes.", flagged="the new attendance, signals and score-checking provisions")
rewrite("E032", "Law 30 (Bowled) rewritten: 'The striker is out Bowled if his wicket is put down by a ball delivered by the bowler, not being a No ball, even if it first touches his bat or person'.", flagged="not out if the ball first touched another player or an umpire")
L("E033", "Law 31 (Timed out): the incoming batsman must be 'in position to take guard or for his partner to be ready to receive the next ball within 3 minutes of the fall of the previous wicket' (1980: wilfully more than two minutes to step on to the field); procedure for protracted delay refers to the umpires awarding a match.",
  UN, "no_cause_stated", "low", "none", "Wikipedia records that the 2000 Code revised the period to three minutes and recast it as being in position to take guard (S19); no source states why.",
  ["S19", "S21", "S01"], date=D00, sec=ST, secsub=CM)
rewrite("E034", "Law 31: the scorebook entry for 'timed out' becomes 'Bowler does not get credit for the wicket'.")
rewrite("E035", "Law 32 (Caught) rewritten with definitions of a fair catch, the field of play, and fielder's position ('touches his bat without having previously been in contact with ...').", flagged="catch precedence rules and catching beyond the boundary while in the air")
rewrite("E036", "Law 33 (Handled the ball) rewritten: 'Either batsman is out Handled the ball if he wilfully touches the ball while in play with a hand or hands not holding the bat unless ...'.", flagged="a batsman is not out Handled the ball if he touched it to avoid injury")
rewrite("E037", "Law 34 (Hit the ball twice) rewritten: the striker is out if the ball, while in play, strikes any part of his person or is struck by his bat and, before the ball has been touched by a fielder, he wilfully strikes it again ...; 'Ball lawfully struck twice' provisions restated.", flagged="new run rules for a ball lawfully struck twice")
rewrite("E038", "Law 35 (Hit wicket) rewritten: the striker is out if, while the ball is in play, his wicket is put down by the bat or person in the actions listed.")
rewrite("E039", "Law 36 (LBW) rewritten as numbered conditions ('(a) the bowler delivers a ball, not being a No ball; (b) the ball, if it is not intercepted full pitch, pitches in line between wicket and wicket or on the off side ...').")
rewrite("E040", "Law 36: new definition 'The off side of the striker's wicket shall be determined by the striker's stance at the moment the ball comes into play for that delivery'.")
rewrite("E041", "Law 37 (Obstructing the field) rewritten ('wilfully obstructs or distracts the opposing side by word or action'; obstructing a ball from being caught; deliberate attempt to distract).", flagged="returning the ball to a fielder is now obstruction")
rewrite("E042", "Law 38 (Run out) rewritten with 'Batsman not Run out' provisions (e.g. a batsman is not out if the ball has not been touched again by a fielder after ...).")
rewrite("E043", "Law 38: 'Which batsman is out' restated in terms of the end at which the wicket is put down.")
rewrite("E044", "Law 38: run-out of a striker with a runner restated with a cross-reference to Law 42.17 (penalty runs).")
rewrite("E045", "Law 39 (Stumped) rewritten as three conditions ('(i) he is out of his ground (ii) receiving a ball which is not a No ball (iii) not attempting a run and the wicket is put down by the wicket-keeper').")
rewrite("E046", "Law 4 (The scorers) rewritten: 'Two scorers shall be appointed to record all runs scored, all wickets taken and, where appropriate, number of overs bowled', with acknowledging signals and correctness of scores.")
L("E047", "Law 40 (Wicket-keeper): new 'Protective equipment' clause: the wicket-keeper is the only fielder permitted to wear gloves and external leg guards (regarded as part of his person for fielding the ball); a wicket-keeper who plainly cannot discharge his duties forfeits the right and wicket-keeper recognition for several Laws.",
  UN, "no_cause_stated", "low", "none", "A new provision on wicket-keeping equipment placed in the Law, plus a new 'Movement by wicket-keeper' unfairness and the glove-webbing rule; no source states a reason.", ["S01"], date=D00, sec=ST, secsub=CM)
rewrite("E048", "Law 41 (The fielder) rewritten: 'Protective equipment' (no fielder other than the wicket-keeper may wear gloves or external leg guards); fielding the ball, limitation of on-side fielders, encroachment; the old figures (e.g. 22 yards, 20.12 m, 3.05 m, 10, 5) are re-set.", flagged="restated fielding restrictions")
rewrite("E049", "Law 42 (Fair and unfair play) rewritten at length (173 records): responsibility of captains and umpires; unfair actions; the match ball (changing its condition); time wasting; dangerous and unfair bowling (fast short-pitched, non-pitching deliveries); batsmen damaging the pitch; protected area; penalty runs; procedures of caution, final warning and report.",
        extra="The Spirit of Cricket Preamble introduced in the same Code frames this Law.", flagged="the full procedures for unfair play and the penalty-run provisions",
        note="Contains substantive provisions (e.g. penalty runs for unfair play) for which the sources found give no reason.")
L("E050", "Apparent move of 'Bowling of fast short pitched balls': the old record is only a cross-reference fragment '(The Bowling of Fast Short Pitched Balls), 42.9.' inside Law 22, not the bowling rule itself moving.", NC, "segmentation_artefact", "high", "derived", "The old text is a cross-reference fragment in another Law; nothing is relocated.", ["S18"])
L("E051", "Law 5 (The ball) rewritten with 'Weight and size', 'Approval of balls', 'New ball', 'Ball lost or unfit' and specifications for women's and junior balls. The 2000 text reads the lower size limit as '8 3/4 in' instead of 8 13/16 in: an AI clean-up slip (the size limits themselves are unchanged).",
  ST, CM, "medium", "inferred", REW + " The apparent '8.8125 to 8.75 in' change is not real: MCC's own 4th edition (2010) text gives 8 13/16 in/22.4 cm.", ["S01", "S17"],
  date=D00, integrity="suspect", sec=NC, secsub="cleaning_artefact_numeric")
rewrite("E052", "Law 6 (The bat) rewritten ('Width and length': length 38 in/96.5 cm; the blade made solely of wood, width 4 1/4 in/10.8 cm; covering material and damage provisions restated).",
        flagged="the restated provisions on covering of the blade")
rewrite("E053", "Law 7 (The pitch): 'The pitch is a rectangular area of the ground 22 yards/20.12 m in length and 10 ft/3.05 m in width' (previously defined as the area between the bowling creases, 5 ft either side of the middle-stump line).", flagged="the pitch is redefined as a 22 yard by 10 ft rectangle")
rewrite("E054", "Law 7: 'Selection and preparation' now by the Ground Authority before the match; changing the pitch restated.")
rewrite("E055", "Law 8 (The wickets) rewritten with numbered sections (width and pitching, size of stumps, size of bails with metric equivalents; spigot dimensions and bail specifications added).", flagged="the added bail/spigot specifications")
rewrite("E056", "Law 9 (The creases) rewritten ('A bowling crease, a popping crease and two return creases shall be marked in white') with 2.44 m return-crease and 1.32 m popping-crease extents set out.", flagged="the restated crease dimensions")
