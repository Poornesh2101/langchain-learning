from langchain_ollama import ChatOllama
from langchain_core.globals import set_debug
import streamlit as st

set_debug(True)

llm = ChatOllama(model="mistral")
st.title("Ask Anything")
question = st.text_input("Enter the Question")

if question:
    response = llm.invoke(question)
    st.write(response.content)