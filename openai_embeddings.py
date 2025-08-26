from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

OPENAI_API_KEY = os.getenv("OPENAPI_API_KEY")

embeddings=OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=OPENAI_API_KEY)

result = embeddings.embed_query("What is the capital of India?")
print(result)