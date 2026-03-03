# from langchain_core.prompts import PromptTemplate
# from langchain_ollama import ChatOllama
# import streamlit as st
#
# llm = ChatOllama(model="llama3.2")
#
# prompt_template = PromptTemplate(input_variables=["country","no_of_paras","language"],
#                                  template=""""You are an expert in traditional cuisines.
# You provide information about a specific dish from a specific country
# Avoid giving information about fictional places. If the country is fictional places
# answer: I don't know. and non-existent answer: Please check the country name. Answer the question: What is the traditional
# cuisine of {country}? Answer in {no_of_paras} short paras in {language}""")
#
# st.title("Cuisines picker")
#
# country = st.text_input("Enter the Cuisine you need")
# no_of_paras = st.number_input("Enter the no of paras you need",min_value=1,max_value=10)
# language = st.selectbox("Enter the language you need",options=["English","Tamil"])
#
# chain = prompt_template | llm
#
# if country and no_of_paras and language:
#     response = chain.invoke({"country":country,
#                              "no_of_paras":no_of_paras,
#                              "language":language})
#     st.write(response.content)
