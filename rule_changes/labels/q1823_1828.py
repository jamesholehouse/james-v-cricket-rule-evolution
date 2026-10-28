"""Labels for 1823 -> 1828.

1823 = Carpenter broadsheet (heading blocks). 1828 = 'The 1828 Code' from The Sporting Magazine of 1828 as quoted in Lillywhite's
Scores and Biographies vol. II, numbered 1-43; the May 19th 1828 amendments (Rait Kerr serials 70, 71) were cut from the dataset text,
so this is the code before them. Real changes in the pair: serial 68 (wicket 27 x 8 in) and serial 69 (bowling crease 6 ft 8 in),
plus the omitted umpire-enforcement sentence (serial 62 note). The 1828 text reverts to 'notch' and some 1820-style phrases in places
where both the 1823 broadsheet and the official 1829 code (ACS, S32-01) and the 1835 code read 'run': labelled as source-lineage
artefacts of the 1828 reprint, not MCC changes. Numbering the laws splits the 1823 heading blocks into many add + move pairs; the add
of each pair is a segmentation artefact.
"""
from _h import make
PAIR = "1823_1828"
L, LABELS = make(PAIR)
ST, UN, NC, SW = "STRUCTURAL", "UNCATEGORISED", "NOT_A_CHANGE", "SEMANTIC_WORDING"

SEG = ("Added numbered law duplicates the 1823 sentence that the matching relocation event moves here (1823 heading blocks split into "
       "numbered laws in 1828); the content difference, if any, is labelled on that relocation.")


def seg(e, law):
    L(e, f"Numbered law {law} added in 1828: same sentence as the 1823 text moved into it (heading-block re-segmentation).", NC,
      "segmentation_artefact", "high", "derived", SEG, ["S18"])


def fmt(e, what):
    L(e, what + " Capitalisation/punctuation/hyphenation/heading merge only.", NC, "format_artefact", "high", "derived",
      "Token comparison of old and new text differs only by case, punctuation, hyphens, a merged heading word or a page number; same in ACS 1829.",
      ["S18", "S32-01"])


def wording(e, what, why):
    L(e, what, ST, "wording_only", "medium", "derived", why, ["S18", "S32-01"])


LIN = ("Source-lineage artefact of the 1828 Sporting Magazine/Scores and Biographies reprint: the 1823 broadsheet and the official 1829 code "
       "(ACS, S32-01) and the 1835 code all read 'run', and Rait Kerr serials 4 and 54b say 'notch' disappeared from the Laws by 1823. "
       "Not an MCC change.")


def lineage(e, what, sub="format_artefact"):
    L(e, what, NC, sub, "medium", "derived", LIN, ["S32-01", "S16", "S18"], integrity="suspect",
      note="1828 dataset text follows an unreliable reprint here; Rait Kerr Appendix III warns Lambert-type editions of 1816-1828 were lax.")


fmt("E001", "Ball law: heading 'The Ball' merged into the sentence; 'MUST' -> 'must'.")
fmt("E002", "No-ball law: the segmenter had taken 'The Ball' as an 1823 heading; 1828 text 'The ball must be bowled ...' is the same wording.")
L("E003", "1823 'When a Striker shall be run out the Run which they were attempting shall not be reckoned.' -> 1828 'When a striker is run out, "
  "the notch which they were running for is not to be reckoned.' (the 1828 sentence is the add in law 28).", NC, "format_artefact", "medium",
  "derived", LIN + " ACS 1829 Law 28: 'the run that they were attempting shall not be reckoned'.", ["S32-01", "S16", "S18"], integrity="suspect")
L("E004", "Omitted: 'The umpires shall enforce this Law.' at the end of the substitutes law (1828 law 33).", UN, "no_cause_stated", "medium",
  "none",
  "Rait Kerr serial 62: 'A direction that the umpires must be punctilious in enforcing this Law was omitted in 1827, but was restored by 1830.' "
  "He gives no cause. The ACS 1829 code already has it again ('The umpires shall enforce this law').", ["S16", "S32-01"],
  date="Omitted 1827 (Rait Kerr, from the Sporting Magazine text); restored by 1829 (ACS).",
  note="Possibly an omission of the reprint rather than an MCC decision; kept as a change because Rait Kerr reports it as one.")
seg("E005", 11)
fmt("E006", "Law 11 'He may order the striker ...' moved from the 1823 bowling block.")
seg("E007", 12)
wording("E008", "Wide law moved to law 12; 'even although he attempt' -> 'even though he attempt'; punctuation.",
        "Synonym 'although' -> 'though' only; the rule (umpire adjudges one run, put down to the byes) is unchanged. The May 1828 change to "
        "'wide balls' (serial 71) is not in the dataset text.")
L("E009", "1823 single-wicket first sentence shown as removed; it is the same sentence the relocation into the 1828 'LAW FOR SINGLE WICKET' "
  "block shows as moved.", NC, "segmentation_artefact", "high", "derived",
  "Duplicate record of a moved sentence (the 1823 single-wicket heading law is dropped by the segmenter but the sentence survives verbatim apart from case).",
  ["S18"])
seg("E010", 13)
fmt("E011", "Law 13 no-ball sentence moved; ';' -> ','.")
seg("E012", 14)
L("E013", "Practice balls: 'no more then two Balls' -> 'no more than two balls'.", NC, "ocr_noise", "high", "derived",
  "'then' for 'than' is a period spelling/typing variant; same rule.", ["S18", "S32-01"])
L("E014", "BETS section shown as removed; the same three sentences are shown moved by the BETS relocation event.", NC,
  "segmentation_artefact", "high", "derived", "Duplicate record of moved text; the BETS section is present in 1828.", ["S18"])
seg("E015", 15)
fmt("E016", "Law 15 'The bowler who takes the two balls ...' moved.")
fmt("E017", "Law 16: heading 'The Striker is Out' merged into the sentence; 'or the stump bowled' -> 'or the stump be bowled'.")
seg("E018", 17)
lineage("E019", "Catch: 1823 'from a Stroke of the Bat, or Hand, (but not wrist)' -> 1828 'from a stroke over or under the bat, or upon his hands "
        "(but not wrists)' (the 1820 wording). ACS 1829 Law 17: 'from a stroke of the bat, or hand (but not wrists)'.")
seg("E020", 18)
wording("E021", "Law 18: 'while the Ball shall be in Play' -> 'while the ball is in play'; 'his Wicket put down' -> 'his wicket is put down'.",
        "Verb mood only; same rule.")
seg("E022", 19)
wording("E023", "Law 19: 'he hit down his wicket' -> 'he hits down his wicket'.", "Verb mood only; same rule.")
fmt("E024", "Bat law: heading 'The Bat' merged into the sentence.")
seg("E025", 20)
lineage("E026", "Law 20: 'under Pretence of running or otherwise' -> 'under pretence of running a notch, or otherwise'. ACS 1829 Law 20: "
        "'under pretence of running, or otherwise'.")
L("E027", "Law 21 added: 'Or, if the ball be struck, and he wilfully strikes it again.' Same as the 1823 sentence shown removed in the "
  "striker-out removal event.", NC, "segmentation_artefact", "high", "derived",
  "The 1823 text joined this and the run-out sentence in one record; the 1828 numbered laws split them, producing remove + add of the same wording.",
  ["S18"])
lineage("E028", "Law 22 added: 'Or, if in running a notch, the wicket be struck down by a throw, or by the hand or arm (with ball in hand) ...'; "
        "1823 'if in running the wicket be struck down' (shown removed). Only 'a notch' differs. ACS 1829 Law 22: 'if in running, the wicket be struck down'.")
seg("E029", 23)
L("E030", "Law 23 dress hit-wicket: the 1823 record is cut at a page break ('knock down the'); same sentence.", NC, "segmentation_artefact",
  "high", "derived", "Old record truncated by the 1823 page break; wording otherwise identical.", ["S18"])
seg("E031", 25)
wording("E032", "LBW law 25: 'he stop the Ball' -> 'he stops the ball'.", "Verb mood only; LBW wording otherwise identical (serial 87 reversal is 1839).")
seg("E033", 26)
fmt("E034", "Law 26 crossed batsmen moved; comma added.")
seg("E035", 27)
lineage("E036", "Law 27: 'When a Ball shall be caught no run shall be reckoned.' -> 'When a ball is caught, no notch shall be reckoned.' "
        "ACS 1829 Law 27: 'no run shall be reckoned'.")
L("E037", "Law 28 added (run-out run not reckoned, 'notch' wording); its 1823 counterpart is the removal labelled as a lineage artefact.", NC,
  "segmentation_artefact", "high", "derived", "Remove + add of one reworded sentence; content labelled on the removal event.", ["S18"])
seg("E038", 29)
wording("E039", "Lost ball law 29: 'allowed six Runs' -> 'allowed six'; quotes round 'Lost Ball'.",
        "Dropping 'Runs' after 'six' does not change the allowance (six runs, Rait Kerr serial 66); ACS 1829 has 'six runs'.")
L("E040", "Stumps: 'twenty-six inches out of the Ground; the BAILS seven inches' -> 'twenty-seven inches out of the ground, the bails eight "
  "inches in length; the stumps of sufficient thickness to prevent the ball from passing through' (the 1823 text had this only as a hand-inked note).",
  "ENJOYMENT", "bowler_batsman_balance", "high", "stated",
  "Rait Kerr serial 68 (wicket increased to 27 by 8 in, stumps thick enough to stop the ball passing through). His ch.2 says that of the "
  "1810-1835 changes 'three were designed to help the bowler by twice increasing the size of the wicket ... and by extending the L.B.W. Law'.",
  ["S16", "S32-01"], date="Serial 68: 'After May 1823 but before 1825'; Bell's Life 27 June 1823 'newly adopted'; Appendix III: adopted May 1823 "
  "'with almost complete certainty'. Edition lag: printed 1823 broadsheet predates it.",
  note="Numbers checked: raw 1828 OCR 'twenty-seven inches ... eight inches'; ACS 1829 Law 3 agrees.")
seg("E041", 30)
fmt("E042", "Law 30 dead-ball sentence moved; 'Wicket Keeper's' -> 'wicket-keeper's', punctuation.")
seg("E043", 31)
fmt("E044", "Law 31 hurt striker retires; commas.")
seg("E045", 32)
fmt("E046", "Law 32 runner-like 'stand out' rule; comma.")
seg("E047", 33)
fmt("E048", "Law 33 substitutes: 'point, or middle Wicket' -> 'point or middle-wicket' (the omitted enforcement sentence is labelled separately).")
seg("E049", 34)
L("E050", "Law 34 hat penalty: dataset 1823 'stop the Ball with his Bat ... add five Runs ... they shall have five' -> 1828 'with his hat ... add "
  "five notches ... they are to have five'.", NC, "ocr_noise", "high", "derived",
  "'Bat' in the 1823 processed text is an OCR/cleaning error: raw OCR reads 'his pat' (p for H, as in 'pall', 'pun'), the 1823 single-wicket law "
  "refers to 'Ball stopped with Hat', and 1820 and ACS 1829 have 'hat'. 'Runs' -> 'notches' is the 1828 reprint's lineage wording (ACS 1829: "
  "'five runs').", ["S18", "S32-01", "S16"], sec=NC, secsub="format_artefact", integrity="suspect",
  note="1823 processed text should read 'Hat'.")
seg("E051", 35)
fmt("E052", "Law 35 guard wicket; commas.")
wording("E053", "Wicket-keeper law 36: heading merged; 'at Reasonable Distance' -> 'at a reasonable distance'.", "Article added; same rule.")
fmt("E054", "Umpires law 37: heading 'The Umpires' merged into the sentence; punctuation.")
seg("E055", 38)
fmt("E056", "Law 38 pitch fair wickets and toss; case only.")
seg("E057", 39)
wording("E058", "Law 39: 'when the Umpires shall call \"Play\"' -> 'when the umpire shall call \"Play\"'; ':' -> ';'.",
        "Singular/plural only (1820 also had 'Umpire'); ACS 1829 has 'umpires'. Same rule.")
L("E059", "Bowling crease: 'six Feet seven inches in Length ... with a RETURN CREASE at each end towards the Bowler at right Angles' -> 'six feet "
  "eight inches in length ... with the return-crease at each end, at right angles'.", ST, "consequential", "high", "stated",
  "Rait Kerr serial 69: 'The Bowling crease is increased to 6 feet 8 inches to conform with the width of the wicket' (the 8-inch wicket of serial 68).",
  ["S16", "S32-01"], date="Serial 69: 'After 1825 but before 1828'.",
  note="'towards the Bowler' is missing in the 1828 reprint but present in ACS 1829 Law 4; not a change. 6 ft 8 in confirmed in raw OCR and ACS 1829.")
seg("E060", 40)
wording("E061", "Law 40: 'unless appealed to by the Adversaries' -> 'by their adversaries'.",
        "Article/pronoun only; ACS 1829 has 'the adversaries'. Same rule.")
seg("E062", 41)
wording("E063", "Law 41 foot no-ball: 'behind the Bowling crease, (within the return crease)' -> 'behind the bowling-crease, and within the return-crease'.",
        "Parenthesis replaced by 'and' (1820 and ACS 1829 have 'and within'); same requirement.")
L("E064", "Law 42 added: 'If the striker run a short notch, the umpire must call \"No Notch.\"' (counterpart of the moved 1823 'One Short' sentence).",
  NC, "segmentation_artefact", "high", "derived", SEG, ["S18"])
lineage("E065", "Short run: 1823 'If the Striker run a short run the umpire must call \"One Short\"' -> 1828 'If the striker run a short notch, the "
        "umpire must call \"No Notch.\"' (the 1820 wording). ACS 1829 Law 42 and the 1835 code: 'One Short'.")
fmt("E066", "Law 43 umpires not to be changed; case/punctuation.")
fmt("E067", "Single-wicket first sentence moved; case/commas.")
L("E068", "Single-wicket rules in the 1828 reprint differ from 1823: run requires touching 'the bowling stump' (1823 adds '(Or Crease in a line "
  "with it)' and 'or go beyond them'); 'nor shall the striker be caught out behind wicket, nor stumped out' is missing; ball to cross 'between the "
  "wicket and the bounds' (1823 'between the Bowling stump, and the Bounds'); 'Runs' -> 'notches'; reference '29th, and 34th Law' -> '29th and 44th "
  "Laws' (1828 has only 43 laws; the hat law is 34).", UN, "no_cause_stated", "low", "none",
  "No source records any single-wicket change in this period (Rait Kerr chronology silent). The 1835 code has the 1823 forms again ('or crease in "
  "a line with it', 'stumped out', 'between the bowling stump, and the bounds', '29th & 34th law'), and the wrong '44th' shows the 1828 reprint "
  "is careless, so these are probably omissions of that reprint rather than MCC changes. ACS 1829 omits single-wicket laws, so no independent check.",
  ["S16", "S18", "S32-01"], integrity="suspect", note="Probably not a real change; owner decision needed.")
lineage("E069", "Bets: 'If the Runs of one Player be laid against those of another' -> 'If the notches of one player be laid against another'; "
        "'the Runs in the first innings' -> 'the notches'.")
fmt("E070", "Popping crease: heading merged into the sentence.")
L("E071", "Wickets law: heading merged; the ground-alteration rule shown removed here reappears as numbered law 7.", NC,
  "segmentation_artefact", "high", "derived",
  "The 1823 heading block held two laws; 1828 numbers them separately (law 6 and law 7) with the same wording apart from punctuation.", ["S18"])
L("E072", "Law 7 added (ground may not be altered without consent ...): same wording as the 1823 sentence shown removed from the wickets block.",
  NC, "segmentation_artefact", "high", "derived", "Remove + add of the same sentence caused by re-segmentation; punctuation only differs.",
  ["S18", "S32-01"])
seg("E073", 8)
fmt("E074", "Law 8 after rain; case only.")
fmt("E075", "Bowler law 9: heading merged; 'change Wickets' -> 'changes wickets'; hyphens; stray page number '-2-'.")
L("E076", "1823 hit-twice, run-out and bail-off sentences shown removed; they reappear as 1828 laws 21 and 22.", NC,
  "segmentation_artefact", "high", "derived",
  "The removed text reappears in the added laws 21-22; the only wording difference ('running a notch') is labelled on the law-22 add.", ["S18"])
