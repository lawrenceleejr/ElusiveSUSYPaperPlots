#from matplotlib_tufte import *
#setup()

import matplotlib.font_manager as fm
fm.fontManager.addfont("../fonts/MyriadPro-Regular.ttf")
fm.fontManager.addfont("../fonts/MyriadPro-Bold.ttf")
from matplotlib import rcParams
rcParams['font.family'] = 'Myriad Pro'

import matplotlib.pyplot as plt
import numpy as np

import ROOT
#import seaborn as sns

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
from matplotlib.colors import to_rgba

import sys
sys.path.insert(0, "..")
from helperFunctions import *

colors = ["#FF595E",  "#1982C4", "#8AC926", "#F2CC8F"] 
colors = [coolorPalette[12],coolorPalette[6],coolorPalette[2],coolorPalette[8]]

data = {}

data["stau_dl_atlas_140"] = np.genfromtxt("data/HEPData-ins1831504-v1-Observed_stau_limits.csv", delimiter=",", skip_header=8, names=["x","y"])
data["stau_ditrack_atlas_140"] = np.genfromtxt("data/HEPData-ins2878503-v1-Figure_fig_13a_obs_d1s.csv", delimiter=",", skip_header=12, names=["x","y"])
data["atlas_sketchy"] = np.genfromtxt("data/atlas_sketchy.txt", delimiter=",", skip_header=12, names=["x","y"])

data["stau_dl_cms_113"] = np.genfromtxt("data/HEPData-ins1940976-stau.csv", delimiter=",", skip_header=9, names=["y","x"])
data["stauLR_cms_lt_101"] = np.genfromtxt("data/cms_stauLR_lt.txt", delimiter=",", skip_header=2, names=["x","y"])

data["stauR_cms_lt_101"] = np.genfromtxt("data/cms_stauR_lt.txt", delimiter=",", skip_header=2, names=["x","y"])
data["stauR_cms_lt_7"] = np.genfromtxt("data/cms_stauR_7_lt.txt", delimiter=",", skip_header=2, names=["x","y"])

data["stauR_lep_lt"] = np.genfromtxt("data/lep_stauR_lt.txt", delimiter=",", skip_header=2, names=["y","x"])

baselength=4
fig, ax = plt.subplots(1,1, figsize=(1.5*baselength, 1*baselength))
                       
### Actual Curves:

i=2
alpha=0.4

ax.set_ylim([0.01,5000])
#ax.set_yscale('symlog',base=10,linthresh=2)
ax.set_yscale('log')

ax.fill((data["stau_dl_atlas_140"]['x']),(data["stau_dl_atlas_140"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.text(400,5, r"A2 140 fb${}^{-1}$" , rotation=10, size=7,clip_on=False)

ax.fill((data["stau_dl_cms_113"]['x']),(data["stau_dl_cms_113"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.text(100,10, r"C2 113 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)


i=3

ax.fill((data["stau_ditrack_atlas_140"]['x']),(data["stau_ditrack_atlas_140"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.text(200,0.03, r"A2 140 fb${}^{-1}$" , rotation=5, size=7,clip_on=False)
ax.fill((data["atlas_sketchy"]['x']),(data["atlas_sketchy"]['y']), facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='...')


i=0

ax.fill((data["stauLR_cms_lt_101"]['x']),(data["stauLR_cms_lt_101"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.text(500,10, r"C2 101 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)


ax.fill((data["stauR_cms_lt_101"]['x']),(data["stauR_cms_lt_101"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.fill((data["stauR_cms_lt_101"]['x']),(data["stauR_cms_lt_101"]['y']), facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
ax.text(500,1000, r"C2 101 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)

ax.fill((data["stauR_cms_lt_7"]['x']),(data["stauR_cms_lt_7"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.fill((data["stauR_cms_lt_7"]['x']),(data["stauR_cms_lt_7"]['y']), facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
ax.text(500,1000, r"C1 5 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)

i=1

ax.fill((data["stauR_lep_lt"]['x']),(data["stauR_lep_lt"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.fill((data["stauR_lep_lt"]['x']),(data["stauR_lep_lt"]['y']), facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
#ax.text(500,1000, r"C2 101 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)

#ax.fill((data["lep_stauR_stable"]['x']), (data["lep_stauR_stable"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
#ax.fill((data["lep_stauR_stable"]['x']), (data["lep_stauR_stable"]['y']), "--", facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')

ax.set_xlabel(r'$m_{\tilde{\tau}}$ [GeV]',)
ax.set_ylabel(r'$\tilde{\tau}$ Lifetime [ns]',)

#ax.set_ylim([0.100,550])
ax.set_xlim([45,700])

# plt.subplots_adjust(wspace=0.03)

#plt.axline((0,0), slope=1, linestyle='--', color='k')


####### y-axis break
from matplotlib.ticker import FixedLocator, FixedFormatter

break_y = 3000  # position of the visual break
stable_y = break_y  # top major tick labeled "stable"

# Major ticks below the break + "stable" at the break
lower_ticks = [0.01, 0.1, 1, 10, 100, 1000]
yticks = lower_ticks + [stable_y]
ax.set_yticks(yticks)

# Tick labels: numeric below, "stable" at top
yticklabels = [f"$10^{int(np.log10(t))}$" for t in lower_ticks] + ["stable"]
ax.set_yticklabels(yticklabels)

# Turn off minor ticks
ax.minorticks_off()

from matplotlib.ticker import LogFormatterMathtext
formatter = LogFormatterMathtext(base=10.0)
ax.yaxis.set_major_formatter(formatter)

# After plotting, manually set the last label
yticks = ax.get_yticks()
yticklabels = [formatter(tick) for tick in yticks]
yticklabels[-1] = "stable"  # replace top tick
ax.set_yticklabels(yticklabels)

ax.hlines(y=1000, xmin=ax.get_xlim()[0], xmax=ax.get_xlim()[1],
          linestyles="--", colors="gray", linewidth=1)

##############

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


#ax.text(100, 500,       r"Stau Limits", size=11,clip_on=False, fontweight="bold")
#ax.text(100, 465,       r"$\tilde{\tau}\tilde{\tau}, \tilde{\tau}\rightarrow \tau \tilde{G}$", size=11,clip_on=False, fontweight="bold")
#ax.text(50, 10**(1.20-1*0.09), r"Various Assumptions", size=11,clip_on=False, ha="right")
#ax.text(100, 430, r"LEP, Run-1 LHC, Run-2 LHC", size=11,clip_on=False)
#ax.text(100, 395, r"95% CL", size=11,clip_on=False)

#ax.text(350, 10**-0.48,       r"Decoupled $\tilde{W}, \tilde{B}$", size=9,clip_on=False, ha="right")

#ax.text(220, 10**0.4,       r"Soft Leptons", size=11,clip_on=False, fontweight="bold")
#ax.text(205, 10**-0.2,       r"Soft Displaced Track", size=11,clip_on=False, fontweight="bold")
#ax.text(100, 10**-0.71,       r"Disappearing Track", size=11,clip_on=False, fontweight="bold")

#ax.text(490, 300,       r"Taus + $p_T^{miss}$", size=11,clip_on=False, fontweight="bold")
#ax.text(45, 90,       r"LEP", size=11,clip_on=False, fontweight="bold")
ax.text(350, 0.1,       r"Displaced Leptons", size=11,clip_on=False, fontweight="bold")
ax.text(525, 500,       r"Anomalous Ionization", size=11,clip_on=False, fontweight="bold")

breathe_logy(ax)


# Force figure to render, so transforms are accurate
fig.subplots_adjust(left=0.15, right=0.93, bottom=0.18, top=0.96)
fig.canvas.draw()

plt.show()

fig.savefig("sleptons.pdf")
# plt.show()
