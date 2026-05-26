# Start  -->  Retriever(retrieved data to generator)  -->  Generator  -->  End  (Graph Structure)
# retriever - giving request to vectorstore and based on the vectorstore we are going to get the response.
# sending the response to the generator.
# at the generaor stage we will have a LLM which take these response as context and then we are going to end state of our graph.



"""Graph builder for LangGraph workflow"""

from langgraph.graph import StateGraph, END
from src.state.rag_state import RAGState
from src.node.reactnode import RAGNodes
from src.node.nodes import RAGNodes


class GraphBuilder:
    """Builds and manages the LangGraph workflow"""
    
    def __init__(self, retriever, llm):
        """
        Initialize graph builder
        
        Args:
            retriever: Document retriever instance
            llm: Language model instance
        """
        self.nodes = RAGNodes(retriever, llm)
        self.graph = None
    
    # to build the graph starting from nodes to edges to conditional edges everything.
    def build(self):
        """
        Build the RAG workflow graph
        
        Returns:
            Compiled graph instance
        """
        # Create state graph
        builder = StateGraph(RAGState)
        
        # Add nodes
        # 1. node interacting with the vector store.
        builder.add_node("retriever", self.nodes.retrieve_docs)
        # 2. which has LLM with it and also has tools as an additonals but is required when we are trying to make the project more complex.
        builder.add_node("responder", self.nodes.generate_answer)
        
        # Set entry point
        builder.set_entry_point("retriever")
        
        # Add edges
        builder.add_edge("retriever", "responder")
        builder.add_edge("responder", END)
        
        # Compile graph
        self.graph = builder.compile()
        return self.graph
    
    ## we need to run this entire pipeline correct?
    ## that is we have to define the run function given below.
    def run(self, question: str) -> dict:
        """
        Run the RAG workflow
        
        Args:
            question: User question
            
        Returns:
            Final state with answer
        """
        if self.graph is None:
            self.build()
        
        initial_state = RAGState(question=question)
        return self.graph.invoke(initial_state)