from agentdotai import AgentDotAiClient

# Replace with your actual Bearer token
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = AgentDotAiClient(bearer_token)

def analyze_competitor(competitor_url, linkedin_handle, twitter_handle):
    print(f"Analyzing competitor: {competitor_url}\n")

    # 1. Grab Web Text
    print("--- Grabbing website text... ---")
    web_text_response = client.action(action_id="grabWebText", params={"url": competitor_url})
    if web_text_response['status'] == 200:
        print("Website text grabbed successfully.")
        website_text = web_text_response['results'][:500] + "..." if web_text_response['results'] else "No website text."
        print(f"Website Text Snippet: {website_text}\n")
    else:
        print(f"Error grabbing website text: {web_text_response['error']}\n")
        website_text = "Error fetching website text."

    # 2. Get LinkedIn Profile
    print("--- Getting LinkedIn profile... ---")
    linkedin_response = client.action(action_id="getLinkedinProfile", params={"profile_handle": linkedin_handle})
    if linkedin_response['status'] == 200:
        print("LinkedIn profile data retrieved.")
        linkedin_profile = linkedin_response['results']['response']
        linkedin_summary = linkedin_profile.get('summary', 'No LinkedIn summary.')
        print(f"LinkedIn Summary: {linkedin_summary[:500]}...\n")
    else:
        print(f"Error getting LinkedIn profile: {linkedin_response['error']}\n")
        linkedin_summary = "Error fetching LinkedIn profile."

    # 3. Get Recent Tweets
    if twitter_handle: # Optional Twitter analysis
        print("--- Getting recent tweets... ---")
        tweets_response = client.action(action_id="getRecentTweets", params={"profile_handle": twitter_handle, "recent_tweets_count": "5"})
        if tweets_response['status'] == 200:
            print("Recent tweets retrieved.")
            tweets = tweets_response['results']
            if tweets:
                print("Recent Tweets:")
                for tweet in tweets:
                    print(f"- {tweet['text'][:100]}...")
            else:
                print("No recent tweets found.")
            print("\n")
        else:
            print(f"Error getting recent tweets: {tweets_response['error']}\n")
            tweets = "Error fetching tweets."
    else:
        tweets = "Twitter analysis skipped."
        print("Skipping Twitter analysis (no handle provided).\n")

    print("--- Competitor Analysis Complete ---")
    return {
        "website_text": website_text,
        "linkedin_summary": linkedin_summary,
        "tweets": tweets
    }

if __name__ == "__main__":
    competitor_website = "https://www.hubspot.com/" # Example Competitor
    competitor_linkedin = "company/hubspot" # Example LinkedIn handle
    competitor_twitter = "HubSpot" # Example Twitter handle (optional)

    analysis_result = analyze_competitor(competitor_website, competitor_linkedin, competitor_twitter)

    # You can further process or save the analysis_result here
    print("\nAnalysis Result:")
    print(analysis_result)
