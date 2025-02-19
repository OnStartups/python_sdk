from agentdotai import AgentDotAiClient
import time

# Replace with your actual Bearer token
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = AgentDotAiClient(bearer_token)

def monitor_website_changes(website_url, variable_name="website_content_var", check_interval_seconds=60):
    print(f"Monitoring website for changes: {website_url}, checking every {check_interval_seconds} seconds.\n")

    try:
        while True:
            # 1. Grab Web Text
            print(f"--- Fetching website content at {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
            web_text_response = client.action(action_id="grabWebText", params={"url": website_url, "mode": "scrape"})

            if web_text_response['status'] == 200:
                current_content = web_text_response['results']

                # 2. Get Stored Variable (previous content)
                stored_content_response = client.action(
                    action_id="getVariableFromDatabase",
                    params={"variable": variable_name, "variable_retrieval_depth": "most_recent_value"}
                )

                previous_content = stored_content_response['results']

                if previous_content != current_content:
                    print("--- Website content changed! ---")
                    print("--- Storing new content to database. ---")
                    store_response = client.action(
                        action_id="storeVariableToDatabase",
                        params={"variable": variable_name, "variable": current_content}
                    )
                    if store_response['status'] == 200:
                        print("New content stored successfully.\n")
                    else:
                        print(f"Error storing new content: {store_response['error']}\n")
                    # In a real application, you might trigger a notification here (email, Slack, etc.)
                    print("--- Changes detected (snippet): ---")
                    print("--- Previous Content (snippet): ---")
                    print(previous_content[:200] + "..." if previous_content else "No previous content.")
                    print("\n--- New Content (snippet): ---")
                    print(current_content[:200] + "...") if current_content else "No current content.")

                else:
                    print("Website content unchanged.\n")

            else:
                print(f"Error fetching website content: {web_text_response['error']}\n")

            time.sleep(check_interval_seconds) # Wait before next check

    except KeyboardInterrupt:
        print("\nWebsite monitoring stopped by user.")
    except Exception as e:
        print(f"\nAn error occurred during website monitoring: {e}")


if __name__ == "__main__":
    website_to_monitor = "https://agent.ai" # Website to monitor for changes
    variable_name_to_store = "agent_ai_website_content" # Variable name in agent database
    interval = 300 # Check every 5 minutes (300 seconds)

    monitor_website_changes(website_to_monitor, variable_name_to_store, interval)
    