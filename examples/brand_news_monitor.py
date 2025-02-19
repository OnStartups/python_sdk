from agentdotai import AgentDotAiClient

# Replace with your actual Bearer token
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = AgentDotAiClient(bearer_token)

def monitor_brand_news(brand_name, date_range="7d", location="US"):
    print(f"Monitoring news for brand: {brand_name}\n")

    # 1. Get Google News
    print("--- Fetching Google News... ---")
    news_response = client.action(
        action_id="getGoogleNews",
        params={"query": brand_name, "date_range": date_range, "location": location}
    )

    if news_response['status'] == 200:
        print("Google News fetched successfully.")
        organic_results = news_response['results'].get('organic_results', [])
        if organic_results:
            print(f"Top News Articles for '{brand_name}':")
            for article in organic_results[:5]: # Display top 5 articles
                print(f"- Source: {article['source']}")
                print(f"  Title: {article['title']}")
                print(f"  Snippet: {article['snippet']}")
                print(f"  Link: {article['link']}\n")
        else:
            print(f"No news articles found for '{brand_name}' in the last {date_range}.")
            articles_summary = "No news articles found."
        articles_summary = f"Found {len(organic_results)} articles. Top articles listed in console."

    else:
        print(f"Error fetching Google News: {news_response['error']}")
        articles_summary = f"Error fetching news: {news_response['error']}"

    print("--- Brand News Monitoring Complete ---")
    return {"news_summary": articles_summary}


if __name__ == "__main__":
    brand = "agent.ai" # Brand to monitor
    news_date_range = "7d" # Monitor news from last 7 days
    news_location = "US" # Monitor news in US

    monitoring_result = monitor_brand_news(brand, news_date_range, news_location)

    # You could send this summary via email, Slack, etc.
    print("\nMonitoring Result Summary:")
    print(monitoring_result)
