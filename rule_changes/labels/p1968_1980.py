"""Labels for the 1968 -> 1980 edition pair (the 1980 Code). The MCC preface (S01) states the aim of the revision;
the 1980 wording is verified against the ACS transcription of the 1980 Code (S11) and the previous wording against the ACS
1947-Code editions (S08, S10)."""
from _h import make
PAIR = "1968_1980"
L, LABELS = make(PAIR)
ST, UN, NC, EN, NE = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "ENJOYMENT", "NOVEL_EVENT"
CM = "consolidation_merge"
REST = ("MCC states that the 1979 revision, begun in 1974, aimed 'to remove certain anomalies, consolidate various Amendments and Notes, "
        "and to achieve greater clarity and simplicity' (preface, S01). The 1980 wording of this Law, with its numbered headed "
        "sub-sections and the former Notes folded in, is consistent with the ACS transcription of the 1980 Code (S11), which also contains later amendments and so does not by itself confirm the 1980 wording.")
D80 = "1980 Code, approved at an MCC Special General Meeting on 21 November 1979 (S01)."
ev = ["S01", "S11"]


def restructure(eid, what, extra="", sec=None, note="", secsub=""):
    """Basis is 'inferred', not 'stated': the preface states the aim of the whole revision, not that a given provision was consolidation."""
    L(eid, what, ST, CM, "medium", "inferred", REST + (" " + extra if extra else ""), ev, sec=sec or "", secsub=secsub, date=D80, note=note)


def flagged(eid, what, extra, note=""):
    """Restructure that also carries substantive changes: secondary UNCATEGORISED."""
    restructure(eid, what + " Also substantive: " + extra, sec=UN, secsub="no_cause_stated", note=note)


def policy(eid, what, why_none, note="", sec=ST, secsub=CM):
    L(eid, what, UN, "no_cause_stated", "low", "none", why_none + " The change was made within the 1980 consolidation, whose general aims (S01) do not explain this particular provision.",
      ["S01", "S11", "S10"], sec=sec, secsub=secsub, date=D80, note=note)


restructure("E001", "Law 1 restructured into headed sub-sections (Number of Players and Captain; Nomination of Players); the 1968 Note that no match with more than eleven a side can be first-class becomes 'a match may be played by agreement between sides of more or less than eleven players but not more than eleven may field'.")
policy("E002", "Law 10 rolling: rolling of 7 minutes allowed before the start of each innings other than the first, and before each day's play; if the start is delayed after the toss the batting captain may have the pitch rolled;  time lost through late declarations reworded (15 minutes).",
       "A reorganised and partly changed set of rolling provisions; no source states a reason.")
policy("E003", "Law 10 mowing: the earlier rule (no mowing during matches of under three days) becomes 'in a match of two or more days' duration the pitch shall be mown daily before play begins'.",
       "Daily mowing for all matches of two or more days replaces mowing on alternate days (three days or more) and none in shorter matches; no source states a reason.", sec="", secsub="")
restructure("E004", "Law 12 (Maintenance of the pitch: batsman may beat the pitch, footholds by sawdust) is absorbed into Law 10 as 'Securing of Footholds and Maintenance of Pitch'.")
policy("E005", "Law 10: new provision for outfield mowing in matches of two or more days: if daily complete mowing is impossible for reasons other than ground and weather conditions, the Ground Authority must tell the captains and umpires before the toss which parts will be mown.",
       "A new procedural provision; no source states a reason.")
policy("E006", "Law 11 (Covering the pitch): complete covering allowed before the start of a match, not during it unless arranged; run-up covers (when possible) may extend 4 ft/1.22 m in front of the popping crease (previously 3 1/2 ft); the Notes about covers being removed each morning are dropped.",
       "Covers may now extend 4 ft instead of 3 1/2 ft (ACS 4th edition and earlier give 3 1/2 ft; the 1968 text's '8 feet' is an AI clean-up artefact, see 1962-1968); no source states a reason for the change.", note="The apparent '8 feet to 4 feet' difference in the raw comparison is an artefact; the real change is 3 1/2 ft to 4 ft.")
policy("E008", "Law 12 (Innings): 'a match shall be of one or two innings of each side according to agreement before the start of play'; alternate innings; the toss: captains toss not later than 15 minutes before scheduled start, the winner notifies his decision not later than 10 minutes before start (the old 'may not alter his decision once notified' is replaced).",
       "Formalises one- and two-innings matches by agreement and adds a time limit for notifying the decision after the toss; no source states a reason.")
policy("E009", "Law 13 (Follow-on): the lead needed to enforce the follow-on becomes 200 runs in a match of five days or more, 150 in a three- or four-day match, 100 in two days, 75 in one day (previously 150 for three days or more); new clause 'Day's play lost' (if no play on the first day of a match of two or more days the figures apply to the number of days remaining).",
       "A new five-day tier (200 runs) is added to the follow-on scale; no source states why. The 'Day's play lost' clause absorbs the old weather-delay Law 16.",
       note="Compare 1892-1896 and 1900 follow-on changes labelled in Rait Kerr (avoid draws): similar theme but no source ties this change to it.")
restructure("E010", "Law 14 (Declarations) restructured: 'Time of Declaration' and 'Forfeiture of Second Innings' (formerly a Note: 10-minute interval, notified in time for 7 minutes' rolling) with cross-reference to Law 10.")
restructure("E011", "New Law 15 'Start of Play' (Call of Play) gathering the provisions on calling Play at the start of each innings, each day and after intervals that had been spread across the intervals Law and Notes.")
restructure("E012", "Old Law 16 (start of play delayed by weather: follow-on and declaration rules apply by the number of days remaining) is merged into Law 13 as the 'Day's play lost' clause.")
policy("E013", "Law 16 (Intervals): umpires allow agreed meal intervals and 10 minutes between innings (the 2-minute allowance for a fresh batsman moves to Law 31); new provisions on the luncheon interval when an innings ends or a stoppage occurs within 10 minutes of it (time remaining is added); the old provisions on trial balls, use of the bat and awarding a match are removed from this Law.",
       "A reorganised Law with some new interval rules (including tea-interval/nine-wickets-down, drinks intervals, and changed interval times); no source states a reason.")
policy("E014", "Law 17 (Cessation of play): 'Call of Time' by the umpire at the bowler's end, removal of bails as a separate step, the last-over Notes (1957/1962/1968) restated as Law text; AND a new rule that a minimum of 20 six-ball (15 eight-ball) overs must be bowled in the last hour of the match, with a formula for deducting overs lost to interruptions.",
       "The last-over provisions restate earlier Notes, but the minimum-overs-in-the-last-hour rule is new (ACS 1980 Code Law 17); no source states a reason.", sec=ST, secsub=CM)
flagged("E015", "Law 18 (Scoring) restructured under headings (A Run; When a boundary is scored; Short runs ...); the short-run provisions are restated and the 'run scored even if short run called' sentence dropped.", "an injured striker run out scores no runs, and runs for obstruction are provided for.")
policy("E016", "Law 19 (Boundaries): boundary of the playing area agreed with both captains before the toss and, if possible, marked by a white line, rope or fence; flags/posts alone mark an imaginary line; an obstacle or person within the area is a boundary only if decided before the toss; sight-screens within the area count as the boundary and a boundary is scored if the ball passes within, under or over them.",
       "New detail on how boundaries are fixed and on sight-screens; no source states a reason.")
policy("E017", "Law 2 restructured (Substitutes; Objection to Substitutes; Substitute not to bat or bowl; A player for whom a substitute has acted; Runners; Fieldsman leaving the field; Batsman leaving the field or retiring; Commencement of innings); AND substantive changes: substitutes are allowed 'by right' for illness or injury, other reasons need the opposing captain's consent; no right of objection to a substitute or where he fields (but he may not keep wicket); a runner must be a member of the batting side who has already batted if possible, with pads and gloves; a fielder absent more than 15 minutes may not bowl until he has been on the field for that long.",
       "Several substantive substitute/runner rules are changed within the restructure; no source states a reason.")
restructure("E018", "Law 20 (Lost ball) restructured under headings ('Runs Scored'); the six-run allowance is unchanged.")
policy("E019", "Law 21 (The result): restructured into 'A Win - Two Innings Matches', one-innings matches decided on the first innings (with continuation after one innings each by agreement, Law 12.5), 'A Tie', 'Draw' and 'Result not determinable' headings; the clause allowing a match to be 'given up as lost' and the 1968 'Law 17' conditions are dropped.",
       "A rewritten result Law; no source states a reason for the substantive changes.", note="Mostly restructuring; flagged UNCATEGORISED because some provisions (given-up matches) were removed.")
L("E020", "Law 22 (The over): 'overs of either 8 or 6 balls according to the agreed conditions' becomes 'overs of either 6 or 8 balls according to agreement before the match' (both lengths remain permitted; the UK 6-ball Note is dropped); AND new provisions: umpire miscount of balls, completing an incomplete over on resumption, bowler incapacitated during an over, and the position of the non-striker.",
  UN, "no_cause_stated", "low", "none", "The over-length wording change is minor (ACS 1980 text, S11). Wikipedia (S13) records the six-ball over becoming standard worldwide from 1979, consistent with the reordering, but no source says it was the intention. The added miscount/incomplete-over/incapacitated-bowler provisions are substantive and unexplained.",
  ["S11", "S13"], sec=ST, secsub="wording_only", date=D80)
restructure("E021", "The rule that a bowler may change ends as often as desired provided he does not bowl two overs consecutively moves into Law 22 under 'Bowler Changing Ends'.")
restructure("E022", "Dead ball restructured as the enumerated list 'The Ball Becomes Dead when:- ...' (finally settled in the hands of the wicket-keeper or bowler; reaches the boundary; lodges in clothing or equipment; etc.).")
restructure("E023", "Dead-ball condition that the ball lodges in the clothing or equipment of a batsman or the clothing of an umpire is now a numbered item; the old definition of 'dress' as a Note is dropped.", extra="The 'dress' definition (1952 Note 4) is no longer needed once equipment is named in the clause.")
restructure("E024", "Provisions allowing the umpire to suspend play before the striker receives a delivery (striker not ready, etc.) become Dead-ball items ('He is satisfied that, for an adequate reason, the striker is not ready to receive the ball and makes no attempt to play it').")
restructure("E025", "'The ball ceases to be Dead on the bowler starting his run or bowling action' becomes the numbered item 'The Bowler starts his run up or bowling action'.")
restructure("E026", "'Ball Finally Settled' becomes a headed paragraph: whether the ball is finally settled is a question for the umpire alone.")
restructure("E027", "Old Law 24 (a bowler shall finish an over in progress unless incapacitated or suspended) is merged into Law 22 (The over).")
policy("E028", "Law 24 (No ball): restructured under 'Mode of Delivery', 'Fair Delivery - The Arm' (bowled not thrown), etc.; the umpire (not the striker's entitlement) indicates the bowler's mode of delivery, and failure by the bowler to indicate a change is unfair and a no-ball; the 1968 Note that breaking the near wicket in delivery is not a no-ball is replaced. KEY CHANGE: the foot-fault test switches from the back-foot/bowling-crease rule ('some part of one foot behind the bowling crease') to the FRONT-FOOT rule (some part of the front foot behind the popping crease); there is a new definition of a throw, and a bowler who attempts to run out the non-striker before delivering is covered.",
       "The back-foot-to-front-foot switch in the no-ball Law is a substantive rule change (ACS 1980 Code, Law 24); no source found here states a reason.", sec=ST, secsub=CM)
flagged("E029", "Law 25 (Wide ball) restructured under 'Judging a Wide' and related headings.", "a wide is now also judged by the striker moving in or out of reach of the ball.")
policy("E030", "Law 26 (Byes and leg-byes) restructured under headings ('Byes', 'Leg-byes', 'Leg-byes not to be scored'); AND leg-byes are now allowed when the striker 'tried to avoid being hit by the ball' (1968: only when he attempted to play the ball with his bat).",
       "A real change to when leg-byes may be scored (ACS 1980 Code Law 26); a safety motive is conceivable but no source states a reason.")
restructure("E031", "Old Law 27 (the ball does not become dead on the call of No ball; the striker may hit a No ball) is merged into Law 24 (No ball).")
flagged("E032", "Law 27 (Appeals) restructured ('Time of Appeals': before the bowler begins his run-up or bowling action; 'Dead ball and appeals'); the rule that an umpire unable to give a decision appeals to the other umpire is dropped from this Law.", "appeal timing is now 'before the bowler begins his run-up', and withdrawal of an appeal is newly provided for.")
restructure("E033", "Law 28 (The wicket is down) restructured as the list 'The wicket is down if:- ...' with explanatory paragraphs, adding the 'All the Stumps Out of the Ground' provision.")
restructure("E034", "Old Law 29 (the ball does not become dead on a Wide; runs from a Wide) is merged into Law 25 (Wide ball).")
policy("E036", "Law 3 (The umpires) restructured under headings (Appointment, Change of Umpire, Special Conditions, ...); AND the umpires become the sole judges of the fitness of ground, weather and light (1968 Law 46 Note 5: the captains decided unless agreed otherwise); only the batting side may elect to continue in poor light; appeals against the light; new 'Exceptional Circumstances'.",
       "Transfer of authority over ground/weather/light from the captains to the umpires is a substantive change (compare 1968 Law 46 Note 5(a) with the 1980 Law 3); no source states a reason.")
restructure("E037", "Provisions on resuming play after interruptions and inspecting the ground (formerly Law 46 Notes) move into Law 3 (The umpires).")
restructure("E038", "The umpires' signals (formerly Law 47) move into Law 3 as the 'Signals' paragraph (Boundary 6, Bye, Leg bye, ...).")
restructure("E039", "Law 3 gains explicit duties of the umpires: calling 'not out' on appeal, correctness of scores, signals; formerly spread across Laws 45-47 and appendices.")
restructure("E040", "Law 30 (Bowled) restructured ('Out Bowled': wicket bowled down even if the ball first touches bat or person; etc.).")
L("E041", "New Law 31 'Timed Out': an incoming batsman is out Timed Out if he wilfully takes more than two minutes to come in (timed from the fall of a wicket to his stepping on to the field); the umpire's duty to make the appeal arises if not complied with.",
  UN, "no_cause_stated", "low", "none",
  "Timed out becomes a specific mode of dismissal in 1980 (Wikipedia/Cricinfo, S19, S21). Earlier editions (1947 and 1968) provided that failing to be in within two minutes could lose the match or end the innings, and Rait Kerr counts nine ways of being out in 1947, whereas ten dismissal types existed before the 2017 Code reduced them to nine (S06), consistent with Timed out having been added. No source states why.",
  ["S19", "S21", "S16", "S06", "S11"], date=D80, sec=ST, secsub="reorganisation")
restructure("E042", "The old Law 17 Note (captains must ensure the in-going batsman passes the out-coming one before leaving the field) moves into Law 31 as 'Batsmen Crossing on the Field of Play'.")
policy("E043", "Law 32 (Caught) restructured ('Out Caught': the ball touches the bat, or the hand holding it below the wrist, and is held by a fielder before it touches the ground; etc.); AND new protective-helmet rules (no catch if the ball lodges in, or has touched, a fielder's helmet) and new boundary-catch rules.",
       "Helmet rules in the catching Law are an equipment-driven change that is plausible (helmets entering the game) but no source states it as the reason, so no cause is asserted.")
restructure("E044", "Old Law 33 (Batsman retiring) is merged into Law 2, whose title now reads '... Batsman Retiring; Batsman Commencing Innings'.")
restructure("E045", "Law 33 (Handled the ball) restructured ('Out Handled the Ball': on appeal, a batsman who wilfully touches the ball while in play with the hand not holding the bat, without the consent of the opposing side).")
restructure("E046", "Law 34 (Hit the ball twice) restructured with new headed paragraphs ('Returning the Ball to a Fieldsman'; 'Runs from Ball Lawfully Struck Twice', with penalty runs) and the rule that a hand holding the bat is part of the bat.")
flagged("E047", "Law 35 (Hit wicket) restructured as a list of ways the wicket is broken in preparing to receive, receiving or setting off after a delivery; the old provision for a wicket broken by a cap or hat falling is subsumed.", "a batsman breaking his wicket while avoiding a throw-in is not out hit wicket.")
L("E048", "Law 36 (L.B.W.) rewritten as 'Striker Attempting to Play the Ball' and 'Striker Making No Attempt to Play the Ball': the striker is out LBW, even if the ball is intercepted outside the line of the off stump, if he made no genuine attempt to play the ball with his bat and the other conditions hold; replaces the 1968 'four questions' formulation.",
  EN, "bowler_batsman_balance", "medium", "stated",
  "Wikipedia records that the LBW Law was changed in 1972 to penalise a batter who had 'played no stroke', after a 'long and heated controversy' about pad play over the preceding three decades; cricketweb describes the 1970-71 reversion and the 1972 return of the current law with a nearly doubled LBW rate (15.2% in 1972). The 1980 Code embodies that 1972 wording.",
  ["S13", "S12", "S11"], date="LBW wording changed 1970-72 (S12, S13) and carried into the 1980 Code.", sec=ST, secsub=CM, note="The 1970/1972 amendments fall between the 1968 and 1980 editions; the 1980 Code consolidates them.")
restructure("E049", "Law 37 (Obstructing the field) restructured: 'Wilful Obstruction' and 'Obstructing a Batsman Attempting to Run' etc.; either batsman on appeal.")
flagged("E050", "Law 38 (Run out) restructured under 'Out Run Out' with headings ('Which Batsman is Out', 'No Run Out in certain cases').", "a batsman who leaves his ground to avoid injury is not run out.")
restructure("E051", "Law 39 (Stumped) restructured ('Out Stumped', 'Action by the Wicket-Keeper', 'Ball Rebounding from Wicket-Keeper's Person').")
restructure("E052", "Law 4 (The scorers) restructured ('Recording Runs', 'Acknowledging Signals'): scorers record all runs and acknowledge umpires' signals; the instruction that umpires wait for a scorer's reply is dropped.")
flagged("E053", "Law 40 (The wicket-keeper) restructured ('Position of Wicket-Keeper', ...).", "a wicket-keeper contravention now makes the ball a no-ball.")
policy("E054", "Law 41 (The fieldsman): 'Fielding the Ball' keeps the 5-penalty-run rule for wilful illegal stopping but adds that the run in progress counts if the batsmen had crossed; new 'Limitation of On-Side Fieldsmen' (not more than two on-side fieldsmen behind the popping crease at the instant of delivery); the old Note forbidding use of a cap to field a ball is dropped.",
       "The limit of two on-side fieldsmen behind the popping crease is a substantive new provision; no source states a reason (a link with the 1930s 'direct attack' debate described by Rait Kerr is plausible but unsourced and not asserted).")
L("E055", "New Law 42 'Unfair Play': captains are responsible at all times for ensuring play is conducted within the spirit of the game as well as within the Laws; umpires are sole judges of fair and unfair play; intervention by the umpire; (replacing the old Law 46 Notes on unfair play).",
  ST, CM, "medium", "inferred", REST + " Rait Kerr describes the earlier notes on unfair play (direct attack, ch.4 p.53-55).", ["S01", "S11", "S16"], date=D80, sec=EN, secsub="fairness_spirit")
flagged("E056", "Unfair-play content from the old Law 46 Notes (direct attack, damaging the pitch, time wasting) moves into the new Law 42 with headings ('Intervention by the Umpire', ...).", "the test for unfair fast short-pitched bowling is loosened from a 'persistent ... systematic attempt at intimidation' to 'an attempt to intimidate', and the caution is routed through the captain.")
restructure("E057", "Old Law 45 (umpires' duties before the toss: special regulations, clock/watch) is folded into Law 3 (The umpires).")
restructure("E058", "Old Law 46 (umpires' conduct, fitness of ground, unfair play) is dissolved into Laws 3, 42 and others.")
restructure("E059", "Old appendix material under Law 47 (signals, scorers' check of scores, regulations for drying pitches in first-class matches in England) is removed from the Laws: signals move to Law 3; the drying regulations are no longer part of the Code.",
            extra="The ACS transcription of the 1980 Code contains no drying appendix.")
policy("E060", "Law 5 (The ball): sizes now also in metric; new-ball provisions: governing body prescribes the number of overs for a new ball in a match of three or more days (replacing UK 85 six-ball overs and the 200-run option); approval of all balls (not only first-class); replacement ball of similar wear; specifications for women's and junior balls added.",
       "A rewritten ball Law with metric units and governing-body-set new-ball interval; no source states a reason.", note="Weight and size limits themselves are unchanged (5 1/2-5 3/4 oz; 8 13/16-9 in).")
L("E061", "Law 6 (The bat): blade must be made of wood; maximum blade width 4 1/4 in (10.8 cm); overall length 38 in (96.5 cm); protective covering of the blade allowed up to 1/16 in thick. (The 1968 text's '4 1/2 in' is an AI clean-up artefact: the width limit was 4 1/4 in since 1771.)",
  UN, "no_cause_stated", "low", "none",
  "Secondary sources (S20; S13 says only that the Laws have provided that the blade must be made of wood) link a wood-only blade requirement to the aluminium 'ComBat' bat used by Dennis Lillee at Perth in December 1979, but the 1980 Code was approved on 21 November 1979 and the S20 registry note itself says sources differ on the exact Law 6 change, so the order is unresolved and no cause is asserted. Possible NOVEL_EVENT/equipment_exploit (attributed) once the chronology is fixed.",
  ["S20", "S13", "S11", "S17"], date="ComBat incident December 1979 (S20); 1980 Code approved 21 Nov 1979 (S01): order unresolved.", sec=NE, secsub="equipment_exploit",
  integrity="suspect", note="Separately, the apparent 4 1/2 to 4 1/4 inch change is a cleaning artefact in the 1968 text (see 1947-1968 labels).")
policy("E062", "Law 7 (The pitch): area stated in metric; new provisions for non-turf pitches (length of playing surface minimum 58 ft/17.68 m, width minimum 6 ft).",
       "Specification of non-turf pitches added; no source states a reason.")
flagged("E063", "Law 8 (The wickets) restructured under 'Width and Pitching', 'Size of Stumps', 'Size of Bails' with metric equivalents (22 yards/20.12 m; 9 in/22.86 cm; stump height 28 in/71.1 cm; bails 4 3/8 in/11.1 cm, projection 1/2 in/1.3 cm).", "the decision to dispense with bails passes from the captains to the umpires, and junior-cricket wicket dimensions (width 8 inches) are added; the 1968 text's '4 5/16 in' bails is an AI clean-up error (4 3/8 in is correct, S17).")
restructure("E064", "Law 9 (The creases) restructured under 'The Bowling Crease', 'The Popping Crease' (back edge of the marking 4 ft/1.22 m from the centre of the stumps, minimum 6 ft/1.83 m either side) and 'The Return Crease' (minimum 4 ft/1.22 m behind the wicket), with metric equivalents.")
restructure("E007", "Old Law 12 (Maintenance of the pitch: the batsman may beat the pitch with his bat; players may secure footholds with sawdust) disappears as a separate Law; its content reappears in Law 10 as 'Securing of Footholds and Maintenance of Pitch'.")
