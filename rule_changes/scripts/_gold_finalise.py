"""Post-process the transcribed gold file: derive date_printed, serial-integrity QA."""
import pandas as pd, re, sys
p="../data/gold/raitkerr_chronology.csv"
d=pd.read_csv(p,dtype=str).fillna("")

# --- corrections from the Opus verification (A_pipeline_gold_report.md: L1-L4, M6), checked against the page images ---
def fix(mask, col, val):
    assert mask.sum() >= 1, (col, val)
    d.loc[mask, col] = val
ch_ = d.row_type == "change"
fix(ch_ & (d.serial == "22"), "particulars", d.loc[ch_ & (d.serial == "22"), "particulars"].iloc[0].replace("4\u00be inches", "4\u00bc inches"))   # L1: page prints 4 1/4
fix(ch_ & (d.serial == "54") & (d["sub"] == "a"), "prior", "4; 16")                                                                  # L2
for sr, pg in (("38", "71"), ("120", "83"), ("137", "86")):                                                                          # L3: start pages
    fix(ch_ & (d.serial == sr), "page", pg)
fix(ch_ & (d.serial.isin(["13", "14", "15", "16", "17", "18", "19", "20"])), "section", "D")                                         # L4
for sr, sub in (("52", ""), ("53", ""), ("54", "a"), ("54", "b"), ("55", ""), ("56", "")):                                          # M6: whole entry (and its date) is bold
    fix(ch_ & (d.serial == sr) & (d["sub"] == sub), "bold_text", "ALL")
fix(ch_ & (d.serial == "58"), "bold_text", "The \u201cNo ball\u201d Law was again modified with the object of curbing round-arm bowling.")
fix(ch_ & (d.serial == "70"), "bold_text", "")
fix(ch_ & (d.serial == "68"), "bold_text", d.loc[ch_ & (d.serial == "68"), "particulars"].iloc[0].split(" (Vide")[0])
fix((d.row_type == "note") & (d.date == "Before 1821"), "bold_text", "The changes listed in Serial Numbers 59 to 61 were almost certainly made in 1819,")
h = d.row_type.eq("heading") & d.particulars.str.startswith("The Revision of 1774")
fix(h, "bold_text", d.loc[h, "particulars"].iloc[0].split("\u2014 ", 1)[1])
last=None; printed=[]
for _,r in d.iterrows():
    if r.row_type!="change":
        printed.append(""); continue
    printed.append(r.date if r.date!=last else "")
    last=r.date
d["date_printed"]=printed
d.to_csv(p,index=False)
ch=d[d.row_type=="change"]
nums=sorted({int(x) for x in ch.serial if x})
missing=[n for n in range(1,139) if n not in nums]
print("rows:",len(d),"| change rows:",len(ch),"| serials:",nums[0],"-",nums[-1],"| missing:",missing)
# reference integrity: every numeric prior/later ref (not a year) must be an existing serial
bad=[]
for _,r in ch.iterrows():
    for col in ("prior","later"):
        for t in re.split(r"[;,]\s*",r[col]):
            t=t.strip()
            if t and t.isdigit() and int(t)<1800 and int(t) not in nums: bad.append((r.serial,col,t))
print("dangling refs:",bad)
# reciprocity: if A lists B as later, B should list A as prior (and vice versa)
pri={};lat={}
for _,r in ch.iterrows():
    if not r.serial: continue
    s=int(r.serial)
    for t in re.split(r"[;,]\s*",r.prior):
        if t.strip().isdigit() and int(t)<1800: pri.setdefault(s,set()).add(int(t))
    for t in re.split(r"[;,]\s*",r.later):
        if t.strip().isdigit() and int(t)<1800: lat.setdefault(s,set()).add(int(t))
nonrec=[]
for a,bs in lat.items():
    for b in bs:
        if a not in pri.get(b,set()): nonrec.append((a,"later->",b,"but",b,"has no prior",a))
for b,as_ in pri.items():
    for a in as_:
        if b not in lat.get(a,set()): nonrec.append((b,"prior<-",a,"but",a,"has no later",b))
print("non-reciprocal refs:",len(nonrec)); [print(" ",x) for x in nonrec]
