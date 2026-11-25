def answer_to_markdown(answer):
    """Return a Markdown document with a title and readable answer text."""
    return "# Document Chatbot Answer\n\n" + answer.strip() + "\n"


def answer_to_text(answer):
    """Return a plain UTF-8 text export."""
    return "DOCUMENT CHATBOT ANSWER\n" + "=" * 24 + "\n\n" + answer.strip() + "\n"
