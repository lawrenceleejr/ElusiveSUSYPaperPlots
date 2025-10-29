import numpy as np
import seaborn as sns
import ROOT
from matplotlib.legend_handler import HandlerPatch

from matplotlib.patches import Rectangle, Circle


def doFillBetween(x,y,axis,n=10,dy=1,color="k",alpha=0.03,log=True,clip_on=True):
    initialY = y
    tmpy = initialY
    print(x,y)

    colorpal = sns.light_palette(color, n)[::-1]
    for i in range(n):
        if log:
            axis.fill_between(x,tmpy, [thing*dy for thing in tmpy],linewidth=0,color=colorpal[i],alpha = alpha*((n-i)/float(n) ) ,  clip_on=clip_on)
            tmpy = [thing*dy for thing in tmpy]
        else:
        	axis.fill_between(x,tmpy, [thing-dy for thing in tmpy],linewidth=0,color=colorpal[i],alpha = alpha*((n-i)/float(n) ) )
        	tmpy = [thing-dy for thing in tmpy]


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



def add_zero_endpoints(arr, point=(0,0)):
    # Create the (0, 0) point with same dtype
    zero_point = np.array([point], dtype=arr.dtype)
    
    # Concatenate zero, original array, zero
    return np.concatenate([zero_point, arr, zero_point])

def breathe_logy(ax):
    limy = ax.get_ylim()
    m0 = limy[0] * (1-0.15)
    ax.spines.bottom.set_position(('data', m0))

    limx = ax.get_xlim()
    span = limx[1] - limx[0]
    m0 = limx[0] - span*0.04
    ax.spines.left.set_position(('data', m0))

def breathe_logx(ax):
    limy = ax.get_ylim()
    span = limy[1] - limy[0]
    m0 = limy[0] - span*0.04
    ax.spines.bottom.set_position(('data', m0))

    limx = ax.get_xlim()
    # span = limx[1] - limx[0]
    m0 = limx[0]  * (1-0.15)
    ax.spines.left.set_position(('data', m0))






# Custom handler to scale rectangle in legend
class HandlerRect(HandlerPatch):
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        # scale rectangle to desired size
        patch = Rectangle([xdescent+5, ydescent],
                            8,8,
                        #   width, height,
                          facecolor=orig_handle.get_facecolor(),
                          edgecolor=orig_handle.get_edgecolor(),
                          lw=0,#orig_handle.get_linewidth(),
                          hatch=orig_handle.get_hatch(),
                          transform=trans)
        return [patch]
    

# 8 green/blue
# 6 bubblegum
coolorPalette = [
     "#d9ed92",#0
     "#b5e48c",#1
     "#99d98c",#2
     "#76c893",#3
     "#52b69a",#4
     "#34a0a4",#5
     "#168aad",#6
     "#1a759f",#7

    "#f7b267",#8
    "#f79d65",#9
    "#f4845f",#10
    "#f27059",#11
    "#f25c54",#12

    # 176,18,22
    "#b01216", # red from template #13
]