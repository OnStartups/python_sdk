from agentdotai import AgentDotAiClient

# Replace with your actual Bearer token
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = AgentDotAiClient(bearer_token)

def summarize_youtube_tutorial(youtube_url, model="gpt4o"):
    print(f"Summarizing YouTube tutorial: {youtube_url}\n")

    # 1. Get YouTube Transcript
    print("--- Fetching YouTube transcript... ---")
    transcript_response = client.action(action_id="getYoutubeTranscript", params={"url": youtube_url})

    if transcript_response['status'] == 200:
        print("YouTube transcript fetched successfully.")
        transcript_text = transcript_response['results']
        print(f"Transcript snippet (first 200 chars): {transcript_text[:200]}...\n")

        # 2. Summarize Transcript using LLM
        print("--- Summarizing transcript using LLM... ---")
        summary_prompt = f"Summarize the following YouTube tutorial transcript in a concise and helpful way:\n\nTranscript:\n{transcript_text}\n\nSummary:"
        summary_response = client.chat(prompt=summary_prompt, model=model)

        if summary_response['status'] == 200:
            video_summary = summary_response['results']
            print("YouTube Tutorial Summary:\n", video_summary, "\n")
        else:
            print(f"Error summarizing transcript: {summary_response['error']}")
            video_summary = f"Error summarizing transcript: {summary_response['error']}"

    else:
        print(f"Error fetching YouTube transcript: {transcript_response['error']}")
        video_summary = f"Error fetching transcript: {transcript_response['error']}"

    print("--- YouTube Tutorial Summarization Complete ---")
    return {"video_summary": video_summary}


if __name__ == "__main__":
    tutorial_url = "https://www.youtube.com/watch?v=TDPqt7ONUCY" # Example YouTube tutorial URL
    llm_summary_model = "gpt4o" # LLM model for summarization

    summary_result = summarize_youtube_tutorial(tutorial_url, llm_summary_model)

    # You can provide this summary to customer service agents or users
    print("\nYouTube Summary Result:")
    print(summary_result)