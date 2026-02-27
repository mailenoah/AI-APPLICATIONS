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


prompt = "Calculate the cost"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=100
)

input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens  

# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)
print(f"Input tokens: {input_tokens}")
print(f"Output tokens: {output_tokens}")
print(f"Estimated cost: ${cost:.6f}")