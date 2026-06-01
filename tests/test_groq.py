from groq import Groq
from src.config.settings import GROQ_API_KEY

print("KEY FOUND:", bool(GROQ_API_KEY))

client = Groq(api_key=GROQ_API_KEY)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
)

print("\nRESPONSE:")
print(response.choices[0].message.content)