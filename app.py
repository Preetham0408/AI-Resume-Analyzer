import streamlit as st

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

if st.button("Analyze Resume"):
    st.success("Resume uploaded sucessfully!")


