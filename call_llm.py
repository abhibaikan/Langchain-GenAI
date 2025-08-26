from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Add your OpenAI API key here
OPENAI_API_KEY = os.getenv("OPENAPI_API_KEY")

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)

result = model.invoke("What is the capital of India?")
print(result)