# agents/composer_agent.py

from langchain_core.tools import tool
from langchain.schema import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
llm=ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama-3.3-70b-versatile"
)

@tool
def compose_plan(all_outputs: dict) -> str:
    """
    Combines all agent outputs into a clean, readable agri plan.
    """
    messages = [
        SystemMessage(content="You are a report generator for agriculture planning."),
        HumanMessage(content=f"""
        Combine the following data into a readable agri plan:
        {all_outputs}
        Include: recommended crops, practices, expected yields, and sustainability insights.
        Format it as a readable report.
        """)
    ]
    return llm(messages).content

