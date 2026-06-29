import streamlit as st
from modules.pdf_parser import extract_pdf_text
from modules.docx_parser import extract_docx_text
from modules.text_preprocessor import clean_text
from modules.keyword_matcher import keywords_match

st.set_page_config(
    page_title = "AI Resume Analyzer",
    page_icon = "📄",
    layout = "wide"
)

st.title("📄 AI Resume Analyser")

st.write(
    "Upload your resume and compare it with a job description."
)

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type = ["pdf","docx"]
)

job_description = st.text_area(
    "Job Description",
    height = 250
)

if uploaded_resume is not None:
    if st.button("Analyze Resume"):
        if not job_description.strip():
            st.warning("Please enter a Job Description.")
            st.stop()

        st.success("Resume analyzed successfully!")

        if uploaded_resume.name.lower().endswith(".pdf"):
            resume_text = extract_pdf_text(uploaded_resume)
        elif uploaded_resume.name.lower().endswith(".docx"):
            resume_text = extract_docx_text(uploaded_resume)
        else:
            st.error("Unsupported file format.")
            st.stop()

        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(job_description)

        score,matched_keywords,missing_keywords = keywords_match(clean_resume,clean_jd)

        st.subheader("ATS Match Score")

        st.metric(
            label="Match Percentage",
            value=f"{score}%"
        )
        
        st.subheader("Matching Keywords")
        st.success(", ".join(matched_keywords) if matched_keywords else "No matched keywords.")

        st.subheader("Missing Keywords")
        st.warning(", ".join(missing_keywords) if missing_keywords else "No missing keywords.")


