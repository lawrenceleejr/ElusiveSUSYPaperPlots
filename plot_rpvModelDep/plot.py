from matplotlib_tufte import *
setup()

import matplotlib.font_manager as fm
fm.fontManager.addfont("../fonts/MyriadPro-Regular.ttf")
fm.fontManager.addfont("../fonts/MyriadPro-Bold.ttf")
from matplotlib import rcParams
rcParams['font.family'] = 'Myriad Pro'


import matplotlib.pyplot as plt
import numpy as np

import ROOT
import seaborn as sns
import csv
from array import array

import sys
sys.path.insert(0, "..")
from helperFunctions import *


# colors = sns.color_palette("husl", 3)
# colors = ["#FF595E",  "#1982C4", "#8AC926",] 
colors = ["#E07A5F",  # Terra Cotta
		"#81B29A",
		"#F2CC8F",  # Sand
        ]  # Sage

# colors = ["#FF0000", "#00FF00", "#0000FF"]
# colors = ["#FF6B6B", "#6BCB77", "#4D96FF"]
# colors = ["#3A86FF",  "#FB5607","#8338EC",]
# colors = ["#FF6B6B","#1A535C", "#4ECDC4", ]
# colors = ["#4477AA", "#CC6677", "#117733"]


baselength=4
ax = [0,0]
fig1, ax[0] = plt.subplots(1,1, figsize=(1.5*baselength, 1*baselength))
fig2, ax[1] = plt.subplots(1,1, figsize=(1.5*baselength, 1*baselength))


data = {}
data["rpv1l"] = np.genfromtxt("data/rpv1l.txt", delimiter=",", skip_header=0, names=["x","y"])
data["multib"] = np.genfromtxt("data/multib.txt", delimiter=",", skip_header=0, names=["x","y"])

data["0l"] =  np.genfromtxt("data/0l.txt", delimiter=",", skip_header=0, names=["x","y"])

data["rpv1l_trunc"] = data["rpv1l"][data['rpv1l']['x'] <= 4e-2]
data["multib_trunc"] = data["multib"][data['multib']['x'] <= 4e-2]



# Create empty lists to hold x and y values
x_vals = []
y_vals = []

# Read CSV file
with open("data/gluinoxs.txt", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) < 2:
            continue  # skip incomplete rows
        try:
            x = float(row[0])
            y = float(row[1])
            x_vals.append(x)
            y_vals.append(y)
        except ValueError:
            continue  # skip rows with non-numeric data

# Create TGraph
x_arr = array('d', x_vals)
y_arr = array('d', y_vals)
xsgraph = ROOT.TGraph(len(x_vals), x_arr, y_arr)


def getXSFromMass(mass):
      return xsgraph.Eval(mass)

def invert_graph(graph):
    n = graph.GetN()
    x = graph.GetX()
    y = graph.GetY()
    return ROOT.TGraph(n, array('d', y), array('d', x))  # swapped

# Invert and interpolate
inverted_xsgraph = invert_graph(xsgraph)

def getMassFromXS(xs):
    return inverted_xsgraph.Eval(xs)      

def arrXSFromMass(arr):
      return [getXSFromMass(x) for x in arr]
def arrMassFromXS(arr):
      return [getMassFromXS(x) for x in arr]




ax[0].plot( (data["rpv1l"]["x"]), data["rpv1l"]["y"], lw=2 , c=colors[0], zorder=0)
ax[0].plot( (data["multib"]["x"]), data["multib"]["y"], lw=2 , c=colors[1],zorder=0)



ax[1].plot( (data["rpv1l"]["x"]), data["rpv1l"]["y"], lw=2 , c=colors[0], zorder=0)
ax[1].plot( (data["multib"]["x"]), data["multib"]["y"], lw=2 , c=colors[1],zorder=0)





# if split evenly with 112
# it will double the cross section limit (make it weaker)

reductionfactor=2

# Since RPV1L cares about getting a prompt lepton, and doesn't care about MET, as soon as there's another component to the chi decay, it loses sensitivity. Since there are two decays, this is reduced by a factor of 4. Since it now has two decay modes, the lifetime is halved.
tmpx = ([x/(reductionfactor) for x in data["rpv1l_trunc"]["x"]])
tmpy = [x*reductionfactor*reductionfactor for x in arrXSFromMass(data["rpv1l_trunc"]["y"])]
tmpy = arrMassFromXS(tmpy)
ax[0].plot( tmpx, tmpy, "--", lw=1.5 , c=colors[0])

doFillBetween(tmpx, tmpy, axis=ax[0], dy=0.99, alpha=0.2, n=50, color=colors[0])


# But on the right side, you don't get a shift since it's all prompt. You do get that same factor 4 reduction in the BR.
newMass = getMassFromXS(getXSFromMass(data["rpv1l"]["y"][-1])*4)
ax[0].plot( 
      [tmpx[-1],data["rpv1l"]["x"][-1]], 
      [tmpy[-1],newMass], 
      ":", lw=1.5 , c="k", alpha=0.3)

# Multi-b on the other hand... it mostly has sensitivity on the left from the chi escapes. So it's affected by the change in lifetime. But since the b's are coming from the prompt Gtt tops, there's no reduction in the upper limit.
tmpx = ([x/reductionfactor for x in data["multib_trunc"]["x"]])
tmpy = [x for x in arrXSFromMass(data["multib_trunc"]["y"])]
tmpy = arrMassFromXS(tmpy)
ax[0].plot( tmpx, tmpy, "--",lw=1.5 , c=colors[1])

doFillBetween(tmpx, tmpy, axis=ax[0], dy=0.99, alpha=0.2, n=50, color=colors[1])

newMass = getMassFromXS(getXSFromMass(data["multib"]["y"][-1])*4)
ax[0].plot( 
      [tmpx[-1],data["multib"]["x"][-1]], 
      [tmpy[-1],newMass], 
      ":", lw=1.5 , c="k", alpha=0.3)





# if this only represents 10% of the total width...
reductionfactor=10

# Since RPV1L cares about getting a prompt lepton, and doesn't care about MET, as soon as there's another component to the chi decay, it loses sensitivity. Since there are two decays, this is reduced by a factor of 4. Since it now has two decay modes, the lifetime is halved.
tmpx = ([x/(reductionfactor) for x in data["rpv1l_trunc"]["x"]])
tmpy = [x*reductionfactor*reductionfactor for x in arrXSFromMass(data["rpv1l_trunc"]["y"])]
tmpy = arrMassFromXS(tmpy)
ax[1].plot( tmpx, tmpy, "--", lw=1.5 , c=colors[0])

doFillBetween(tmpx, tmpy, axis=ax[1], dy=0.99, alpha=0.2, n=50, color=colors[0])


# But on the right side, you don't get a shift since it's all prompt. You do get that same factor 4 reduction in the BR.
newMass = getMassFromXS(getXSFromMass(data["rpv1l"]["y"][-1])*100)
ax[1].plot( 
      [tmpx[-1],data["rpv1l"]["x"][-1]], 
      [tmpy[-1],newMass], 
      ":", lw=1.5 , c="k", alpha=0.3)

# Multi-b on the other hand... it mostly has sensitivity on the left from the chi escapes. So it's affected by the change in lifetime. But since the b's are coming from the prompt Gtt tops, there's no reduction in the upper limit.
tmpx = ([x/reductionfactor for x in data["multib_trunc"]["x"]])
tmpy = [x for x in arrXSFromMass(data["multib_trunc"]["y"])]
tmpy = arrMassFromXS(tmpy)
ax[1].plot( tmpx, tmpy, "--",lw=1.5 , c=colors[1])

doFillBetween(tmpx, tmpy, axis=ax[1], dy=0.99, alpha=0.2, n=50, color=colors[1])


newMass = getMassFromXS(getXSFromMass(data["multib"]["y"][-1])*100)
ax[1].plot( 
      [tmpx[-1],data["multib"]["x"][-1]], 
      [tmpy[-1],newMass], 
      ":", lw=1.5 , c="k", alpha=0.3)







# And when you turn on 112, you start to get limits from 0L. This similarly uses the chi escaping the detector, so only the lifetime change is relevant.
# But the problem is in that analysis, the 
# Nevermind -- this actually doens't do anything. No idea what the Gtt eff is for 0L instead of the Gqq.
# tmpx = ([x/reductionfactor for x in data["0l"]["x"]])
# tmpy = [x for x in arrXSFromMass(data["0l"]["y"])]
# tmpy = arrMassFromXS(tmpy)
# ax[0].plot( tmpx, tmpy, "--",lw=1.5 , c=colors[2])




# 






ax[0].set_xlabel(r'$\lambda^{\prime\prime}_{323}$',)
ax[0].set_ylabel(r'$m(\tilde{g})$ [GeV]',)
ax[0].set_xlim([5e-4,1])
ax[0].set_ylim([1000,2400])

ax[1].set_xlabel(r'$\lambda^{\prime\prime}_{323}$',)
ax[1].set_ylabel(r'$m(\tilde{g})$ [GeV]',)
ax[1].set_xlim([5e-4,1])
ax[1].set_ylim([1000,2400])

# # ax[0].spines['bottom'].set_visible(False)
# ax[0].xaxis.set_ticks_position('none')  # Optional: hide the ticks
# ax[0].tick_params(bottom=False)     
# ax[0].set_xticklabels([])
# ax[0].set_xlabel("")


# ax[0].set_xlabel(r'$\lambda^{\prime\prime}_{323}=\lambda^{\prime\prime}_{112}$',)
# ax[0].set_ylabel(r'$m(\tilde{g})$ [GeV]',)
# ax[0].set_xlim([-3.2,0])
# ax[0].set_ylim([1000,2500])


ax[0].set_xscale('log')
ax[1].set_xscale('log')



ax[0].text(-0., 2400,       r"Limits on RPV SUSY, ATLAS", size=11,clip_on=False, ha="right", fontweight="bold")
ax[0].text(-0., 2400-1*80, r"RPV Model Dependence", size=11,clip_on=False, ha="right")


ax[0].text(-3.45, 1200, r"$\Gamma_{\tilde{\chi}^0_1}\  (\lambda^{\prime\prime}_{323})=50\%$", size=13,clip_on=False,  color="k", alpha=1, fontweight='bold')

ax[1].text(-3.45, 1400, r"$\Gamma_{\tilde{\chi}^0_1}\  (\lambda^{\prime\prime}_{323})=10\%$", size=13,clip_on=False,  color="k", alpha=1, fontweight='bold')



ax[1].text(-2.0, 1800, r"$\Gamma_{\tilde{\chi}^0_1}\  (\lambda^{\prime\prime}_{323})=100\%$", size=13,clip_on=False,  color="k", alpha=1, fontweight='bold')

ax[0].text(-0.5, 1450, r"$≥3$ b-jets", size=11,clip_on=False,  color="k", alpha=1, fontweight='bold')
ax[0].text(-0.5, 2100, r"$1\ell$+jets", size=11,clip_on=False,  color="k", alpha=1, fontweight='bold')



breathe_logx(ax[0])
breathe_logx(ax[1])

fig1.subplots_adjust(left=0.15, right=0.96, bottom=0.18, top=0.95)
fig2.subplots_adjust(left=0.15, right=0.96, bottom=0.18, top=0.95)
# Force figure to render, so transforms are accurate
# fig.canvas.draw()

# ax[1].set_xticklabels([
#       r"$10^{-3.5}$",
#       r"$10^{-3}$",
#       r"$10^{-2.5}$",
#       r"$10^{-2}$",
#       r"$10^{-1.5}$",
#       r"$10^{-1}$",
#       r"$10^{-0.5}$",
#       r"$10^{-0}$",
# ])

fig1.savefig("RPVModelDep_2.pdf")
fig2.savefig("RPVModelDep_10.pdf")
# plt.show()