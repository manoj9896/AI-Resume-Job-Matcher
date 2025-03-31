import streamlit as st
from agents.jobMatchingAgent import agent
import json

st.title("Score Calculator")

print("st.session_state. \n \n", st.session_state)


if "jobDetails" in st.session_state and "resume" in st.session_state:
    jobDetails = st.session_state["jobDetails"]
    resume = st.session_state["resume"]
    st.text_area("Job Details", value=jobDetails)
    st.text_area("Resume Details", value=resume)
    button = st.button("Calculate")
    if button:
        score = agent.invoke(
            {"resume": json.dumps(resume), "jobDescription": json.dumps(jobDetails)}
        )
        st.write(score)
        st.session_state.score = score
