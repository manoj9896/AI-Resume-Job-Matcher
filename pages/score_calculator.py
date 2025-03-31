import streamlit as st

st.title("Score Calculator")

print("st.session_state. \n \n", st.session_state)


if "jobDetails" in st.session_state and "resume" in st.session_state:
    st.text_area("Job Details", value=st.session_state["resume"])
    st.text_area("Resume Details", value=st.session_state["resume"])
