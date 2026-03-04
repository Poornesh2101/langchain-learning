from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="gemma:2b")

response = llm.invoke("What 2+2")

print(response.content)