import rasterio

def get_soil_info(lat, lon):
    with rasterio.open("data/soil_data.tif") as src:
        coords = [(lon, lat)]  # Note: rasterio expects (x=lon, y=lat)
        values = list(src.sample(coords))[0]
        return {
            "bulk_density": values[0],
            "clay": values[1],
            "carbon": values[2],
            "ph": values[3],
            "sand": values[4],
            "silt": values[5]
        }

