# from langchain_ollama import ChatOllama
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
# import streamlit as st
#
# title_prompt = PromptTemplate.from_template("Craft an impactful speech title for: {topic}. Return ONLY the title.")
# speech_prompt = PromptTemplate.from_template("Write a 150-word {emotion} speech for the title: {title}")
#
# st.title("Speech Generator")
#
# topic = st.text_input("Enter the topic of the Speech")
# emotion = st.selectbox("Emotion",
#                        ["Inspiring",
#                         "Passionate",
#                         "Empathetic",
#                         "Motivational",
#                         "Enthusiastic",
#                         "Hopeful"])
#
# st.write("Model Selection")
# title_model = st.selectbox("Title Model", ["llama3.2", "mistral"])
# speech_model = st.selectbox("Speech Model", ["llama3.2", "mistral"])
#
# llm1 = ChatOllama(model=title_model)
# llm2 = ChatOllama(model=speech_model)
#
# first_chain = title_prompt | llm1 | StrOutputParser()
# second_chain = speech_prompt | llm2 | StrOutputParser()
#
#
# if topic and emotion:
#     with st.spinner("llama 3.2 loaded..."):
#         generated_title = first_chain.invoke({"topic":topic,"emotion":emotion})
#         st.header(generated_title)
#
#     with st.spinner("mistral model loaded..."):
#         generated_speech = second_chain.invoke({"title":generated_title})
#         st.write(generated_speech)
