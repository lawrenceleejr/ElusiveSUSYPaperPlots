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


import sys
sys.path.insert(0, "..")
from helperFunctions import *


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


data_gg = {}

data_gg["arXiv_1908.04722"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_1908.04722/HEPData-ins1749379-v1-T1tttt_observed_mass_limit_curve.csv", delimiter=",", skip_header=11, names=["x","y"])
data_gg["arXiv_1908.04722"] = add_zero_endpoints(data_gg["arXiv_1908.04722"])

data_gg["arXiv_1909.08457"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_1909.08457/HEPData-ins1754675-v4-Exclusion_contour_from_Fig.7a_(Obs.).csv", delimiter=",", skip_header=11, names=["x","y"])
data_gg["arXiv_1909.08457"] = add_zero_endpoints(data_gg["arXiv_1909.08457"],(100,100))

data_gg["arXiv_2008.06032_1"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2008.06032/HEPData-ins1811596-v1-Exclusion_Limits_(Obs.)_Gtt.csv", delimiter=",", skip_header=10, names=["x","y"])
data_gg["arXiv_2008.06032_1"] = add_zero_endpoints(data_gg["arXiv_2008.06032_1"],(100,100))

data_gg["arXiv_2008.06032_2"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2008.06032/HEPData-ins1811596-v1-Exclusion_Limits_(Obs.)_Two-step.csv", delimiter=",", skip_header=10, names=["x","y"])
data_gg["arXiv_2008.06032_2"] = add_zero_endpoints(data_gg["arXiv_2008.06032_2"],(100,100))

data_gg["arXiv_2010.14293"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2010.14293/HEPData-ins1827025-v2-Obs.Contour_3.csv", delimiter=",", skip_header=9, names=["x","y"])
data_gg["arXiv_2010.14293"] = add_zero_endpoints(data_gg["arXiv_2010.14293"],(0,0))

data_gg["arXiv_2101.01629"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2101.01629/HEPData-ins1839446-v2-Exclusion_contour_1_(obs.).csv", delimiter=",", skip_header=9, names=["x","y"])
data_gg["arXiv_2101.01629"] = add_zero_endpoints(data_gg["arXiv_2101.01629"],(50,50))


data_gg["arXiv_2103.01290_1"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2103.01290/HEPData-ins1849522-v1-Figure_10-a_Observed_Lines.csv", delimiter=",", skip_header=505, skip_footer=166, names=["x","y"])
data_gg["arXiv_2103.01290_1"] = add_zero_endpoints(data_gg["arXiv_2103.01290_1"],(0,0))

data_gg["arXiv_2103.01290_2"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2103.01290/HEPData-ins1849522-v1-Figure_10-b_Observed_Lines.csv", delimiter=",", skip_header=475, skip_footer=154, names=["x","y"])
data_gg["arXiv_2103.01290_2"] = add_zero_endpoints(data_gg["arXiv_2103.01290_2"],(0,0))

data_gg["arXiv_2103.01290_3"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2103.01290/HEPData-ins1849522-v1-Figure_11_Observed_Lines.csv", delimiter=",", skip_header=677, skip_footer=223, names=["x","y"])
data_gg["arXiv_2103.01290_3"] = add_zero_endpoints(data_gg["arXiv_2103.01290_3"],(0,0))



data_gg["arXiv_2204.13072_1"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2204.13072/HEPData-ins2072870-v1-Figure_16a_Observed_Limit.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_gg["arXiv_2204.13072_1"] = add_zero_endpoints(data_gg["arXiv_2204.13072_1"],(0,0))

data_gg["arXiv_2204.13072_2"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2204.13072/HEPData-ins2072870-v1-Figure_16b_Observed_Limit.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_gg["arXiv_2204.13072_2"] = add_zero_endpoints(data_gg["arXiv_2204.13072_2"],(0,0))

data_gg["arXiv_2204.13072_3"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2204.13072/HEPData-ins2072870-v1-Figure_16c_Observed_Limit.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_gg["arXiv_2204.13072_3"] = add_zero_endpoints(data_gg["arXiv_2204.13072_3"],(0,0))





data_gg["arXiv_2206.06012_1"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2206.06012/HEPData-ins2094882-v2-Observed_limit_for_gH_model.csv", delimiter=",", skip_header=12, skip_footer=0, names=["x","y"])
data_gg["arXiv_2206.06012_1"] = add_zero_endpoints(data_gg["arXiv_2206.06012_1"],(0,0))

data_gg["arXiv_2206.06012_2"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2206.06012/HEPData-ins2094882-v2-Observed_limit_for_gZ_model.csv", delimiter=",", skip_header=12, skip_footer=0, names=["x","y"])
data_gg["arXiv_2206.06012_2"] = add_zero_endpoints(data_gg["arXiv_2206.06012_2"],(0,0))




data_gg["arXiv_2211.08028_1"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2211.08028/HEPData-ins2182381-v2-Observed_CLs_limit_for_Gbb_from_CC.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_gg["arXiv_2211.08028_1"] = add_zero_endpoints(data_gg["arXiv_2211.08028_1"],(0,0))

data_gg["arXiv_2211.08028_2"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2211.08028/HEPData-ins2182381-v2-Observed_CLs_limit_for_Gbb_from_NN.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_gg["arXiv_2211.08028_2"] = add_zero_endpoints(data_gg["arXiv_2211.08028_2"],(0,0))

data_gg["arXiv_2211.08028_3"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2211.08028/HEPData-ins2182381-v2-Observed_CLs_limit_for_Gtt_from_CC.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_gg["arXiv_2211.08028_3"] = add_zero_endpoints(data_gg["arXiv_2211.08028_3"],(0,0))

data_gg["arXiv_2211.08028_4"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2211.08028/HEPData-ins2182381-v2-Observed_CLs_limit_for_Gtt_from_NN.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_gg["arXiv_2211.08028_4"] = add_zero_endpoints(data_gg["arXiv_2211.08028_4"],(0,0))



data_gg["arXiv_2307.01094_1"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2307.01094/HEPData-ins2673888-v1-Exclusion_contour(Obs)_from_Fig_7(a).csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_gg["arXiv_2307.01094_1"] = add_zero_endpoints(data_gg["arXiv_2307.01094_1"],(0,0))

data_gg["arXiv_2307.01094_2"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2307.01094/HEPData-ins2673888-v1-Exclusion_contour(Obs)_from_Fig_7(c).csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_gg["arXiv_2307.01094_2"] = add_zero_endpoints(data_gg["arXiv_2307.01094_2"],(0,0))

data_gg["arXiv_2307.01094_3"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2307.01094/HEPData-ins2673888-v1-Exclusion_contour(Obs)_from_Fig_7(e).csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_gg["arXiv_2307.01094_3"] = add_zero_endpoints(data_gg["arXiv_2307.01094_3"],(0,0))

data_gg["arXiv_2307.01094_4"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_2307.01094/HEPData-ins2673888-v1-Exclusion_contour(Obs)_from_Fig_7(f).csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_gg["arXiv_2307.01094_4"] = add_zero_endpoints(data_gg["arXiv_2307.01094_4"],(0,0))

print(data_gg)



data_qq = {}

data_qq["arXiv_1908.04722_1"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_1908.04722/HEPData-ins1749379-v1-T2qq_(1_flavor)_observed_mass_limit_curve.csv", delimiter=",", skip_header=11, skip_footer=0, names=["x","y"])
data_qq["arXiv_1908.04722_1"] = add_zero_endpoints(data_qq["arXiv_1908.04722_1"],(0,0))

data_qq["arXiv_1908.04722_2"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_1908.04722/HEPData-ins1749379-v1-T2qq_observed_mass_limit_curve.csv", delimiter=",", skip_header=11, skip_footer=0, names=["x","y"])
data_qq["arXiv_1908.04722_2"] = add_zero_endpoints(data_qq["arXiv_1908.04722_2"],(0,0))




data_qq["arXiv_1909.03460"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_1909.03460/HEPData-ins1753215-v1-Figure_13_(T2qq).csv", delimiter=",", skip_header=11, skip_footer=0, usecols=(0,1), names=["x","y"])
data_qq["arXiv_1909.03460"] = add_zero_endpoints(data_qq["arXiv_1909.03460"],(0,0))




data_qq["arXiv_2010.14293_1"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_2010.14293/HEPData-ins1827025-v2-Obs.Contour_1.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_qq["arXiv_2010.14293_1"] = add_zero_endpoints(data_qq["arXiv_2010.14293_1"],(0,0))

data_qq["arXiv_2010.14293_2"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_2010.14293/HEPData-ins1827025-v2-Obs.Contour_2.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_qq["arXiv_2010.14293_2"] = add_zero_endpoints(data_qq["arXiv_2010.14293_2"],(0,0))

data_qq["arXiv_2010.14293_3"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_2010.14293/HEPData-ins1827025-v2-Obs.Contour_4.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_qq["arXiv_2010.14293_3"] = add_zero_endpoints(data_qq["arXiv_2010.14293_3"],(0,0))

data_qq["arXiv_2010.14293_4"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_2010.14293/HEPData-ins1827025-v2-Obs.Contour_5.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","dy"])
data_qq["arXiv_2010.14293_4"] = add_zero_endpoints(data_qq["arXiv_2010.14293_4"],(0,0))





data_qq["arXiv_2101.01629_1"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_2101.01629/HEPData-ins1839446-v2-Exclusion_contour_3_(obs.).csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_qq["arXiv_2101.01629_1"] = add_zero_endpoints(data_qq["arXiv_2101.01629_1"],(0,0))

data_qq["arXiv_2101.01629_2"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_2101.01629/HEPData-ins1839446-v2-Exclusion_contour_4_(obs.).csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_qq["arXiv_2101.01629_2"] = add_zero_endpoints(data_qq["arXiv_2101.01629_2"],(0,0))

data_qq["arXiv_2101.01629_3"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_2101.01629/HEPData-ins1839446-v2-Exclusion_contour_5_(obs.).csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_qq["arXiv_2101.01629_3"] = add_zero_endpoints(data_qq["arXiv_2101.01629_3"],(0,0))

data_qq["arXiv_2101.01629_4"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_2101.01629/HEPData-ins1839446-v2-Exclusion_contour_6_(obs.).csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","dy"])
data_qq["arXiv_2101.01629_4"] = add_zero_endpoints(data_qq["arXiv_2101.01629_4"],(0,0))




data_qq["arXiv_2307.01094_1"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_2307.01094/HEPData-ins2673888-v1-Exclusion_contour(Obs)_from_Fig_7(b).csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_qq["arXiv_2307.01094_1"] = add_zero_endpoints(data_qq["arXiv_2307.01094_1"],(100,100))

data_qq["arXiv_2307.01094_2"] = np.genfromtxt("data/SQUARKSQUARKX/arXiv_2307.01094/HEPData-ins2673888-v1-Exclusion_contour(Obs)_from_Fig_7(d).csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_qq["arXiv_2307.01094_2"] = add_zero_endpoints(data_qq["arXiv_2307.01094_2"],(100,100))










baselength=4
fig, ax = plt.subplots(1,1, figsize=(1.5*baselength, 1*baselength))


### Actual Curves:

#
i=0

alpha=2/len(data_gg)#0.3

ax.fill(data_gg["arXiv_1908.04722"]['x'], data_gg["arXiv_1908.04722"]['y'], color=colors[i], alpha=alpha, lw=0)

ax.fill(data_gg["arXiv_1909.08457"]['x'], data_gg["arXiv_1909.08457"]['y'], color=colors[i], alpha=alpha, lw=0)

ax.fill(data_gg["arXiv_2008.06032_1"]['x'], data_gg["arXiv_2008.06032_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2008.06032_2"]['x'], data_gg["arXiv_2008.06032_2"]['y'], color=colors[i], alpha=alpha, lw=0)

ax.fill(data_gg["arXiv_2010.14293"]['x'], data_gg["arXiv_2010.14293"]['y'], color=colors[i], alpha=alpha, lw=0)

ax.fill(data_gg["arXiv_2101.01629"]['x'], data_gg["arXiv_2101.01629"]['y'], color=colors[i], alpha=alpha, lw=0)


ax.fill(data_gg["arXiv_2103.01290_1"]['x'], data_gg["arXiv_2103.01290_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2103.01290_2"]['x'], data_gg["arXiv_2103.01290_2"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2103.01290_3"]['x'], data_gg["arXiv_2103.01290_3"]['y'], color=colors[i], alpha=alpha, lw=0)


ax.fill(data_gg["arXiv_2204.13072_1"]['x'], data_gg["arXiv_2204.13072_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2204.13072_2"]['x'], data_gg["arXiv_2204.13072_2"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2204.13072_3"]['x'], data_gg["arXiv_2204.13072_3"]['y'], color=colors[i], alpha=alpha, lw=0)


ax.fill(data_gg["arXiv_2206.06012_1"]['x'], data_gg["arXiv_2206.06012_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2206.06012_2"]['x'], data_gg["arXiv_2206.06012_2"]['y'], color=colors[i], alpha=alpha, lw=0)



ax.fill(data_gg["arXiv_2211.08028_1"]['x'], data_gg["arXiv_2211.08028_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2211.08028_2"]['x'], data_gg["arXiv_2211.08028_2"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2211.08028_3"]['x'], data_gg["arXiv_2211.08028_3"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2211.08028_4"]['x'], data_gg["arXiv_2211.08028_4"]['y'], color=colors[i], alpha=alpha, lw=0)


ax.fill(data_gg["arXiv_2307.01094_1"]['x'], data_gg["arXiv_2307.01094_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2307.01094_2"]['x'], data_gg["arXiv_2307.01094_2"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2307.01094_3"]['x'], data_gg["arXiv_2307.01094_3"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_gg["arXiv_2307.01094_4"]['x'], data_gg["arXiv_2307.01094_4"]['y'], color=colors[i], alpha=alpha, lw=0)




i=1

alpha=1/len(data_qq)#0.3

ax.fill(data_qq["arXiv_1908.04722_1"]['x'], data_qq["arXiv_1908.04722_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_qq["arXiv_1908.04722_2"]['x'], data_qq["arXiv_1908.04722_2"]['y'], color=colors[i], alpha=alpha, lw=0)


# ax.fill(data_qq["arXiv_1909.03460"]['x'], data_qq["arXiv_1909.03460"]['y'], color=colors[i], alpha=alpha, lw=0)

ax.fill(data_qq["arXiv_2010.14293_1"]['x'], data_qq["arXiv_2010.14293_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_qq["arXiv_2010.14293_2"]['x'], data_qq["arXiv_2010.14293_2"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_qq["arXiv_2010.14293_3"]['x'], data_qq["arXiv_2010.14293_3"]['y'], color=colors[i], alpha=alpha, lw=0)
# ax.fill(data_qq["arXiv_2010.14293_4"]['x'], data_qq["arXiv_2010.14293_4"]['y'], color=colors[i], alpha=alpha, lw=0)

ax.fill(data_qq["arXiv_2101.01629_1"]['x'], data_qq["arXiv_2101.01629_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_qq["arXiv_2101.01629_2"]['x'], data_qq["arXiv_2101.01629_2"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_qq["arXiv_2101.01629_3"]['x'], data_qq["arXiv_2101.01629_3"]['y'], color=colors[i], alpha=alpha, lw=0)
# ax.fill(data_qq["arXiv_2101.01629_4"]['x'], data_qq["arXiv_2101.01629_4"]['y'], color=colors[i], alpha=alpha, lw=0)


ax.fill(data_qq["arXiv_2307.01094_1"]['x'], data_qq["arXiv_2307.01094_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_qq["arXiv_2307.01094_2"]['x'], data_qq["arXiv_2307.01094_2"]['y'], color=colors[i], alpha=alpha, lw=0)



















ax.set_xlabel(r'$m_{X}$ [GeV]',)
ax.set_ylabel(r'$m_{\chi^0_1}$ [GeV]',)
# ax.xaxis.set_label_coords(1.02, -0.07)
# ax.set_ylabel(r'Excluded Stop Squark Mass $m_{\tilde{t}}$ [GeV]')
# ax.set_xlim([2e-6,2e4])
# ax2.set_xlim([1.1e13,9e18])
ax.set_ylim([0,2500])
ax.set_xlim([0,2700])
# plt.grid()


# plt.subplots_adjust(wspace=0.03)


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# ax.yaxis.tick_left()
# ax.tick_params(labelright='off')
# ax2.yaxis.tick_right()
# ax2.tick_params(top='off', right='off', which='both')

# d = .015 # how big to make the diagonal lines in axes coordinates
# # arguments to pass plot, just so we don't keep repeating them
# kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
# ax.plot((1-d,1+d), (-d,+d), **kwargs)
# ax.plot((1-d,1+d),(1-d,1+d), **kwargs)

# kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
# ax2.plot((-3*d,+3*d), (1-d,1+d), **kwargs)
# ax2.plot((-3*d,+3*d), (-d,+d), **kwargs, )


# ax.text(1e-6, 160, "Prompt", size=9,clip_on=False)
# ax2.text(1.1e17, 160, "Stable", size=9,clip_on=False)

ax.text(200, 2050,       r"Sparticle Limits, Strong Production", size=11,clip_on=False, fontweight="bold")
ax.text(200, 2050-1*150, r"Various Assumptions", size=11,clip_on=False)
ax.text(200, 2050-2*150, r"Run-2 LHC", size=11,clip_on=False)

ax.text(1700, 1000, r"Gluinos", size=11,clip_on=False, color="k", alpha=0.6, fontweight='bold')
ax.text(1000, 500, r"Squarks", size=11,clip_on=False,  color="k", alpha=0.6, fontweight='bold')


ax.text(1000, 500, r"Make another plot with EWK production", size=11,clip_on=False,  color="k", alpha=0.6, fontweight='bold')



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

ax.text(100, 160, r"$m_{\tilde{\chi}^0_1}>m_X$", size=9,clip_on=False, rotation=angle_deg, ha='left', va='bottom')
ax.plot( [0,2500], [0,2500], "--", lw=0.5, color="black" )



fig.savefig("Vanilla.pdf")
# plt.show()