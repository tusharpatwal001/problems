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

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MAX_15"), google_api_key=os.getenv("GEMINI_API_KEY")
)


@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: add, sub, mul, div, modulus
    """
    try:
        if operation == "add":
            result = first_num + second_num
        elif operation == "sub":
            result = first_num - second_num
        elif operation == "mul":
            result = first_num * second_num
        elif operation == "modulus":
            result = first_num % second_num
        elif operation == "div":
            if second_num == 0:
                return {"error": "Division by zero is not allowed"}
            result = first_num / second_num
        else:
            return {"error": f"Unsupported operation '{operation}'"}

        return {
            "first_num": first_num,
            "second_num": second_num,
            "operation": operation,
            "result": result,
        }
    except Exception as e:
        return {"error": str(e)}


tools = [calculator]
llm_with_tools = llm.bind_tools(tools)


# defininig state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def build_graph():

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
    chatbot = build_graph()

    result = await chatbot.ainvoke(
        {
            "messages": [
                HumanMessage(
                    content="Find the modulus(%) of 2345 and 23 and give the answer like a cricket commentator."
                )
            ]
        }
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
