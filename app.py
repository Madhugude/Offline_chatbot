
import streamlit as st
import ollama
import uuid

from src.documents import extract_and_chunk
from src.rag import index_chunks, retrieve_context
from src.formatting import answer_to_markdown, answer_to_text
from src.ui import apply_custom_css


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Local GPT",
    page_icon="💬",
    layout="wide"
)

apply_custom_css()


# ==========================================
# 2. SESSION STATE INITIALIZATION
# ==========================================

# Store all conversations
if "chats" not in st.session_state:
    st.session_state.chats = {}

# Track currently selected conversation
if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

# Track document indexing status
if "indexed" not in st.session_state:
    st.session_state.indexed = False


# ==========================================
# 3. CREATE NEW CHAT FUNCTION
# ==========================================

def create_new_chat():

    chat_id = str(uuid.uuid4())

    st.session_state.chats[chat_id] = {
        "title": "New Chat",
        "messages": []
    }

    st.session_state.current_chat = chat_id


# Create initial conversation
if st.session_state.current_chat is None:
    create_new_chat()


# ==========================================
# 4. SIDEBAR
# ==========================================

with st.sidebar:

    st.title("💬 Local GPT")

    st.caption("Your personal offline AI assistant")

    # New Chat button
    if st.button(
        "＋ New Chat",
        use_container_width=True
    ):
        create_new_chat()
        st.rerun()

    st.divider()

    # Conversation history
    st.subheader("Recent Chats")

    for chat_id, chat in reversed(
        list(st.session_state.chats.items())
    ):

        if st.button(
            chat["title"],
            key=f"chat_{chat_id}",
            use_container_width=True
        ):

            st.session_state.current_chat = chat_id
            st.rerun()

    st.divider()

    # Model settings
    st.subheader("⚙️ Model Settings")

    chat_model = st.text_input(
        "Chat Model",
        value="qwen2.5:3b"
    )

    embedding_model = st.text_input(
        "Embedding Model",
        value="nomic-embed-text"
    )

    st.divider()

    # Document upload
    st.subheader("📁 Knowledge Files")

    uploaded_files = st.file_uploader(
        "Upload PDF or TXT files",
        type=["pdf", "txt"],
        accept_multiple_files=True
    )

    if st.button(
        "Index Documents",
        type="primary",
        use_container_width=True,
        disabled=not uploaded_files
    ):

        try:

            with st.spinner("Processing documents..."):

                chunks = extract_and_chunk(uploaded_files)

                count = index_chunks(
                    chunks,
                    embedding_model
                )

            st.session_state.indexed = count > 0

            st.success(
                f"Successfully indexed {count} text chunks!"
            )

        except Exception as error:

            st.error(
                f"Document indexing failed: {error}"
            )

    if st.session_state.indexed:
        st.success("Document knowledge is ready")

    else:
        st.info("General chat is available without documents")


# ==========================================
# 5. GET CURRENT CONVERSATION
# ==========================================

current_chat = st.session_state.current_chat

current_messages = st.session_state.chats[
    current_chat
]["messages"]


# ==========================================
# 6. MAIN CHAT INTERFACE
# ==========================================

st.title("Local GPT")

st.caption(
    "Ask anything. Your AI assistant runs locally using Ollama."
)


# Display previous messages
if current_messages:

    for message in current_messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

else:

    st.markdown(
        """
        ### What can I help you with today?

        - 💡 Explain complex concepts
        - 💻 Generate and explain code
        - 📚 Ask questions about your documents
        - 🧠 Learn Artificial Intelligence and Machine Learning
        """
    )


# ==========================================
# 7. USER INPUT
# ==========================================

prompt = st.chat_input(
    "Message Local GPT..."
)


if prompt:

    # Add user message
    current_messages.append({
        "role": "user",
        "content": prompt
    })

    # Automatically generate chat title
    if len(current_messages) == 1:

        title = prompt.strip().replace("\n", " ")

        if len(title) > 35:
            title = title[:35] + "..."

        st.session_state.chats[
            current_chat
        ]["title"] = title

    # Display user message
    with st.chat_message("user"):

        st.markdown(prompt)


    # ======================================
    # 8. GENERATE AI RESPONSE
    # ======================================

    with st.chat_message("assistant"):

        try:

            # Retrieve relevant document context
            context = ""
            sources = []

            if st.session_state.indexed:

                context, sources = retrieve_context(
                    prompt,
                    embedding_model
                )

            # System instructions
            system_message = """
            You are a helpful AI assistant.

            Your task is to provide accurate,
            clear and human-readable answers.

            Follow these rules:

            1. Use simple language when appropriate.
            2. Use headings for long answers.
            3. Use bullet points for lists.
            4. Use Markdown formatting.
            5. Format programming code correctly.
            6. Give examples when useful.
            7. Do not invent information.
            """

            # Add document context when available
            if context:

                system_message += f"""

                The following information was retrieved
                from the user's uploaded documents.

                Use it when relevant to the question.

                If the documents do not contain enough
                information, clearly explain that.

                Document context:

                {context}
                """

            # Keep recent conversation context
            history = current_messages[-12:]

            request_messages = [
                {
                    "role": "system",
                    "content": system_message
                }
            ] + history

            # Stream response from Ollama
            with st.spinner("Thinking..."):

                def generate_response():

                    stream = ollama.chat(
                        model=chat_model,
                        messages=request_messages,
                        stream=True,
                        options={
                            "temperature": 0.4
                        }
                    )

                    for part in stream:

                        content = part.get(
                            "message", {}
                        ).get("content", "")

                        if content:
                            yield content

                answer = st.write_stream(
                    generate_response()
                )

            # Display document sources
            if sources:

                st.markdown("**Sources**")

                for source in sources:
                    st.markdown(f"- `{source}`")

                answer += "\n\n**Sources**\n"

                for source in sources:
                    answer += f"- {source}\n"

            # Save assistant response
            current_messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as error:

            error_message = (
                f"Could not generate a response.\n\n"
                f"Error: `{error}`\n\n"
                f"Check that Ollama is running and that "
                f"the model `{chat_model}` is installed."
            )

            st.error(error_message)

            # Save error in conversation
            current_messages.append({
                "role": "assistant",
                "content": error_message
            })


# ==========================================
# 9. EXPORT LATEST ANSWER
# ==========================================

latest_answer = next(
    (
        message["content"]
        for message in reversed(current_messages)
        if message["role"] == "assistant"
    ),
    ""
)

if latest_answer:

    st.divider()

    st.subheader("📥 Export Answer")

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            "Download Markdown",
            data=answer_to_markdown(latest_answer),
            file_name="answer.md",
            mime="text/markdown"
        )

    with col2:

        st.download_button(
            "Download Text",
            data=answer_to_text(latest_answer),
            file_name="answer.txt",
            mime="text/plain"
        )
