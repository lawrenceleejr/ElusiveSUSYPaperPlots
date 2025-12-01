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

colors = [coolorPalette[12],coolorPalette[6],coolorPalette[2],coolorPalette[8],coolorPalette[4]]

data = {}

data["stau_prompt_atlas_140"] = np.genfromtxt("data/HEPData-ins2754043-v1-Table_13.csv", delimiter=",", skip_header=10, names=["x","y"])
data["stau_prompt_atlas_dm"] = m1_dm(data["stau_prompt_atlas_140"])
data["stauR_prompt_atlas_140"] = np.genfromtxt("data/HEPData-ins2754043-v1-Table_25.csv", delimiter=",", skip_header=10, names=["x","y"])
data["stauR_prompt_atlas_dm"] = m1_dm(data["stauR_prompt_atlas_140"])
#print(data["stau_prompt_atlas_dm"])

data["lep_stauR"] = np.genfromtxt("data/lep_stauR.txt", delimiter=" ", skip_header=1, names=["x","y"])
data["lep_stauR_dm"] = m1_dm(data["lep_stauR"])
#print(data["lep_stauR_dm"])

data["lep_stauR_stable"] = np.genfromtxt("data/lep_stauR_stable.txt", delimiter=" ", skip_header=3, names=["x","y"])

data["cms_7_stauR_stable"] = np.genfromtxt("data/cms_stau1_8_stable.txt", delimiter=" ", skip_header=2, names=["x","y"])
data["cms_stauR_stable"] = np.genfromtxt("data/cms_stauR_stable.txt", delimiter=" ", skip_header=2, names=["x","y"])
data["cms_stauLR_stable"] = np.genfromtxt("data/cms_stauLR_stable.txt", delimiter=" ", skip_header=2, names=["x","y"])

baselength=4
ax = [0,0]

fig1, (ax[0],ax[1]) = plt.subplots(1,2, figsize=(2.5*baselength, 1*baselength))

#fig1, ax = plt.subplots(1,1, figsize=(1.5*baselength, 1*baselength))

### Actual Curves:

i=2
alpha=0.4

#ax.set_yscale('symlog',base=10,linthresh=2)
ax[0].set_ylim([10**-0.5,10**2.75])

ax[0].fill((data["stau_prompt_atlas_dm"]['x']),(data["stau_prompt_atlas_dm"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[0].fill((data["stauR_prompt_atlas_dm"]['x']),(data["stauR_prompt_atlas_dm"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[0].fill((data["stauR_prompt_atlas_dm"]['x']),(data["stauR_prompt_atlas_dm"]['y']), facecolor='none',ec=to_rgba(colors[i],0.6),hatch='\\\\\\', lw=1)
ax[0].text(325,145 , r"A2 140 fb${}^{-1}$" , rotation=38, size=7,clip_on=False)


i=1

ax[0].fill((data["lep_stauR_dm"]['x']), (data["lep_stauR_dm"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[0].fill((data["lep_stauR_dm"]['x']), (data["lep_stauR_dm"]['y']), "--", facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
ax[0].fill((data["lep_stauR_stable"]['x']), (data["lep_stauR_stable"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[0].fill((data["lep_stauR_stable"]['x']), (data["lep_stauR_stable"]['y']), "--", facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')

i=0

ax[0].fill((data["cms_7_stauR_stable"]['x']), (data["cms_7_stauR_stable"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[0].fill((data["cms_7_stauR_stable"]['x']), (data["cms_7_stauR_stable"]['y']), "--", facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
ax[0].text(125,2, r"C1 5 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)

ax[0].fill((data["cms_stauR_stable"]['x']), (data["cms_stauR_stable"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[0].fill((data["cms_stauR_stable"]['x']), (data["cms_stauR_stable"]['y']), "--", facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
ax[0].fill((data["cms_stauLR_stable"]['x']), (data["cms_stauLR_stable"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[0].text(400,2, r"C2 101 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)

ax[0].set_xlabel(r'$m_{\tilde{\tau}}$ [GeV]',)
ax[0].set_ylabel(r'$\Delta m (\tilde{\tau},\tilde{\chi}_1^0)$ [GeV]',)

#ax.set_ylim([0.100,550])
ax[0].set_xlim([45,700])

# plt.subplots_adjust(wspace=0.03)

#plt.axline((0,0), slope=1, linestyle='--', color='k')

#draw line
xmin, xmax = ax[0].get_xlim()
x = np.linspace(xmin, xmax, 500)

ax[0].plot(x, x, "--", color="gray", linewidth=1)

# try to make piece-wise linear scale
ymin, ymax = ax[0].get_ylim()
y = np.linspace(ymin, ymax, 100)

from matplotlib.scale import ScaleBase
from matplotlib.transforms import Transform
from matplotlib.ticker import AutoLocator

# Parameters
threshold = 2
scale1 = 10.0  # slope below threshold
scale2 = 1.0  # slope above threshold

# Forward transform
class PiecewiseLinearTransform(Transform):
    input_dims = output_dims = 1
    is_separable = True

    def transform_non_affine(self, y):
        y = np.array(y)
        return np.where(y <= threshold,
                        y*scale1,
                        threshold*scale1 + (y-threshold)*scale2)

    def inverted(self):
        return InvertedPiecewiseLinearTransform()

# Inverse transform
class InvertedPiecewiseLinearTransform(Transform):
    input_dims = output_dims = 1
    is_separable = True

    def transform_non_affine(self, y):
        y = np.array(y)
        return np.where(y <= threshold*scale1,
                        y/scale1,
                        threshold + (y - threshold*scale1)/scale2)

    def inverted(self):
        return PiecewiseLinearTransform()

# Define custom scale
class PiecewiseLinearScale(ScaleBase):
    name = 'piecewise'

    def get_transform(self):
        return PiecewiseLinearTransform()

    def set_default_locators_and_formatters(self, axis):
        axis.set_major_locator(AutoLocator())
        
    def limit_range_for_scale(self, vmin, vmax, minpos):
        return vmin, vmax

# Register the scale
from matplotlib.scale import register_scale
register_scale(PiecewiseLinearScale)
ax[0].set_yscale('piecewise')

#xlim = ax[0].get_xlim()  # current x-axis limits

# small horizontal width for the slash in data units
#dx = 0.02*(xlim[1] - xlim[0])
#slash_x = [xlim[0], xlim[0] + dx]

# y in data coordinates (threshold)
#slash_y = [threshold, threshold + 0.05*(ax[0].get_ylim()[1]-ax[0].get_ylim()[0])]
#ax[0].set_xlim(xlim)

# Add tick and label at threshold
# Transform threshold to axis coordinates
from matplotlib.ticker import FixedLocator, FixedFormatter

# Get existing ticks
yticks = list(ax[0].get_yticks())

# Add the threshold tick if it’s not already present
if not any(np.isclose(y, threshold) for y in yticks):
    yticks.append(threshold)

# Sort ticks so they are in order
yticks = sorted(yticks)

# Create labels: use LaTeX for the threshold tick
yticklabels = []
for y in yticks:
    if np.isclose(y, threshold):
        yticklabels.append(r"$m_\tau$")  # LaTeX label
    else:
        yticklabels.append(f"{y:.1f}")

ax[0].yaxis.set_major_locator(FixedLocator(yticks))
ax[0].yaxis.set_major_formatter(FixedFormatter(yticklabels))

#############
#plt.show()


ax[0].spines['right'].set_visible(False)
ax[0].spines['top'].set_visible(False)


ax[0].text(100, 500,       r"Stau Limits", size=11,clip_on=False, fontweight="bold")
#ax[0].text(50, 10**(1.20-1*0.09), r"Various Assumptions", size=11,clip_on=False, ha="right")
ax[0].text(100, 465, r"LEP, Run-1 LHC, Run-2 LHC", size=11,clip_on=False)
ax[0].text(100, 430, r"95% CL", size=11,clip_on=False)

ax[0].text(100, 375,       r"$\tilde{\tau}\tilde{\tau}, \tilde{\tau}\rightarrow \tau \tilde{\chi}_1^0$", size=11,clip_on=False, fontweight="bold")

#ax[0].text(350, 10**-0.48,       r"Decoupled $\tilde{W}, \tilde{B}$", size=9,clip_on=False, ha="right")

#ax[0].text(220, 10**0.4,       r"Soft Leptons", size=11,clip_on=False, fontweight="bold")
#ax[0].text(205, 10**-0.2,       r"Soft Displaced Track", size=11,clip_on=False, fontweight="bold")
#ax[0].text(100, 10**-0.71,       r"Disappearing Track", size=11,clip_on=False, fontweight="bold")

ax[0].text(490, 300,       r"Taus + $p_T^{miss}$", size=11,clip_on=False, fontweight="bold")
ax[0].text(45, 90,       r"LEP", size=11,clip_on=False, fontweight="bold")
ax[0].text(230, 10,       r"Stable LLPs", size=11,clip_on=False, fontweight="bold")

breathe_logy(ax[0])



################################
#Fig 2
################################

dataLLP = {}

dataLLP["stau_dl_atlas_140"] = np.genfromtxt("data/HEPData-ins1831504-v1-Observed_stau_limits.csv", delimiter=",", skip_header=8, names=["x","y"])
dataLLP["stau_ditrack_atlas_140"] = np.genfromtxt("data/HEPData-ins2878503-v1-Figure_fig_13a_obs_d1s.csv", delimiter=",", skip_header=12, names=["x","y"])
dataLLP["atlas_sketchy"] = np.genfromtxt("data/atlas_sketchy.txt", delimiter=",", skip_header=12, names=["x","y"])

dataLLP["stau_dl_cms_113"] = np.genfromtxt("data/HEPData-ins1940976-stau.csv", delimiter=",", skip_header=9, names=["y","x"])
dataLLP["stauLR_cms_lt_101"] = np.genfromtxt("data/cms_stauLR_lt.txt", delimiter=",", skip_header=2, names=["x","y"])

dataLLP["stauR_cms_lt_101"] = np.genfromtxt("data/cms_stauR_lt.txt", delimiter=",", skip_header=2, names=["x","y"])
dataLLP["stauR_cms_lt_7"] = np.genfromtxt("data/cms_stauR_7_lt.txt", delimiter=",", skip_header=2, names=["x","y"])

dataLLP["stauR_lep_lt"] = np.genfromtxt("data/lep_stauR_lt.txt", delimiter=",", skip_header=2, names=["y","x"])

### Actual Curves:

i=4
alpha=0.4

ax[1].set_ylim([0.01,5000])
#ax[1].set_yscale('symlog',base=10,linthresh=2)
ax[1].set_yscale('log')

ax[1].fill((dataLLP["stau_dl_atlas_140"]['x']),(dataLLP["stau_dl_atlas_140"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[1].text(200,0.04, r"A2 140 fb${}^{-1}$" , rotation=10, size=7,clip_on=False)

ax[1].fill((dataLLP["stau_dl_cms_113"]['x']),(dataLLP["stau_dl_cms_113"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[1].text(325,0.4, r"C2 113 fb${}^{-1}$" , rotation=45, size=7,clip_on=False)


i=3

ax[1].fill((dataLLP["stau_ditrack_atlas_140"]['x']),(dataLLP["stau_ditrack_atlas_140"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[1].text(400,5, r"A2 140 fb${}^{-1}$" , rotation=10, size=7,clip_on=False)
ax[1].fill((dataLLP["atlas_sketchy"]['x']),(dataLLP["atlas_sketchy"]['y']), facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='...')


i=0

ax[1].fill((dataLLP["stauLR_cms_lt_101"]['x']),(dataLLP["stauLR_cms_lt_101"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
#ax[1].text(500,10, r"C2 101 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)


ax[1].fill((dataLLP["stauR_cms_lt_101"]['x']),(dataLLP["stauR_cms_lt_101"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[1].fill((dataLLP["stauR_cms_lt_101"]['x']),(dataLLP["stauR_cms_lt_101"]['y']), facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
ax[1].text(550,3000, r"C2 101 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)

ax[1].fill((dataLLP["stauR_cms_lt_7"]['x']),(dataLLP["stauR_cms_lt_7"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[1].fill((dataLLP["stauR_cms_lt_7"]['x']),(dataLLP["stauR_cms_lt_7"]['y']), facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
ax[1].text(120,3000, r"C1 5 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)

i=1

ax[1].fill((dataLLP["stauR_lep_lt"]['x']),(dataLLP["stauR_lep_lt"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax[1].fill((dataLLP["stauR_lep_lt"]['x']),(dataLLP["stauR_lep_lt"]['y']), facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
#ax[1].text(500,1000, r"C2 101 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)

#ax[1].fill((dataLLP["lep_stauR_stable"]['x']), (dataLLP["lep_stauR_stable"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
#ax[1].fill((dataLLP["lep_stauR_stable"]['x']), (dataLLP["lep_stauR_stable"]['y']), "--", facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')

ax[1].set_xlabel(r'$m_{\tilde{\tau}}$ [GeV]',)
ax[1].set_ylabel(r'$\tilde{\tau}$ Lifetime [ns]',labelpad=0.2)

#ax[1].set_ylim([0.100,550])
ax[1].set_xlim([45,700])

# plt.subplots_adjust(wspace=0.03)

#plt.axline((0,0), slope=1, linestyle='--', color='k')


####### y-axis break
from matplotlib.ticker import FixedLocator, FixedFormatter

break_y = 3000  # position of the visual break
stable_y = break_y  # top major tick labeled "stable"

# Major ticks below the break + "stable" at the break
lower_ticks = [0.01, 0.1, 1, 10, 100, 1000]
yticks = lower_ticks + [stable_y]
ax[1].set_yticks(yticks)

# Tick labels: numeric below, "stable" at top
yticklabels = [f"$10^{int(np.log10(t))}$" for t in lower_ticks] + ["stable"]
ax[1].set_yticklabels(yticklabels)

# Turn off minor ticks
ax[1].minorticks_off()

from matplotlib.ticker import LogFormatterMathtext
formatter = LogFormatterMathtext(base=10.0)
ax[1].yaxis.set_major_formatter(formatter)

# After plotting, manually set the last label
yticks = ax[1].get_yticks()
yticklabels = [formatter(tick) for tick in yticks]
yticklabels[-1] = "stable"  # replace top tick
ax[1].set_yticklabels(yticklabels)

ax[1].hlines(y=1000, xmin=ax[1].get_xlim()[0], xmax=ax[1].get_xlim()[1],
          linestyles="--", colors="gray", linewidth=1)

##############

ax[1].spines['right'].set_visible(False)
ax[1].spines['top'].set_visible(False)


#ax[1].text(100, 500,       r"Stau Limits", size=11,clip_on=False, fontweight="bold")
#ax[1].text(100, 465,       r"$\tilde{\tau}\tilde{\tau}, \tilde{\tau}\rightarrow \tau \tilde{G}$", size=11,clip_on=False, fontweight="bold")
#ax[1].text(50, 10**(1.20-1*0.09), r"Various Assumptions", size=11,clip_on=False, ha="right")
#ax[1].text(100, 430, r"LEP, Run-1 LHC, Run-2 LHC", size=11,clip_on=False)
#ax[1].text(100, 395, r"95% CL", size=11,clip_on=False)

#ax[1].text(350, 10**-0.48,       r"Decoupled $\tilde{W}, \tilde{B}$", size=9,clip_on=False, ha="right")

#ax[1].text(220, 10**0.4,       r"Soft Leptons", size=11,clip_on=False, fontweight="bold")
#ax[1].text(205, 10**-0.2,       r"Soft Displaced Track", size=11,clip_on=False, fontweight="bold")
#ax[1].text(100, 10**-0.71,       r"Disappearing Track", size=11,clip_on=False, fontweight="bold")

#ax[1].text(490, 300,       r"Taus + $p_T^{miss}$", size=11,clip_on=False, fontweight="bold")

ax[1].text(100, 0.01,       r"LEP", size=11,clip_on=False, fontweight="bold")
ax[1].text(500, 0.02,       r"$\tilde{\tau}\tilde{\tau}, \tilde{\tau}\rightarrow \tau \tilde{G}$", size=11,clip_on=False, fontweight="bold")


ax[1].text(375, 0.2,       r"Displaced Leptons", size=11,clip_on=False, fontweight="bold")
ax[1].text(225, 50,       r"Anomalous Ionization", size=11,clip_on=False, fontweight="bold")
ax[1].text(550, 450,       r"Stable LLPs", size=11,clip_on=False, fontweight="bold")

breathe_logy(ax[1])


# Force figure to render, so transforms are accurate


# Force figure to render, so transforms are accurate
fig1.subplots_adjust(left=0.10, right=0.96, bottom=0.18, top=0.96)
fig1.canvas.draw()

#plt.show()

fig1.savefig("sleptons.pdf")
# plt.show()
