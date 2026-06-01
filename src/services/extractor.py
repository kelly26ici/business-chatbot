from groq import Groq
from src.config.settings import GROQ_API_KEY
from src.models.customer import Customer
import json

client = Groq(api_key=GROQ_API_KEY)

def extract_customer_info(conversation: list, customer: Customer) -> Customer:
    # Build a summary of conversation for extraction
    convo_text = "\n".join([f"{m['role']}: {m['content']}" for m in conversation])
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are a data extractor. Extract customer info from the conversation.
Return ONLY a JSON object with these fields (only include fields you found, leave others out):
{
    "name": "customer name if mentioned",
    "email": "email if mentioned",
    "paid": true/false if payment was mentioned,
    "payment_amount": amount as number if mentioned,
    "payment_date": "date if mentioned",
    "preferences": ["list", "of", "interests"],
    "tags": ["list", "of", "relevant", "tags"]
}
Return ONLY the JSON, no explanation, no markdown."""
            },
            {
                "role": "user",
                "content": f"Extract info from this conversation:\n{convo_text}"
            }
        ]
    )
    
    try:
        extracted = json.loads(response.choices[0].message.content)
        
        # Update customer with extracted info
        if "name" in extracted and extracted["name"]:
            customer.name = extracted["name"]
        if "email" in extracted and extracted["email"]:
            customer.email = extracted["email"]
        if "paid" in extracted:
            customer.paid = extracted["paid"]
        if "payment_amount" in extracted:
            customer.payment_amount = extracted["payment_amount"]
        if "payment_date" in extracted:
            customer.payment_date = extracted["payment_date"]
        if "preferences" in extracted:
            customer.preferences = extracted["preferences"]
        if "tags" in extracted:
            customer.tags = extracted["tags"]
            
    except json.JSONDecodeError:
        pass  # If extraction fails, keep existing customer data
    
    return customer