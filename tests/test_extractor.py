from src.services.extractor import extract_customer_info
from src.models.customer import Customer

customer = Customer(phone="+254712345678")

conversation = [
    {"role": "user", "content": "Hi my name is Kelly, I want to buy your premium plan"},
    {"role": "assistant", "content": "Hi Kelly! Our premium plan is 2000 bob per month"},
    {"role": "user", "content": "Okay I just paid 2000 bob via Mpesa"},
    {"role": "assistant", "content": "Thank you Kelly! Payment confirmed"}
]

updated_customer = extract_customer_info(conversation, customer)
print("Name:", updated_customer.name)
print("Paid:", updated_customer.paid)
print("Amount:", updated_customer.payment_amount)
print("Tags:", updated_customer.tags)