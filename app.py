import streamlit as st
from modules.pdf_parser import extract_pdf_text
from modules.docx_parser import extract_docx_text

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
        st.success("Resume uploaded successfully!")

        if uploaded_resume.name.endswith(".pdf"):
            resume_text = extract_pdf_text(uploaded_resume)
        else:
            resume_text = extract_docx_text(uploaded_resume)

        st.subheader("Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )


