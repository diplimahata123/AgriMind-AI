# agents/practice_agent.py

from langchain_core.tools import tool
from langchain.schema import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
llm=ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama-3.3-70b-versatile"
)

@tool
def suggest_practices(crops: str, soil_data: dict, climate_data: dict) -> str:
    """
    Recommends irrigation, fertilization, and pest control practices.
    """
    messages = [
        SystemMessage(content="You are an expert in sustainable farming practices."),
        HumanMessage(content=f"""
        For the following crops:\n{crops}
        Under these soil conditions:\n{soil_data}
        And climate conditions:\n{climate_data}
        Suggest sustainable practices for irrigation, fertilization, and pest control.
        """)
    ]
    return llm(messages).content
