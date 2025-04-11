# agents/crop_agent.py

from langchain_core.tools import tool
from langchain.schema import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

llm=ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama-3.3-70b-versatile"
)

@tool
def recommend_crops(soil_analysis: str, climate_analysis: str) -> str:
    """
    Based on soil and climate reports, suggest best-fit crops.
    """
    messages = [
        SystemMessage(content="You are an expert agronomist."),
        HumanMessage(content=f"""
        Based on this soil analysis:\n{soil_analysis}
        and this climate analysis:\n{climate_analysis}
        List 3-5 most suitable crops with reasons.
        """)
    ]
    return llm(messages).content
