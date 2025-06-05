import matplotlib.pyplot as plt
import numpy as np

import ROOT
import seaborn as sns

colors = sns.color_palette("husl", 4)

def add_zero_endpoints(arr, point=(0,0)):
    """
    Adds a (0, 0) point at the beginning and end of a structured numpy array
    with fields 'x' and 'y'.
    
    Parameters:
        arr (np.ndarray): A structured array with dtype containing 'x' and 'y'.
    
    Returns:
        np.ndarray: A new structured array with (0,0) added at both ends.
    """
    # Create the (0, 0) point with same dtype
    zero_point = np.array([point], dtype=arr.dtype)
    
    # Concatenate zero, original array, zero
    return np.concatenate([zero_point, arr, zero_point])

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

fig, ax = plt.subplots(1,1)


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


# ax.spines['right'].set_visible(False)
# ax2.spines['left'].set_visible(False)
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

# ax.text(2e-6, 2050, r"Stop Squark R-Hadron, Various Decays", size=11,clip_on=False)



fig.savefig("test.pdf")
plt.show()