# Changelog

All notable changes to the `AgentDotAi` Python library will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-02-18

### Added

- Initial release of the `AgentAi` Python library.
- Provides a client (`AgentDotAiClient`) for interacting with the Agent.ai Actions API.
- Includes a generic `action()` method to call any API action by its `action_id`.
- Implements a convenient `chat()` method for using the `invokeLlm` action.
- Consistent response structure for all API calls, returning a dictionary with `status`, `error`, `results`, and `metadata` keys.
- Basic error handling integrated within the client.
- Includes example scripts in the `examples/` directory demonstrating various use cases.

### Supported API Actions (v0.1.0):

**Get Data Actions:**

- `grabWebText`: Extract text content from a web page.
- `grabWebScreenshot`: Capture a screenshot of a web page.
- `getYoutubeTranscript`: Fetch transcript from a YouTube video.
- `getYoutubeChannel`: Retrieve YouTube channel data.
- `getTwitterUsers`: Search and retrieve Twitter user profiles.
- `getGoogleNews`: Fetch news articles from Google News.
- `runYoutubeSearch`: Perform a YouTube search.
- `getSearchResults`: Fetch search results from Google or YouTube.
- `getRecentTweets`: Get recent tweets from a Twitter handle.
- `getLinkedinProfile`: Retrieve LinkedIn profile data.
- `getLinkedinActivity`: Get recent LinkedIn activity from profiles.
- `getCompanyObject`: Enrich company data using Breeze Intelligence.
- `getBlueskyPosts`: Fetch recent Bluesky posts from a user handle.
- `searchBlueskyPosts`: Search for Bluesky posts by keywords.
- `getInstagramProfile`: Retrieve Instagram profile data.
- `getInstagramFollowers`: Get Instagram followers data.

**Use AI Actions:**

- `outputAudio`: Convert text to speech.
- `invokeLlm`: Use a Language Model (LLM) to generate text.
- `generateImage`: Generate an image using AI models.

**Advanced Actions:**

- `invokeAgent`: Invoke another Agent.
- `restCall`: Make a REST API call.
- `convertFile`: Convert a file to a different format.
- `convertFileOptions`: Get file conversion options.
- `storeVariableToDatabase`: Store a variable in the agent's database.
- `getVariableFromDatabase`: Retrieve a variable from the agent's database.

---

**Note:** Date format is YYYY-MM-DD.