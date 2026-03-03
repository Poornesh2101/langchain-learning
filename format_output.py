from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
parser = JsonOutputParser()
format_instructions = parser.get_format_instructions()

title_prompt = PromptTemplate.from_template("Craft an impactful speech title for: {topic}. Return ONLY the title.")
speech_prompt = PromptTemplate(
    template="""Write a 150-word {emotion} speech for the title: {title}.

    You must return a JSON object with exactly these three keys:
    1. "title": The title provided.
    2. "emotion": The emotion used.
    3. "speech": The generated speech text.

    {format_instructions}""",
    input_variables=["title", "emotion"],
    partial_variables={"format_instructions": format_instructions}
)

st.title("Speech Generator")

topic = st.text_input("Enter the topic of the Speech")
emotion = st.selectbox("Emotion",
                       ["Inspiring",
                        "Passionate",
                        "Empathetic",
                        "Motivational",
                        "Enthusiastic",
                        "Hopeful"])

st.write("Model Selection")
title_model = st.selectbox("Title Model", ["llama3.2", "gpt-4o-mini"])
speech_model = st.selectbox("Speech Model", ["llama3.2", "gpt-4o-mini"])

llm1 = ChatOllama(model=title_model)
llm2 = ChatOpenAI(model=speech_model)

first_chain = title_prompt | llm1 | StrOutputParser()
second_chain = speech_prompt | llm2 | parser


if topic and emotion:
    with st.spinner(f"Brainstorming with {title_model}"):
        generated_title = first_chain.invoke({"topic":topic})
        st.header(generated_title)

    with st.spinner(f"Brainstorming with {speech_model}"):
        generated_speech = second_chain.invoke({"title": generated_title,"emotion":emotion})
        st.write(generated_speech['title'])
        st.write(generated_speech['emotion'])
        st.write(generated_speech['speech'])