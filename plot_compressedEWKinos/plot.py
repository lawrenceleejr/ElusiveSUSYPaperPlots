from matplotlib_tufte import *
setup()

import matplotlib.pyplot as plt
import numpy as np

import ROOT
import seaborn as sns

# colors = sns.color_palette("husl", 3)
colors = ["#FF595E",  "#1982C4", "#8AC926", "#F2CC8F"] 
# colors = ["#E07A5F",  # Terra Cotta
# 		"#F2CC8F",  # Sand
# 		"#81B29A"]  # Sage

# colors = ["#FF0000", "#00FF00", "#0000FF"]
# colors = ["#FF6B6B", "#6BCB77", "#4D96FF"]
# colors = ["#3A86FF", "#8338EC", "#FB5607"]
# colors = ["#FF6B6B", "#4ECDC4", "#1A535C"]
# colors = ["#4477AA", "#CC6677", "#117733"]

def add_zero_endpoints(arr, point=(0,0)):
    # Create the (0, 0) point with same dtype
    zero_point = np.array([point], dtype=arr.dtype)
    
    # Concatenate zero, original array, zero
    return np.concatenate([zero_point, arr, zero_point])


def add_box_endpoints(arr, point=1e-8):
    # Create the (0, 0) point with same dtype
    points = np.array([
		(arr[-1][0],arr[-1][1]),
		(arr[-1][0],point),
		(arr[0][0],point),
		], dtype=arr.dtype)
    
    # Concatenate zero, original array, zero
    return np.concatenate([points, arr])


def add_box_endpoints_y(arr, point=1e-8):
    # Create the (0, 0) point with same dtype
    points = np.array([
		(arr[-1][0],arr[-1][1]),
		(point,arr[-1][1]),
		(point,arr[0][1]),
		], dtype=arr.dtype)
    
    # Concatenate zero, original array, zero
    return np.concatenate([points, arr])

# https://arxiv.org/pdf/1810.12602
def lifetimeToDm(lifetime):
	return 0.93*0.1/np.power(lifetime,1/3)

def dmToLifetime(dm):
	return np.power(0.93/dm,3)*1e-3

def arrLifetimeToDm(arr):
      return [lifetimeToDm(x) for x in arr]

# def sortBySecondField(arr):
# 	print(arr)
# 	return arr[arr[:, 1].argsort()]

data = {}

data["purehiggsino"] = np.genfromtxt("data/purehiggsino.txt", delimiter=",", skip_header=0, names=["x","y"])

data["lep"] = np.genfromtxt("data/lep.txt", delimiter=",", skip_header=0, names=["x","y"])
data["lep"].sort(order="y")
data["lep"] = add_box_endpoints_y(data["lep"])


data["disappearing_atlas_r2_36_higgsino"] = np.genfromtxt("data/disappearing_atlas_r2_36_higgsino.txt", delimiter=",", skip_header=0, names=["x","y"])
data["disappearing_atlas_r2_36_higgsino"].sort(order="y")
data["disappearing_atlas_r2_36_higgsino"] = add_box_endpoints_y(data["disappearing_atlas_r2_36_higgsino"])

data["disappearing_atlas_r2_136_higgsino"] = np.genfromtxt("data/disappearing_atlas_r2_136_higgsino.txt", delimiter=",", skip_header=0, names=["x","y"])
data["disappearing_atlas_r2_136_higgsino"].sort(order="y")
data["disappearing_atlas_r2_136_higgsino"] = add_box_endpoints_y(data["disappearing_atlas_r2_136_higgsino"])


data["disappearing_cms_r2_101_higgsino"] = np.genfromtxt("data/disappearing_cms_r2_101_higgsino.txt", delimiter=",", skip_header=5, skip_footer=83, names=["y","x"])
data["disappearing_cms_r2_101_higgsino"].sort(order="y")
data["disappearing_cms_r2_101_higgsino"] = add_box_endpoints_y(data["disappearing_cms_r2_101_higgsino"])
# print(data["disappearing_cms_r2_101_higgsino"])


data["disappearing_cms_r2_137_higgsino_dm"] = np.genfromtxt("data/disappearing_cms_r2_137_higgsino_dm.txt", delimiter=",", skip_header=5, names=["x","y"])
data["disappearing_cms_r2_137_higgsino_dm"].sort(order="y")
data["disappearing_cms_r2_137_higgsino_dm"] = add_box_endpoints_y(data["disappearing_cms_r2_137_higgsino_dm"])


data["disappearing_atlas_hl_3000_higgsino"] = np.genfromtxt("data/disappearing_atlas_hl_3000_higgsino.txt", delimiter=",", skip_header=0, names=["x","y"])
data["disappearing_atlas_hl_3000_higgsino"].sort(order="y")
data["disappearing_atlas_hl_3000_higgsino"] = add_box_endpoints_y(data["disappearing_atlas_hl_3000_higgsino"])



data["disappearing_atlas_hl_3000_higgsino_dm"] = np.genfromtxt("data/disappearing_atlas_hl_3000_higgsino_dm.txt", delimiter=",", skip_header=0, names=["x","y"])
data["disappearing_atlas_hl_3000_higgsino_dm"].sort(order="y")
data["disappearing_atlas_hl_3000_higgsino_dm"] = add_box_endpoints_y(data["disappearing_atlas_hl_3000_higgsino_dm"])






data["displaced_atlas_r2_140_higgsino"] = np.genfromtxt("data/displaced_atlas_r2_140_higgsino.txt", delimiter=",", skip_header=11, names=["x","y"])



data["3l_atlas_r2_139_higgsino"] = np.genfromtxt("data/3l_atlas_r2_139_higgsino.txt", delimiter=",", skip_header=9, names=["x","y"])
data["3l_atlas_r2_139_higgsino"] = add_box_endpoints_y(data["3l_atlas_r2_139_higgsino"])


# https://www.hepdata.net/record/80609
data["soft2l_atlas_r2_36_higgsino"] = np.genfromtxt("data/soft2l_atlas_r2_36_higgsino.txt", delimiter=",", skip_header=10, names=["x","y"])
# data["soft2l_atlas_r2_36_higgsino"].sort(order="y")
# data["soft2l_atlas_r2_36_higgsino"] = add_box_endpoints_y(data["soft2l_atlas_r2_36_higgsino"])


# https://www.hepdata.net/record/ins1767649
data["soft2l_atlas_r2_139_higgsino"] = np.genfromtxt("data/soft2l_atlas_r2_139_higgsino.txt", delimiter=",", skip_header=8, names=["x","y"])
data["soft2l_atlas_r2_139_higgsino"] = add_box_endpoints_y(data["soft2l_atlas_r2_139_higgsino"])



data["soft2l_atlas_hl_3000_higgsino"] = np.genfromtxt("data/soft2l_atlas_hl_3000_higgsino.txt", delimiter=",", skip_header=10, names=["x","y"])
data["soft2l_atlas_hl_3000_higgsino"].sort(order="y")
data["soft2l_atlas_hl_3000_higgsino"] = add_box_endpoints_y(data["soft2l_atlas_hl_3000_higgsino"])





# data["displaced_"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_1908.04722/HEPData-ins1749379-v1-T1tttt_observed_mass_limit_curve.csv", delimiter=",", skip_header=11, names=["x","y"])



# data["softl_"] = np.genfromtxt("data/GLUINOGLUINOX/arXiv_1908.04722/HEPData-ins1749379-v1-T1tttt_observed_mass_limit_curve.csv", delimiter=",", skip_header=11, names=["x","y"])






baselength=4
fig, ax = plt.subplots(1,1, figsize=(1.5*baselength, 2*baselength))


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




ax.plot(data["purehiggsino"]['x'],  np.log10((data["purehiggsino"]['y'])), ":", color="k", alpha=1, lw=1)


### Actual Curves:

#
i=0
alpha=0.4

ax.fill(data["disappearing_atlas_r2_36_higgsino"]['x'], np.log10(data["disappearing_atlas_r2_36_higgsino"]['y']), color=colors[i], alpha=alpha, lw=1)
ax.fill(data["disappearing_atlas_r2_136_higgsino"]['x'], np.log10(arrLifetimeToDm(data["disappearing_atlas_r2_136_higgsino"]['y'])), color=colors[i], alpha=alpha, lw=1)

ax.fill(data["disappearing_cms_r2_101_higgsino"]['x'], np.log10(arrLifetimeToDm(data["disappearing_cms_r2_101_higgsino"]['y'])), color=colors[i], alpha=alpha, lw=1)

ax.fill(data["disappearing_cms_r2_137_higgsino_dm"]['x'], np.log10((data["disappearing_cms_r2_137_higgsino_dm"]['y'])), color=colors[i], alpha=alpha, lw=1)


ax.plot(data["disappearing_atlas_hl_3000_higgsino"]['x']-data["disappearing_atlas_hl_3000_higgsino"]['y'],  np.log10(arrLifetimeToDm(1e-3*data["disappearing_atlas_hl_3000_higgsino"]['y'])), "--", color=colors[i], alpha=1, lw=1,zorder=0)




i=1

ax.fill(data["displaced_atlas_r2_140_higgsino"]['x'], np.log10(data["displaced_atlas_r2_140_higgsino"]['y']), color=colors[i], alpha=alpha, lw=1)


i=2


ax.fill(data["soft2l_atlas_r2_36_higgsino"]['x']-data["soft2l_atlas_r2_36_higgsino"]['y'], np.log10(data["soft2l_atlas_r2_36_higgsino"]['y']), color=colors[i], alpha=alpha, lw=1)
ax.fill(data["soft2l_atlas_r2_139_higgsino"]['x']-data["soft2l_atlas_r2_139_higgsino"]['y'], np.log10(data["soft2l_atlas_r2_139_higgsino"]['y']), color=colors[i], alpha=alpha, lw=1)



ax.plot(data["soft2l_atlas_hl_3000_higgsino"]['x'], np.log10(data["soft2l_atlas_hl_3000_higgsino"]['y']), "--", color=colors[i], alpha=1, lw=1, zorder=0)

# i=3

# ax.fill(data["3l_atlas_r2_139_higgsino"]['x'], np.log10(data["3l_atlas_r2_139_higgsino"]['y']), color=colors[i], alpha=alpha, lw=1)




# ax.fill(data["lep_chargino"]['x'], np.log10(data["lep_chargino"]['y']), color="k", alpha=1, lw=1)


# alpha=1/len(data_qq)#0.3

# ax.fill(data_qq["arXiv_1908.04722_1"]['x'], data_qq["arXiv_1908.04722_1"]['y'], color=colors[i], alpha=alpha, lw=1)


ax.fill(data["lep"]['x'], np.log10(data["lep"]['y']), "--", color=(0.9,0.9,0.9), alpha=1, lw=1, ec=(0.7,0.7,0.7))




ax.set_xlabel(r'$m_{\tilde{\chi}_1^0}$ [GeV]',)
ax.set_ylabel(r'Log $\Delta m (\tilde{\chi}_1^\pm,\tilde{\chi}_1^0)$ [GeV]',)
# ax.xaxis.set_label_coords(1.02, -0.07)
# ax.set_ylabel(r'Excluded Stop Squark Mass $m_{\tilde{t}}$ [GeV]')
# ax.set_xlim([2e-6,2e4])
# ax2.set_xlim([1.1e13,9e18])
ax.set_ylim([-0.75,1.25])
ax.set_xlim([50,350])
# ax.set_yscale('log')



# plt.subplots_adjust(wspace=0.03)


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


ax.text(345, 1.15,       r"Higgsino LSP", size=11,clip_on=False, fontweight="bold", ha="right")
ax.text(345, 1.15-1*0.05, r"Various Assumptions", size=11,clip_on=False, ha="right")
ax.text(345, 1.15-2*0.05, r"Run-2 LHC", size=11,clip_on=False, ha="right")

ax.text(350, -0.48,       r"Pure Higgsino LSP", size=9,clip_on=False, ha="right")

ax.text(200, 0.35,       r"Soft Leptons", size=11,clip_on=False, fontweight="bold")
ax.text(180, -0.2,       r"Displaced Track", size=11,clip_on=False, fontweight="bold")
ax.text(240, -0.69,       r"Disappearing Track", size=11,clip_on=False, fontweight="bold")

ax.text(60, -0.71,       r"LEP", size=11,clip_on=False, fontweight="bold")


ax.text(105, -0.7, r"A2 36 fb${}^{-1}$" , rotation=-14, size=7,clip_on=False)
ax.text(210, -0.73, r"A2 136 fb${}^{-1}$", rotation=-10, size=7,clip_on=False)





breathe(ax)


# Force figure to render, so transforms are accurate
fig.subplots_adjust(left=0.25, right=0.93, bottom=0.18, top=0.96)
fig.canvas.draw()




fig.savefig("Higgsino.pdf")
# plt.show()