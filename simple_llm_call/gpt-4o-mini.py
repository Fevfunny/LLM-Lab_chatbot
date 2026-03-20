# 4.	Use gpt-4o-mini to create 5 SQL interview questions for beginners.

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm=ChatOpenAI(model="gpt-4o-mini",
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"))

response=llm.invoke("create 5 SQL interview questions for beginners")

print(response.content)
