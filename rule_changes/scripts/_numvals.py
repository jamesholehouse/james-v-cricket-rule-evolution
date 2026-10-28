"""Numeric-value extraction shared by the diff (02), the audit (07) and the text classifier (08b/_textclass).

values(text) -> list of numbers mentioned (digits, mixed numbers like '8 13/16', '4-5/16' or '8⅞', fractions like '1/2',
decimals, number words, Unicode super/subscript fractions). Cross-references ('Law 28.3', 'Notes 2 and 3', clause paths like
25.6.7.1) and calendar years are dropped, so a change of notation ('5½' -> '5.5') or of cross-reference numbering is not a numeric
change of the rule. A number written after a cross-reference ('Law 42.17, 5 Penalty runs') is kept.
"""
import re

UNI = {"½": .5, "¼": .25, "¾": .75, "⅛": .125, "⅜": .375, "⅝": .625, "⅞": .875, "⅓": 1 / 3, "⅔": 2 / 3}
UNI_CH = "".join(UNI)
WORDS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
                                    "fifteen sixteen seventeen eighteen nineteen twenty".split())}
WORDS.update(dict(thirty=30, forty=40, fifty=50, sixty=60, seventy=70, eighty=80, ninety=90, hundred=100, half=.5,
                  quarter=.25, once=1, twice=2))
_SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉⁄",
                     "0123456789" "0123456789" "/")
UNITS = (r"(?:metres?|m\b|yards?|yds?|inch(?:es)?|in\b\.?|ounces?|oz|cm|mm|g\b|grams?|kg|lbs?|feet|foot|ft|minutes?|mins?|seconds?|"
         r"hours?|runs?|overs?|balls?|days?|per cent|%)")
# a bare number after one of these is a cross-reference list item only if followed by a parenthetical title or a list continuation
ITEM = r"\(?[A-Z]?\d+(?:\.\d+)*[a-z]?\)?(?:\s*\([^)]{0,60}\))?"
_SEP = r"(?:\s*(?:,|and|&|or|to)){1,2}\s*"
_NOT_QTY = r"(?!\s*(?:penalty|runs?|overs?|balls?|minutes?|mins?|seconds?|days?|hours?|inch|inches|in\b|feet|ft|yards?|ounces?|oz|per cent|%))"
REFS = re.compile(
    r"(?:Laws?|Notes?|paragraphs?|clauses?|Appendix|sub-?clauses?|see)\s*" + ITEM +
    r"(?:" + _SEP + r"(?:\(?[A-Z]?\d+(?:\.\d+)+[a-z]?\)?(?:\s*\([^)]{0,60}\))?|\d+[a-z]?(?:\s*\([^)]{0,60}\))?" + _NOT_QTY + r"))*"
    r"|\b\d{1,2}(?:\.\d{1,2}){2,4}\b"                                   # multi-dot clause paths (25.6.7.1)
    r"|\b[1-9]\d?\.\d{1,2}\b(?=\s*\([A-Z])",                            # 28.2 (Fielding the ball)
    re.I)
NUM = re.compile(
    r"(?P<mixed>\d+)(?:\s+|-)(?P<mn>\d+)/(?P<md>\d+)"                    # 8 13/16, 4-5/16
    r"|(?P<wu>\d+(?:\.\d+)?)\s*(?P<u>[" + UNI_CH + r"])"                 # 8⅞, 5 ½
    r"|(?P<fn>\d+)/(?P<fd>\d+)"                                          # 1/2
    r"|(?P<dec>\d+(?:\.\d+)?)"                                           # 4.25, 9
    r"|(?P<u2>[" + UNI_CH + r"])"                                        # ½
    r"|\b(?P<w>" + "|".join(WORDS) + r")\b", re.I)


def values(text):
    t = re.sub(r"(\d)([⁰¹²³⁴-⁹]+)", r"\1 \2", text or "")  # 4¹¹/₁₆ -> 4 11/16
    t = t.translate(_SUP)
    t = REFS.sub(" ", t)
    out = []
    for m in NUM.finditer(t):
        if m.group("mixed"):
            v = float(m.group("mixed")) + int(m.group("mn")) / int(m.group("md")) if int(m.group("md")) else float(m.group("mixed"))
        elif m.group("wu"):
            v = float(m.group("wu")) + UNI[m.group("u")]
        elif m.group("fn"):
            v = int(m.group("fn")) / int(m.group("fd")) if int(m.group("fd")) else 0.0
        elif m.group("dec"):
            v = float(m.group("dec"))
        elif m.group("u2"):
            v = UNI[m.group("u2")]
        else:
            v = float(WORDS[m.group("w").lower()])
        v = round(v, 3)
        if 1700 <= v <= 2100 and float(v).is_integer():
            continue
        out.append(v)
    return out
