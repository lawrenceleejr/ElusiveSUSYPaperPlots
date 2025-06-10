from matplotlib_tufte import *
setup()

import matplotlib.pyplot as plt
import numpy as np

import ROOT
import seaborn as sns
import csv
from array import array

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


baselength=4
fig, ax = plt.subplots(1,1, figsize=(1.5*baselength, 1*baselength))


data = {}
data["rpv1l"] = np.genfromtxt("data/rpv1l.txt", delimiter=",", skip_header=0, names=["x","y"])
data["multib"] = np.genfromtxt("data/multib.txt", delimiter=",", skip_header=0, names=["x","y"])

data["0l"] =  np.genfromtxt("data/0l.txt", delimiter=",", skip_header=0, names=["x","y"])

data["rpv1l_trunc"] = data["rpv1l"][data['rpv1l']['x'] <= 4e-2]
data["multib_trunc"] = data["multib"][data['multib']['x'] <= 4e-2]




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


ax.plot( np.log10(data["rpv1l"]["x"]), data["rpv1l"]["y"], lw=3 , c=colors[0], zorder=10)
ax.plot( np.log10(data["multib"]["x"]), data["multib"]["y"], lw=3 , c=colors[1],zorder=10)


# if split evenly with 223, 123
# it will double the cross section limit (make it weaker)

reductionfactor=2

# Since RPV1L cares about getting a prompt lepton, and doesn't care about MET, as soon as there's another component to the chi decay, it loses sensitivity. Since there are two decays, this is reduced by a factor of 4. Since it now has two decay modes, the lifetime is halved.
tmpx = np.log10([x/(reductionfactor) for x in data["rpv1l_trunc"]["x"]])
tmpy = [x*reductionfactor*reductionfactor for x in arrXSFromMass(data["rpv1l_trunc"]["y"])]
tmpy = arrMassFromXS(tmpy)
ax.plot( tmpx, tmpy, "--", lw=1.5 , c=colors[0])

# But on the right side, you don't get a shift since it's all prompt. You do get that same factor 4 reduction in the BR.
newMass = getMassFromXS(getXSFromMass(data["rpv1l"]["y"][-1])*4)
ax.plot( 
      [tmpx[-1],data["rpv1l"]["x"][-1]], 
      [tmpy[-1],newMass], 
      ":", lw=1.5 , c=colors[0])

# Multi-b on the other hand... it mostly has sensitivity on the left from the chi escapes. So it's affected by the change in lifetime. But since the b's are coming from the prompt Gtt tops, there's no reduction in the upper limit.
tmpx = np.log10([x/reductionfactor for x in data["multib_trunc"]["x"]])
tmpy = [x for x in arrXSFromMass(data["multib_trunc"]["y"])]
tmpy = arrMassFromXS(tmpy)
ax.plot( tmpx, tmpy, "--",lw=1.5 , c=colors[1])

# And when you turn on 112, you start to get limits from 0L. This similarly uses the chi escaping the detector, so only the lifetime change is relevant.
# But the problem is in that analysis, the 
# Nevermind -- this actually doens't do anything. No idea what the Gtt eff is for 0L instead of the Gqq.
# tmpx = np.log10([x/reductionfactor for x in data["0l"]["x"]])
# tmpy = [x for x in arrXSFromMass(data["0l"]["y"])]
# tmpy = arrMassFromXS(tmpy)
# ax.plot( tmpx, tmpy, "--",lw=1.5 , c=colors[2])




# 






ax.set_xlabel(r'$\lambda^{\prime\prime}_{323}$',)
ax.set_ylabel(r'$m(\tilde{g})$ [GeV]',)
ax.set_xlim([-3.5,0])
ax.set_ylim([1000,2500])


# ax.set_xlabel(r'$\lambda^{\prime\prime}_{323}=\lambda^{\prime\prime}_{112}$',)
# ax.set_ylabel(r'$m(\tilde{g})$ [GeV]',)
# ax.set_xlim([-3.2,0])
# ax.set_ylim([1000,2500])


# ax.set_xscale('log')



ax.text(200, 2050,       r"Sparticle Limits, Strong Production", size=11,clip_on=False, fontweight="bold")
ax.text(200, 2050-1*150, r"Various Assumptions", size=11,clip_on=False)
ax.text(200, 2050-2*150, r"Run-2 LHC", size=11,clip_on=False)

ax.text(1700, 1000, r"Gluinos", size=11,clip_on=False, color="k", alpha=0.6, fontweight='bold')
ax.text(1000, 500, r"Squarks", size=11,clip_on=False,  color="k", alpha=0.6, fontweight='bold')


# breathe(ax)

fig.subplots_adjust(left=0.125, right=0.96, bottom=0.15, top=0.98)
# Force figure to render, so transforms are accurate
fig.canvas.draw()

# Transform from data to display coordinates
p0 = ax.transData.transform((0, 0))
p1 = ax.transData.transform((1, 1))

# Compute angle in screen/display space
dx, dy = p1 - p0
angle_rad = np.arctan2(dy, dx)
angle_deg = np.degrees(angle_rad)

# ax.text(100, 160, r"$m_{\tilde{\chi}^0_1}>m_X$", size=9,clip_on=False, rotation=angle_deg, ha='left', va='bottom')
# ax.plot( [0,2500], [0,2500], "--", lw=0.5, color="black" )



fig.savefig("RPVModelDep.pdf")
# plt.show()