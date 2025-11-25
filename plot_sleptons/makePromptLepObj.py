import csv,math
import numpy as np


import sys
sys.path.insert(0, "..")
from helperFunctions import *

def array_to_enclosed_obj(
    arr,
    obj_path="output.obj",
    y_thickness=1,   # how far to extrude in +y
    scalex=1e-2,        # global scale factor
    scalez=2e-3,
):
    """
    Build a fully enclosed OBJ volume from a NumPy array with
    columns 'x' and 'z'. The curve runs in the x–z plane.

    Geometry:
        bottom: ( x, 0,      z )
        top:    ( x, y_thick, z )

    All coordinates scaled by 'scale'.
    """

    # Ensure structured or dict-like dtype
    if not ('x' in arr.dtype.names and 'z' in arr.dtype.names):
        raise ValueError("Array must have columns named 'x' and 'z'")

    xs = arr['x']
    zs = arr['z']

    n = len(xs)
    if n < 2:
        raise ValueError("Need at least 2 points to build a volume.")

    # -------------------------------------------------------
    # Build vertices (scaled)
    # bottom: y = 0
    # top:    y = y_thickness
    # -------------------------------------------------------
    vertices_bottom = [
        (xs[i] * scalex, 0.0,             zs[i] * scalez)
        for i in range(n)
    ]
    vertices_top = [
        (xs[i] * scalex, -y_thickness, zs[i] * scalez)
        for i in range(n)
    ]

    # -------------------------------------------------------
    # Write OBJ
    # -------------------------------------------------------
    with open(obj_path, "w") as obj:

        # Vertex block
        for v in vertices_bottom:
            obj.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for v in vertices_top:
            obj.write(f"v {v[0]} {v[1]} {v[2]}\n")

        # index helpers
        def b(i): return 1 + i
        def t(i): return 1 + n + i

        # -------------------------
        # Side walls between points
        # -------------------------
        for i in range(n - 1):
            b1, b2 = b(i), b(i+1)
            t1, t2 = t(i), t(i+1)

            obj.write(f"f {b1} {t1} {t2}\n")
            obj.write(f"f {b1} {t2} {b2}\n")

        # -------------------------
        # Bottom cap (fan)
        # -------------------------
        for i in range(1, n - 1):
            obj.write(f"f {b(0)} {b(i)} {b(i+1)}\n")

        # -------------------------
        # Top cap (reverse winding)
        # -------------------------
        for i in range(1, n - 1):
            obj.write(f"f {t(0)} {t(i+1)} {t(i)}\n")

        # -------------------------
        # Front end cap (first segment)
        # -------------------------
        obj.write(f"f {b(0)} {t(0)} {t(1)}\n")
        obj.write(f"f {b(0)} {t(1)} {b(1)}\n")

        # -------------------------
        # Back end cap (last segment)
        # -------------------------
        i = n - 1
        obj.write(f"f {b(i)} {t(i-1)} {t(i)}\n")
        obj.write(f"f {b(i)} {b(i-1)} {t(i-1)}\n")

    print(f"OBJ written to {obj_path}")


data_slsl = {}

data_slsl["arXiv_1908.08215"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_1908.08215/HEPData-ins1750597-v4-Exclusion_contour_(obs)_3.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","z"])
data_slsl["arXiv_1908.08215"] = add_zero_endpoints(data_slsl["arXiv_1908.08215"],(0,0))

data_slsl["arXiv_2209.13935_1"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_comb_obs_nominal_SR0j.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2209.13935_1"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_1"],(0,0))

data_slsl["arXiv_2209.13935_2"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_comb_obs_nominal_SR1j.csv", delimiter=",", skip_header=10, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2209.13935_2"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_2"],(0,0))

data_slsl["arXiv_2209.13935_3"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_ee_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2209.13935_3"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_3"],(0,0))

data_slsl["arXiv_2209.13935_4"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_eLeL_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2209.13935_4"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_4"],(0,0))

data_slsl["arXiv_2209.13935_5"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_eReR_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2209.13935_5"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_5"],(0,0))

data_slsl["arXiv_2209.13935_6"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_mm_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2209.13935_6"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_6"],(0,0))

data_slsl["arXiv_2209.13935_7"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_mLmL_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2209.13935_7"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_7"],(0,0))

data_slsl["arXiv_2209.13935_8"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2209.13935/HEPData-ins2157951-v1-excl_mRmR_obs_nominal.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2209.13935_8"] = add_zero_endpoints(data_slsl["arXiv_2209.13935_8"],(0,0))

data_slsl["arXiv_1911.12606_1"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_1911.12606/HEPData-ins1767649-v5-Figure_2a_LH_slepton_Observed.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","z"])
data_slsl["arXiv_1911.12606_1"] = add_zero_endpoints(data_slsl["arXiv_1911.12606_1"],(0,0))

data_slsl["arXiv_1911.12606_2"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_1911.12606/HEPData-ins1767649-v5-Figure_2a_RH_slepton_Observed.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","z"])
data_slsl["arXiv_1911.12606_2"] = add_zero_endpoints(data_slsl["arXiv_1911.12606_2"],(0,0))

data_slsl["arXiv_1911.12606_3"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_1911.12606/HEPData-ins1767649-v5-Figure_16a_Observed.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","z"])
data_slsl["arXiv_1911.12606_3"] = add_zero_endpoints(data_slsl["arXiv_1911.12606_3"],(0,0))


data_slsl["arXiv_2402.00603_1"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2402.00603/HEPData-ins2754043-v1-Table_13.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2402.00603_1"] = add_zero_endpoints(data_slsl["arXiv_2402.00603_1"],(0,0))

data_slsl["arXiv_2402.00603_2"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2402.00603/HEPData-ins2754043-v1-Table_19.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2402.00603_2"] = add_zero_endpoints(data_slsl["arXiv_2402.00603_2"],(0,0))

data_slsl["arXiv_2402.00603_3"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2402.00603/HEPData-ins2754043-v1-Table_25.csv", delimiter=",", skip_header=8, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2402.00603_3"] = add_zero_endpoints(data_slsl["arXiv_2402.00603_3"],(0,0))


data_slsl["arXiv_2207.02254_1"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2207.02254/HEPData-ins2106478-v1-Figure_007-a_observed_exclusions.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2207.02254_1"] = add_zero_endpoints(data_slsl["arXiv_2207.02254_1"],(0,0))

data_slsl["arXiv_2207.02254_2"] = np.genfromtxt("../plot_vanillaSUSY/data/SLEPTONSLEPTON/arXiv_2207.02254/HEPData-ins2106478-v1-Figure_007-b_observed_exclusions.csv", delimiter=",", skip_header=9, skip_footer=0, names=["x","z"])
data_slsl["arXiv_2207.02254_2"] = add_zero_endpoints(data_slsl["arXiv_2207.02254_2"],(0,0))



for thing in data_slsl:
    array_to_enclosed_obj(
        data_slsl[thing],
        obj_path=f"data/SLEPTONSLEPTON/{thing}_obs.obj",
        y_thickness=0.1,
    )
