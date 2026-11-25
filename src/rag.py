import chromadb
import ollama

DB_PATH = "./chroma_db"
COLLECTION_NAME = "document_chunks"


def get_collection():
    client = chromadb.PersistentClient(path=DB_PATH)
    return client.get_or_create_collection(name=COLLECTION_NAME)


def create_embedding(text, embedding_model):
    # Embedding model is used only for vector creation, never for chat.
    response = ollama.embed(model=embedding_model, input=text)
    return response["embeddings"][0]


def index_chunks(chunks, embedding_model):
    collection = get_collection()

    existing = collection.get()
    if existing.get("ids"):
        collection.delete(ids=existing["ids"])

    if not chunks:
        return 0

    ids, texts, metadatas, embeddings = [], [], [], []
    for index, item in enumerate(chunks):
        ids.append(f"chunk-{index}")
        texts.append(item["text"])
        metadatas.append({
            "source": item["source"],
            "chunk": item["chunk"],
        })
        embeddings.append(create_embedding(item["text"], embedding_model))

    collection.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings,
    )
    return len(texts)


def retrieve_context(question, embedding_model, top_k=4):
    collection = get_collection()
    if collection.count() == 0:
        return "", []

    vector = create_embedding(question, embedding_model)
    results = collection.query(
        query_embeddings=[vector],
        n_results=min(top_k, collection.count()),
    )

    docs = results.get("documents", [[]])[0]
    metadata = results.get("metadatas", [[]])[0]
    context = "\n\n---\n\n".join(docs)

    sources = []
    for item in metadata:
        source = item.get("source", "Unknown file")
        if source not in sources:
            sources.append(source)
    return context, sources
