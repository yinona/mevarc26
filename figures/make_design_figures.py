
"""Design-pass figures for the MeVArc 2026 deck (2 Oct 2026).
Numbers: cond26/data/zenodo/package_v2/results.json; E(r) digitized from
cond26/figures/efield_vs_radius.eps (axes calibrated on its tick marks);
geometry: cond26/main.tex L94-101 (r_i 6.5 mm, r_o 20 mm, h1 60 um, h2 70 um).
Figures are drawn at their final on-slide size (B_legibility rule: no font below 8 pt).
Usage: python make_design_figures.py <mevarc26/figures> <results.json> <efield csv>
"""
import sys, json, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.patheffects as pe
from matplotlib.patches import Rectangle, Polygon, FancyBboxPatch
from PIL import Image
from scipy.stats import gamma as G

FIG, RESULTS, EFCSV = sys.argv[1:4]
CM = 1/2.54
INK="#17243A"; PURPLE="#4C2A85"; TEAL="#007C83"; COPPER="#C7663A"; MUTED="#5D6978"; STEEL="#607D8B"
HIGH, PERIPH, REF = COPPER, PURPLE, TEAL
plt.rcParams.update({"font.family":"sans-serif","font.sans-serif":["Helvetica","Arial","DejaVu Sans"],
    "font.size":9,"axes.labelsize":9.5,"xtick.labelsize":9,"ytick.labelsize":9,"axes.edgecolor":INK,
    "axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK,"text.color":INK,
    "axes.spines.top":False,"axes.spines.right":False,"pdf.fonttype":42})

R = json.load(open(RESULTS))
grp = {"center":[d for d in R if d["label"].startswith("FE Center")],
       "edge":[d for d in R if d["label"].startswith("FE Edge")],
       "periph":[d for d in R if d["label"].startswith("FE Periphery")],
       "ref":[d for d in R if d["label"].startswith("REF")]}
ref_mean = np.mean([d["mean"] for d in grp["ref"]])
ref_sem  = np.sqrt(np.mean([d["sem_grain"]**2 for d in grp["ref"]]))
hf_mean  = np.mean([d["mean"] for d in grp["center"]+grp["edge"]])
ef = np.loadtxt(EFCSV, delimiter=",")

def save(fig, stem, png=False):
    if png: fig.savefig(f"{FIG}/{stem}.png", dpi=300)
    else:   fig.savefig(f"{FIG}/{stem}.pdf")
    plt.close(fig)

def tier_shade(ax):
    ax.axvspan(0,6.5,color=HIGH,alpha=0.10,lw=0); ax.axvspan(6.5,20,color=HIGH,alpha=0.045,lw=0); ax.axvspan(20,30,color=PERIPH,alpha=0.07,lw=0)

# ---- frame 7: geometry + E(r) + tiers + ROI positions, 8.0 x 5.8 cm ---------
def f07():
    fig = plt.figure(figsize=(8.0*CM,5.8*CM),dpi=300)
    gs = fig.add_gridspec(2,1,height_ratios=[0.78,1.0],hspace=0.08,left=0.135,right=0.985,top=0.985,bottom=0.20)
    # cross-section (gap drawn x100 exaggerated: 60 um -> 6 mm on the y axis in "mm" units)
    ax = fig.add_subplot(gs[0]); tier_shade(ax)
    ax.add_patch(Rectangle((0,-4),30,4,color=COPPER,alpha=0.75,lw=0))
    ax.text(0.5,-2.0,"cathode (heat-treated OFE Cu)",fontsize=8,color="white",fontweight="bold",va="center")
    anode = Polygon([(0,6),(6.5,6),(20,7),(20,13.5),(0,13.5)],closed=True,color=STEEL,alpha=0.75,lw=0); ax.add_patch(anode)
    ax.text(9.5,10.4,"anode (sloped)",fontsize=8,color="white",fontweight="bold",ha="center",va="center")
    ax.annotate("",xy=(3.2,0),xytext=(3.2,6),arrowprops=dict(arrowstyle="<->",color=INK,lw=0.8))
    ax.text(3.7,3.0,"60 µm",fontsize=7.5,va="center")
    ax.annotate("",xy=(17.5,0),xytext=(17.5,6.8),arrowprops=dict(arrowstyle="<->",color=INK,lw=0.8))
    ax.text(17.0,3.4,"70 µm",fontsize=7.5,va="center",ha="right")
    for r,lab in [(6.5,"6.5 mm"),(20,"20 mm")]:
        ax.plot([r,r],[0,16.5],color=MUTED,lw=0.7,ls="--")
    ax.text(0.5,15.3,"gap drawn ×100",fontsize=7,color=MUTED,va="center")
    ax.text(25,15.3,"beyond the anode",fontsize=7.5,color=PERIPH,ha="center",va="center")
    ax.text(25,6.0,"reference:\nE = 0",fontsize=7.5,color=REF,fontweight="bold",ha="center",va="center",linespacing=1.0)
    ax.set_xlim(0,30); ax.set_ylim(-4,17); ax.set_axis_off()
    # E(r)
    ax2 = fig.add_subplot(gs[1]); tier_shade(ax2)
    ax2.plot(ef[:,0],ef[:,1]*80,color=INK,lw=1.7)
    for g,m in {"center":"o","edge":"s","periph":"D"}.items():
        c = HIGH if g!="periph" else PERIPH
        for d in grp[g]:
            ax2.plot(d["r_mm"],np.interp(d["r_mm"],ef[:,0],ef[:,1])*80,m,ms=5.5,color=c,mec=INK,mew=0.6,zorder=5)
    ax2.text(3.3,66,"center\n~80 MV/m",ha="center",va="top",fontsize=8,color=HIGH,fontweight="bold",linespacing=1.0)
    ax2.text(13.2,66,"edge\n~69–77 MV/m",ha="center",va="top",fontsize=8,color=HIGH,fontweight="bold",linespacing=1.0)
    ax2.text(25.2,12,"periphery\n≤2.5 MV/m",ha="center",va="bottom",fontsize=8,color=PERIPH,fontweight="bold",linespacing=1.0)
    ax2.text(13.2,30,"markers = EBSD regions",ha="center",va="center",fontsize=7.5,color=MUTED)
    ax2.set_xlim(0,30); ax2.set_ylim(0,92); ax2.set_yticks([0,40,80])
    ax2.set_xticks([0,6.5,10,20,30]); ax2.set_xticklabels(["0","6.5","10","20","30"])
    ax2.set_xlabel("radial position on cathode (mm)",labelpad=1.5); ax2.set_ylabel("surface field (MV/m)",labelpad=2)
    save(fig,"geometry_efield_tiers")

# ---- frame 8: SEM with callouts, 7.4 x 4.95 cm (B7 measurements) -------------
def f08():
    sem=Image.open(f"{FIG}/sem_lowmag.png").convert("RGB").crop((0,0,1800,1195))
    fig,ax=plt.subplots(figsize=(7.4*CM,4.95*CM),dpi=300); fig.subplots_adjust(0,0,1,1); ax.imshow(sem); ax.set_axis_off()
    ax.add_patch(Rectangle((730,530),340,140,fill=False,ec=HIGH,lw=1.6))
    ax.annotate("EBSD map\n500 µm wide",xy=(1070,650),xytext=(1130,780),fontsize=8.5,fontweight="bold",color="white",
                bbox=dict(boxstyle="round,pad=0.25",fc=HIGH,ec="none"),arrowprops=dict(arrowstyle="-",color=HIGH,lw=1.4))
    for (x,y) in [(490,170),(830,220),(1420,1040)]: ax.add_patch(plt.Circle((x,y),70,fill=False,ec=REF,lw=1.4,ls="--"))
    ax.annotate("breakdown craters",xy=(560,170),xytext=(120,330),fontsize=8.5,fontweight="bold",color="white",
                bbox=dict(boxstyle="round,pad=0.25",fc=REF,ec="none"),arrowprops=dict(arrowstyle="-",color=REF,lw=1.4))
    ax.annotate("",xy=(830,220),xytext=(830,530),arrowprops=dict(arrowstyle="<->",color="white",lw=1.2))
    ax.text(850,400,"0.47 mm",color="white",fontsize=8,fontweight="bold",va="center",path_effects=[pe.withStroke(linewidth=2,foreground=INK)])
    ax.add_patch(Rectangle((60,1120),660,22,color="white"))
    ax.text(390,1105,"1 mm",ha="center",va="bottom",fontsize=9,fontweight="bold",color="white",path_effects=[pe.withStroke(linewidth=2.2,foreground=INK)])
    save(fig,"sem_lowmag_callouts",png=True)

# ---- frame 10: LAM pair at matched magnification + shared colour bar ---------
def f10():
    fe=Image.open(f"{FIG}/lam_fe_center.png").convert("RGB"); rf=Image.open(f"{FIG}/lam_ref_edge.png").convert("RGB")
    um_fe, um_rf = 200/322, 100/190; H_um, W_um = 279, 485
    fe_c=fe.crop((25,0,25+int(round(W_um/um_fe)),int(round(H_um/um_fe)))); rf_c=rf.crop((0,0,int(round(W_um/um_rf)),int(round(H_um/um_rf))))
    fig=plt.figure(figsize=(12.4*CM,5.3*CM),dpi=300)
    gs=fig.add_gridspec(2,2,height_ratios=[1,0.12],hspace=0.12,wspace=0.04,left=0.02,right=0.98,top=0.995,bottom=0.13)
    for j,(im,lab,col) in enumerate([(fe_c,"field-exposed center, ~80 MV/m",HIGH),(rf_c,"unexposed reference",REF)]):
        ax=fig.add_subplot(gs[0,j]); ax.imshow(im,extent=(0,W_um,H_um,0)); ax.set_axis_off()
        ax.add_patch(Rectangle((12,H_um-32),100,7,color=INK))
        ax.text(62,H_um-38,"100 µm",ha="center",va="bottom",fontsize=9,color="white",fontweight="bold",path_effects=[pe.withStroke(linewidth=2,foreground=INK)])
        ax.text(8,10,lab,ha="left",va="top",fontsize=9.5,fontweight="bold",color="white",bbox=dict(boxstyle="round,pad=0.25",fc=col,ec="none"))
    cax=fig.add_subplot(gs[1,:]); cax.imshow(np.linspace(0,1,256)[None,:],aspect="auto",cmap="jet",extent=(0,5,0,1))
    cax.set_yticks([]); cax.set_xticks([0,1,2,3,4,5]); cax.set_xticklabels(["0°","1°","2°","3°","4°","5°"],fontsize=8.5); cax.tick_params(length=2,pad=1)
    for s in cax.spines.values(): s.set_visible(True); s.set_linewidth(0.5)
    cax.text(0.08,0.5,"flat lattice",ha="left",va="center",fontsize=8,color="white",fontweight="bold")
    cax.text(4.92,0.5,"strongly curved",ha="right",va="center",fontsize=8,color="white",fontweight="bold")
    cax.text(2.5,0.5,"LAM, same scale for both maps",ha="center",va="center",fontsize=8,color=INK,fontweight="bold")
    save(fig,"lam_pair_matched",png=True)

# ---- frame 11: three tiers, 8.7 x 5.6 cm --------------------------------------
def f11():
    fig,ax=plt.subplots(figsize=(8.7*CM,5.6*CM),dpi=300); tier_shade(ax)
    ax.axhspan(ref_mean-ref_sem,ref_mean+ref_sem,color=REF,alpha=0.18,lw=0); ax.axhline(ref_mean,color=REF,lw=1.4,ls="--")
    for g,m in {"center":"o","edge":"s","periph":"D"}.items():
        c = HIGH if g!="periph" else PERIPH
        for d in grp[g]:
            ax.errorbar(d["r_mm"],d["mean"],yerr=d["sem_grain"],fmt=m,ms=6.5,color=c,mec=INK,mew=0.6,ecolor=c,capsize=2.5,lw=1.2,zorder=5)
    ax.text(3.5,1.31,"center\n~80 MV/m",ha="center",va="bottom",fontsize=8.5,color=HIGH,fontweight="bold",linespacing=1.0)
    ax.text(8.9,1.09,"edge\n~69–77 MV/m",ha="center",va="top",fontsize=8.5,color=HIGH,fontweight="bold",linespacing=1.0)
    ax.text(26.0,0.86,"periphery\n≤2.5 MV/m",ha="center",va="bottom",fontsize=8.5,color=PERIPH,fontweight="bold",linespacing=1.0)
    ax.text(0.6,0.715,"unexposed reference (±1 s.e.)",ha="left",va="bottom",fontsize=8.5,color=REF,fontweight="bold")
    ax.annotate("",xy=(19.2,hf_mean),xytext=(19.2,ref_mean),arrowprops=dict(arrowstyle="<->",color=INK,lw=1.1))
    ax.text(18.6,(hf_mean+ref_mean)/2+0.05,"~75%\nhigher",va="center",ha="right",fontsize=9.5,fontweight="bold",linespacing=1.0)
    
    ax.set_xlim(0,30); ax.set_ylim(0.5,1.5); ax.set_yticks([0.6,0.8,1.0,1.2,1.4])
    ax.set_xticks([0,6.5,10,20,30]); ax.set_xticklabels(["0","6.5","10","20","30"])
    ax.set_xlabel("radial position on cathode (mm)"); ax.set_ylabel("mean low-angle LAM (deg)")
    for x,t in [(3.25,"flat gap"),(13.2,"sloped anode"),(25,"beyond anode")]:
        ax.text(x,0.525,t,ha="center",va="bottom",fontsize=7.5,color=MUTED)
    fig.tight_layout(pad=0.3); save(fig,"tiers_plot")

# ---- frame 12: distributions with shaded >2 deg tail, 8.4 x 5.4 cm -----------
def f12():
    fig,ax=plt.subplots(figsize=(8.4*CM,5.4*CM),dpi=300); x=np.linspace(0.001,5,400)
    sel={"center":("FE Center ROI2",HIGH,"-"),"edge":("FE Edge ROI2",HIGH,(0,(3,1.5))),
         "periph":("FE Periphery ROI2",PERIPH,"-"),"ref":("REF Center ROI1",REF,"-")}
    for g,(lab,c,ls) in sel.items():
        d=[q for q in R if q["label"]==lab][0]
        cen=np.array(d["centers"]); cnt=np.array(d["counts"]); dens=cnt/cnt.sum()/0.1
        ax.step(cen,dens,where="mid",color=c,lw=0.8,alpha=0.45)
        pdf=G.pdf(x,d["k"],scale=d["theta"]); ax.plot(x,pdf,color=c,lw=2.0 if g!="edge" else 1.6,ls=ls)
        if g in ("center","ref"): ax.fill_between(x,0,pdf,where=x>=2,color=c,alpha=0.35 if g=="center" else 0.6,lw=0)
    ax.axvline(2,color=INK,lw=0.8,ls=":")
    ax.text(1.05,1.22,"unexposed\nreference",color=REF,fontweight="bold",fontsize=8.5,ha="left",va="top",linespacing=1.0)
    ax.text(1.22,0.86,"periphery",color=PERIPH,fontweight="bold",fontsize=8.5,ha="left",va="bottom")
    ax.text(1.55,0.60,"center (solid)\nedge (dashed)",color=HIGH,fontweight="bold",fontsize=8.5,ha="left",va="bottom",linespacing=1.0)
    ax.text(3.0,0.22,"tail above 2°:\n~14% field-exposed\n~1.6% reference",fontsize=8.5,ha="left",va="bottom",linespacing=1.05)
    ax.text(4.95,1.22,"same shape k ≈ 2.7\nscale θ: 0.24° $\\rightarrow$ 0.46°",fontsize=8,ha="right",va="top",color=MUTED,linespacing=1.05)
    ax.set_xlim(0,5); ax.set_ylim(0,1.3); ax.set_yticks([0,0.5,1.0])
    ax.set_xlabel("local average misorientation, LAM (deg)"); ax.set_ylabel("probability density")
    fig.tight_layout(pad=0.3); save(fig,"tail_plot")

# ---- frame 18: result card, 6.8 x 5.4 cm ---------------------------------------
def f18():
    fig,ax=plt.subplots(figsize=(7.0*CM,5.4*CM),dpi=300)
    labels=["center\n~80","edge\n69–77","periphery\n≤2.5","reference\n0"]
    vals=[np.mean([d["mean"] for d in grp[g]]) for g in ("center","edge","periph","ref")]
    errs=[np.sqrt(np.mean([d["sem_grain"]**2 for d in grp[g]])) for g in ("center","edge","periph","ref")]
    cols=[HIGH,HIGH,PERIPH,REF]
    ax.bar(range(4),vals,yerr=errs,color=cols,width=0.68,capsize=3,ecolor=INK,lw=0)
    for i,v in enumerate(vals): ax.text(i,v+0.06,f"{v:.2f}°",ha="center",va="bottom",fontsize=9,fontweight="bold",color=cols[i])
    ax.set_xticks(range(4)); ax.set_xticklabels(labels,fontsize=8); ax.tick_params(axis="x",length=0)
    ax.set_ylabel("mean low-angle LAM (deg)"); ax.set_ylim(0,1.65); ax.set_yticks([0,0.5,1.0,1.5])
    ax.annotate("",xy=(3,1.5),xytext=(0.5,1.5),arrowprops=dict(arrowstyle="<->",color=INK,lw=1.1))
    ax.text(1.75,1.52,"~75% higher",ha="center",va="bottom",fontsize=9.5,fontweight="bold")
    ax.text(1.5,-0.42,"MV/m",ha="center",va="top",fontsize=8,color=MUTED)
    ax.set_title("One cathode, nine EBSD regions",fontsize=9.5,loc="left",pad=4)
    fig.tight_layout(pad=0.3); save(fig,"result_card")

# optional 4th argument: comma-separated subset, e.g. f07 (3 Oct: regenerate one figure)
SEL = sys.argv[4].split(",") if len(sys.argv) > 4 else None
for f in (f07,f08,f10,f11,f12,f18):
    if SEL is None or f.__name__ in SEL: f()
OUT = {"f07":"geometry_efield_tiers.pdf","f08":"sem_lowmag_callouts.png","f10":"lam_pair_matched.png","f11":"tiers_plot.pdf","f12":"tail_plot.pdf","f18":"result_card.pdf"}
print("figures written:", ", ".join(v for k, v in OUT.items() if SEL is None or k in SEL))
