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
response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        {"role": "user", "content": "Give me a quick summary of Portugal."},
        {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)

response1 = client.chat.completions.create(
   model="gpt-4o-mini",
   # Add in the extra examples and responses
   messages=[
       {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
       {"role": "user", "content": "Give me a quick summary of Portugal."},
       {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
    {"role": "user", "content": "Give me a quick summary of Japan."},
        {"role": "assistant", "content": "Japan is an island nation in East Asia known for its advanced technology, rich culture, and capital city Tokyo."},

        {"role": "user", "content": "Give me a quick summary of Brazil."},
        {"role": "assistant", "content": "Brazil is the largest country in South America, famous for the Amazon rainforest and its capital Brasília."},

        {"role": "user", "content": "Give me a quick summary of Kenya."},
        {"role": "assistant", "content": "Kenya is an East African nation known for its diverse wildlife, Great Rift Valley, and capital Nairobi."},

       {"role": "user", "content": "Give me a quick summary of Greece."}
   ]
)

print(response1.choices[0].message.content)