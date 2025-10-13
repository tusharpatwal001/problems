from langgraph.graph import START, END, StateGraph
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import  InMemorySaver
from langgraph.graph.message import add_messages

# initialize llm model
llm = ChatOllama(model='gemma3:4b')

# initialize state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# build node
def chatbot_node(state: ChatState):
    messages = state["messages"]
    response = llm.invoke(messages)

    return {"messages": [response]}


# initialize the graph
graph = StateGraph(ChatState)

# add nodes
graph.add_node("chatbot_node", chatbot_node)

# add edge
graph.add_edge(START, "chatbot_node")
graph.add_edge("chatbot_node", END)

# initialize memory saver
checkpointer = InMemorySaver()

# compile graph
chatbot = graph.compile(checkpointer=checkpointer)



