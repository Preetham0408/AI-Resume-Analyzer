import re

def extract_keywords(text):
    """
    Extract unique keywords from text.
    """

    words = re.findall(r"[a-zA-Z][a-zA-Z+#.]*",text.lower())

    stop_words = {
        "the","is","are","and","or","to","of","in","for",
        "with","on","at","a","an","by","be","this",
        "that","it","from","will","can","have","has"
    }

    special_keywords = {"c", "c#", "r", "go", "js", "py"}
    keywords = set()

    for word in words:
        if (len(word) > 2 or word in special_keywords) and word not in stop_words:
            keywords.add(word)

    return keywords

def keywords_match(resume_text,jd_text):

    resume_keywords = extract_keywords(resume_text)

    jd_keywords = extract_keywords(jd_text)

    matched = sorted(resume_keywords & jd_keywords)

    missing = sorted(jd_keywords - resume_keywords)

    if len(jd_keywords) == 0 :
        score = 0
    else :
        score = round(len(matched)/len(jd_keywords)*100,2)

# this returns a tuple type
    return score,matched,missing