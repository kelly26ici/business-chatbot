from fastapi import FastAPI, Request, Query
from src.config.settings import WHATSAPP_VERIFY_TOKEN
from src.handlers.message_handler import handle_message
import asyncio

app = FastAPI()

# ---------------------------
# VERIFY WEBHOOK (GET)
# ---------------------------
@app.get("/webhook")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_token: str = Query(None, alias="hub.verify_token"),
    hub_challenge: str = Query(None, alias="hub.challenge")
):
    if hub_mode == "subscribe" and hub_token == WHATSAPP_VERIFY_TOKEN:
        return int(hub_challenge)

    print("WEBHOOK VERIFY FAILED")
    return {"error": "Invalid verification token"}


# ---------------------------
# RECEIVE MESSAGES (POST)
# ---------------------------
@app.post("/webhook")
async def receive_message(request: Request):
    try:
        data = await request.json()
        print("RAW WEBHOOK DATA:", data)

        entry = data.get("entry", [{}])[0]
        changes = entry.get("changes", [{}])[0]
        value = changes.get("value", {})

        messages = value.get("messages")

        if not messages:
            print("No messages in payload")
            return {"status": "no messages"}

        message = messages[0]
        phone = message.get("from")
        msg_type = message.get("type")

        print("PHONE:", phone)
        print("TYPE:", msg_type)

        if msg_type == "text":
            user_input = message["text"]["body"]
            print("USER INPUT:", user_input)

            await handle_message(phone, user_input)
        else:
            print(f"Unsupported message type: {msg_type}")

        return {"status": "ok"}

    except Exception as e:
        print("WEBHOOK ERROR:", str(e))
        return {"status": "error"}