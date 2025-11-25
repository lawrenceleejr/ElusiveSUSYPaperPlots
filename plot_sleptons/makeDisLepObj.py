import csv,math

def csv_to_enclosed_obj(
    csv_path,
    obj_path="output.obj",
    header_rows=1,
    offset=70.0,        # extrusion plane: z = x - offset
    scalex=1e-2,         # global scale factor
    scalez=1e-2,         # global scale factor
    offsety=3,
):
    """
    Build a fully enclosed OBJ volume from a 2-column CSV.

    CSV format:
      col1 = mass (GeV)    -> x
      col2 = lifetime (ns) -> y

    For each CSV point:
      bottom vertex: (x, y, 0)
      top vertex:    (x, y, x - offset)

    All coordinates are scaled by `scale` before exporting.
    """

    xs, ys = [], []

    # --------------------------------------
    # Read CSV
    # --------------------------------------
    with open(csv_path, newline="") as f:
        reader = csv.reader(f)
        for _ in range(header_rows):
            next(reader)

        for row in reader:
            if len(row) < 2:
                continue
            xs.append(float(row[0]))
            ys.append(float(row[1]))

    n = len(xs)
    if n < 2:
        raise ValueError("Need at least 2 rows of data.")

    # --------------------------------------
    # Build vertices (scaled)
    # --------------------------------------
    vertices_bottom = [
        (xs[i] * scalex, -1*math.log10(ys[i])-offsety , 0.0)
        for i in range(n)
    ]
    vertices_top = [
        (xs[i] * scalex, -1*math.log10(ys[i])-offsety , (xs[i] - offset) * scalez)
        # (xs[i] * scale, math.log10(ys[i]) , 0)
        for i in range(n)
    ]
    print([(xs[i] * scalex, math.log10(ys[i]) ) for i in range(n)])

    # --------------------------------------
    # Write OBJ
    # --------------------------------------
    with open(obj_path, "w") as obj:

        # Vertices
        for v in vertices_bottom:
            obj.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for v in vertices_top:
            obj.write(f"v {v[0]} {v[1]} {v[2]}\n")

        # Index helpers: bottom i → 1..n, top i → n+1..2n
        def b(i): return 1 + i
        def t(i): return 1 + n + i

        # --------------------------------------
        # Side walls
        # --------------------------------------
        for i in range(n - 1):
            b1, b2 = b(i), b(i+1)
            t1, t2 = t(i), t(i+1)

            obj.write(f"f {b1} {t1} {t2}\n")
            obj.write(f"f {b1} {t2} {b2}\n")

        # --------------------------------------
        # Bottom cap (fan)
        # --------------------------------------
        for i in range(1, n - 1):
            obj.write(f"f {b(0)} {b(i)} {b(i+1)}\n")

        # --------------------------------------
        # Top cap (fan, reverse winding)
        # --------------------------------------
        for i in range(1, n - 1):
            obj.write(f"f {t(0)} {t(i+1)} {t(i)}\n")

        # --------------------------------------
        # Front end cap
        # --------------------------------------
        obj.write(f"f {b(0)} {t(0)} {t(1)}\n")
        obj.write(f"f {b(0)} {t(1)} {b(1)}\n")

        # --------------------------------------
        # Back end cap
        # --------------------------------------
        i = n - 1
        obj.write(f"f {b(i)} {t(i-1)} {t(i)}\n")
        obj.write(f"f {b(i)} {b(i-1)} {t(i-1)}\n")

    print(f"OBJ written to {obj_path}")


csv_to_enclosed_obj(csv_path="data/atlas_139_displep/HEPData-ins1831504-v1-Observed_smuon_limits.csv", obj_path="data/atlas_139_displep/HEPData-ins1831504-v1-Observed_smuon_limits.obj", header_rows=8, offset=70.0)
csv_to_enclosed_obj(csv_path="data/atlas_139_displep/HEPData-ins1831504-v1-Observed_LH_smuon_limits.csv", obj_path="data/atlas_139_displep/HEPData-ins1831504-v1-Observed_LH_smuon_limits.obj", header_rows=8, offset=70.0)
csv_to_enclosed_obj(csv_path="data/atlas_139_displep/HEPData-ins1831504-v1-Observed_RH_smuon_limits.csv", obj_path="data/atlas_139_displep/HEPData-ins1831504-v1-Observed_RH_smuon_limits.obj", header_rows=8, offset=70.0)

csv_to_enclosed_obj(csv_path="data/atlas_139_displep/HEPData-ins1831504-v1-Observed_LH_stau_limits.csv", obj_path="data/atlas_139_displep/HEPData-ins1831504-v1-Observed_LH_stau_limits.obj", header_rows=8, offset=70.0)



csv_to_enclosed_obj(csv_path="data/atlas_140_dedx/HEPData-ins2878503-v1-Figure_fig_13a_obs.csv", obj_path="data/atlas_140_dedx/HEPData-ins2878503-v1-Figure_fig_13a_obs.obj", header_rows=13, offset=170.0)