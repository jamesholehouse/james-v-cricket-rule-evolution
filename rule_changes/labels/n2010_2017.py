"""Labels for events added after the first labelling pass (authored against the pipeline output of the verification-fix run).
Evidence: MCC 2017 preface (S02); MCC 2013 explanation (S03); NZC/BOP 2017 summary (S05); news summary (S06)."""
from _h import make
PAIR = "2010_2017"
L, LABELS = make(PAIR)
ST, UN, NC, EF = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "EXTERNAL_FORCE"
D17 = "2017 Code, in force 1 October 2017 (S02)."
RE = ("MCC: 'The game had evolved quickly, requiring six Editions of the 2000 Code to be published in only fifteen years. A new Code was necessary "
      "to rationalise these amendments and to list the Laws in a more logical format and order' (preface, S02).")
GN = ("MCC: 'for the first time in 2017, the Laws were written in a gender-neutral format, reflecting, and further encouraging, the rising popularity "
      "of the game amongst women and girls' (preface, S02).")


def conseq(eid, what, extra=""):
    L(eid, what, ST, "consequential", "medium", "inferred", RE + " Cross-references and sub-clause numbers follow the new numbering." + (" " + extra if extra else ""), ["S02"], date=D17)


def reorg(eid, what, extra=""):
    L(eid, what, ST, "reorganisation", "medium", "inferred", RE + (" " + extra if extra else ""), ["S02"], date=D17)


def gn(eid, what, extra=""):
    L(eid, what, EF, "legal_social", "high", "stated", GN + (" " + extra if extra else ""), ["S02"], date=D17)


def pol(eid, what, why="A substantive amendment between the 2010 and 2017 texts (2013 and 2015/16 editions or the 2017 Code); no source found states a reason.", sec=ST, secsub="reorganisation", ev=None):
    L(eid, what, UN, "no_cause_stated", "low", "none", why, ev or ["S02"], date=D17, sec=sec, secsub=secsub)


pol("E008", "Law 11 (Intervals): when a stoppage occurs with 10 minutes or less to the agreed lunch time, the interval is taken immediately 'whether or not agreement is reached in the circumstances of 11.4' (previously 'notwithstanding 5 above'); 'will' becomes 'shall'.")
reorg("E017", "Law 16 (The result): 'two innings'/'one innings' hyphenated; the provision that a match is lost by a side that concedes defeat or refuses to play is restated with 'Note also 16.6' and 'See also Law 42.6.1'.")
gn("E020", "Law 17: 'when the bowler starts his run up or, if he has no run up, his action' becomes 'starts his/her run-up or, if there is no run-up, starts his/her action'.")
conseq("E021", "Law 17: the Laws under which a ball does not count in the over are renumbered (2.6->24.4, 41.2->28.2, 42.4->41.4, 42.5->41.5) and 'when 5 penalty runs are awarded ... under' becomes 'when any of ... is applied'; '(a) and (b) above' becomes '17.3.1 and 17.3.2'.")
L("E027", "Law 18 (Scoring runs): the 'Runs scored for Lost ball' clause is replaced by a list of runs debited to the bowler (all runs scored by the striker, as No ball extras, as Wides); the run-out-of-a-striker-with-a-runner clause is restated as 'when the striker is dismissed in any of the circumstances in 18.11.1.1 to 18.11.1.6, the not out batsman shall return to his/her original end'.",
  ST, "consolidation_merge", "medium", "inferred", "News reports say Lost ball is 'now covered under Dead ball' (S06) with no stated reason; MCC's stated aim was a more logical Code (S02).", ["S06", "S02"], date=D17)
L("E031", "Law 2 (The umpires): 'the implements of the game conform' becomes 'the implements used in the match conform'.", ST, "wording_only", "medium", "inferred", RE, ["S02"], date=D17)
conseq("E032", "Law 2: a pointer 'See Appendix A.2.' (implements and equipment) is added.")
pol("E034", "Law 2 (The umpires): suspension of play for dangerous or unreasonable conditions: 'If at any time the umpires together agree that the conditions ... are dangerous or unreasonable, they shall immediately suspend play' becomes 'The Umpires shall immediately suspend play ... if either umpire considers that the conditions ... are either dangerous or unreasonable'.",
    why="Either umpire alone (not both together) may now suspend play; this continues the 2010 transfer of authority over ground, weather and light to the umpires (NZC key change, S15), but no source states the reason for this step.")
gn("E038", "Law 20 (Dead ball): 'he leaves his normal position for consultation' becomes 'leaving his/her normal position for consultation'.")
L("E039", "Law 20 (Dead ball): 'within the game or outside it' becomes 'within the match or outside it'; 'while he is preparing' becomes 'while preparing'; a pointer 'Note also 20.4.2.7' is added.", ST, "terminology", "medium", "inferred", RE, ["S02"], date=D17)
pol("E043", "Law 21 (No ball): the list of Laws that bear on No balls is renumbered (e.g. 40.3->27.3, 41.5->28.4, 42.6->41.6); and the revocation rule changes from 'An umpire shall revoke his call of No ball if the ball does not leave the bowler's hand for any reason' to 'if Dead ball is called under any of Laws 20.4.2.4 to 20.4.2.9'.",
    why="The conditions for revoking a No ball call are rewritten (the 2019 list, S04, amends 21.12 again); no source states a reason for the 2017 version.", ev=["S02", "S04"])
conseq("E047", "Law 22 (Wide ball): the cross-reference '(see 3(b) and (c) above)' becomes 'see 22.3'.")
conseq("E055", "Law 25 (Batsman's innings; runners): 'notwithstanding (i) above' becomes 'even though out of the match as in 25.6.7.1' and the wording is gender-neutral.")
gn("E058", "Law 27 (Wicket-keeper): 'his wicket' becomes 'his/her wicket' and the cross-reference 'Law 23.4(b)(vi)' becomes 'Law 20.4.2.6 (Umpire calling and signalling Dead ball)'.")
conseq("E064", "Law 29 (The wicket is broken): cross-references renumbered ('ways stated in 1 above' -> 'in 29.1'); fielders may replace a bail or bails or put back stumps, shown as a bulleted list.")
conseq("E074", "Law 31 (Appeals): 'in accordance with 3 above' becomes 'in accordance with 31.3'; gender-neutral wording.")
L("E086", "Law 38 (Run out): the pointer 'See Laws 2.8 and 29.2' and the clause that runs completed by a runner and the other batsman are not scored if a striker who has a runner is himself Run out are removed from this Law; the substance reappears in Law 18.", ST, "reorganisation", "medium", "inferred", RE, ["S02"], date=D17)
gn("E091", "Law 31 (Timed out): 'for his partner to be ready' becomes 'for the other batsman to be ready'.")
pol("E096", "Law 42/41 (damage to the pitch): the diff pairs the fielder and the batsman paragraphs (both exist in 2017 Law 41.12 and 41.14); the real differences are for batsmen: damage 'deliberate or avoidable' (previously 'avoidable'), a warning to both batsmen with each incoming batsman informed, the report goes to the 'offending side', and a new heading 'Striker in protected area'.",
    why="Partly an alignment of parallel paragraphs; the substantive differences are not explained by any source.", ev=["S02", "S06"])
reorg("E099", "Law 41 (Penalty runs): restated as bulleted rules; 'Notwithstanding the provisions of Law 21.6' becomes 'even if a result has already been achieved'; 5 Penalty runs awarded to the fielding side are 'added as Penalty extras to that side's total in its most recently completed innings'.")
L("E104", "Law 5 (The bat): 'unacceptable damage is deterioration greater than normal wear and tear' becomes 'any change that is greater than normal wear and tear'.", ST, "wording_only", "low", "inferred", RE, ["S02"], date=D17)
