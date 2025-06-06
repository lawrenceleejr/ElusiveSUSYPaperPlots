from matplotlib_tufte import *
setup()

import matplotlib.pyplot as plt
import numpy as np

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
fig, ax = plt.subplots(1,1, figsize=(1.5*baselength, 1*baselength))


def doFillBetween(x,y,n=10,dy=1,color="k",alpha=0.03,log=True,axis=ax):
	initialY = y
	tmpy = initialY

	colorpal = sns.light_palette(color, n)[::-1]
	for i in range(n):
		if log:
			axis.fill_between(x,tmpy, [thing*dy for thing in tmpy],linewidth=0,color=colorpal[i],alpha = alpha*((n-i)/float(n) ) )
			tmpy = [thing*dy for thing in tmpy]


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
	"atlas_run2_ee_selectron_300_1": {"etrig":238/870, "axe":52.2/870, "sig":0},
	# 1400 Gluino. 3.018E-02 pb * 1000 fb/pb * 36 ifb = 1086.48
	"atlas_36_0l_gluino_rjr_g2a_1400_800": {"etrig":673/1086, "axe":44.7/1086,"sig":0}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-07/tabaux_009.pdf
	"atlas_36_1l_stop_1000_1": {"etrig":16881/102121, "axe":3192.5/102121,"sig":0}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/
	"atlas_20_8TeV_1l_stop_700_1_e": {"etrig":2462.9/20000, "axe":303.5/20000,"sig":0}, #https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/

}

### Actual Curves:

#
i=0


ax.plot( [0.8], [0.9], "o", label="Run-2 X Ana")

# Run-2 ATLAS Displaced Leptons (ee channel, selectron (300,1))
ax.plot( [results["atlas_run2_ee_selectron_300_1"]["axe"]], [results["atlas_run2_ee_selectron_300_1"]["etrig"]], "o", label=r"Run-2 Displaced $ee$, $m, \tau = (300 GeV, 1 ns)$ ")


# Stop 1L
ax.plot( [results["atlas_20_8TeV_1l_stop_700_1_e"]["axe"]], [results["atlas_20_8TeV_1l_stop_700_1_e"]["etrig"]], "o", label=r"Run-1 Stop 1L ")
ax.plot( [results["atlas_36_1l_stop_1000_1"]["axe"]], [results["atlas_36_1l_stop_1000_1"]["etrig"]], "o", label=r"Run-2 Stop 1L ")



# Run-2 ATLAS Displaced Leptons (\mu\mu channel, selectron (300,1))
# ax.plot( [549.9/870], [238/870], "o", label=r"Run-2 Displaced $\mu\mu$, $m, \tau = (300 GeV, 1 ns)$ ")

# Higgsino DT

# HL-LHC Projection https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PUBNOTES/ATL-PHYS-PUB-2018-031/
# ATLAS 36 https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-06/tab_02.png

for line in ax.get_lines():
    label = line.get_label()
    if label.startswith('_'):  # Ignore default/empty labels
        continue
    xdata, ydata = line.get_data()
    ax.annotate(label,
                xy=(xdata[0], ydata[0]),
                xytext=(5, 5),
                textcoords='offset points',
                fontsize=9)




ax.set_xlabel(r'$A\times\varepsilon$',)
ax.set_ylabel(r'$\varepsilon_{trigger}$',)
# ax.xaxis.set_label_coords(1.02, -0.07)
# ax.set_ylabel(r'Excluded Stop Squark Mass $m_{\tilde{t}}$ [GeV]')
# ax.set_xlim([2e-6,2e4])
# ax2.set_xlim([1.1e13,9e18])
ax.set_ylim([0,1])
ax.set_xlim([0,1])
# plt.grid()


# plt.subplots_adjust(wspace=0.03)


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


# ax.text(200, 2050,       r"Sparticle Limits, Strong Production", size=11,clip_on=False, fontweight="bold")
# ax.text(200, 2050-1*150, r"Various Assumptions", size=11,clip_on=False)
# ax.text(200, 2050-2*150, r"Run-2 LHC", size=11,clip_on=False)

# ax.text(1700, 1000, r"Gluinos", size=11,clip_on=False, color="k", alpha=0.6, fontweight='bold')
# ax.text(1000, 500, r"Squarks", size=11,clip_on=False,  color="k", alpha=0.6, fontweight='bold')


breathe(ax)


# Force figure to render, so transforms are accurate
fig.canvas.draw()

# Transform from data to display coordinates
p0 = ax.transData.transform((0, 0))
p1 = ax.transData.transform((1, 1))

# Compute angle in screen/display space
dx, dy = p1 - p0
angle_rad = np.arctan2(dy, dx)
angle_deg = np.degrees(angle_rad)

ax.text(100, 160, r"Forbidden", size=9,clip_on=False, rotation=angle_deg, ha='left', va='bottom')
ax.plot( [0,2500], [0,2500], "--", lw=0.5, color="black" )



fig.savefig("TrigVsAe.pdf")
plt.show()