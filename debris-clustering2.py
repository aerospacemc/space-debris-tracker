import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.impute import SimpleImputer
from skyfield.api import load, EarthSatellite

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

# Load TLE data
tle_data = load_tle_from_file(file_path)

# Initialize Skyfield
ts = load.timescale()

# Convert TLEs into satellite objects
satellites = []
for name, line1, line2 in tle_data:
    try:
        sat = EarthSatellite(line1, line2, name)
        satellites.append(sat)
    except Exception as e:
        print(f"Error parsing TLE for {name}: {e}")

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
    inclination = np.degrees(np.arccos(h_vec[2] / h))
    e_vec = (np.cross(vel, h_vec) / mu) - (pos / r)
    e = np.linalg.norm(e_vec)
    N_vec = np.cross([0, 0, 1], h_vec)
    N = np.linalg.norm(N_vec)
    RAAN = np.degrees(np.arctan2(N_vec[1], N_vec[0])) % 360 if N != 0 else 0
    if N != 0 and e != 0:
        arg_perigee = np.degrees(np.arccos(np.dot(N_vec, e_vec) / (N * e)))
        if e_vec[2] < 0:
            arg_perigee = 360 - arg_perigee
    else:
        arg_perigee = 0
    return [np.log10(r), inclination, RAAN, e]

# Extract parameters for each satellite
params_list = []
for sat in satellites:
    params = extract_params(sat)
    params_list.append(params)

params_array = np.array(params_list)

# Normalize the features
scaler = StandardScaler()
params_normalized = scaler.fit_transform(params_array)

# Check for NaNs
nan_rows = np.isnan(params_normalized).any(axis=1)
if np.any(nan_rows):
    print(f"Found {np.sum(nan_rows)} rows with NaNs. Removing them.")
    params_clean = params_normalized[~nan_rows]
else:
    params_clean = params_normalized

# Run clustering
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.5, min_samples=1).fit(params_clean)
labels = db.labels_

# Output object names with their cluster assignment
for idx, label in enumerate(labels):
    print(f"Object: {satellites[idx].name} - Cluster: {label}")

# Plot inclination vs RAAN for clusters
import matplotlib.pyplot as plt
plt.scatter(params_clean[:,1], params_clean[:,2], c=labels, cmap='tab10', alpha=0.7)
plt.xlabel('Inclination (deg)')
plt.ylabel('RAAN (deg)')
plt.title('Debris Clusters in Orbital Parameter Space')
plt.colorbar(label='Cluster ID')
plt.show()
