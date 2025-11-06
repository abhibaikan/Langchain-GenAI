
from langchain_openai import ChatOpenAI
from templates import joke_structured_prompt
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



# Initialize the LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)

# Create the chain
chain = LLMChain(llm=llm, prompt=joke_structured_prompt)

# Run the chain with a topic
response = chain.run({"topic": "chickens"})

# Parse and print the structured JSON output
import json
try:
	joke_json = json.loads(response)
	print(joke_json)
except Exception as e:
	print("Failed to parse JSON:", response)