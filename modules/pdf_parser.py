import fitz

def extract_pdf_text(uploaded_file):
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        text = ""

        for page in doc:
            text += page.get_text()

        doc.close()

        return text
    except:
        return "Unable to  read PDF file."