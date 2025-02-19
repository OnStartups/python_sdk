from agentdotai import AgentDotAiClient

# Replace with your actual Bearer token
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = AgentDotAiClient(bearer_token)

def generate_social_content(topic, model="gpt4o", image_model="DALL-E 3"):
    print(f"Generating social media content about: {topic}\n")

    # 1. Get LLM generated text for social post
    print("--- Generating social media post text... ---")
    llm_response = client.chat(
        prompt=f"Write a short, engaging social media post about {topic}. Include relevant hashtags.",
        model=model
    )

    if llm_response['status'] == 200:
        social_post_text = llm_response['results']
        print("Social media text generated:\n", social_post_text, "\n")
    else:
        print(f"Error generating social media text: {llm_response['error']}\n")
        social_post_text = "Error generating social media post."

    # 2. Generate Image (optional, but recommended for social media)
    print("--- Generating image for social media post... ---")
    image_prompt = f"Create an image related to: {topic}, {llm_response['results'][:100]}..." # Using snippet of generated text for image prompt
    image_response = client.action(
        action_id="generateImage",
        params={"prompt": image_prompt, "model": image_model, "model_style": "digital art", "model_aspect_ratio": "1:1"}
    )

    if image_response['status'] == 200:
        image_url = image_response['results']['images'][0]['url'] if image_response['results'] and image_response['results'].get('images') else None
        if image_url:
            print(f"Image generated successfully. URL: {image_url}\n")
            image_tag = f"<img src='{image_url}' alt='Social Media Image for {topic}' width='300'>" # HTML tag for display in README
        else:
            image_tag = "Image generation failed to return URL."
            print("Image generation failed to return URL.\n")

    else:
        print(f"Error generating image: {image_response['error']}\n")
        image_tag = f"Image generation error: {image_response['error']}"

    print("--- Social Media Content Generation Complete ---")
    return {
        "social_post_text": social_post_text,
        "image_url": image_url if image_response['status'] == 200 and image_url else "N/A",
        "image_tag_for_readme": image_tag
    }


if __name__ == "__main__":
    content_topic = "The future of AI agents in marketing" # Topic for content generation
    llm_model_choice = "gpt4o" # LLM model for text
    image_gen_model = "DALL-E 3" # Image generation model

    content_result = generate_social_content(content_topic, llm_model_choice, image_gen_model)

    # Print Results - you can adapt this to post to social media platforms
    print("\nSocial Media Content Generation Result:")
    print("Social Post Text:\n", content_result['social_post_text'])
    print("Image URL:", content_result['image_url'])
    print("\nImage Tag (for README.md):\n", content_result['image_tag_for_readme'])

