"""Compact result chart for the Conclusions frame (frame 21), 2 Oct 2026 late.
Same numbers and tier colours as result_card.pdf (make_design_figures.py f18):
mean low-angle LAM per tier from cond26/data/zenodo/package_v2/results.json.
Drawn at its on-slide size (3.7 x 2.9 cm), no font below 7 pt.
Usage: python make_result_card_small.py <mevarc26/figures> <results.json>
"""
import sys, json, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG, RESULTS = sys.argv[1:3]
CM = 1/2.54
INK="#17243A"; PURPLE="#4C2A85"; TEAL="#007C83"; COPPER="#C7663A"; MUTED="#5D6978"
plt.rcParams.update({"font.family":"sans-serif","font.sans-serif":["Helvetica","Arial","DejaVu Sans"],
    "font.size":7,"axes.edgecolor":INK,"text.color":INK,"xtick.color":INK,"ytick.color":INK,
    "axes.spines.top":False,"axes.spines.right":False,"axes.spines.left":False,"pdf.fonttype":42})
R = json.load(open(RESULTS))
grp = {"center":[d for d in R if d["label"].startswith("FE Center")],
       "edge":[d for d in R if d["label"].startswith("FE Edge")],
       "periph":[d for d in R if d["label"].startswith("FE Periphery")],
       "ref":[d for d in R if d["label"].startswith("REF")]}
keys=("center","edge","periph","ref")
vals=[np.mean([d["mean"] for d in grp[g]]) for g in keys]
cols=[COPPER,COPPER,PURPLE,TEAL]
fig,ax=plt.subplots(figsize=(3.7*CM,2.9*CM),dpi=300)
ax.bar(range(4),vals,color=cols,width=0.7,lw=0)
for i,v in enumerate(vals):
    ax.text(i,v+0.04,f"{v:.2f}°",ha="center",va="bottom",fontsize=7.5,fontweight="bold",color=cols[i])
ax.set_xticks(range(4)); ax.set_xticklabels(["center","edge","periph.","ref."],fontsize=7)
ax.tick_params(axis="x",length=0,pad=2); ax.set_yticks([]); ax.set_ylim(0,1.74); ax.set_xlim(-0.5,3.5)
ax.text(-0.5,1.74,"mean LAM, one cathode",fontsize=7,color=MUTED,ha="left",va="top")
fig.subplots_adjust(left=0.01,right=0.99,bottom=0.16,top=0.99)
fig.savefig(f"{FIG}/result_card_small.pdf"); print([round(v,3) for v in vals])
