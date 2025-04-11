import rasterio
import numpy as np

# List of your soil band files
input_files = [
    "data/bd.tif",         # Band 1: bulk density
    "data/clay.tif",       # Band 2: clay
    "data/ocd.tif",        # Band 3: organic carbon
    "data/PH_water.tif",   # Band 4: pH in water
    "data/sand.tif",       # Band 5: sand
    "data/sild.tif",       # Band 6: silt (I assume you meant "silt")
]

# Open all rasters and read first band
bands = []
for file in input_files:
    with rasterio.open(file) as src:
        band = src.read(1)
        bands.append(band)
        profile = src.profile  # Save metadata from first file

# Stack into multi-band array
stacked = np.stack(bands)

# Update metadata for multi-band
profile.update({
    "count": len(bands)
})

# Write the output file
with rasterio.open("data/soil_data.tif", "w", **profile) as dst:
    dst.write(stacked)

print("✅ Created data/soil_data.tif with 6 bands.")
