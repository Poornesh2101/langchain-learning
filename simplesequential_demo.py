import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

# Setup
llm = ChatOllama(model="llama3.2")

# Prompts
title_prompt = PromptTemplate.from_template("Craft an impactful speech title for: {topic}. Return ONLY the title.")
speech_prompt = PromptTemplate.from_template("Write a 350-word speech for the title: {title}")

# Chains (Keep them pure! No Streamlit code inside the pipes)
title_chain = title_prompt | llm | StrOutputParser()
speech_chain = speech_prompt | llm | StrOutputParser()

st.title("🎤 Speech Architect Pro")
topic = st.text_input("Enter your topic")

if topic:
    # Step 1: Generate and Display Title
    with st.spinner("Brainstorming title..."):
        generated_title = title_chain.invoke({"topic": topic})
        st.header(f"Title: {generated_title}")  # UI update happens here, not in the chain

    # Step 2: Generate and Display Speech
    with st.spinner("Drafting speech..."):
        # Pass the result of Step 1 into Step 2
        final_speech = speech_chain.invoke({"title": generated_title})
        st.write(final_speech)