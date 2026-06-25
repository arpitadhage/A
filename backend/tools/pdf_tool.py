import fitz


def parse_pdf(state: dict):

    pdf_path = state["file_path"]

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    state["contents"]["pdf"].append(
    {
        "text": text,
        "pages": len(doc)
    }
)
    

    return state

