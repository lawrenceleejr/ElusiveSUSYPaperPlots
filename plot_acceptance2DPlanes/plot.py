#!/usr/bin/env python

from matplotlib_tufte import *
setup()

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import ConnectionPatch

import ROOT
import seaborn as sns

# colors = sns.color_palette("husl", 3)
colors = ["#FF595E",  "#1982C4", "#8AC926",] 
# colors = ["#E07A5F",  # Terra Cotta
# 		"#F2CC8F",  # Sand
# 		"#81B29A"]  # Sage

# colors = ["#FF0000", "#00FF00", "#0000FF"]
# colors = ["#FF6B6B", "#6BCB77", "#4D96FF"]
# colors = ["#3A86FF", "#8338EC", "#FB5607"]
# colors = ["#FF6B6B", "#4ECDC4", "#1A535C"]
# colors = ["#4477AA", "#CC6677", "#117733"]




baselength=4
fig, (ax2,ax1) = plt.subplots(2,1, figsize=(1.8*baselength, 2*1*baselength))

ax2.set_yscale('log')



def doFillBetween(x,y,n=10,dy=1,color="k",alpha=0.03,log=True,axis=ax1):
    initialY = y
    tmpy = initialY
    print(x,y)

    colorpal = sns.light_palette(color, n)[::-1]
    for i in range(n):
        if log:
            axis.fill_between(x,tmpy, [thing*dy for thing in tmpy],linewidth=0,color=colorpal[i],alpha = alpha*((n-i)/float(n) ) ,  clip_on=False)
            tmpy = [thing*dy for thing in tmpy]
        # else:
        # 	axis.fill_between(x,tmpy, [thing*dy for thing in tmpy],linewidth=0,color=colorpal[i],alpha = alpha*((n-i)/float(n) ) )
        # 	tmpy = [thing*dy for thing in tmpy]


def getArraysFromTGraph(tgraph):
    xArray, yArray = [],[]
    for iPoint in range(tgraph.GetN()):
        x,y = ROOT.Double(0), ROOT.Double(0)
        # print (x,y)
        tgraph.GetPoint(iPoint,x,y)
        xArray.append(x)
        yArray.append(y)
    # print (xArray)
    return xArray,yArray




results = {
    #xslimit in pb
    "atlas_run2_ee_selectron_300_1": {"label":r"ATL R2 Disp $ee$ (300,1)","etrig":238/870, "axe":52.2/870, "xslimit":3/36000}, #fake
    "atlas_run2_ee_selectron_500_0.1": {"label":r"ATL R2 Disp $ee$ (500,0.1)","etrig":66.3/93.6, "axe":17.7/93.6, "xslimit":3/36000}, #fake

    "atlas_run2_mumu_smuon_500_0.01": {"label":r"ATL R2 Disp $\mu\mu$ (500,0.01)","etrig":66.3/93.6, "axe":0.02/3.28, "xslimit":3.28e-3}, 
    "atlas_run2_mumu_smuon_500_0.1": {"label":r"ATL R2 Disp $\mu\mu$ (500,0.1)","etrig":66.3/93.6, "axe":13.6/93.6, "xslimit":1.49e-04}, 
    "atlas_run2_micro_mumu_smuon_500_0.01": {"label":r"+µDisp $\mu\mu$","etrig":48.2/93.6, "axe":6.7/93.6, "xslimit":0.169e-3},
    # 0.16*0.63,

    # CMS full run2: https://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-18-003/index.html
    # says trig eff somewhere between 20-40%
    "cms_run2_mumu_500_0.3": {"label":r"CMS Disp $\mu\mu$","etrig":0.4, "axe":.26, "xslimit":0.0002172},
    "cms_run2_mumu_500_3":   {"label":r"","etrig":0.4, "axe":0.23,   "xslimit":0.00017812},

    "cms_run2_mumu_500_0.1": {"label":r"","etrig":0.4, "axe":.19,   "xslimit":0.00038671},
    "cms_run2_mumu_500_1":   {"label":r"","etrig":0.4, "axe":.33,   "xslimit":0.00015616},
    "cms_run2_mumu_500_10":  {"label":r"","etrig":0.4, "axe":.13,   "xslimit":0.00038567},
    "cms_run2_mumu_500_100": {"label":r"","etrig":0.4, "axe":.0048, "xslimit":0.009802},


    # 1400 Gluino. 3.018E-02 pb * 1000 fb/pb * 36 ifb = 1086.48
    "atlas_36_0l_gluino_rjr_g2a_1400_800": {"etrig":673/1086, "axe":44.7/1086,"xslimit":0}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-07/tabaux_009.pdf
    "atlas_36_1l_stop_1000_1": {"label":r"+R2", "etrig":16881/102121, "axe":3192.5/102121,"xslimit":0.0091}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-16/
    "atlas_36_1l_stop_700_1": {"label":r"+R2","etrig":0.037, "axe":0.83*0.037,"xslimit":0.021}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-16/
    "atlas_20_8TeV_1l_stop_700_1_e": {"label":r"ATL R1 Stop $1\ell$ (700,1)","etrig":2462.9/20000, "axe":303.5/20000,"xslimit":0.01}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/

    "atlas_20_dvmet": {"label":r"ATL R1 DV+MET","etrig":0.885, "axe":.376,"xslimit":3e-4}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2014-02/figaux_10a.png 1 TeV
    # XS from https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2014-02/fig_18a.png


    #  let's compare at 3cm, 0.1ns, 1 TeV, large dm.
    "atlas_36_dvmet": {"label":r"+R2","etrig":717/827, "axe":442/827,"xslimit":1.5e-4}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-16/

    "atlas_137_dvmet": {"label":r"ATL R2 137 DV+MET","etrig":0.99, "axe":0.4,"xslimit":5e-4}, #https://www.uvic.ca/science/physics/current/masters/theses/index.php

    "atlas_137_dvjets_rpv": {"label":r"ATL R2 DV+Jets","etrig":0.966, "axe":0.577,"xslimit":0.040096/1000}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-13/tabaux_05.png
    # 1500,0.1


    "cms_137_dijet": {"label":r"CMS R2 Dijet","etrig":1, "axe":0.5,"xslimit":2e-2/0.5}, 


    "atlas_36_rpvmultijet": {"label":r"ATL R2 RPV Jets","etrig":0.997, "axe":3.9/99.8,"xslimit":1.5e-2}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-22/
    # 6 jet, 1800
    "atlas_140_rpvmultijet": {"label":r"ATL R2 140 RPV Jets","etrig":1.0, "axe":12/410,"xslimit":4.5e-3}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-22/
    # 6 jet, 1800


    "atlas_1_dt": {"label":r"ATL R1 DT","etrig":0.902, "axe":0.068,"xslimit":3.5e-2},
    # 1 ns
    "atlas_20_dt": {"label":r"+20 ifb","etrig":0.088, "axe":0.00087,"xslimit":1},
    "atlas_36_dt": {"label":r"+R2","etrig":0.2, "axe":0.0038,"xslimit":0.11},
    "atlas_139_dt": {"label":r"+Full R2","etrig":770/2800, "axe":8.6/2800,"xslimit":0.037},


}

### Actual Curves:

#
i=0


# ax.plot( [0.8], [0.9], "o", label="Run-2 X Ana")
doFillBetween([0,1], [0,1], axis=ax1, dy=0.99, alpha=0.2, n=100)
ax1.plot([0,1], [0,1], c="k",lw=0.5)

# perfect analysis would exclude 3 events for a given dataset.
# for 139 ifb, this corresponds to a cross section of 3/139 fb
# xs*(axe=1)*lumi=3
# 3/lumi = xs limit
x = np.linspace(0.001,1,1000)
for lumibenchmark in [36,139]: #0.1 for test
    doFillBetween(x, 3/(lumibenchmark*1000*x), axis=ax2, dy=0.994, alpha=0.2, n=200)
    # doFillBetween([0,1], [3/(lumibenchmark*1000),3/(lumibenchmark*1000)], axis=ax2, dy=0.994, alpha=0.2, n=200)

    ax2.plot(x, 3/(lumibenchmark*1000*x),c="k",lw=0.5)
    ax2.plot([0,1], [3/(lumibenchmark*1000),3/(lumibenchmark*1000)],"--",c="k",lw=0.5)
    ax2.text(0.98, 3/(lumibenchmark*1000)*0.65 , f"Minimum for {lumibenchmark} fb"+r"${}^{-1}$", size=9,clip_on=False, ha="right")
    # this should actually scale with A*e!!!
    # Will be some curve upwards






listtoplot = [
    "atlas_20_8TeV_1l_stop_700_1_e",
    # "atlas_36_1l_stop_1000_1",
    "atlas_36_1l_stop_700_1",

    # "atlas_run2_ee_selectron_300_1",
    # "atlas_run2_ee_selectron_500_0.1",
    # "cms_run2_ee_selectron_500_1cm",
    "atlas_run2_mumu_smuon_500_0.01",
    "atlas_run2_micro_mumu_smuon_500_0.01",
    # Add newer trigger for run 3
    "cms_run2_mumu_500_0.3",

    "atlas_run2_mumu_smuon_500_0.1",
    "cms_run2_mumu_500_3",   

    # "cms_run2_mumu_500_0.1", 
    # "cms_run2_mumu_500_1",   
    # "cms_run2_mumu_500_10",  
    # "cms_run2_mumu_500_100", 


    # disappearing track evolution?

    "atlas_20_dvmet",
    "atlas_36_dvmet", #fix numbers (were made up)
    "atlas_137_dvmet",
    # Add DV+jets since it's full dataset

    # Some EWK evolution?

    # Dijet search to fill in upper right? Or RPV?

    # 3 TeV quark quark
    # CMS https://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-19-012/
    # States Axe ~ 0.5
    # Gives upper limit xs
    # Trigger efficiency assumed to be 1 as stated in paper
    "cms_137_dijet",

    # RPV 1L+jets for higgsinos
    # DV for RPV Higgsinos

    "atlas_137_dvjets_rpv",

    "atlas_36_rpvmultijet",
    "atlas_140_rpvmultijet",

    # different masses of normal dijet. see TLA turn on
    

    # prompt sleptons near the diagonal should be in the upper left. show a train of them going to increasing dM


    # "atlas_1_dt",
    # 1 ns
    # "atlas_20_dt",
    "atlas_36_dt",
    "atlas_139_dt",




]

arrows = [
    ("atlas_20_8TeV_1l_stop_700_1_e","atlas_36_1l_stop_700_1",""),
    ("atlas_20_dvmet","atlas_36_dvmet",""),
    ("atlas_36_dvmet","atlas_137_dvmet",""),
    ("atlas_run2_mumu_smuon_500_0.01", "atlas_run2_micro_mumu_smuon_500_0.01",""),
    ("atlas_36_rpvmultijet","atlas_140_rpvmultijet",""),

]



lines = [
    ("cms_run2_mumu_500_0.3","atlas_run2_mumu_smuon_500_0.01",""),
    ("cms_run2_mumu_500_3","atlas_run2_mumu_smuon_500_0.1",""),
]



for key1,key2,label in arrows:

    ax1.annotate("",
        xy=(results[key2]["axe"],results[key2]["etrig"]),
        xytext=(results[key1]["axe"],results[key1]["etrig"]),
        arrowprops=dict(arrowstyle="-|>", color='black', lw=1.5)
    )
    ax2.annotate("",
        xy=(results[key2]["axe"],results[key2]["xslimit"]),
        xytext=(results[key1]["axe"],results[key1]["xslimit"]),
        arrowprops=dict(arrowstyle="-|>", color='black', lw=1.5)
    )

    # ax1.plot( [results[key1]["axe"],results[key2]["axe"]], [results[key1]["etrig"],results[key2]["etrig"]], "-", label=label, c="k",lw=1.5)
    # ax2.plot( [results[key1]["axe"],results[key2]["axe"]], [results[key1]["xslimit"],results[key2]["xslimit"]], "-", label=label, c="k",lw=1.5)


for key1,key2,label in lines:

    ax1.annotate("",
        xy=(results[key2]["axe"],results[key2]["etrig"]),
        xytext=(results[key1]["axe"],results[key1]["etrig"]),
        arrowprops=dict(arrowstyle="-", color='black', lw=1.5)
    )
    ax2.annotate("",
        xy=(results[key2]["axe"],results[key2]["xslimit"]),
        xytext=(results[key1]["axe"],results[key1]["xslimit"]),
        arrowprops=dict(arrowstyle="-", color='black', lw=1.5)
    )

for key in listtoplot:

    con = ConnectionPatch(xyA=(results[key]["axe"], results[key]["etrig"]),
                        xyB=(results[key]["axe"], results[key]["xslimit"]),
                        coordsA="data", coordsB="data",
                        axesA=ax1, axesB=ax2, color="k", lw=0.1, alpha=0.15)
    con.set_zorder(-100)
    # ax1.add_artist(con)
    ax2.add_artist(con)
    ax1.set_zorder(-1)

    if "atlas" in key:
        marker = "o"
    elif "cms" in key:
        marker = "^"
    ax1.plot( [results[key]["axe"]], [results[key]["etrig"]], marker, label=results[key]["label"], mew=0.5, mec="k", clip_on=False, zorder=100)
    ax2.plot( [results[key]["axe"]], [results[key]["xslimit"]], marker, label=results[key]["label"], mew=0.5, mec="k", clip_on=False, zorder=100)

# Run-2 ATLAS Displaced Leptons (ee channel, selectron (300,1))
# ax.plot( [results["atlas_run2_ee_selectron_300_1"]["axe"]], [results["atlas_run2_ee_selectron_300_1"]["etrig"]], "o", label=r"Run-2 Displaced $ee$, $m, \tau = (300 GeV, 1 ns)$ ")
# ax.plot( [results["atlas_run2_ee_selectron_500_0.1"]["axe"]], [results["atlas_run2_ee_selectron_500_0.1"]["etrig"]], "o", label=r"Run-2 Displaced $ee$, $m, \tau = (500 GeV, 0.1 ns)$ ")

# Stop 1L
# ax.plot( [results["atlas_20_8TeV_1l_stop_700_1_e"]["axe"]], [results["atlas_20_8TeV_1l_stop_700_1_e"]["etrig"]], "o", label=r"Run-1 Stop 1L ")
# ax.plot( [results["atlas_36_1l_stop_1000_1"]["axe"]], [results["atlas_36_1l_stop_1000_1"]["etrig"]], "o", label=r"Run-2 Stop 1L ")

# ax.plot( [results["atlas_36_0l_gluino_rjr_g2a_1400_800"]["axe"]], [results["atlas_36_0l_gluino_rjr_g2a_1400_800"]["etrig"]], "o", label=r"Run-2 Gluino 0L RJR ")
# ax.plot( [results["atlas_36_1l_stop_1000_1"]["axe"]], [results["atlas_36_1l_stop_1000_1"]["etrig"]], "o", label=r"Run-2 Stop 1L ")


# Run-2 ATLAS Displaced Leptons (\mu\mu channel, selectron (300,1))
# ax.plot( [549.9/870], [238/870], "o", label=r"Run-2 Displaced $\mu\mu$, $m, \tau = (300 GeV, 1 ns)$ ")

# Higgsino DT

# HL-LHC Projection https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PUBNOTES/ATL-PHYS-PUB-2018-031/
# ATLAS 36 https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-06/tab_02.png



maxxvalue = 1

for line in ax2.get_lines():
    label = line.get_label()
    if label.startswith('_'):  # Ignore default/empty labels
        continue
    xdata, ydata = line.get_data()
    if xdata[0]<0.7:
        ha="left"
        xoffset = 5
    else:
        ha="right"
        xoffset = -5
    ax2.annotate(label,
                xy=(xdata[0], ydata[0]),
                xytext=(xoffset, 5),
                textcoords='offset points',
                fontsize=9,
                ha=ha)


ax1.set_xlabel(r'$A\times\varepsilon$',)
ax1.set_ylabel(r'$\varepsilon_{\text{trigger}}$',)
ax1.set_ylim([0,1])
ax1.set_xlim([-0.00,maxxvalue])

ax2.set_xlabel(r'$A\times\varepsilon$',)
ax2.set_ylabel(r'95% CL Excluded Cross Section [pb]',)
ax2.set_ylim([1e-5,0.1])
ax2.set_xlim([-0.00,maxxvalue])



# ax.text(200, 2050,       r"Sparticle Limits, Strong Production", size=11,clip_on=False, fontweight="bold")
# ax.text(200, 2050-1*150, r"Various Assumptions", size=11,clip_on=False)
# ax.text(200, 2050-2*150, r"Run-2 LHC", size=11,clip_on=False)

# ax.text(1700, 1000, r"Gluinos", size=11,clip_on=False, color="k", alpha=0.6, fontweight='bold')
# ax.text(1000, 500, r"Squarks", size=11,clip_on=False,  color="k", alpha=0.6, fontweight='bold')


breathe(ax1)
breathe(ax2)

# ax1.margins(x=0.1, y=0.2)


plt.subplots_adjust(top=0.95, bottom=0.1, left=0.15, right=0.95)

# Force figure to render, so transforms are accurate
fig.canvas.draw()

# Transform from data to display coordinates
p0 = ax1.transData.transform((0, 0))
p1 = ax1.transData.transform((1, 1))

# Compute angle in screen/display space
dx, dy = p1 - p0
angle_rad = np.arctan2(dy, dx)
angle_deg = np.degrees(angle_rad)

# ax1.text(100, 160, r"Forbidden", size=9,clip_on=False, rotation=angle_deg, ha='left', va='bottom')
# ax1.plot( [0,1], [0,1], "--", lw=0.5, color="black" )
# doFillBetween([0,1], [0,1], axis=ax1, dy=0.99, alpha=0.5, n=100)


ax1.text(0.6, 0.25 , r"SUSY Analysis Features", size=11,clip_on=False, fontweight="bold")
ax1.text(0.6, 0.25-0.05, r"Various Assumptions", size=11,clip_on=False)
ax1.text(0.6, 0.25-0.10, r"Run-1/2/3 LHC", size=11,clip_on=False)




fig.savefig("Axe.pdf")
# plt.show()