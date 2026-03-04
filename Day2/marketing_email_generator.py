from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st

# loading API KEY
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash") # setting llm model

# Prompts
product_prompt = PromptTemplate.from_template(
    """You are an experienced marketing specialist. 
    Create a catchy subject line for: {product_name}.
    Highlight these features: {features}.
    Target Audience: {target_audience}.
    Respond with ONLY the subject line text."""
)

email_prompt = PromptTemplate.from_template(
    """Write a 100-word marketing email for: {product_name}. 
    Use the subject line: {subject_line}. 
    Target audience: {target_audience}."""
)

st.title("Marketing Email Generator")

# chains
subject_line_chain = product_prompt | llm | StrOutputParser()
email_chain = email_prompt | llm | StrOutputParser()

col1,col2 = st.columns(2)

with col1:
    product_name = st.text_input("Product Name", placeholder="e.g. Solar Backpack")
    target_audience = st.text_input("Target Audience", placeholder="e.g. Digital Nomads")

with col2:
    features = st.text_area("Product Features", placeholder="e.g. Waterproof, 20W Panel", height=150)

if st.button("Generator Email"):
    if product_name and target_audience and features:
        with st.status("Generating Email...",expanded=True) as status:
            st.write(f"Loading {llm.model}....")
            subject_line = subject_line_chain.invoke({"product_name": product_name,
                                                      "features": features,
                                                      "target_audience": target_audience})
            st.write("Writing Structured Email....")
            Generated_email = email_chain.invoke({"product_name":product_name,
                                              "subject_line":subject_line,
                                              "target_audience":target_audience})

        status.update(label="Email Generated",state= "complete")

        st.divider()
        st.write(Generated_email)
    else:
        st.warning("Please Fill all the field")