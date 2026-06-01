from src.services.chat import chat

PHONE = "+254700000000"

print("Live Chat Test")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    try:
        response = chat(PHONE, user_input)

        print("\nAI:", response)
        print()

    except Exception as e:
        print("\nERROR:", e)
        break