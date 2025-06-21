import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from skyfield.api import load, EarthSatellite
from datetime import datetime  # <-- add this line

# Path to your TLE file
file_path = '/home/osint/debris-env/FENGUN_1C_DEB_TLE.txt'

# Function to load TLEs from file
def load_tle_from_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    tle_list = []
    i = 0
    while i < len(lines):
        # Skip non-TLE lines or blank lines
        if lines[i].startswith(('0 ', '1 ', '2 ')) or lines[i].strip() == '':
            i += 1
            continue
        # parse a block: name, line1, line2
        name = lines[i].strip()
        line1 = lines[i+1].strip()
        line2 = lines[i+2].strip()
        tle_list.append((name, line1, line2))
        i += 3
    return tle_list

# Load TLEs
tle_data = load_tle_from_file(file_path)

# Initialize Skyfield
ts = load.timescale()

# Parse TLEs into Skyfield satellite objects
satellites = []
for name, line1, line2 in tle_data:
    try:
        sat = EarthSatellite(line1, line2, name)
        satellites.append(sat)
    except Exception as e:
        print(f"Error parsing {name}: {e}")

# Function to extract orbital parameters
def extract_params(sat):
    # Use fixed date for consistency
    geocentric = sat.at(ts.utc(2023, 1, 1))
    pos = geocentric.position.km
    vel = geocentric.velocity.km_per_s
    r = np.linalg.norm(pos)
    mu = 398600.4418
    h_vec = np.cross(pos, vel)
    h = np.linalg.norm(h_vec)
    inclination = np.degrees(np.arccos(h_vec[2]/h))
    e_vec = (np.cross(vel, h_vec)/mu) - (pos/r)
    e = np.linalg.norm(e_vec)
    N_vec = np.cross([0,0,1], h_vec)
    N = np.linalg.norm(N_vec)
    RAAN = np.degrees(np.arctan2(N_vec[1], N_vec[0])) % 360 if N != 0 else 0
    if N != 0 and e != 0:
        arg_perigee = np.degrees(np.arccos(np.dot(N_vec, e_vec)/(N*e)))
        if e_vec[2] < 0:
            arg_perigee = 360 - arg_perigee
    else:
        arg_perigee = 0
    return [np.log10(r), inclination, RAAN, e]

# Extract parameters and collect epoch/time info
params_list = []
epoch_list = []
names_list = []

for sat in satellites:
    try:
        params = extract_params(sat)
        params_list.append(params)
        # Use model epoch (e.g., the TLE epoch)
        epoch_list.append(sat.model.epoch.utc_jpl())
        names_list.append(sat.name)
    except:
        continue

# Convert epoch JD to datetime for filtering
def jd_to_datetime(jd):
    t = ts.tjd(jd)
    return t.utc_datetime()

dt_array = np.array([jd_to_datetime(jd) for jd in epoch_list])

# Filtering: last 6 months (adjust date as needed)
#cutoff_date = datetime(2025, 1, 1)

cutoff_date = datetime(2000, 1, 1)  # or another earlier date


filter_mask = dt_array > cutoff_date

# Check min/max date in your data
print(f"Min date: {min(dt_array)}")
print(f"Max date: {max(dt_array)}")



print(f"Total TLE entries loaded: {len(tle_data)}")
print(f"Number of satellites parsed: {len(satellites)}")
print(f"Number of debris parameters extracted: {len(params_list)}")

print(f"Data date range: {min(dt_array)} to {max(dt_array)}")
print(f"Filtering debris newer than: {cutoff_date}")
print(f"Number of debris after filter: {np.sum(Dt_array > cutoff_date)}")



# Keep only recent debris
filtered_params = np.array([params for i, params in enumerate(params_list) if filter_mask[i]])
filtered_names = [name for i, name in enumerate(names_list) if filter_mask[i]]

# --- Normalize parameters ---
scaler = StandardScaler()
params_norm = scaler.fit_transform(filtered_params)

# --- Remove NaNs --
nan_mask = np.isnan(params_norm).any(axis=1)
if np.any(nan_mask):
    print(f"Found {np.sum(nan_mask)} rows with NaNs, removing.")
    params_norm = params_norm[~nan_mask]
    filtered_names = [name for i, name in enumerate(filtered_names) if not nan_mask[i]]

# --- Clustering ---
db = DBSCAN(eps=0.5, min_samples=1).fit(params_norm)
labels = db.labels_

# 11. **Print debris object and cluster assignment**
print("Debris Object : Cluster")
for name, label in zip(filtered_names, labels):
    print(f"{name} : Cluster {label}")
