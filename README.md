# agent.ai Python Library

[![PyPI version](https://badge.fury.io/py/agentai.svg)](https://badge.fury.io/py/agentai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple and modern Python library for interacting with the [Agent.ai Actions API](https://agent.ai/actions).

## Installation

```bash
pip install agent-dot-ai 
```

## Example Usage

Before you can start using the library, you'll need to sign up for an account at [Agent.ai](https://agent.ai) and obtain a Bearer token from [https://agent.ai/user/settings#credits](https://agent.ai/user/settings#credits).

Here's an example of using the library to run an action that will fetch web text:

```python
from agentai import AgentAiClient

# Replace with your actual Bearer token
bearer_token = "YOUR_BEARER_TOKEN_HERE"
client = AgentAiClient(bearer_token)

# Example: Grab web text
web_text_response = client.action(
    action_id="grabWebText",
    params={"url": "https://agent.ai"}
)

if web_text_response['status'] == 200:
    print("Web Text Response Status:", web_text_response['status'])
    print("First 100 chars of Response:", web_text_response['results'][:100] + "...")
else:
    print(f"Error: Status Code: {web_text_response['status']}, Message: {web_text_response['error']}")
```

Here's an example of using the library to ask an LLM a question:

```python
chat_response = client.chat(prompt="What is an AI agent?", model="gpt4o")
if chat_response['status'] == 200:
    print("\nChat Response (first 100 chars):", chat_response['results'][:100] + "...")
else:
    print(f"Error: Status Code: {chat_response['status']}, Message: {chat_response['error']}")
```

Here's an example of using the library to grab Google News articles for a topic in a location and with a lookback period:

```python
google_news_response = client.action(
    action_id="getGoogleNews",
    params={"query": "AI advancements", "date_range": "7d", "location": "Boston"}
)
if google_news_response['status'] == 200:
    print("\nGoogle News Location:", google_news_response['metadata']['search_information']['location_used'])
else:
    print(f"Error: Status Code: {google_news_response['status']}, Message: {google_news_response['error']}")
```

For more examples, see the examples/ directory.

## Error Handling

The library's action() and chat() methods return dictionaries with the following keys:

- status: HTTP status code of the API response.
- error: Error message string (if an error occurred, otherwise None).
- results: The API response data (if successful, otherwise None).
- metadata: Metadata from the API response (if available, otherwise None).

Check the status code to determine if the API call was successful. If not, examine the error message.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for feature requests or bug reports.

## License

This project is licensed under the MIT License.
