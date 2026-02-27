import os 
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Open api key not found from env file")GI

def get_response(prompt):
    client = OpenAI(api_key = api_key )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_completion_tokens=100,
        messages=[{"role": "user","content":prompt}],
    )        
   

    return response.choices[0].message.content
response = get_response("Explain about different role, user, system and, use bullet point for your response?")
print(response)