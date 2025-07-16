# TO-DO:
# Remove random EW chichi
# Find elusive gluino
# Add CMS

from matplotlib_tufte import *
setup()

import matplotlib.font_manager as fm
fm.fontManager.addfont("../fonts/MyriadPro-Regular.ttf")
fm.fontManager.addfont("../fonts/MyriadPro-Bold.ttf")
from matplotlib import rcParams
rcParams['font.family'] = 'Myriad Pro'

import matplotlib.pyplot as plt
import numpy as np

import math
from datetime import datetime
import matplotlib.dates as mdates

import seaborn as sns
# import csv
# from array import array

import sys
sys.path.insert(0, "..")

# Choose a colormap
cmap = plt.get_cmap('plasma')
# Generate evenly spaced colors
num_colors = 6
colors = [cmap(i / (num_colors - 1)) for i in range(num_colors)]

def breathe_datex(ax):
    limy = ax.get_ylim()
    span = limy[1] - limy[0]
    m0 = limy[0] - span*0.04
    ax.spines.bottom.set_position(('data', m0))

    limx = ax.get_xlim()
    # span = limx[1] - limx[0]
    m0 = limx[0]  * (1-0.05)
    ax.spines.left.set_position(('data', m0))

def breathe_datey(ax):
    limy = ax.get_ylim()
    m0 = limy[0] * (1-0.15)
    ax.spines.bottom.set_position(('data', m0))

    limx = ax.get_xlim()
    span = limx[1] - limx[0]
    m0 = limx[0] - span*0.04
    ax.spines.left.set_position(('data', m0))   
    
# get data
data_gg = np.genfromtxt('xsec_v_year_gg.dat', delimiter=',', comments='#', dtype=None, encoding='utf-8')
dates_gg = [datetime.strptime(d, '%Y-%m-%d') for d in data_gg['f5']]
xsec_gg = data_gg['f2']
mass_gg = data_gg['f4']

print(data_gg)

data_chichi = np.genfromtxt('xsec_v_year_chichi.dat', delimiter=',', comments='#', dtype=None, encoding='utf-8')
dates_chichi = [datetime.strptime(d, '%Y-%m-%d') for d in data_chichi['f5']]
xsec_chichi = data_chichi['f2']
mass_chichi = data_chichi['f4']

data_stop = np.genfromtxt('xsec_v_year_stopstop.dat', delimiter=',', comments='#', dtype=None, encoding='utf-8')
dates_stop = [datetime.strptime(d, '%Y-%m-%d') for d in data_stop['f5']]
xsec_stop = data_stop['f2']
mass_stop = data_stop['f4']

data_stop_llp = np.genfromtxt('xsec_v_year_stop_llp.dat', delimiter=',', comments='#', dtype=None, encoding='utf-8')


dates_stop_llp = [datetime.strptime(d, '%Y-%m-%d') for d in data_stop_llp['f5']]
xsec_stop_llp = data_stop_llp['f2']
mass_stop_llp = data_stop_llp['f4']

data_higgsino = np.genfromtxt('xsec_v_year_higgsino.dat', delimiter=',', comments='#', dtype=None, encoding='utf-8')
dates_higgsino = [datetime.strptime(d, '%Y-%m-%d') for d in data_higgsino['f5']]
xsec_higgsino = data_higgsino['f2']
mass_higgsino = data_higgsino['f4']

data_dt = np.genfromtxt('xsec_v_year_dispTrack.dat', delimiter=',', comments='#', dtype=None, encoding='utf-8')
dates_dt = [datetime.strptime(d, '%Y-%m-%d') for d in data_dt['f5']]
xsec_dt = data_dt['f2']
mass_dt = data_dt['f4']

# calculate naturalness
# mu = higgsino parameter
# M3 = gluino mass parameter

###################
# Naturalness try one from chatGPT:
###################
#def delta_mu(mu, MZ=91.1876):
#    return 2 * mu**2 / MZ**2

#def tuning_mu(mu):
#    return 100 / delta_mu(mu)

# def delta_gluino(M3, MZ=91.1876, Lambda=1e16):
#     alpha_s = 0.118
#     yt = 0.9
#     L = np.log(Lambda / M3)
#     coeff = (2 * yt**2 / np.pi**2) * (alpha_s / np.pi)
#     d_mHu2 = coeff * M3**2 * L**2
#     return abs(d_mHu2 / (MZ**2 / 2))

# def tuning_gluino(M3):
#     return 100 / delta_gluino(M3)

# def delta_stop(mstop, MZ=91.1876, Lambda=1e16):
#     yt = 0.9
#     L = np.log(Lambda / mstop)
#     d_mHu2 = (3 * yt**2 / (8 * np.pi**2)) * mstop**2 * L
#     return abs(d_mHu2 / (MZ**2 / 2))

# def tuning_stop(stop):
#     return 100 / delta_stop(stop)

# # Scan over some representative values
# print(f"{'mu':>5}  {'M3':>5}  {'mstop':>6}  {'Δμ':>6}  {'ΔM3':>6}  {'Δst':>6}  {'Δtot':>6}  {'Tuning[%]':>10}")
# for mu in [200, 500, 1000]:
#     for M3 in [500, 1000, 2400]:
#         for mstop in [500, 1000, 2500]:
#             d_mu = delta_mu(mu)
#             d_g = delta_gluino(M3)
#             d_st = delta_stop(mstop)
#             d_tot = max(d_mu, d_g, d_st)
#             tuning = 100 / d_tot
#             print(f"{mu:5}  {M3:5}  {mstop:6}  {d_mu:6.1f}  {d_g:6.1f}  {d_st:6.1f}  {d_tot:6.1f}  {tuning:10.2f}")

# tune_gg = tuning_gluino(mass_gg)
# tune_chichi = tuning_mu(mass_chichi)
# tune_stop = tuning_stop(mass_stop)


############ Naturalness try 2 from chatGPT
# This comes from: https://arxiv.org/pdf/1611.05873 and https://arxiv.org/pdf/hep-ph/0602096
# and is an update of the Barbieri-Giudice measure (for mH)

# Constants
mh = 125.0  # Higgs mass in GeV
alpha_s = 0.118  # strong coupling
yt = 0.93  # top Yukawa at EW scale
Lambda = 1e16  # messenger scale in GeV

def log_ratio(high, low):
    return np.log(high / low)

def delta_gluino(M3):
    """Fine-tuning from gluino mass (2-loop)"""
    logL = log_ratio(Lambda, M3)
    delta = (2 / mh**2) * ((2 * alpha_s / np.pi)**2) * M3**2 * logL**2
    return delta

def delta_stop(mstop):
    """Fine-tuning from stop mass (1-loop)"""
    logL = log_ratio(Lambda, mstop)
    delta = (3 * yt**2 / (4 * np.pi**2)) * (mstop**2 / mh**2) * logL
    return delta

def delta_mu(mu):
    """Fine-tuning from Higgsino mass (tree level)"""
    return 4 * mu**2 / mh**2


tune_gg = 1.0/delta_gluino(mass_gg)
tune_stop = 1.0/delta_stop(mass_stop)
tune_stop_llp = 1.0/delta_stop(mass_stop_llp)
tune_higgsino= 1.0/delta_mu(mass_higgsino)
tune_dt= 1.0/delta_mu(mass_dt)

# Create subplots with shared x-axis
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 6), gridspec_kw={'height_ratios': [1, 1, 1]})

# Top plot: Xsec versus year
ax1.plot(dates_gg,xsec_gg, '.-', label=r'$\tilde{g}\tilde{g}\rightarrow q\bar{q}q\bar{q}\tilde{\chi}_1^0\tilde{\chi}_1^0$',lw=1.5, color=colors[0])
ax1.plot(dates_chichi,xsec_chichi, '.-', label=r'$\tilde{\chi}^{\pm}_1\tilde{\chi}_2^0\rightarrow ll\tilde{\chi}_1^0+X$ via $\tilde{l}$',lw=1.5, color=colors[1])
ax1.plot(dates_stop,xsec_stop, '.-', label=r'$\tilde{t}_1\tilde{t}_1\rightarrow t\bar{t}\tilde{\chi}_1^0\tilde{\chi}_1^0$',lw=1.5, color=colors[3])
ax1.plot(dates_stop_llp,xsec_stop_llp, '.--', label=r'LLP $\tilde{t}_1\tilde{t}_1$',lw=1.5, color=colors[3])
ax1.plot(dates_higgsino,xsec_higgsino, '.-', label=r'GGM $\tilde{H}$',lw=1.5, color=colors[4])
ax1.plot(dates_dt,xsec_dt, '.--', label=r'pure $\tilde{H}$ via dispTrack',lw=1.5, color=colors[4])

# # Manual Tufte-like adjustments
#ax1.spines['right'].set_visible(False)
#ax1.spines['top'].set_visible(False)
#ax1.tick_params(axis='x', direction='out', length=5, width=0.5)
#ax1.tick_params(axis='y', direction='out', length=5, width=0.5)

# Tuftelike doesn't work with datetimes...
#dates_num = mdates.date2num(dates_gg)
#tuftelike.adjust(dates_num, xsec_gg)
#tuftelike.adjust(dates_gg,xsec_gg)
#tuftelike.adjust(dates_chichi,xsec_chichi)
#tuftelike.adjust(dates_stop,xsec_stop)
#tuftelike.adjust(dates_stop_llp,xsec_stop_llp)
#tuftelike.adjust(dates_higgsino,xsec_higgsino)
#tuftelike.adjust(dates_dt,xsec_dt)

#ax1.xaxis_date()  # tell matplotlib to interpret x axis as dates
#ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
#fig.autofmt_xdate()  # optional, auto rotate date labels

ax1.set_ylabel(r'$\sigma_{\mathrm{excluded}}$ [fb]', fontsize=12)
ax1.set_yscale('log')
ax1.legend(
    loc='center left',
    bbox_to_anchor=(0.9, 1),
    fontsize=8,
    handletextpad=0.5,
    labelspacing=0.2,
    borderaxespad=0.2,
    frameon=False
)

# Middle plot: Mass excluded versus year
ax2.plot(dates_gg,mass_gg, '.-', label=r'$\tilde{g}\tilde{g}\rightarrow q\bar{q}q\bar{q}\tilde{\chi}_1^0\tilde{\chi}_1^0$',lw=1.5, color=colors[0])
ax2.plot(dates_chichi,mass_chichi, '.-', label=r'$\tilde{\chi}^{\pm}_1\tilde{\chi}_2^0\rightarrow ll\tilde{\chi}_1^0+X$ via $\tilde{l}$',lw=1.5, color=colors[1])
ax2.plot(dates_stop,mass_stop, '.-', label=r'$\tilde{t}_1\tilde{t}_1\rightarrow t\bar{t}\tilde{\chi}_1^0\tilde{\chi}_1^0$',lw=1.5, color=colors[3])
ax2.plot(dates_stop_llp,mass_stop_llp, '.--', label=r'LLP $\tilde{t}_1\tilde{t}_1$',lw=1.5, color=colors[3])
ax2.plot(dates_higgsino,mass_higgsino, '.-', label=r'GGM $\tilde{H}$',lw=1.5, color=colors[4])
ax2.plot(dates_dt,mass_dt, '.--', label=r'pure $\tilde{H}$ via dispTrack',lw=1.5, color=colors[4])
ax2.set_ylabel(r'$m_{\mathrm{excluded}}$ [GeV]', fontsize=12)

# # Manual Tufte-like adjustments
#ax2.spines['right'].set_visible(False)
#ax2.spines['top'].set_visible(False)
#ax2.tick_params(axis='y', direction='out', length=5, width=0.5)

# Bottom plot: Fine tuning now required 
ax3.plot(dates_gg,tune_gg, '.-', label=r'$\tilde{g}\tilde{g}\rightarrow q\bar{q}q\bar{q}\tilde{\chi}_1^0\tilde{\chi}_1^0$',lw=1.5, color=colors[0])
ax3.plot(dates_stop,tune_stop, '.-', label=r'$\tilde{t}_1\tilde{t}_1\rightarrow t\bar{t}\tilde{\chi}_1^0\tilde{\chi}_1^0$',lw=1.5, color=colors[3])
ax3.plot(dates_stop_llp,tune_stop_llp, '.--', label=r'LLP $\tilde{t}_1\tilde{t}_1$',lw=1.5, color=colors[3])
ax3.plot(dates_higgsino,tune_higgsino, '.-', label=r'GGM $\tilde{H}$',lw=1.5, color=colors[4])
ax3.plot(dates_dt,tune_dt, '.--', label=r'pure $\tilde{H}$ via dispTrack',lw=1.5, color=colors[4])
ax3.set_ylabel('Fine tuning metric [%]', fontsize=12)
ax3.set_yscale('log')

# # Manual Tufte-like adjustments
#ax3.spines['right'].set_visible(False)
#ax3.spines['top'].set_visible(False)
#ax3.tick_params(axis='y', direction='out', length=5, width=0.5)

plt.subplots_adjust(right=0.82)

breathe_datex(ax1)
breathe_datex(ax2)
breathe_datex(ax3)
breathe_datey(ax1)
breathe_datey(ax2)
breathe_datey(ax3)

fig.savefig("xsec_v_year.pdf")
# plt.show()
