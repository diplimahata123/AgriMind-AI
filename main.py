from geopy.geocoders import Nominatim
from agents.soil_agent import run_soil_analysis
from agents.climate_agent import get_climate
from agents.crop_agent import recommend_crops
from agents.practice_agent import suggest_practices
from agents.yield_agent import predict_yield
from agents.composer_agent import compose_plan
from utils.climate_fetcher import get_climate_data
from utils.soil_extractor import get_soil_info

def get_coordinates(place):
    geolocator = Nominatim(user_agent="agrimind_ai")
    location = geolocator.geocode(place)
    if location:
        return location.latitude, location.longitude
    else:
        raise ValueError("❌ Location not found. Try a more specific name.")

def main():
    print("🌾 Welcome to AgriMind AI – Smart Agriculture Planner")
    user_input = input("📍 Enter a place name (e.g., 'jhargram') or lat,lon (e.g., '28.6,77.2'): ").strip()

    if "," in user_input:
        lat, lon = map(float, user_input.split(","))
    else:
        lat, lon = get_coordinates(user_input)

    print(f"\n🔍 Analyzing location: {lat}, {lon}...\n")

    # Get raw soil and climate data
    soil_data = get_soil_info(lat, lon)
    climate_data = get_climate_data(lat, lon)

    # Agent 1: Soil Analysis
    print("🧪 Analyzing Soil...")
    soil_report = run_soil_analysis(lat, lon)

    # Agent 2: Climate Analysis
    print("🌦️ Fetching Climate Data...")
    climate_report = get_climate.invoke({"climate_data": climate_data})

    # Agent 3: Crop Recommendation
    print("🌱 Recommending Suitable Crops...")
    crop = recommend_crops.invoke({
        "soil_analysis": soil_report,
        "climate_analysis": climate_report
    })

    # Agent 4: Recommend Practices (FIXED INPUTS)
    practices = suggest_practices.invoke({
        "crops": crop,
        "soil_data": soil_data,         # ✅ Raw data, not report
        "climate_data": climate_data    # ✅ Raw data, not report
    })

    # Agent 5: Yield Estimation
    yield_report = predict_yield.invoke({
    "crops": crop,
    "soil_data": soil_data,
    "climate_data": climate_data,
    "practices": practices  
    })


    # Agent 6: Compose Final Plan
    print("🧠 Composing Full Agri Plan...\n")
   
    plan = compose_plan.invoke({
    "all_outputs": {
        "soil_report": soil_report,
        "climate_report": climate_report,
        "crops": crop,
        "practices": practices,
        "yield_report": yield_report
    }
    })

   
    print("🌾 AgriMind AI – Final Report:")
    print("-" * 60)
    print(plan)
    print("-" * 60)

if __name__ == "__main__":
    main()
