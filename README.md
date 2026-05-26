# 📚 RAG Data Retrieval Project

An advanced **Retrieval-Augmented Generation (RAG)** based intelligent document retrieval system that enables users to query documents using AI-powered semantic search and context-aware response generation.

This project combines **LLMs, vector databases, document ingestion pipelines, graph-based workflows, and Streamlit UI** to create a scalable and modular RAG architecture.

---

# 🚀 Features

- 📄 PDF Document Ingestion
- 🔗 URL-based Data Retrieval
- 🧠 Semantic Search using Vector Embeddings
- 🤖 AI-Powered Response Generation
- 🌐 Streamlit-based Interactive UI
- ⚡ Fast Retrieval Pipeline
- 🧩 Modular Project Architecture
- 🔍 Context-Aware Query Answering
- 📦 Configurable Components
- 🛠️ Extensible Graph-Based Workflow

---

# 🏗️ Project Architecture

```text
User Query
     │
     ▼
Streamlit UI
     │
     ▼
Graph Builder / Workflow Engine
     │
     ▼
Retriever
     │
     ▼
Vector Store
     │
     ▼
Relevant Context
     │
     ▼
LLM Response Generation
     │
     ▼
Final AI Response
```

---

# 📂 Project Structure

```bash
RAG data retrieval Project/
│
├── data/
│   ├── attention.pdf
│   └── url.txt
│
├── src/
│   ├── __pycache__/
│   ├── config/
│   ├── document_ingestion/
│   ├── graph_builder/
│   ├── node/
│   ├── state/
│   ├── vectorstore/
│   └── __init__.py
│
├── README.md
├── main.py
├── pyproject.toml
├── requirements.txt
├── streamlit_app.py
└── uv.lock
```

---

# 📁 Folder Explanation

## 📂 data/

Contains the raw data sources used for ingestion.

### Files:
- `attention.pdf` → PDF document used for semantic retrieval
- `url.txt` → Stores URLs for web-based ingestion

---

## 📂 src/

Main source code directory containing all core modules.

---

## 📂 config/

Contains configuration settings for:
- API keys
- Environment variables
- Model configurations
- Embedding settings

---

## 📂 document_ingestion/

Handles:
- PDF loading
- Text extraction
- Chunking
- Cleaning
- Preprocessing

Technologies commonly used:
- PyPDFLoader
- RecursiveCharacterTextSplitter
- LangChain document loaders

---

## 📂 graph_builder/

Responsible for:
- Workflow orchestration
- Building RAG execution pipelines
- Managing graph-based node execution

This layer helps in making the system modular and scalable.

---

## 📂 node/

Contains independent processing nodes such as:
- Query node
- Retrieval node
- Generation node
- Evaluation node

Each node performs a specific AI workflow task.

---

## 📂 state/

Maintains:
- Workflow state
- Shared memory
- Intermediate outputs
- Context tracking

Useful for managing multi-step AI pipelines.

---

## 📂 vectorstore/

Handles:
- Embedding generation
- Vector database storage
- Similarity search
- Semantic retrieval

Can be integrated with:
- FAISS
- ChromaDB
- Pinecone
- Weaviate

---

# ⚙️ Tech Stack

## 👨‍💻 Programming Language
- Python

---

## 🤖 AI / LLM Frameworks
- LangChain
- LangGraph
- OpenAI / LLM APIs

---

## 📚 Vector Database
- FAISS / ChromaDB

---

## 🌐 Frontend
- Streamlit

---

## 📄 Document Processing
- PyPDF
- Unstructured
- Recursive Text Splitters

---

## 🔍 Embedding Models
- OpenAI Embeddings
- HuggingFace Embeddings

---

# 🔄 Workflow Pipeline

## Step 1 — Data Ingestion
- Load PDFs and URLs
- Extract raw text

## Step 2 — Text Chunking
- Split large documents into smaller chunks
- Optimize for embedding generation

## Step 3 — Embedding Generation
- Convert text chunks into vector embeddings

## Step 4 — Store in Vector Database
- Save embeddings for semantic retrieval

## Step 5 — User Query
- User enters query through Streamlit UI

## Step 6 — Similarity Search
- Retrieve most relevant document chunks

## Step 7 — Context Augmentation
- Inject retrieved context into LLM prompt

## Step 8 — AI Response Generation
- Generate accurate context-aware answers

---

# 🖥️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/rag-data-retrieval-project.git
```

---

## 2️⃣ Move Into Project Directory

```bash
cd rag-data-retrieval-project
```

---

## 3️⃣ Create Virtual Environment

### Using UV

```bash
uv venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the root directory.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# ▶️ Running the Project

## Run Main Application

```bash
python main.py
```

---

## Run Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

# 📸 Sample Use Cases

- 📚 AI Research Assistant
- 🧾 PDF Question Answering
- 🏢 Enterprise Knowledge Base
- ⚖️ Legal Document Search
- 🧠 Academic Paper Retrieval
- 💬 Intelligent Chat with Documents
- 🔎 Semantic Search Engines

---

# 📈 Future Improvements

- Multi-document retrieval
- Hybrid search (BM25 + Vector Search)
- Conversation memory
- Multi-modal RAG
- Agentic workflows
- Real-time web retrieval
- Authentication system
- Deployment on cloud platforms

---

# 🧪 Example Query

```text
"What is the main concept explained in the Attention paper?"
```

---

# 📊 Key Concepts Used

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Chunking Strategies
- Prompt Engineering
- LLM Orchestration
- Graph-Based AI Pipelines

---

# 🛡️ Challenges Solved

- Reducing hallucinations in LLM responses
- Improving contextual accuracy
- Efficient document retrieval
- Managing scalable AI workflows
- Building modular retrieval pipelines

---

# 📌 Requirements

Example dependencies:

```txt
streamlit
langchain
langgraph
openai
faiss-cpu
pypdf
python-dotenv
tiktoken
```

---

# 🤝 Contribution

Contributions are welcome!

Steps:
1. Fork the repository
2. Create a new branch
3. Commit changes
4. Push to branch
5. Create Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Kshitij Goswami

Passionate about:
- AI Engineering
- RAG Systems
- LLM Applications
- Data Analytics
- Full Stack Development
- Cloud & AI Infrastructure

---

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub to support the project!
