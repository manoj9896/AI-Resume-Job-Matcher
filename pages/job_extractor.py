import streamlit as st
from agents.jobAgent import agent

st.title("Job Postings")


if jobDescription := st.text_area("Enter the job description"):
    message = st.chat_message("assistant")
    jobStructuredData = agent.invoke({"jobDescription": jobDescription})
    st.session_state.jobDetails = jobStructuredData

    message.write(jobStructuredData)
    # st.chat_message("user")
    # st.write("User Message : ", user_message)
    # st.session_state.messages.append({"role": "user", "content": user_message})
