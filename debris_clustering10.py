import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from skyfield.api import load, EarthSatellite
from datetime import datetime, timezone

# Path to your TLE file
file_path = '/home/osint/debris-env/FENGUN_1C_DEB_TLE.txt'

# Function to load TLEs from file
def load_tle_from_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    tle_list = []
    i = 0
    while i < len(lines):
        if lines[i].startswith(('0 ', '1 ', '2 ')) or lines[i].strip() == '':
            i += 1
            continue
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

# Verify first few epoch dates
print("--- Epochs of first 10 satellites ---")
for sat in satellites[:10]:
    try:
        epoch_jd = sat.epoch.utc_jpl()
        epoch_dt = sat.epoch.utc_datetime().replace(tzinfo=timezone.utc)
        print(f"{sat.name} epoch (JD): {epoch_jd}")
        print(f"{sat.name} epoch (datetime): {epoch_dt}")
    except Exception as e:
        print(f"Error fetching epoch for {sat.name}: {e}")

# 4. Extract orbital parameters
def extract_params(sat):
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

# Collect parameters and epochs
params_list = []
epoch_dates = []
names_list = []

for sat in satellites:
    try:
        params = extract_params(sat)
        epoch_dt = sat.epoch.utc_datetime().replace(tzinfo=timezone.utc)
        params_list.append(params)
        epoch_dates.append(epoch_dt)
        names_list.append(sat.name)
    except:
        continue

# Convert epoch datetime to ensure timezone consistency
dt_array = np.array(epoch_dates)

# 7. Filter debris based on recent epoch (e.g., last 6 months)
cutoff_date = datetime(2023, 1, 1, tzinfo=timezone.utc)
filter_mask = dt_array > cutoff_date

# Filter data
filtered_params = np.array([params for i, params in enumerate(params_list) if filter_mask[i]])
filtered_names = [name for i, name in enumerate(names_list) if filter_mask[i]]

# Check if there is data after filtering
if len(filtered_params) == 0:
    print("No debris data after filtering! Adjust your cutoff date.")
    exit()

# 8. Normalize data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
params_norm = scaler.fit_transform(filtered_params)

# 9. Check for NaNs
nan_mask = np.isnan(params_norm).any(axis=1)

# --- Remove NaNs if any ---
#nan_mask = np.isnan(params_norm).any(axis=1)

if np.any(nan_mask):
    print(f"Found {np.sum(nan_mask)} NaN rows. Removing them.")
    params_norm = params_norm[~nan_mask]
    filtered_names = [name for i, name in enumerate(filtered_names) if not nan_mask[i]]

# --- Clustering ---
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.5, min_samples=1).fit(params_norm)
labels = db.labels_

# --- Output clustering results ---
print("Object : Cluster")
for name, label in zip(filtered_names, labels):
    print(f"{name} : {label}")

# --- Visualize: Inclination vs RAAN (or other parameters) ---
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.scatter(params_norm[:,1], params_norm[:,2], c=labels, cmap='tab10', alpha=0.7)
plt.xlabel('Inclination (normalized)')
plt.ylabel('RAAN (normalized)')
plt.title('FENGYUN 1C Debris Clusters')
plt.colorbar(label='Cluster ID')
plt.show()

