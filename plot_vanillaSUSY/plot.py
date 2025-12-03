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
# colors = ["#FF595E",  "#1982C4", "#8AC926",] 
# colors = ["#E07A5F",  # Terra Cotta
# 		"#F2CC8F",  # Sand
# 		"#81B29A"]  # Sage

# colors = ["#FF0000", "#00FF00", "#0000FF"]
# colors = ["#FF6B6B", "#6BCB77", "#4D96FF"]
# colors = ["#3A86FF", "#8338EC", "#FB5607"]
# colors = ["#FF6B6B", "#4ECDC4", "#1A535C"]
# colors = ["#4477AA", "#CC6677", "#117733"]



colors = [
     coolorPalette[8],
     coolorPalette[-1],
     coolorPalette[3],
     coolorPalette[6],
     
]



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








data_slsl = {}

data_slsl["arXiv_1908.08215"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_1908.08215/HEPData-ins1750597-v4-Exclusion_contour_(obs)_3.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_slsl["arXiv_1908.08215"] = add_zero_endpoints(data_slsl["arXiv_1908.08215"],(0,0))


data_slsl["arXiv_2209.13935_1"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_comb_obs_nominal_SR0j.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2209.13935_1"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_1"],(0,0))

data_slsl["arXiv_2209.13935_2"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_comb_obs_nominal_SR1j.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2209.13935_2"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_2"],(0,0))

data_slsl["arXiv_2209.13935_3"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_ee_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2209.13935_3"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_3"],(0,0))

data_slsl["arXiv_2209.13935_4"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_eLeL_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2209.13935_4"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_4"],(0,0))

data_slsl["arXiv_2209.13935_5"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_eReR_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2209.13935_5"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_5"],(0,0))

data_slsl["arXiv_2209.13935_6"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_mm_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2209.13935_6"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_6"],(0,0))

data_slsl["arXiv_2209.13935_7"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_mLmL_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2209.13935_7"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_7"],(0,0))

data_slsl["arXiv_2209.13935_8"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_mRmR_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2209.13935_8"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_8"],(0,0))



# data_slsl["arXiv_2503.13135_1"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2503.13135/HEPData-ins2901728-v1-Observed_exclusion_limit_from_Aux._Fig._3.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
# data_slsl["arXiv_2503.13135_1"] = add_zero_endpoints(data_slsl["arXiv_2503.13135_1"],(0,0))

# data_slsl["arXiv_2503.13135_2"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2503.13135/HEPData-ins2901728-v1-Observed_exclusion_limit_from_Fig._15.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
# data_slsl["arXiv_2503.13135_2"] = add_zero_endpoints(data_slsl["arXiv_2503.13135_2"],(0,0))


# data_slsl["arXiv_2503.13135_3"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2503.13135/HEPData-ins2901728-v1-Observed_exclusion_limit_from_Fig._16a.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
# data_slsl["arXiv_2503.13135_3"] = add_zero_endpoints(data_slsl["arXiv_2503.13135_3"],(0,0))


# data_slsl["arXiv_2503.13135_4"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2503.13135/HEPData-ins2901728-v1-Observed_exclusion_limit_from_Fig._16b.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
# data_slsl["arXiv_2503.13135_4"] = add_zero_endpoints(data_slsl["arXiv_2503.13135_4"],(0,0))




data_slsl["arXiv_1911.12606_1"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_1911.12606/HEPData-ins1767649-v5-Figure_2a_LH_slepton_Observed.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_slsl["arXiv_1911.12606_1"] = add_zero_endpoints(data_slsl["arXiv_1911.12606_1"],(0,0))

data_slsl["arXiv_1911.12606_2"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_1911.12606/HEPData-ins1767649-v5-Figure_2a_RH_slepton_Observed.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_slsl["arXiv_1911.12606_2"] = add_zero_endpoints(data_slsl["arXiv_1911.12606_2"],(0,0))

data_slsl["arXiv_1911.12606_3"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_1911.12606/HEPData-ins1767649-v5-Figure_16a_Observed.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_slsl["arXiv_1911.12606_3"] = add_zero_endpoints(data_slsl["arXiv_1911.12606_3"],(0,0))


data_slsl["arXiv_2402.00603_1"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2402.00603/HEPData-ins2754043-v1-Table_13.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2402.00603_1"] = add_zero_endpoints(data_slsl["arXiv_2402.00603_1"],(0,0))

data_slsl["arXiv_2402.00603_2"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2402.00603/HEPData-ins2754043-v1-Table_19.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2402.00603_2"] = add_zero_endpoints(data_slsl["arXiv_2402.00603_2"],(0,0))

data_slsl["arXiv_2402.00603_3"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2402.00603/HEPData-ins2754043-v1-Table_25.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2402.00603_3"] = add_zero_endpoints(data_slsl["arXiv_2402.00603_3"],(0,0))


data_slsl["arXiv_2207.02254_1"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2207.02254/HEPData-ins2106478-v1-Figure_007-a_observed_exclusions.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2207.02254_1"] = add_zero_endpoints(data_slsl["arXiv_2207.02254_1"],(0,0))

data_slsl["arXiv_2207.02254_2"] = np.genfromtxt("data/SLEPTONSLEPTON/arXiv_2207.02254/HEPData-ins2106478-v1-Figure_007-b_observed_exclusions.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","y"])
data_slsl["arXiv_2207.02254_2"] = add_zero_endpoints(data_slsl["arXiv_2207.02254_2"],(0,0))






data_ewk = {}

data_ewk["arXiv_2205.09597_1"] = np.genfromtxt("data/EWKinos/arXiv_2205.09597/HEPData-ins2085373-v2-Figure_4a_Observed_Lines.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2205.09597_1"] = add_zero_endpoints(data_ewk["arXiv_2205.09597_1"],(0,0))

data_ewk["arXiv_2205.09597_2"] = np.genfromtxt("data/EWKinos/arXiv_2205.09597/HEPData-ins2085373-v2-Figure_4b_Observed_Lines.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2205.09597_2"] = add_zero_endpoints(data_ewk["arXiv_2205.09597_2"],(0,0))

data_ewk["arXiv_2205.09597_3"] = np.genfromtxt("data/EWKinos/arXiv_2205.09597/HEPData-ins2085373-v2-Figure_4c_Observed_Lines.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2205.09597_3"] = add_zero_endpoints(data_ewk["arXiv_2205.09597_3"],(0,0))

data_ewk["arXiv_2205.09597_4"] = np.genfromtxt("data/EWKinos/arXiv_2205.09597/HEPData-ins2085373-v2-Figure_5a_WW_WH_Observed_Lines.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2205.09597_4"] = add_zero_endpoints(data_ewk["arXiv_2205.09597_4"],(0,0))

data_ewk["arXiv_2205.09597_5"] = np.genfromtxt("data/EWKinos/arXiv_2205.09597/HEPData-ins2085373-v2-Figure_5a_WW_WZ_Observed_Lines.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2205.09597_5"] = add_zero_endpoints(data_ewk["arXiv_2205.09597_5"],(0,0))

data_ewk["arXiv_2205.09597_6"] = np.genfromtxt("data/EWKinos/arXiv_2205.09597/HEPData-ins2085373-v2-Figure_5b_Observed_Lines.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2205.09597_6"] = add_zero_endpoints(data_ewk["arXiv_2205.09597_6"],(0,0))






data_ewk["arXiv_2402.00603_1"] = np.genfromtxt("data/EWKinos/arXiv_2402.00603/HEPData-ins2754043-v1-Table_31.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2402.00603_1"] = add_zero_endpoints(data_ewk["arXiv_2402.00603_1"],(0,0))

data_ewk["arXiv_2402.00603_2"] = np.genfromtxt("data/EWKinos/arXiv_2402.00603/HEPData-ins2754043-v1-Table_35.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2402.00603_2"] = add_zero_endpoints(data_ewk["arXiv_2402.00603_2"],(0,0))

data_ewk["arXiv_2402.00603_3"] = np.genfromtxt("data/EWKinos/arXiv_2402.00603/HEPData-ins2754043-v1-Table_37.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2402.00603_3"] = add_zero_endpoints(data_ewk["arXiv_2402.00603_3"],(0,0))

data_ewk["arXiv_2402.00603_4"] = np.genfromtxt("data/EWKinos/arXiv_2402.00603/HEPData-ins2754043-v1-Table_51.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2402.00603_4"] = add_zero_endpoints(data_ewk["arXiv_2402.00603_4"],(0,0))



data_ewk["arXiv_2402.08347_1"] = np.genfromtxt("data/EWKinos/arXiv_2402.08347/HEPData-ins2758009-v1-Table_4.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2402.08347_1"] = add_zero_endpoints(data_ewk["arXiv_2402.08347_1"],(0,0))

data_ewk["arXiv_2402.08347_2"] = np.genfromtxt("data/EWKinos/arXiv_2402.08347/HEPData-ins2758009-v1-Table_10.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2402.08347_2"] = add_zero_endpoints(data_ewk["arXiv_2402.08347_2"],(0,0))

data_ewk["arXiv_2402.08347_3"] = np.genfromtxt("data/EWKinos/arXiv_2402.08347/HEPData-ins2758009-v1-Table_16.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","y"])
data_ewk["arXiv_2402.08347_3"] = add_zero_endpoints(data_ewk["arXiv_2402.08347_3"],(0,0))






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

ax.text(0.1,0.9,       r"Sparticle Limits, Strong Production", size=11,clip_on=False, fontweight="bold",transform=ax.transAxes)
ax.text(0.1,0.9-1*0.05, r"Various Assumptions", size=11,clip_on=False,transform=ax.transAxes)
ax.text(0.1,0.9-2*0.05, r"Run-2 LHC", size=11,clip_on=False,transform=ax.transAxes)
ax.text(0.1,0.9-3*0.05, r"95% CL", size=11,clip_on=False,transform=ax.transAxes)

ax.text(1700, 1000, r"Gluinos", size=11,clip_on=False, color="k", alpha=1.0, fontweight='bold')
ax.text(500, 200, r"Squarks", size=11,clip_on=False,  color="k", alpha=1.0, fontweight='bold')


# ax.text(1000, 300, r"Make another plot with EWK production", size=11,clip_on=False,  color="k", alpha=1.0, fontweight='bold')
# ax.text(1000, 200, r"Add stops to the squark category", size=11,clip_on=False,  color="k", alpha=1.0, fontweight='bold')



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

ax.text(100, 190, r"$m_{\tilde{\chi}^0_1}>m_X$", size=9,clip_on=False, rotation=angle_deg, ha='left', va='bottom')
doFillBetween([0,2500], [0,2500], axis=ax, dy=-10, alpha=0.4, n=30, log=False,clip_on=False)
ax.plot( [0,2500], [0,2500], "-", lw=0.5, color="black" )
# ax1.plot([0,1], [0,1], c="k",lw=0.5)
# ax1.text(0.7, 0.7 , r"$A\times\varepsilon=\varepsilon_{\mathrm{trigger}}$", size=9,clip_on=False, ha="right")
# ax1.text(0.6, 0.64 , r"Trigger Limited Searches Near Diagonal", rotation=31, size=9,clip_on=False, ha="left")





fig.savefig("Vanilla_Strong.pdf")


plt.cla()
plt.clf()






baselength=4
fig, ax = plt.subplots(1,1, figsize=(1.5*baselength, 1*baselength))


### Actual Curves:



#
i=3

alpha=2/len(data_ewk)#0.3
if alpha>0.5:
     alpha=0.5
if alpha<0.1:
     alpha=0.1
alpha=0.3

ax.fill(data_ewk["arXiv_2205.09597_1"]['x'], data_ewk["arXiv_2205.09597_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_ewk["arXiv_2205.09597_2"]['x'], data_ewk["arXiv_2205.09597_2"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_ewk["arXiv_2205.09597_3"]['x'], data_ewk["arXiv_2205.09597_3"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_ewk["arXiv_2205.09597_4"]['x'], data_ewk["arXiv_2205.09597_4"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_ewk["arXiv_2205.09597_5"]['x'], data_ewk["arXiv_2205.09597_5"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_ewk["arXiv_2205.09597_6"]['x'], data_ewk["arXiv_2205.09597_6"]['y'], color=colors[i], alpha=alpha, lw=0)


ax.fill(data_ewk["arXiv_2402.00603_1"]['x'], data_ewk["arXiv_2402.00603_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_ewk["arXiv_2402.00603_2"]['x'], data_ewk["arXiv_2402.00603_2"]['y'], color=colors[i], alpha=alpha, lw=0)
# ax.fill(data_ewk["arXiv_2402.00603_3"]['x'], data_ewk["arXiv_2402.00603_3"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_ewk["arXiv_2402.00603_4"]['x'], data_ewk["arXiv_2402.00603_4"]['y'], color=colors[i], alpha=alpha, lw=0)



ax.fill(data_ewk["arXiv_2402.08347_1"]['x'], data_ewk["arXiv_2402.08347_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_ewk["arXiv_2402.08347_2"]['x'], data_ewk["arXiv_2402.08347_2"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_ewk["arXiv_2402.08347_3"]['x'], data_ewk["arXiv_2402.08347_3"]['y'], color=colors[i], alpha=alpha, lw=0)




#
i=2

alpha=2/len(data_slsl)#0.3
if alpha>0.5:
     alpha=0.5
if alpha<0.1:
     alpha=0.1
alpha=0.3

ax.fill(data_slsl["arXiv_1908.08215"]['x'], data_slsl["arXiv_1908.08215"]['y'], color=colors[i], alpha=alpha, lw=0)


ax.fill(data_slsl["arXiv_2209.13935_1"]['x'], data_slsl["arXiv_2209.13935_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_2209.13935_2"]['x'], data_slsl["arXiv_2209.13935_2"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_2209.13935_3"]['x'], data_slsl["arXiv_2209.13935_3"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_2209.13935_4"]['x'], data_slsl["arXiv_2209.13935_4"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_2209.13935_5"]['x'], data_slsl["arXiv_2209.13935_5"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_2209.13935_6"]['x'], data_slsl["arXiv_2209.13935_6"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_2209.13935_7"]['x'], data_slsl["arXiv_2209.13935_7"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_2209.13935_8"]['x'], data_slsl["arXiv_2209.13935_8"]['y'], color=colors[i], alpha=alpha, lw=0)


# ax.fill(data_slsl["arXiv_2503.13135_1"]['x'], data_slsl["arXiv_2503.13135_1"]['y'], color=colors[i], alpha=alpha, lw=0)
# ax.fill(data_slsl["arXiv_2503.13135_2"]['x'], data_slsl["arXiv_2503.13135_2"]['y'], color=colors[i], alpha=alpha, lw=0)
# ax.fill(data_slsl["arXiv_2503.13135_3"]['x'], data_slsl["arXiv_2503.13135_3"]['y'], color=colors[i], alpha=alpha, lw=0)
# ax.fill(data_slsl["arXiv_2503.13135_4"]['x'], data_slsl["arXiv_2503.13135_4"]['y'], color=colors[i], alpha=alpha, lw=0)



ax.fill(data_slsl["arXiv_1911.12606_1"]['x'], data_slsl["arXiv_1911.12606_1"]['x']-data_slsl["arXiv_1911.12606_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_1911.12606_2"]['x'], data_slsl["arXiv_1911.12606_2"]['x']-data_slsl["arXiv_1911.12606_2"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_1911.12606_3"]['x'], data_slsl["arXiv_1911.12606_3"]['x']-data_slsl["arXiv_1911.12606_3"]['y'], color=colors[i], alpha=alpha, lw=0)




ax.fill(data_slsl["arXiv_2402.00603_1"]['x'], data_slsl["arXiv_2402.00603_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_2402.00603_2"]['x'], data_slsl["arXiv_2402.00603_2"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_2402.00603_3"]['x'], data_slsl["arXiv_2402.00603_3"]['y'], color=colors[i], alpha=alpha, lw=0)




ax.fill(data_slsl["arXiv_2207.02254_1"]['x'], data_slsl["arXiv_2207.02254_1"]['y'], color=colors[i], alpha=alpha, lw=0)
ax.fill(data_slsl["arXiv_2207.02254_2"]['x'], data_slsl["arXiv_2207.02254_2"]['y'], color=colors[i], alpha=alpha, lw=0)












ax.set_xlabel(r'$m_{X}$ [GeV]',)
ax.set_ylabel(r'$m_{\chi^0_1}$ [GeV]',)
# ax.xaxis.set_label_coords(1.02, -0.07)
# ax.set_ylabel(r'Excluded Stop Squark Mass $m_{\tilde{t}}$ [GeV]')
# ax.set_xlim([2e-6,2e4])
# ax2.set_xlim([1.1e13,9e18])
ax.set_ylim([0,1200])
ax.set_xlim([0,1300])
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

ax.text(0.1,0.9,       r"Sparticle Limits, EW Production", size=11,clip_on=False, fontweight="bold",transform=ax.transAxes)
ax.text(0.1,0.9-1*0.05, r"Various Assumptions", size=11,clip_on=False,transform=ax.transAxes)
ax.text(0.1,0.9-2*0.05, r"Run-2 LHC", size=11,clip_on=False,transform=ax.transAxes)
ax.text(0.1,0.9-3*0.05, r"95% CL", size=11,clip_on=False,transform=ax.transAxes)

ax.text(750, 200, r"EWKinos", size=11,clip_on=False, color="k", alpha=1.0, fontweight='bold')
ax.text(200, 50, r"Sleptons", size=11,clip_on=False,  color="k", alpha=1.0, fontweight='bold')


# ax.text(1000, 300, r"Make another plot with EWK production", size=11,clip_on=False,  color="k", alpha=1.0, fontweight='bold')
# ax.text(1000, 200, r"Add stops to the squark category", size=11,clip_on=False,  color="k", alpha=1.0, fontweight='bold')



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

ax.text(50, 100, r"$m_{\tilde{\chi}^0_1}>m_X$", size=9,clip_on=False, rotation=angle_deg, ha='left', va='bottom')
doFillBetween([0,2500], [0,2500], axis=ax, dy=-5, alpha=0.4, n=30, log=False,clip_on=False)
ax.plot( [0,2500], [0,2500], "-", lw=0.5, color="black" )

fig.savefig("Vanilla_EW.pdf")