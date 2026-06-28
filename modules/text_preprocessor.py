import re

def clean_text(text) :
    """
    Clean extracted text from resume and job discription
    """

    if not text:
        return ""

    text = text.lower();

    text = re.sub(r"\s+"," ",text)

    text = text.strip()

    return text

