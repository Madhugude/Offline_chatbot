from pypdf import PdfReader

CHUNK_SIZE = 900
CHUNK_OVERLAP = 150


def read_upload(upload):
    """Extract readable text from a PDF or TXT Streamlit upload."""
    name = upload.name.lower()
    if name.endswith(".pdf"):
        reader = PdfReader(upload)
        pages = []
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            if text.strip():
                pages.append(f"[Page {page_number}]\n{text}")
        return "\n\n".join(pages)

    raw = upload.getvalue()
    return raw.decode("utf-8", errors="replace")


def split_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Split text into overlapping, human-readable chunks."""
    text = " ".join(text.split())
    if not text:
        return []

    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = max(end - overlap, start + 1)
    return chunks


def extract_and_chunk(uploads):
    all_chunks = []
    for upload in uploads:
        text = read_upload(upload)
        for chunk_number, chunk in enumerate(split_text(text), start=1):
            all_chunks.append({
                "text": chunk,
                "source": upload.name,
                "chunk": chunk_number,
            })
    return all_chunks
