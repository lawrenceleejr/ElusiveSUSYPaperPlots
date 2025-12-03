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
import seaborn as sns

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
from matplotlib.colors import to_rgba

import sys
sys.path.insert(0, "..")
from helperFunctions import *

colors = ["#FF595E",  "#1982C4", "#8AC926", "#F2CC8F"] 
colors = [coolorPalette[12],coolorPalette[6],coolorPalette[2]]

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
fig, ax = plt.subplots(1,1, figsize=(1.5*baselength, 1*baselength))

### Actual Curves:

i=2
alpha=0.4

#ax.set_yscale('symlog',base=10,linthresh=2)
ax.set_ylim([10**-0.5,10**2.75])

ax.fill((data["stau_prompt_atlas_dm"]['x']),(data["stau_prompt_atlas_dm"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.fill((data["stauR_prompt_atlas_dm"]['x']),(data["stauR_prompt_atlas_dm"]['y']), color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.fill((data["stauR_prompt_atlas_dm"]['x']),(data["stauR_prompt_atlas_dm"]['y']), facecolor='none',ec=to_rgba(colors[i],0.6),hatch='\\\\\\', lw=1)
ax.text(325,145 , r"A2 140 fb${}^{-1}$" , rotation=38, size=7,clip_on=False)


i=1

ax.fill((data["lep_stauR_dm"]['x']), (data["lep_stauR_dm"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.fill((data["lep_stauR_dm"]['x']), (data["lep_stauR_dm"]['y']), "--", facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
ax.fill((data["lep_stauR_stable"]['x']), (data["lep_stauR_stable"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.fill((data["lep_stauR_stable"]['x']), (data["lep_stauR_stable"]['y']), "--", facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')

i=0

ax.fill((data["cms_7_stauR_stable"]['x']), (data["cms_7_stauR_stable"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.fill((data["cms_7_stauR_stable"]['x']), (data["cms_7_stauR_stable"]['y']), "--", facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
ax.text(125,2, r"C1 5 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)

ax.fill((data["cms_stauR_stable"]['x']), (data["cms_stauR_stable"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.fill((data["cms_stauR_stable"]['x']), (data["cms_stauR_stable"]['y']), "--", facecolor='none', ec=to_rgba(colors[i],0.6), lw=1, hatch='\\\\\\')
ax.fill((data["cms_stauLR_stable"]['x']), (data["cms_stauLR_stable"]['y']), "--", color=to_rgba(colors[i],alpha), ec=to_rgba(colors[i],0.6), lw=1)
ax.text(400,2, r"C2 101 fb${}^{-1}$" , rotation=0, size=7,clip_on=False)

ax.set_xlabel(r'$m_{\tilde{\tau}}$ [GeV]',)
ax.set_ylabel(r'$\Delta m (\tilde{\tau},\tilde{\chi}_1^0)$ [GeV]',)

#ax.set_ylim([0.100,550])
ax.set_xlim([45,700])

# plt.subplots_adjust(wspace=0.03)

#plt.axline((0,0), slope=1, linestyle='--', color='k')

#draw line
xmin, xmax = ax.get_xlim()
x = np.linspace(xmin, xmax, 500)
# ax.plot(x, x, "--", color="gray", linewidth=1)
ax.plot( [xmin,xmax], [xmin, xmax], "-", lw=0.5, color="black" )


doFillBetween([xmin,xmax], [xmin, xmax], axis=ax, dy=-2, alpha=0.4, n=30, log=False,clip_on=False)


#plt.show()
# Compute angle in screen/display space

# Transform from data to display coordinates
p0 = ax.transData.transform((0, 0))
p1 = ax.transData.transform((1, 1))
dx, dy = p1 - p0
angle_rad = np.arctan2(dy, dx)
angle_deg = np.degrees(angle_rad)

ax.text(50, 70, r"$m_{\tilde{\chi}^0_1}>m_{\tilde{\tau}}$", size=9,clip_on=False, rotation=angle_deg, ha='left', va='bottom')



# try to make piece-wise linear scale
ymin, ymax = ax.get_ylim()
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
ax.set_yscale('piecewise')

#xlim = ax.get_xlim()  # current x-axis limits

# small horizontal width for the slash in data units
#dx = 0.02*(xlim[1] - xlim[0])
#slash_x = [xlim[0], xlim[0] + dx]

# y in data coordinates (threshold)
#slash_y = [threshold, threshold + 0.05*(ax.get_ylim()[1]-ax.get_ylim()[0])]
#ax.set_xlim(xlim)

# Add tick and label at threshold
# Transform threshold to axis coordinates
from matplotlib.ticker import FixedLocator, FixedFormatter

# Get existing ticks
yticks = list(ax.get_yticks())

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
        yticklabels.append(f"{y:.0f}")

ax.yaxis.set_major_locator(FixedLocator(yticks))
ax.yaxis.set_major_formatter(FixedFormatter(yticklabels))

#############
#plt.show()


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


ax.text(100, 500,       r"Stau Limits", size=11,clip_on=False, fontweight="bold")
ax.text(100, 465,       r"$\tilde{\tau}\tilde{\tau}, \tilde{\tau}\rightarrow \tau \tilde{\chi}_1^0$", size=11,clip_on=False, fontweight="bold")
#ax.text(50, 10**(1.20-1*0.09), r"Various Assumptions", size=11,clip_on=False, ha="right")
ax.text(100, 430, r"LEP, Run-1 LHC, Run-2 LHC", size=11,clip_on=False)
ax.text(100, 395, r"95% CL", size=11,clip_on=False)

#ax.text(350, 10**-0.48,       r"Decoupled $\tilde{W}, \tilde{B}$", size=9,clip_on=False, ha="right")

#ax.text(220, 10**0.4,       r"Soft Leptons", size=11,clip_on=False, fontweight="bold")
#ax.text(205, 10**-0.2,       r"Soft Displaced Track", size=11,clip_on=False, fontweight="bold")
#ax.text(100, 10**-0.71,       r"Disappearing Track", size=11,clip_on=False, fontweight="bold")

ax.text(490, 300,       r"Taus + $p_T^{miss}$", size=11,clip_on=False, fontweight="bold")
ax.text(105, 30,       r"LEP", size=11,clip_on=False, fontweight="bold")
ax.text(230, 10,       r"Stable LLPs", size=11,clip_on=False, fontweight="bold")

breathe_logy(ax)


# Force figure to render, so transforms are accurate
fig.subplots_adjust(left=0.15, right=0.93, bottom=0.18, top=0.96)
fig.canvas.draw()


fig.savefig("sleptons.pdf")
# plt.show()
