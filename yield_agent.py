# agents/yield_agent.py

from langchain_core.tools import tool
from langchain.schema import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

llm=ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama-3.3-70b-versatile"
)

@tool
def predict_yield(crops: str, soil_data: dict, climate_data: dict, practices: str) -> str:
    """
    Estimates expected yield per hectare for the selected crops.
    """
    messages = [
        SystemMessage(content="You are an expert in crop yield forecasting."),
        HumanMessage(content=f"""
        Estimate expected yield (tons/hectare) for the following:
        Crops: {crops}
        Soil: {soil_data}
        Climate: {climate_data}
        Practices: {practices}
        Return results as crop name → estimated yield.
        """)
    ]
    return llm(messages).content
