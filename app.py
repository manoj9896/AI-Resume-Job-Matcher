import streamlit as st

st.header("AI Resume & Job Matcher")

print("check ", st.session_state)
# page definition
resume_extractor_page = st.Page(
    "./pages/resume_extractor.py", title="Resume Parsing", icon="📄"
)
job_extractor_page = st.Page(
    "./pages/job_extractor.py", title="Job Postings", icon="🔗"
)

score_page = st.Page("./pages/score_calculator.py", title="Score Calculator", icon="💯")

# Create navigation
pg = st.navigation([resume_extractor_page, job_extractor_page, score_page])
pg.run()
