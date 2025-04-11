# utils/climate_fetcher.py

import random

def get_climate_data(lat: float, lon: float) -> dict:
    """
    Returns mock climate data for the given location.
    Replace this with real API calls (e.g., NASA POWER, Open-Meteo, Copernicus) for live data.
    """
    # Simulate realistic ranges based on location (customize if needed)
    return {
        "latitude": lat,
        "longitude": lon,
        "avg_temperature_c": round(random.uniform(18, 32), 1),
        "annual_rainfall_mm": round(random.uniform(600, 1600), 1),
        "humidity_percent": round(random.uniform(50, 90), 1),
        "drought_risk": random.choice(["low", "medium", "high"]),
        "frost_risk": random.choice(["low", "medium", "high"]),
        "season": random.choice(["kharif", "rabi", "dry", "wet"]),
    }
