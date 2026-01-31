from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Your prompt
prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used."

# Use chat completions endpoint
response = client.chat.completions.create(
    model=deployment,
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=100
)

# Extract the completion
print(response.choices[0].message.content)