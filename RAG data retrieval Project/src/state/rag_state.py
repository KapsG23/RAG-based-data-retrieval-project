"""RAG state definition for LangGraph"""

from typing import List
from pydantic import BaseModel
from langchain.schema import Document

class RAGState(BaseModel):
    """State object for RAG workflow"""
    
    # 3 parameters/variables to store in the rag state class.
    # question we are storing it.
    # retrieved_docs which is actually coming from the retriever.
    # answer which is actually coming from the LLM in string format.
    question: str
    retrieved_docs: List[Document] = []
    answer: str = ""