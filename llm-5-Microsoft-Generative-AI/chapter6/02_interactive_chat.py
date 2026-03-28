"""
LESSON 2: Interactive Chat
Purpose: Chat continuously with Azure OpenAI until you choose to quit
Learn: Client setup, message history, multi-turn conversation
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
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)
print("Azure OpenAI client created")

# Step 3: Get deployment name
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
print(f"Using deployment: {deployment}")

# Step 4: Interactive chat loop
print("\n" + "=" * 50)
print("INTERACTIVE CHAT WITH AZURE OPENAI")
print("=" * 50)
print("Type your message and press Enter.")
print("Type 'quit' or 'exit' to end the chat.")

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() in {"quit", "exit"}:
        print("\nChat ended.")
        break

    if not user_input:
        print("Please type a message.")
        continue

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
    )

    assistant_message = response.choices[0].message.content
    print(f"\nAssistant: {assistant_message}")

    messages.append({"role": "assistant", "content": assistant_message})

    print("\n" + "-" * 50)
    print("RESPONSE METADATA")
    print("-" * 50)
    print(f"Model used: {response.model}")
    print(f"Tokens - Prompt: {response.usage.prompt_tokens}")
    print(f"Tokens - Completion: {response.usage.completion_tokens}")
    print(f"Tokens - Total: {response.usage.total_tokens}")
    print(f"Finish reason: {response.choices[0].finish_reason}")
