import os 
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Check if key is loaded
if not api_key:
    raise ValueError("OpenAI API key not found from env file")

# Create OpenAI client
client = OpenAI(api_key=api_key)





# Conversation history
messages = [
    {"role": "system", "content": "You are a helpful tutor that explains things clearly and concisely."}
]

# User messages
user_msgs = [
    "Introduce yourself.",
    "What is a Python list?",
    "Summarize your previous answer in two bullet points."
]

# Loop through the conversation
for q in user_msgs:
    
    print("User:", q)

    # Add user message to history
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)

    # Send request to the model
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=100
    )

    # Extract assistant reply
    assistant_reply = response.choices[0].message.content

    print("Assistant:", assistant_reply)
    print()

    # Store assistant reply in history
    assistant_dict = {"role": "assistant", "content": assistant_reply}
    messages.append(assistant_dict)