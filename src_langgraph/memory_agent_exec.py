import os
import getpass
from dotenv import load_dotenv

load_dotenv()

from typing import Annotated, TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.schema import HumanMessage, AIMessage
from langchain.chat_models import ChatOpenAI
from utils import show_graph


class State(TypedDict):
    messages: Annotated[list, add_messages]


llm = ChatOpenAI(temperature=0)

print(llm([HumanMessage(content="Hello, I am Alice.")]))
# def chatbot_node(state: State):
#     response_msg = llm(state["messages"])
#     return {"messages": [response_msg]}


# graph_builder = StateGraph(State)
# graph_builder.add_node("Chatbot", chatbot_node)
# graph_builder.add_edge(START, "Chatbot")
# graph_builder.add_edge("Chatbot", END)


# from langgraph.checkpoint.memory import MemorySaver

# memory_saver = MemorySaver()
# graph = graph_builder.compile(checkpointer=memory_saver)
# show_graph(graph)

# thread_id = "example_session_1"
# config = {"configurable": {"thread_id": thread_id}}

# user_input1 = {"messages": [HumanMessage(content="Hello, I am Alice.")]}
# result1 = graph.invoke(user_input1, config=config)
# print("AI답변 1:", result1["messages"][-1].content)


# user_input2 = {"messages": [HumanMessage(content="What is my name?")]}
# result2 = graph.invoke(user_input2, config=config)  # 같은 thread_id로 두 번째 대화 실행
# print(
#     "AI답변 2:", result2["messages"][-1].content
# )  # AI의 응답 출력 (이전 대화 기억 활용 기대)
