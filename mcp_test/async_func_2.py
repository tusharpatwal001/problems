from langgraph.graph import StateGraph
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
import asyncio
import os
import sys
from pathlib import Path
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MAX_15"), google_api_key=os.getenv("GEMINI_API_KEY")
)

script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "math.py"))
client = MultiServerMCPClient(
    {
        "arith": {
            "transport": "stdio",
            "command": sys.executable,
            "args": [script_path],
        }
    }
)


# defininig state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


async def build_graph():

    tools = await client.get_tools()

    print(tools)

    llm_with_tools = llm.bind_tools(tools)

    async def chat_node(state: ChatState):
        messages = state["messages"]
        resposne = await llm_with_tools.ainvoke(messages)
        return {"messages": [resposne]}

    tool_node = ToolNode(tools)

    # defining graph
    graph = StateGraph(ChatState)

    graph.add_node("chat_node", chat_node)
    graph.add_node("tools", tool_node)

    # connections
    graph.set_entry_point("chat_node")
    graph.add_conditional_edges("chat_node", tools_condition)
    graph.add_edge("tools", "chat_node")

    chatbot = graph.compile()

    return chatbot


async def main():
    # chatbot = await build_graph()
    chatbot = await build_graph()

    result = await chatbot.ainvoke(
        {
            "messages": [
                HumanMessage(
                    content="find the power of 2 ke power 32"
                )
            ]
        }
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
