from src.database.customer_repo import get_customer, update_customer, save_message, get_conversation_history

# Test create new customer
customer = get_customer("+254712345678")
print("Customer:", customer)

# Test save message
save_message("+254712345678", "user", "Hello, I want to buy something")
save_message("+254712345678", "assistant", "Sure! What are you looking for?")

# Test get history
history = get_conversation_history("+254712345678")
print("History:", history)