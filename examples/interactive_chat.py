from agentdotai import AgentDotAiClient

# Replace with your actual Bearer token
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = AgentDotAiClient(bearer_token)

def interactive_chat_shell(model="gpt4o"):
    print("Starting interactive chat shell. Type 'exit' to quit.\n")

    try:
        while True:
            user_prompt = input("You: ")
            if user_prompt.lower() == 'exit':
                break

            chat_response = client.chat(prompt=user_prompt, model=model)

            if chat_response['status'] == 200:
                chatbot_response = chat_response['results']
                print(f"Agent: {chatbot_response}\n")
            else:
                print(f"Agent Error: {chat_response['error']}\n")

    except KeyboardInterrupt:
        print("\nChat session ended by user.")
    except Exception as e:
        print(f"\nAn error occurred during chat: {e}")


if __name__ == "__main__":
    chat_model_choice = "gpt4o" # LLM model for chat (you can change this)

    interactive_chat_shell(chat_model_choice)
