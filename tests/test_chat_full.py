from src.services.chat import chat
from dotenv import load_dotenv
load_dotenv()

phone = "+254794582488"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    chat(phone, user_input)