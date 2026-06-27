from docx import Document

def extract_docx_text(uploaded_file):
    try:
        doc = Document(uploaded_file)

        text = ""

        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        return text
    except:
        return "Unable to read docx file."