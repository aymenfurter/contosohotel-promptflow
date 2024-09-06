
from promptflow import tool
import os
import openai
import dotenv

@tool
def my_python_tool(question: str, history: str) -> str:
    dotenv.load_dotenv()

    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT_ID")

    client = openai.AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version="2024-02-01",
    )

    message = f"Question: {question}\nChat History: {history}"

    completion = client.chat.completions.create(
        model=deployment,
        messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
        extra_body={
            "data_sources":[
                {
                    "type": "azure_search",
                    "parameters": {
                        "endpoint": os.environ["AZURE_AI_SEARCH_ENDPOINT"],
                        "index_name": os.environ["AZURE_AI_SEARCH_INDEX"],
                        "authentication": {
                            "type": "api_key",
                            "key": os.environ["AZURE_AI_SEARCH_API_KEY"],
                        }
                    }
                }
            ],
        }
    )

    return completion.choices[0].message.content