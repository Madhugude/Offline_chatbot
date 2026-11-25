# \# 💬 Offline AI Chatbot

# 

# An offline, GPT-style conversational AI application built using \*\*Python, Streamlit, and Ollama\*\*. The application runs a locally hosted Large Language Model (LLM), supports conversational history, and can answer questions using uploaded documents through Retrieval-Augmented Generation (RAG).

# 

# \## 🚀 Features

# 

# \### Current Features

# \- \*\*Local AI Inference:\*\* Run AI models locally using Ollama.

# \- \*\*GPT-Style Chat Interface:\*\* Interactive conversational interface built with Streamlit.

# \- \*\*Conversation History:\*\* Create multiple independent conversations and switch between them.

# \- \*\*Streaming Responses:\*\* Display AI-generated responses progressively.

# \- \*\*Markdown Formatting:\*\* Present answers in readable paragraphs, headings, lists, and code blocks.

# \- \*\*Document Upload:\*\* Upload PDF and TXT files.

# \- \*\*Document Question Answering:\*\* Retrieve relevant document content using RAG.

# \- \*\*Answer Export:\*\* Download AI responses in Markdown and plain-text formats.

# \- \*\*Privacy:\*\* Documents and AI inference remain on your local machine.

# 

# \### Planned Features

# \- Rename and delete conversations.

# \- Persistent conversation storage using SQLite.

# \- Improved document management.

# \- Multiple model selection.

# \- Enhanced GPT-style interface.

# 

# \## 🛠️ Technology Stack

# 

# | Technology | Purpose |

# |---|---|

# | Python | Core programming language |

# | Streamlit | Frontend and user interface |

# | Ollama | Local LLM inference |

# | Qwen 2.5 3B | Conversational AI model |

# | Nomic Embed Text | Text embeddings |

# | ChromaDB | Vector database |

# | PyPDF | PDF text extraction |

# | SQLite | Planned conversation persistence |

# | Git \& GitHub | Version control |

# 

# \## 📂 Project Structure

# 

# ```text

# offline-ai-chatbot/

# │

# ├── app.py

# ├── requirements.txt

# ├── README.md

# ├── .gitignore

# │

# ├── src/

# │   ├── \_\_init\_\_.py

# │   ├── ui.py

# │   ├── rag.py

# │   ├── documents.py

# │   └── formatting.py

# │

# └── chroma\_db/

# ```

# 

# \*\*File descriptions:\*\*

# 

# \- `app.py` – Main Streamlit application and chat management.

# \- `ui.py` – Custom CSS and interface styling.

# \- `rag.py` – Embedding generation, vector storage, and document retrieval.

# \- `documents.py` – PDF/TXT extraction and text chunking.

# \- `formatting.py` – Answer formatting and file exports.

# \- `requirements.txt` – Python dependencies.

# \- `README.md` – Project documentation.

# 

# \## ⚙️ Installation and Setup

# 

# \### 1. Clone the repository

# 

# ```bash

# git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

# ```

# 

# Navigate into the project:

# 

# ```bash

# cd YOUR-REPOSITORY

# ```

# 

# \### 2. Create a virtual environment

# 

# ```bash

