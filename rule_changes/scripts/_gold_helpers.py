"""Shared helper for appending hand-transcribed Rait Kerr (1950) ch. 6 rows.

Each part file calls add(...) and finally write(path, mode). Columns:
  serial     printed serial number of change (int)
  sub        a/b/c when one serial has several paragraphs with separate prior/later refs
  date       date as printed (blank = inherited, see date_inherited_from)
  section    A-E (1744 code only; later entries are unlabelled in the book)
  particulars  printed text (verbatim, OCR-corrected against the page image)
  bold_text  portion printed in bold = Rait Kerr's 'fresh light' on date/significance ("ALL" = whole entry)
  prior, later  cross-references to other serials (semicolon separated) or years (e.g. 1884); '' = em dash
  struck_text  text struck through by hand in the scanned copy
  annotation  handwritten marginal note in the scanned copy
  page       printed book page
  row_type   change | note | heading
"""
import csv

COLS = ["serial", "sub", "date", "section", "particulars", "bold_text", "prior", "later",
        "struck_text", "annotation", "page", "row_type"]
ROWS = []


def add(serial, particulars, prior="", later="", date="", section="", bold="", sub="",
        struck="", annot="", page="", row_type="change"):
    ROWS.append(dict(serial=serial, sub=sub, date=date, section=section,
                     particulars=particulars, bold_text=bold, prior=prior, later=later,
                     struck_text=struck, annotation=annot, page=page, row_type=row_type))


def write(path, mode="w"):
    with open(path, mode, newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        if mode == "w":
            w.writeheader()
        w.writerows(ROWS)
    print(len(ROWS), "rows ->", path)
