from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Initialize Parser and Instructions
parser = JsonOutputParser()
format_instructions = parser.get_format_instructions()

llm = ChatOpenAI(model="gpt-4o")

# Product Prompt
product_prompt = PromptTemplate.from_template(
    """You are an experienced marketing specialist. 
    Create a catchy subject line for: {product_name}.
    Highlight these features: {features}.
    Target Audience: {target_audience}.
    Respond with ONLY the subject line text."""
)

# Email Prompt
email_prompt = PromptTemplate(
    template="""Write a 100-word marketing email for: {product_name}. 
    Use the subject line: {subject_line}. 
    Target audience: {target_audience}.

    {format_instructions}
    Ensure you return exactly three keys: 'subject', 'audience', and 'email'.""",
    input_variables=["product_name", "subject_line", "target_audience"],
    partial_variables={"format_instructions": format_instructions}
)

# 4. Chains
subject_chain = product_prompt | llm | StrOutputParser()
email_chain = email_prompt | llm | parser

# 5. UI
st.title("Marketing Email Generator")

col1, col2 = st.columns(2)
with col1:
    product_name = st.text_input("Product Name", placeholder="e.g. Solar Backpack")
    target_audience = st.text_input("Target Audience", placeholder="e.g. Digital Nomads")
with col2:
    product_features = st.text_area("Product Features", placeholder="e.g. Waterproof, 20W Panel")

if st.button("Generate Email"):
    if product_name and product_features and target_audience:
        with st.status("Crafting your campaign...", expanded = False) as status:
            # Step 1: Subject Line
            st.write("Generating Subject Line...")
            subject_line = subject_chain.invoke({
                "product_name": product_name,
                "features": product_features,
                "target_audience": target_audience
            })

            # Step 2: Full Email JSON
            st.write("Writing Structured Email...")
            generated_data = email_chain.invoke({
                "product_name": product_name,
                "subject_line": subject_line,
                "target_audience": target_audience
            })
            status.update(label="Campaign Ready!", state="complete")

        # 6. Displaying the Structured Results safely
        st.divider()
        st.subheader(f"Subject: {generated_data.get('subject', subject_line)}")
        st.caption(f"Targeting: {generated_data.get('audience', target_audience)}")
        st.markdown(generated_data.get('email', "Email content missing."))
    else:
        st.warning("Please fill in all fields!")