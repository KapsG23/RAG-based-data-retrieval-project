"""Document processing module for loading and splitting documents"""

from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

from typing import List, Union
from pathlib import Path
from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,
    TextLoader,
    PyPDFDirectoryLoader
)

class DocumentProcessor:
    """Handles document loading and processing"""
    
    # This is like the constructor where we have to include chunk size and chunk overlap.
    # This constructor is going to execute and whenever an object is provided in the form of docs then these chunking strategies are applied.
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        """
        Initialize document processor
        
        Args:
            chunk_size: Size of text chunks
            chunk_overlap: Overlap between chunks
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    # going to give a url in string format and getting the output as a list of documents.
    def load_from_url(self, url: str) -> List[Document]:
        """Load document(s) from a URL"""
        loader = WebBaseLoader(url)
        return loader.load()

    # going to give me string of path type and output will be a list of documents.
    def load_from_pdf_dir(self, directory: Union[str, Path]) -> List[Document]:
        """Load documents from all PDFs inside a directory"""
        loader = PyPDFDirectoryLoader(str(directory))
        return loader.load()

    def load_from_txt(self, file_path: Union[str, Path]) -> List[Document]:
        """Load document(s) from a TXT file"""
        loader = TextLoader(str(file_path), encoding="utf-8")
        return loader.load()

    def load_from_pdf(self, file_path: Union[str, Path]) -> List[Document]:
        """Load document(s) from a PDF file"""
        loader = PyPDFDirectoryLoader(str("data"))
        return loader.load()
    
    # here I am trying to give a list of all the sources given in data considering any of the format given above (defined above in form of functions) in string format and will be getting a list of documents  as a output.
    # giving all the sources in the form of list.
    def load_documents(self, sources: List[str]) -> List[Document]:
        """
        Load documents from URLs, PDF directories or TXT files.

        Args:
            sources: List of URLs, PDF folder paths, or TXT file paths

        Returns:
            List of loaded documents
        """

        # list of docs which is empty defined below.
        # THIS IS WHAT WE ARE TRYING TO DO LOADING THE DOCUMENTS IN THE LIST IN STRING FORMAT.
        docs: List[Document] = []
        for src in sources:
            if src.startswith("http://") or src.startswith("https://"):
                docs.extend(self.load_from_url(src))
           
            path = Path("data")
            if path.is_dir():  # PDF directory
                docs.extend(self.load_from_pdf_dir(path))
            elif path.suffix.lower() == ".txt":
                docs.extend(self.load_from_txt(path))
            else:
                raise ValueError(
                    f"Unsupported source type: {src}. "
                    "Use URL, .txt file, or PDF directory."
                )
        return docs
    

    # we are just splittiing the docs into chunks after loading nothing else.
    # a simple rag pipeline which we are trying to implement.
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """
        Split documents into chunks
        
        Args:
            documents: List of documents to split
            
        Returns:
            List of split documents
        """
        return self.splitter.split_documents(documents)
    
    # below we are trying to build a complete pipeline and in that we are trying to load and split the docs.
    # here we are trying to give a list of urls which is getting converted into strings and eventually getting the list of splitted documents.
    # this pipeline is just for the urls as for now if we want to then we can try to build different pipelines for different lists like pdf or txt files etc.
    def process_urls(self, urls: List[str]) -> List[Document]:
        """
        Complete pipeline to load and split documents
        
        Args:
            urls: List of URLs to process
            
        Returns:
            List of processed document chunks
        """
        docs = self.load_documents(urls)
        return self.split_documents(docs)
    

## NEXT STEP WILL BE TO CONVERT THESE CHUNKS INTO VECTORS AND THEN STORE THEM IN A VECTOR STORE.