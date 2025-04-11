# agents/climate_agent.py

from langchain_core.tools import tool
from langchain.schema import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama-3.3-70b-versatile"
)

@tool
def get_climate(climate_data: dict) -> str:
    """
    Evaluates climate conditions and returns optimal growing season, risks, and insights.
    """
    messages = [
        SystemMessage(content="You are a climate scientist specializing in agriculture."),
        HumanMessage(content=f"""
        Given this climate data: {climate_data},
        describe the suitable growing season, any weather risks, and drought/frost likelihood.
        """)
    ]
    return llm(messages).content
