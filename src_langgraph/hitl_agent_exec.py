from dotenv import load_dotenv
load_dotenv()
import sqlite3
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from utils import show_graph

from pydantic import BaseModel
from typing import Optional

class State()