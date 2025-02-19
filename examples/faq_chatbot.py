from agentdotai import AgentDotAiClient

# Replace with your actual Bearer token
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = AgentDotAiClient(bearer_token)

def faq_chatbot(website_url):
    print(f"Creating FAQ chatbot for website: {website_url}\n")

    # 1. Grab Web Text (crawl mode to get more content, assuming FAQ might be spread across pages)
    print("--- Crawling website for FAQ content... ---")
    web_text_response = client.action(action_id="grabWebText", params={"url": website_url, "mode": "scrape"})

    if web_text_response['status'] == 200:
        print("Website text crawled successfully.")
        website_content = web_text_response['results']
        # Basic FAQ extraction - in a real scenario, you'd use more sophisticated parsing
        faq_content = website_content # For simplicity, using all crawled content as context
        print(f"FAQ content snippet (first 200 chars): {faq_content[:200]}...\n")

        # 2. Interactive Chat with FAQ context
        print("--- Starting interactive FAQ chatbot. Type 'exit' to quit. ---")
        while True:
            user_question = input("You: ")
            if user_question.lower() == 'exit':
                break

            # Use chat function with FAQ context in the prompt
            chatbot_prompt = f"Answer the following question based on the FAQ content provided below:\n\nFAQ Content:\n{faq_content}\n\nQuestion:\n{user_question}\n\nAnswer:"
            chat_response = client.chat(prompt=chatbot_prompt, model="gpt4o")

            if chat_response['status'] == 200:
                chatbot_answer = chat_response['results']
                print(f"Chatbot: {chatbot_answer}\n")
            else:
                print(f"Chatbot Error: {chat_response['error']}\n")

    else:
        print(f"Error crawling website: {web_text_response['error']}")

    print("--- FAQ Chatbot Session Ended ---")


if __name__ == "__main__":
    target_website = "https://www.agent.ai" # Replace with a website that has FAQ content

    faq_chatbot(target_website)
