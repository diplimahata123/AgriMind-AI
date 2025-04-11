import gradio as gr
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

def agrimind_pipeline(user_input):
    try:
        if "," in user_input:
            lat, lon = map(float, user_input.split(","))
        else:
            lat, lon = get_coordinates(user_input)

        soil_data = get_soil_info(lat, lon)
        climate_data = get_climate_data(lat, lon)
        soil_report = run_soil_analysis(lat, lon)
        climate_report = get_climate.invoke({"climate_data": climate_data})
        crop = recommend_crops.invoke({
            "soil_analysis": soil_report,
            "climate_analysis": climate_report
        })
        practices = suggest_practices.invoke({
            "crops": crop,
            "soil_data": soil_data,
            "climate_data": climate_data
        })
        yield_report = predict_yield.invoke({
            "crops": crop,
            "soil_data": soil_data,
            "climate_data": climate_data,
            "practices": practices
        })
        plan = compose_plan.invoke({
            "all_outputs": {
                "soil_report": soil_report,
                "climate_report": climate_report,
                "crops": crop,
                "practices": practices,
                "yield_report": yield_report
            }
        })

        return f"📍 Location: {lat}, {lon}\n\n🌾 Agri Plan:\n\n{plan}"

    except Exception as e:
        return f"❌ Error: {str(e)}"

# UI Layout
iface = gr.Interface(
    fn=agrimind_pipeline,
    inputs=gr.Textbox(label="Enter a place name or lat,lon", placeholder="e.g. Jhargram or 22.5,88.3"),
    outputs="text",
    title="AgriMind AI 🌾",
    description="Smart Agriculture Planner - Get a complete agri plan based on soil, climate, and crop analysis.")

if __name__ == "__main__":
    iface.launch()
    


