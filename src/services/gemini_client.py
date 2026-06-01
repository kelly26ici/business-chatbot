import os
import google.generativeai as genai
from dotenv import load_dotenv
from src.config.constants import GEMINI_MODEL

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(GEMINI_MODEL)


def generate_response(messages: list) -> str:
    """
    Convert OpenAI-style messages → Gemini format
    """
    # Combine messages into a single prompt (simple + stable)
    prompt = ""

    for m in messages:
        role = m["role"]
        content = m["content"]
        prompt += f"{role.upper()}: {content}\n"

    response = model.generate_content(prompt)
    return response.text