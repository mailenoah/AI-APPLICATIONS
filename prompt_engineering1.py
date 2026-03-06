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

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content


response = get_response("What is prompt engineering?")
print(response)