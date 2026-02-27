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


# ============ PROMPT 1: Zero-shot prompting with reviews ============
prompt1 = """Classify the sentiment of each review from 1 to 5.:
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable. 
4. Can't wait to show them off!"""

response1 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt1}],
    max_completion_tokens=100
)

print("=" * 50)
print("Classify the sentiment of each review:")
print("=" * 50)
print(response1.choices[0].message.content)


# ============ PROMPT 2:One-shot prompting ============
prompt2 ="""Classify sentiment as 1-5 (negative to positive):
1. Love these! = 5
2. Unbelievably good! = 
3. Shoes fell apart on the second use. = 
4. The shoes look nice, but they aren't very comfortable. = 
5. Can't wait to show them off! =
 
 """


response2 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt2}],
    max_completion_tokens=100,
    temperature=2
)

print("\n" + "=" * 50)
print("One-shot prompting:")
print("=" * 50)
print(response2.choices[0].message.content)


# ============ PROMPT 3:Few-shot prompting ============
prompt3 ="""Classify sentiment as 1-5 (negative to positive):
1. ____
2. Love these! = 5
3. Unbelievably good! = 
4. Shoes fell apart on the second use. = 
5. The shoes look nice, but they aren't very comfortable. = 

"""


response3 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt3}],
    max_completion_tokens=100,
    temperature=2
)

print("\n" + "=" * 50)
print("Few-shot prompting:")
print("=" * 50)
print(response3.choices[0].message.content)

# ============ PROMPT 4:Few-shot2 prompting ============
prompt4 ="""Classify sentiment as 1-5 (negative to positive):
1. Comfortable, but not very pretty = 2
2. Love these! = 5
3. Unbelievably good! = 
4. Shoes fell apart on the second use. = 
5. The shoes look nice, but they aren't very comfortable. = 
6. Can't wait to show them off! = """

response4 = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt4}],
    max_completion_tokens=100,
    temperature=2
)

print("\n" + "=" * 50)
print("Few-shot2 prompting:")
print("=" * 50)
print(response4.choices[0].message.content)