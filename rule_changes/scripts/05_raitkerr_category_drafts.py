"""
05_raitkerr_category_drafts.py
First category labels, for Rait Kerr's own chronology entries (data/gold/raitkerr_chronology.csv), drafted by Claude
from Rait Kerr's own text (his chapters 2-5 state causes for many changes). Each label records HOW the cause is
known (basis) and cites where; where he gives no cause the label is UNCATEGORISED. All rows are unreviewed.

Output: rule_changes/data/categories/raitkerr_drafts.csv

Usage (from the repo root):
    .venv/bin/python rule_changes/scripts/05_raitkerr_category_drafts.py
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "rule_changes/data/categories/raitkerr_drafts.csv"
_T = json.load(open(ROOT / "rule_changes/schema/taxonomy_v0.json"))
TAX = _T["categories"]
BASIS = set(_T["basis_values"])
RK = "Rait Kerr 1950"
ROWS = []


def r(serial, cat, sub, conf, basis, why, ev, sec="", secsub="", sub_id="", note=""):
    ROWS.append(dict(serial=str(serial), sub=sub_id, category=cat, subtype=sub, secondary_category=sec,
                     secondary_subtype=secsub, confidence=conf, basis=basis, rationale=why,
                     evidence=" | ".join(f"{RK} {e}" for e in ev), notes=note, review_status="unreviewed",
                     taxonomy_version="v0"))


NE, EF, EC, EN, ST, UN = "NOVEL_EVENT", "EXTERNAL_FORCE", "ECONOMY", "ENJOYMENT", "STRUCTURAL", "UNCATEGORISED"
NC = "no_cause_stated"
# ---- baseline 1744 code (serials 1-21) ----
for s in range(1, 22):
    r(s, "BASELINE", "", "high", "stated", "Description of the 1744 code, the starting point; not a change.", ["ch.6 p.65-69"])
# ---- 1771-1788 ----
r(22, NE, "equipment_exploit", "high", "stated",
  "A player named White of Ryegate brought a bat the width of the stumps to a match; Hambledon's committee limited bat width to 4 1/4 in. so that no more risks would be run.",
  ["ch.2 p.21-22", "ch.6 p.69"])
for s in (23, 24, 31, 33):
    r(s, ST, "drafting_omission", "medium", "conjecture",
      "Among five omissions from the previous code in the 1774 revision which 'may well have resulted from careless drafting'; the entry itself says the point is merely no longer mentioned.",
      ["ch.2 p.22", "ch.6 p.70-71"], note="Rait Kerr counts five omissions; the five bold 'no longer' entries are 23, 24, 31, 32a, 33.")
r(32, ST, "drafting_omission", "medium", "conjecture", "One of the five 1774 omissions (Hit wicket Law disappears temporarily).",
  ["ch.2 p.22", "ch.6 p.71"], sub_id="a")
r(32, EN, "bowler_batsman_balance", "low", "attributed",
  "First specific L.B.W. Law. Beldham is recorded as remembering it as 'a cure for the shabby methods adopted by the batsmen' (Rait Kerr notes 1744 umpires could already adjudicate 'standing unfair to strike').",
  ["ch.6 p.69"], sub_id="b", note="Cause rests on one recollection that Rait Kerr himself qualifies.")
for s in (25, 28, 30):
    r(s, ST, "codification_definition", "medium", "stated",
      "1774 revision: changes 'mainly directed towards the closer definition necessary for the more serious game in course of development' (Hambledon conception).",
      ["ch.2 p.21-22"])
r(26, ST, "codification_definition", "medium", "stated", "Confirms the 4 1/4 in. limit set in 1771; part of the 1774 closer-definition revision.", ["ch.2 p.22", "ch.6 p.70"])
for s in (27, 29):
    r(s, UN, NC, "low", "none", "Listed among the 1774 alterations but no cause is given.", ["ch.6 p.70"])
r(34, NE, "single_incident", "high", "stated",
  "Three-stump wicket introduced after a Hambledon v Kent single-wicket match (May 1775) in which Lumpy Stevens' balls passed between Small's stumps three times, which 'was considered a hard thing upon the bowler'.",
  ["ch.2 p.22-23", "ch.6 p.71"], sec=EN, secsub="bowler_batsman_balance")
r(35, ST, "documentary_first_appearance", "high", "stated", "Records only that the Wallis print of 1785 is the first edition to mention the three-stump wicket (not a rule change).", ["ch.6 p.71"])
r(36, ST, "documentary_first_appearance", "low", "none", "Maidstone edition mentions two bails per wicket; no cause given.", ["ch.6 p.71"])
r(37, ST, "drafting_omission", "medium", "inferred", "Hit wicket Law reappears in the same edition after its 1774 omission.", ["ch.6 p.71"])
r(38, UN, NC, "low", "none", "New Obstruction Law in the second Maidstone edition; Rait Kerr infers only that a committee slightly revised the 1774 code before the M.C.C. formed.", ["ch.6 p.71-72"])
r(39, ST, "codification_definition", "medium", "inferred", "Number of stumps not specified: 'the three-stump wicket had been so commonly accepted by this year that no special reference to it was thought necessary'.", ["ch.6 p.72"])
r(40, EN, "quality_of_play", "medium", "conjecture",
  "First Law allowing rolling/watering/mowing of the pitch by mutual consent: 'surely the earliest sign of the now accepted principle that bad conditions make for bad cricket'; 'doubtless it reflected the tremendous advance made in bowling technique' (David Harris).",
  ["ch.2 p.23-24"])
for s in (41, 43):
    r(s, ST, "codification_definition", "high", "stated", "1788 code: three of its four new provisions were closer definitions (L.B.W., obstruction of a catch, disallowance of runs on a catch/run out), 'in strict keeping with Hambledon's established conception of the game as one deserving more detailed legislation'.", ["ch.2 p.23"])
r(42, ST, "drafting_omission", "medium", "inferred", "Reintroduction of Hit wicket confirmed in new words after the 1774 omission.", ["ch.6 p.73"])
r(44, ST, "drafting_omission", "medium", "inferred", "Umpire jurisdiction for catch appeals 'again introduced' after its 1774 omission (33).", ["ch.6 p.73"])
for s in (45, 46):
    r(s, UN, NC, "low", "none", "1798 entry; no cause given (restores a point dropped in 1774).", ["ch.6 p.73"])
r(47, EN, "bowler_batsman_balance", "high", "stated", "Rait Kerr: the benefits to the bowler of 47 and 48 are 'the first evidence of a set policy to maintain an even balance between the bowler and the batsman'; the Marylebone period's major alterations gave 'assistance to the bowler by increasing the size of the wicket, and by allowing a new ball at the start of each innings'.", ["ch.6 p.73", "ch.2 p.24"])
r(48, EN, "bowler_batsman_balance", "high", "stated", "Larger wicket (24x7 in.) to help the bowler, as for 47.", ["ch.6 p.73", "ch.2 p.24"])
r(49, EF, "dress_fashion", "medium", "conjecture", "5-run penalty for a fieldsman stopping the ball with his hat: 'No doubt the adoption of the top hat as part of the usual attire of the players led to this introduction.'", ["ch.6 p.73"], sub_id="a")
r(49, ST, "documentary_first_appearance", "medium", "stated", "'Dead ball' used for the first time in this Law.", ["ch.6 p.73"], sub_id="b")
r(50, ST, "documentary_first_appearance", "medium", "stated", "Bails referred to in the plural for the first time in a reliable edition.", ["ch.6 p.73"])
r(51, UN, NC, "low", "none", "Lost ball Law introduced; no cause given.", ["ch.6 p.73"])
r(52, UN, NC, "low", "none", "Pitch selection by the umpires; Rait Kerr lists such changes only as 'general points' (substitutes, tossing, pitching wickets).", ["ch.6 p.74", "ch.2 p.29"], note="Possibly 1809 rather than 1811 (handwritten annotation).")
r(53, UN, NC, "low", "none", "Tossing decides choice of innings; 'general points' only.", ["ch.6 p.74", "ch.2 p.29"])
r(54, NE, "bowling_innovation", "medium", "inferred", "Striker may play at and score off a No ball: a handwritten annotation of unknown authorship in the scanned copy, attached to serial 52 in the gold file, says serials 54, 55 and 56 'provide the first evidence of the attack, to develop in later years, against the introduction of round-arm bowling' (Willes, from c.1802; 'throwing'); the printed text itself is struck through.", ["ch.6 p.74 (handwritten annotation recorded on gold serial 52; printed text struck through)", "ch.2 p.26"], sec=EN, secsub="bowler_batsman_balance", sub_id="a")
r(54, UN, NC, "low", "none", "'run' replaces 'notch' for the first time; terminology change, no cause given.", ["ch.6 p.74"], sub_id="b")
r(55, NE, "bowling_innovation", "medium", "inferred", "Ball must be bowled under-hand, hand below the elbow: as 54: the handwritten annotation on gold serial 52 (author unknown) names serial 55 among the first evidence of the attack on round-arm ('throwing') bowling.", ["ch.6 p.74 (handwritten annotation recorded on gold serial 52)", "ch.2 p.26"])
r(56, NE, "single_incident", "medium", "conjecture", "First Law for Wides 'probably resulted from' the 1810 Lord Frederick Beauclerk v Osbaldeston/Lambert single-wicket match, where Lambert bowled wide without penalty and Lord Frederick lost his temper, wicket and the match.", ["ch.2 p.29", "ch.6 p.74"])
r(57, UN, NC, "low", "none", "Trial balls for a fresh bowler; no cause given.", ["ch.6 p.75"])
r(58, NE, "bowling_innovation", "high", "stated", "'No ball' Law modified 'with the object of curbing round-arm bowling'; the Law was so complicated that it 'materially assisted the sponsors of the march of intellect'.", ["ch.6 p.75", "ch.2 p.26"])
r(59, EN, "bowler_batsman_balance", "high", "stated", "Larger wicket (26x7): of the major 1810-35 changes, three 'were designed to help the bowler by twice increasing the size of the wicket... and by extending the L.B.W. Law'.", ["ch.2 p.29"])
r(60, ST, "consequential", "high", "stated", "Popping crease moved to 4 ft 'as a result of the increase in the height of the wicket'.", ["ch.6 p.75"])
r(62, UN, NC, "low", "none", "Substitute restrictions; Rait Kerr describes the 1810-35 substitute/toss/pitching changes as 'general points'.", ["ch.2 p.29"])
r(63, UN, NC, "low", "none", "Pitch selection left to the umpires; 'general point'.", ["ch.2 p.29"])
r(64, UN, NC, "low", "none", "Pitch may be changed after rain by mutual consent; no cause given.", ["ch.6 p.76"])
r(65, UN, NC, "low", "none", "Bowling crease lengthened with return creases; no cause given (see 69 for the next adjustment).", ["ch.6 p.76"])
r(66, UN, NC, "low", "none", "Lost ball allowance raised; no cause given.", ["ch.6 p.76"])
r(67, EN, "bowler_batsman_balance", "high", "stated", "L.B.W. altered: 'This alteration was certainly designed to assist the bowler' (and encouraged the round-arm supporters).", ["ch.6 p.76", "ch.2 p.29"])
r(68, EN, "bowler_batsman_balance", "high", "stated", "Larger wicket (27x8), second increase in this period, to help the bowler.", ["ch.2 p.29", "ch.6 p.76"])
r(69, ST, "consequential", "high", "stated", "Bowling crease lengthened 'to conform with the width of the wicket'.", ["ch.6 p.76"])
r(70, NE, "bowling_innovation", "high", "stated", "'No ball' Law simplified as 'a sequel to the experimental round-arm matches played in 1827' (Knight's campaign; Ward's amendment at the May 1828 meeting).", ["ch.6 p.76", "ch.2 p.27-28"])
r(71, UN, NC, "low", "none", "Wide to be entered as such not as a Bye; no cause given.", ["ch.6 p.77"])
r(72, NE, "bowling_innovation", "medium", "inferred", "Penalty for a No ball (1829): among the changes by which restraint on the 'New style' was insisted on.", ["ch.2 p.29-30"], sec=EN, secsub="bowler_batsman_balance")
r(74, NE, "bowling_innovation", "high", "stated", "Round-arm bowling legalised (14 May 1835) after umpires increasingly turned a blind eye to the lifting of the arm; 'matters finally came to a head in 1834'.", ["ch.2 p.28-29", "ch.6 p.77"])
r(76, EC, "betting_stakes", "medium", "inferred", "Umpires barred from betting; Rait Kerr notes it 'appears later in the day than might be expected, since the selling of matches had become a scandal many years earlier' (betting/bookmaker scandals c.1820).", ["ch.6 p.77", "ch.2 p.19-21"])
r(78, EN, "avoid_draws", "high", "stated", "First 'follow on' Law; follow-on and declaration Laws were 'primarily directed towards reducing the number of drawn matches'; the follow-on's inspiration was 'the desire to avoid the burlesque of batsmen knocking down their own wickets'.", ["ch.4 p.55", "ch.3 p.31"])
r(80, UN, NC, "low", "none", "Umpire to call No ball/Wide promptly; no cause given.", ["ch.6 p.78"], sub_id="a")
r(80, UN, NC, "low", "none", "Ball dead on the call of Wide; no cause given.", ["ch.6 p.78"], sub_id="b")
r(82, ST, "codification_definition", "medium", "inferred", "Ball size specified for the first time; Rait Kerr lists limits on bat and ball dimensions among 'entirely general' changes.", ["ch.3 p.31", "ch.6 p.78"])
r(83, ST, "codification_definition", "high", "stated", "Official statement that a wicket has three stumps (long used in earlier unofficial editions).", ["ch.6 p.78"])
r(84, EN, "bowler_batsman_balance", "medium", "stated", "Removal of a fresh bowler's trial balls (1838) was the 'pin prick' that began the M.C.C.'s effort to restrain the bowler.", ["ch.3 p.33"])
r(87, EN, "bowler_batsman_balance", "medium", "stated", "L.B.W. reverted to the 1788 form (ball must pitch straight): one of three changes within ten years of 1835 'all directed towards limiting [round-arm bowling's] effect'.", ["ch.3 p.32"])
r(89, EN, "quality_of_play", "high", "stated", "Batting side reckons all runs from a Wide: after William Denison's protests about 'the liberal contribution of wide balls' by bowlers imitating Alfred Mynn's pace, which damaged scientific batsmanship and hazarded results.", ["ch.3 p.32-33"])
r(90, NE, "bowling_innovation", "high", "stated", "June 1845: 'the M.C.C. launched their full assault' on the increasing number of bowlers bowling over-arm by issuing a much more definite No ball Law.", ["ch.3 p.33-34"], sec=EN, secsub="bowler_batsman_balance")
r(91, ST, "clarification_umpire_workability", "high", "stated", "Wide redefined (not 'fairly within the reach of the batsman') after the 1845 request to define the limit; 'the general publicity given... satisfied both the umpires and the players by removing the uncertainty'.", ["ch.3 p.33"])
r(92, UN, NC, "low", "none", "Umpires to change ends after each innings; no cause given.", ["ch.6 p.79"])
r(93, UN, NC, "low", "none", "Pitch may be swept and rolled between innings on request; no cause given.", ["ch.6 p.79"])
r(94, UN, NC, "low", "none", "Consent of opposite side required for a fielding substitute.", ["ch.6 p.79"], sub_id="a")
r(94, UN, NC, "low", "none", "Runner allowed for an injured striker; no cause given.", ["ch.6 p.79"], sub_id="b", note="Medical context implied by text but not stated by source.")
r(95, EN, "avoid_draws", "medium", "inferred", "Follow-on limit reduced to 60/80 runs: later refinement of the 1835 follow-on Law.", ["ch.4 p.55"])
r(97, NE, "bowling_innovation", "high", "stated", "May 1858: No ball Law reinforced to cover the bowler's action 'immediately preceding delivery' because over-arm bowling persisted; special umpire instructions followed in 1859.", ["ch.3 p.35"])
r(99, EN, "bowler_batsman_balance", "high", "stated", "April 1863 proposal to alter L.B.W. (any part of the person between wicket and wicket); carried but declared invalid because notice had not been given in accordance with the rules.", ["ch.3 p.36-37", "ch.6 p.80"], note="Not put into practice (a procedural failure of notice, not a drafting omission).")
r(100, NE, "bowling_innovation", "high", "stated", "10 June 1864: over-arm bowling recognised after the 1862 England v Surrey incident (Willsher no-balled six times by Lillywhite), the 1863 failed meeting, and public opinion that 'forced the issue'.", ["ch.3 p.35-37", "ch.6 p.80"])
r(101, EN, "bowler_batsman_balance", "high", "stated", "1870: bowler may change ends twice; 'clearly designed to help the bowlers'.", ["ch.3 p.39"])
r(102, UN, NC, "low", "none", "Pitch may be rolled for 10 minutes before play (decided 1883, promulgated 1884); stems from a recommendation of the County Secretaries, 'a reflection of the increasing prestige of County cricket' (the agent, not a cause).", ["ch.6 p.81", "ch.3 p.39"])
r(61, UN, NC, "low", "none", "Striker out Hit wicket if any part of his dress breaks the wicket; no cause given.", ["ch.6 p.75"])
r(73, UN, NC, "low", "none", "Old provision letting the bowler water his run-up deleted; no cause given.", ["ch.6 p.77"])
r(75, UN, NC, "low", "none", "Substitutes (even with consent) may not bowl, keep wicket, etc.; 'general points' only.", ["ch.6 p.77", "ch.2 p.29"])
r(77, ST, "codification_definition", "medium", "inferred", "38 in. limit on bat length introduced; Rait Kerr lists 'limitations for the dimensions of the bat and the ball' among the 'entirely general' changes of 1835-84.", ["ch.3 p.31", "ch.6 p.77"])
r(79, UN, NC, "low", "none", "Fresh bowler may take two trial balls but must then finish the over; no cause given (trial balls removed in 1838, see 84).", ["ch.6 p.78"], sub_id="a")
r(79, UN, NC, "low", "none", "Umpire again instructed to call 'Over' after four balls; no cause given.", ["ch.6 p.78"], sub_id="b")
r(81, UN, NC, "low", "none", "An appeal must be made before the next ball is bowled; no cause given.", ["ch.6 p.78"])
r(85, UN, NC, "low", "none", "Removal of the remaining bail makes the wicket 'down' for a run out; no cause given (reversed in 1947, see 135).", ["ch.6 p.78"])
r(86, UN, NC, "low", "none", "Practice with the bat prohibited during play; no cause given.", ["ch.6 p.78"])
r(88, UN, NC, "low", "none", "Interval between innings reverts to 10 minutes; no cause given.", ["ch.6 p.79"])
r(96, UN, NC, "low", "none", "A retired batsman may resume only by consent of the fielding side; no cause given.", ["ch.6 p.80"])
r(98, UN, NC, "low", "none", "Rolling between innings at the request of the side next to bat; no cause given.", ["ch.6 p.80"])
# ---- 1884 code (unnumbered) ----
for sub, txt in (("u1a", "number of players, innings, scoring and results, umpires and scorers referred to for the first time"),
                 ("u1b", "free use of the term 'Dead ball'"), ("u2", "thickness of the bail specified"),
                 ("u3", "Boundaries officially mentioned (in use many years earlier)")):
    r("", ST, "codification_definition", "high", "stated", f"1884 code (a revision 'by defining terms, supplying omissions, and better wording, but without altering the spirit of the game'): {txt}.", ["ch.4 p.42-43", "ch.6 p.81"], sub_id=sub)
r("", NE, "tactic_abuse", "high", "stated", "April 1884: Lord Harris secured a last-minute clause directing the umpire to call 'No ball' if not satisfied of the absolute fairness of a delivery, against the 'throwing' that bowlers openly boasted of doing once an over.", ["ch.3 p.39-40"], sub_id="u4")
r("", ST, "reorganisation", "high", "stated", "Three one-day Laws removed from the general code and shown separately.", ["ch.6 p.82"], sub_id="u5")
r("", UN, NC, "low", "none", "Not a change: observation that the 1863 L.B.W. proposal was not revived.", ["ch.6 p.82"], sub_id="u6", note="non-change entry")
for s in (103, 104, 105, 106, 107):
    r(s, ST, "codification_definition", "medium", "inferred", "Part of the 1884 revision, 'supplying omissions' and defining terms, with no change of intent claimed.", ["ch.4 p.42-43", "ch.6 p.82"])
r(108, EC, "time_saving", "medium", "stated", "Over lengthened 4 to 5 balls (1889), then 6 (1900): 'These changes were designed to save time during play' (also an offset to the bowler's gain in 109).", ["ch.4 p.52"], sec=EN, secsub="bowler_batsman_balance")
r(109, EN, "bowler_batsman_balance", "high", "stated", "1889: bowler may change ends freely provided he does not bowl two overs in succession; listed among 'other measures adopted to assist the bowler' (improved pitches).", ["ch.4 p.52", "ch.4 p.46-49"], sec=EF, secsub="pitch_technology")
r(110, EN, "avoid_draws", "high", "stated", "Declaration allowed (1889): follow-on and declaration were 'primarily directed towards reducing the number of drawn matches, which resulted from the huge scores following on the improvement of pitches and batting technique'.", ["ch.4 p.55"], sec=EF, secsub="pitch_technology")
r(111, EN, "avoid_draws", "medium", "inferred", "Follow-on limit raised to 120 (1894) during the 'muddled thought' about the then-obligatory follow-on.", ["ch.4 p.55"])
r(112, UN, NC, "low", "none", "Ball becomes dead if it lodges in the batsman's clothing (3 May 1899); no cause given.", ["ch.6 p.83"])
r(113, NE, "tactic_abuse", "high", "stated", "Either umpire may call No ball (Oct 1899): the M.C.C.'s response to the 1890s 'throwing' scandal.", ["ch.4 p.49"])
r(114, NE, "single_incident", "high", "stated", "Follow-on made optional (May 1900) after considerable pressure from Australia and 'the failure to win a Test match after Australia had automatically followed on in 1899 at Old Trafford'.", ["ch.4 p.55"], sec=EN, secsub="avoid_draws")
r(115, EN, "avoid_draws", "medium", "inferred", "Declaration allowed in a three-day match after luncheon on the second day: declaration Laws aimed at fewer drawn matches.", ["ch.4 p.55"])
r(116, EC, "time_saving", "medium", "stated", "Over lengthened from 5 to 6 balls (1900); 'designed to save time during play'.", ["ch.4 p.52"])
r(117, EN, "bowler_batsman_balance", "high", "stated", "1902: bowling crease lengthened to 8 ft 8 in. on the recommendation of the County captains (proposed by umpire Thoms in 1888); listed under 'other measures adopted to assist the bowler' (though many judges later thought it a mistake).", ["ch.4 p.52"])
for s in (118, 119):
    r(s, EN, "avoid_draws", "medium", "inferred", "Refinement of when a declaration is allowed (one/two-day and three-day matches).", ["ch.4 p.55"])
r(120, UN, NC, "low", "none", "Striker cannot be stumped off a No ball but may be run out; Rait Kerr notes only that it 'was destined to cause much difficulty in interpretation' (later 136; the 1943 Bradford enquiry).", ["ch.6 p.83-84", "ch.5 p.60"])
r(121, UN, NC, "low", "none", "Follow-on/declaration rules to apply by days remaining after a weather-delayed start; text concerns weather but no cause is given.", ["ch.6 p.84"])
r(122, EF, "equipment_manufacture", "high", "stated", "Ball size reduced (1927): in 1925 it emerged that few first-class balls conformed to the Law; once gauged, bowlers complained the standard balls were too large and manufacturers had 'unwittingly provided an admirable trial of a smaller ball, which in 1927 was legalised'.", ["ch.4 p.52"], sec=EN, secsub="bowler_batsman_balance")
for s in (123, 124):
    r(s, EN, "avoid_draws", "medium", "inferred", "Follow-on/declaration limits adjusted (1927).", ["ch.4 p.55"])
r(125, EN, "bowler_batsman_balance", "high", "stated", "1931: wicket enlarged to 28 x 9 in. 'after extensive trials at home and overseas', within the pitch-improvement/help-the-bowler legislation.", ["ch.4 p.53", "ch.4 p.46-49"], sec=EF, secsub="pitch_technology")
r(126, UN, NC, "low", "none", "Time for sweeping and rolling the pitch reduced to 7 minutes; no cause given.", ["ch.6 p.84"])
r(127, UN, NC, "low", "none", "Clarifies that the 5-run penalty is in addition to runs made; no cause given.", ["ch.6 p.84"])
r(128, EN, "bowler_batsman_balance", "high", "stated", "L.B.W. extended to balls pitching off the wicket (1937) after trials in 1935-36: the culmination of the long reform campaign against pad-play defence enabled by improved pitches (Shrewsbury's back-play, padding), Lyttelton's 1928 formula.", ["ch.4 p.49-52"], sec=EF, secsub="pitch_technology")
# ---- 1947 code ----
for sub, txt in (("u1", "definition of 'Pitch' and 'Wicket'"), ("u2", "'Special Regulation' defined"),
                 ("u3", "new Dead ball Law collecting scattered references"), ("u4", "L.B.W. more closely defined"),
                 ("u5", "umpires no longer pitch the wickets but satisfy themselves they are properly pitched")):
    r("", ST, "codification_definition", "high", "stated", f"1947 code, whose terms of reference were 'a logical rearrangement, the incorporation in the Laws of appropriate matter hitherto given in the form of Notes, the provision of definitions wherever necessary, and the elimination of obscurities': {txt}.", ["ch.5 p.60-61", "ch.6 p.85"], sub_id=sub)
r(129, ST, "clarification_umpire_workability", "medium", "stated", "Only alterations in the conduct of the game in 1947 'occurred where actual experience had shown that the old Laws had caused difficulty for the umpires'.", ["ch.5 p.63", "ch.6 p.85"])
r(130, ST, "elasticity_for_conditions", "high", "stated", "The old code 'did not provide sufficient elasticity to meet the requirements of the various levels of competitive cricket, or of the differing climates in which the game had come to be played'.", ["ch.5 p.60", "ch.6 p.85"])
r(131, EN, "fairness_spirit", "high", "stated", "Final over played out at either captain's request: consultation found the previous batting-side-only option 'one-sided', so it was made fairer.", ["ch.5 p.62"], sub_id="a")
r(131, ST, "elasticity_for_conditions", "high", "stated", "Over of 6 or 8 balls permitted 'to meet the requirements of cricket overseas' (8-ball over already used in Australia and South Africa).", ["ch.6 p.86", "ch.4 p.52"], sub_id="b")
r(132, ST, "codification_definition", "high", "stated", "New Dead ball Law: part of the 1947 definitions/rearrangement.", ["ch.5 p.60-61", "ch.6 p.86"])
r(133, ST, "clarification_umpire_workability", "high", "stated", "Back-foot grounding requirement dropped: 'umpires had found it impossible to adjudicate on this point, and as a matter of course had disregarded the old instruction'.", ["ch.6 p.86"])
r(134, ST, "clarification_umpire_workability", "medium", "inferred", "Makes clear the striker cannot create a Wide by stepping back: an umpire-difficulty clarification.", ["ch.5 p.63", "ch.6 p.86"])
r(135, ST, "clarification_umpire_workability", "high", "stated", "Wicket 'down' now requires the bail to fall clear of the grooves: the consultation showed 'the unsatisfactory nature of the custom' that the slightest disturbance sufficed; Australian view approved.", ["ch.5 p.62"])
r(136, ST, "clarification_umpire_workability", "high", "stated", "Running out/stumping reverted to the 18th-century conception 'to eliminate many difficulties of interpretation'; the whole revision was triggered by a 1943 Bradford League enquiry about a Run out off a No ball.", ["ch.6 p.86", "ch.5 p.60"])
r(137, ST, "clarification_umpire_workability", "high", "stated", "'The old Laws were obscure' on the wicket-keeper taking the ball in front of the wicket; the Law now states where he must remain.", ["ch.6 p.86-87"])
r(138, ST, "codification_definition", "high", "stated", "Fills a gap: previously no mention of incommoding the striker by any fielder but the wicket-keeper.", ["ch.6 p.87"])


def check():
    cats = set(TAX)
    seen = set()
    for x in ROWS:
        assert x["category"] in cats, x
        assert x["subtype"] == "" or x["subtype"] in TAX[x["category"]]["subtypes"], x
        assert x["secondary_subtype"] == "" or x["secondary_subtype"] in TAX[x["secondary_category"]]["subtypes"], x
        assert x["basis"] in BASIS, x
        if x["category"] not in ("UNCATEGORISED", "BASELINE"):
            assert x["evidence"] and x["rationale"], x
        if x["secondary_category"]:
            assert x["secondary_category"] in cats, x
        if x["serial"]:
            seen.add(int(x["serial"]))
    return seen


if __name__ == "__main__":
    seen = check()
    gold = list(csv.DictReader(open(ROOT / "rule_changes/data/gold/raitkerr_chronology.csv")))
    need = {int(g["serial"]) for g in gold if g["row_type"] == "change" and g["serial"]}
    missing = sorted(need - seen)
    print("serials without a label:", missing)
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(ROWS[0]))
        w.writeheader()
        w.writerows(ROWS)
    from collections import Counter
    c = Counter(x["category"] for x in ROWS)
    print(len(ROWS), "rows ->", OUT, dict(c))
