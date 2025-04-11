# agents/soil_agent.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain_core.tools import tool
from langchain.schema import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from utils.soil_extractor import get_soil_info
llm=ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama-3.3-70b-versatile"
)


@tool
def analyze_soil(soil_data: dict) -> str:
    """
    Analyzes the given soil data and returns soil type, fertility rating, and suggestions.
    """
    messages = [
        SystemMessage(content="You are an expert soil scientist."),
        HumanMessage(content=f"""
        Analyze this soil profile: {soil_data}.
        Classify the soil type, rate fertility (low/medium/high), and suggest improvements if needed.
        """)
    ]
    return llm(messages).content


def run_soil_analysis(lat: float, lon: float) -> str:
    """
    Combines raster reading and LLM analysis. Input: lat/lon. Output: full soil report.
    """
    raw_values = get_soil_info(lat, lon)
    report = analyze_soil.invoke({"soil_data": raw_values})
    return report
