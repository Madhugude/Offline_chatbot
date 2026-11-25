# Offline AI Document Chatbot

A beginner-friendly local RAG chatbot. Upload PDF or TXT documents, ask questions, and receive readable answers grounded in the uploaded content.

## Technology
- Python
- Streamlit
- Ollama (local chat and embedding models)
- ChromaDB (local vector database)
- PyPDF (PDF text extraction)

## Requirements
1. Python 3.10 or newer
2. Ollama installed and running
3. Models downloaded locally:
   - `qwen2.5:3b` (chat)
   - `nomic-embed-text` (embeddings)

## Setup on Windows PowerShell

Open a terminal in this project folder.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Download models (one time; requires internet):

```powershell
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
```

Run Ollama, then launch the app:

```powershell
streamlit run app.py
```

## Use
1. Upload PDF or TXT files in the sidebar.
2. Click **Index documents**.
3. Ask a question in the chat.
4. Download the answer as Markdown or plain text.

## Human-readable project files
- `app.py`: application interface
- `src/documents.py`: reads and chunks uploaded documents
- `src/rag.py`: embeddings, retrieval, and local model response
- `src/formatting.py`: formats answers and exports them as readable files

Uploaded source documents and the local ChromaDB database are intentionally excluded from Git using `.gitignore`.

## GitHub
Create an empty repository on GitHub, then run:

```powershell
git init
git add .
git commit -m "Create offline document chatbot"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the URL with your own repository URL. Do not commit private documents, API keys, or local database files.
