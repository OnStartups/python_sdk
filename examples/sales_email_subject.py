from agentdotai import AgentDotAiClient

# Replace with your actual Bearer token
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = AgentDotAiClient(bearer_token)

def generate_email_subjects(product_name, target_audience, num_subjects=3):
    print(f"Generating sales email subject lines for product: {product_name} targeting: {target_audience}\n")

    # 1. Generate Email Subject Lines using LLM
    print("--- Generating email subject lines... ---")
    llm_response = client.chat(
        prompt=f"Generate {num_subjects} highly engaging and personalized email subject lines for a sales email promoting {product_name} to {target_audience}. Make them concise and attention-grabbing.",
        model="gpt4o"
    )

    if llm_response['status'] == 200:
        subject_lines = llm_response['results'].strip().split('\n') # Split into lines if LLM returns multiple subjects
        print("Generated Email Subject Lines:")
        for i, subject in enumerate(subject_lines[:num_subjects]): # Limit to requested number
            print(f"{i+1}. {subject.strip()}") # Strip whitespace for cleaner output
        subject_lines_output = "\n".join([f"- {line.strip()}" for line in subject_lines[:num_subjects]]) # For README formatting

    else:
        print(f"Error generating email subject lines: {llm_response['error']}")
        subject_lines_output = f"Error: {llm_response['error']}"


    print("--- Email Subject Line Generation Complete ---")
    return {"subject_lines": subject_lines_output}


if __name__ == "__main__":
    product = "agent.ai Platform" # Example product
    audience = "Marketing and Sales Professionals" # Example target audience
    number_of_subjects = 10 # Number of subject lines to generate

    subjects_result = generate_email_subjects(product, audience, number_of_subjects)

    # You could use these subject lines in your sales outreach campaigns
    print("\nEmail Subject Line Generation Result:")
    print(subjects_result['subject_lines'])
