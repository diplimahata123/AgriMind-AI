# langgraph_runner.py

from agents.soil_agent import analyze_soil
from agents.climate_agent import get_climate  
from agents.crop_agent import recommend_crops
from agents.practice_agent import suggest_practices
from agents.yield_agent import predict_yield
from agents.composer_agent import compose_plan

def run_agri_pipeline(lat, lon, soil_data: dict, climate_data: dict):
    # Step 1: Analyze soil
    soil_analysis = analyze_soil.invoke({"soil_data": soil_data})
    
    # Step 2: Analyze climate
    climate_analysis = get_climate.invoke({"climate_data": climate_data})  # ✅ Fix here
    
    # Step 3: Recommend crops
    crop_suggestions = recommend_crops.invoke({
        "soil_data": soil_data,
        "climate_data": climate_data
    })
    
    # Step 4: Recommend farming practices
    practice_suggestions = suggest_practices.invoke({
        "soil_data": soil_data,
        "climate_data": climate_data,
        "crops": crop_suggestions
    })
    
    # Step 5: Estimate yield
    yield_estimate = predict_yield.invoke({
        "soil_data": soil_data,
        "climate_data": climate_data,
        "crops": crop_suggestions,
        "practices": practice_suggestions
    })
    
    # Step 6: Compose full plan
    full_report = compose_plan.invoke({
        "soil_analysis": soil_analysis,
        "climate_analysis": climate_analysis,
        "crops": crop_suggestions,
        "practices": practice_suggestions,
        "yield": yield_estimate
    })
    
    return full_report

