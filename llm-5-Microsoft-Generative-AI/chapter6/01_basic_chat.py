"""
LESSON 1: Basic Chat Completion
Purpose: Make your first API call to Azure OpenAI
Learn: Client setup, basic message structure, response handling
"""

from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# Step 1: Load environment variables
load_dotenv()
print("Environment variables loaded")

# Step 2: Create client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)
print("✋ Azure OpenAI client created")

# Step 3: Get deployment name
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
print(f"Using deployment: {deployment}")

# Step 4: Create a simple chat message
print("\n" + "="*50)
print("SENDING REQUEST TO AZURE OPENAI")
print("="*50)

response = client.chat.completions.create(
    model=deployment,
    messages=[
        {"role": "user", "content": "Say hello in a friendly way!"}
    ]
)

# Step 5: Extract and print response
assistant_message = response.choices[0].message.content
print(f"\n🤖 Assistant: {assistant_message}")

# Step 6: Print metadata
print("\n" + "="*50)
print("RESPONSE METADATA")
print("="*50)
print(f"Model used: {response.model}")
print(f"Tokens - Prompt: {response.usage.prompt_tokens}")
print(f"Tokens - Completion: {response.usage.completion_tokens}")
print(f"Tokens - Total: {response.usage.total_tokens}")
print(f"Finish reason: {response.choices[0].finish_reason}")