from langchain_community.chat_models import ChatOllama
import streamlit as st

llm = ChatOllama(model="mistral")

st.title("Ask Anything")

question = st.text_input("Enter the Question")

if question:
    response = llm.invoke(question)
    st.write(response.content)
