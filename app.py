from agent import agent_response

print("AutoStream AI Agent Started (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = agent_response(user_input)
    print("Agent:", response)