from src.services.chat import chat
from src.services.whatsapp import send_message
import traceback

async def handle_message(phone: str, user_input: str):
    try:
        print(f"[DEBUG] Message received from {phone}: {user_input}")
        
        response = chat(phone, user_input)
        print(f"[DEBUG] AI response: {response}")
        
        await send_message(phone, response)
        print("HANDLER HIT")
        print("RESPONSE:", response)
    except Exception as e:
        print(f"[ERROR] {type(e).__name__}: {e}")
        traceback.print_exc()