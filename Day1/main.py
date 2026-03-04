from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.6)
question = input("Enter the question: ")
response = llm.invoke(question)

print(response.content)