
# Task 5: Rule-Based AI Chatbot

print("Welcome to Simple AI Chatbot!")
print("Type 'bye' to exit the chatbot.")

while True:
    user = input("\nYou: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Welcome.")

    elif user == "how are you":
        print("Bot: I'm fine. Thank you!")

    elif user == "what is your name":
        print("Bot: I am a Simple AI Chatbot.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
