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


# ============ PROMPT 1: Restaurant Slogan ============
prompt1 = """Give the eye catching slogan for a restaurant with Italian, Chinese food and fine-dining, fast-food etc"""

response1 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt1}],
    max_completion_tokens=100
)

print("=" * 50)
print("RESTAURANT SLOGAN:")
print("=" * 50)
print(response1.choices[0].message.content)


# ============ PROMPT 2: Product Description ============
prompt2 = """
I need a product description for SonicPro headphones, wireless headphone with 40 hour of battery life. Active noise cancellation (ANC), foldable design
"""

response2 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt2}],
    max_completion_tokens=100,
    temperature=2
)

print("\n" + "=" * 50)
print("PRODUCT DESCRIPTION:")
print("=" * 50)
print(response2.choices[0].message.content)