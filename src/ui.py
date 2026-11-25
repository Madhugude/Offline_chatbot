
import streamlit as st


def apply_custom_css():
    st.markdown(
        """
        <style>

        /* Main application background */
        .stApp {
            background-color: #212121;
            color: #FFFFFF;
        }

        /* Main content area */
        .main .block-container {
            max-width: 1000px;
            padding-top: 2rem;
            padding-bottom: 5rem;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #171717;
            border-right: 1px solid #333333;
        }

        /* Sidebar text */
        [data-testid="stSidebar"] p {
            color: #E5E5E5;
        }

        /* Chat messages */
        [data-testid="stChatMessage"] {
            background-color: #2A2A2A;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 12px;
        }

        /* Chat input */
        [data-testid="stChatInput"] {
            background-color: #303030;
            border-radius: 15px;
        }

        [data-testid="stChatInput"] textarea {
            color: white;
        }

        /* Buttons */
        .stButton button {
            border-radius: 10px;
            border: 1px solid #444444;
            background-color: #303030;
            color: white;
        }

        .stButton button:hover {
            border-color: #888888;
            color: white;
        }

        /* Headings */
        h1, h2, h3 {
            color: #FFFFFF;
        }

        /* Code blocks */
        [data-testid="stCode"] {
            border-radius: 10px;
        }

        /* Download buttons */
        .stDownloadButton button {
            border-radius: 10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
