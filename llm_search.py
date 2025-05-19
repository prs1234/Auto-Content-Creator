import os
from langchain_community.llms import OpenAI

def query_openai_api(prompt):
    llm = OpenAI(
        temperature=0.7,
        model_name="gpt-3.5-turbo-instruct",  # or text-davinci-003
        openai_api_key=""         # Optional if already set in ENV
    )
    response = llm.predict(prompt)
    return response

