from src.config.constants import SYSTEM_PROMPT, AI_PROVIDER, GROQ_DEFAULT
from src.database.customer_repo import (
    get_customer,
    update_customer,
    save_message,
    get_conversation_history
)
from src.services.extractor import extract_customer_info

from src.services.groq_client import generate_response as groq_response

print("CHAT MODULE LOADED")


def call_groq(messages: list) -> str:
    return groq_response(messages)


def chat(phone: str, user_input: str) -> str:
    customer = get_customer(phone)
    history = get_conversation_history(phone)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    if customer.name:
        messages[0]["content"] += f"\nYou are talking to {customer.name}."

    messages += history
    messages.append({"role": "user", "content": user_input})

    save_message(phone, "user", user_input)

    if AI_PROVIDER == "groq":
        assistant_message = call_groq(messages)
    else:
        raise ValueError("AI_PROVIDER must be 'groq'")

    save_message(phone, "assistant", assistant_message)

    updated_history = history + [
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": assistant_message}
    ]

    updated_customer = extract_customer_info(updated_history, customer)
    update_customer(updated_customer)

    return assistant_message