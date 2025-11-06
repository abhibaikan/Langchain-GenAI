from langchain.prompts import PromptTemplate

joke_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Tell me a joke about {topic}."
)

# Structured output prompt using JSON schema
joke_structured_prompt = PromptTemplate(
    input_variables=["topic"],
    template=(
        "You are a helpful assistant. Generate a joke about {topic}. "
        "Return the result as a JSON object with the following schema: "
        "{\\\"topic\\\": string, \\\"joke\\\": string, \\\"length\\\": integer}"
    )
)
