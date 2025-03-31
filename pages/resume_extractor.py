import streamlit as st
from pypdf import PdfReader
from agents.resumeAgent import agent
from langchain_core.output_parsers.json import JsonOutputParser

st.title("Resume Parsing")

if "messages" not in st.session_state:
    st.session_state.messages = []
else:
    for messsage in st.session_state.messages:
        message = st.chat_message("user")
        message.markdown(messsage["content"])

print(st.session_state)

if user_message := st.chat_input():
    message = st.chat_message("assistant")
    message.write(user_message)
    # st.chat_message("user")
    # st.write("User Message : ", user_message)
    st.session_state.messages.append({"role": "user", "content": user_message})

resumeFile = st.file_uploader("Upload Your Resume", type=".pdf")
if resumeFile:
    print(resumeFile.name)
    pdfReader = PdfReader(resumeFile)
    resumeText = ""

    for page in pdfReader.pages:
        resumeText = resumeText + " " + page.extract_text()

    print(resumeText)
    message = agent.invoke({"resume": resumeText})
    st.write(message)
    st.session_state.resume = message
