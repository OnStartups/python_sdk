# Examples Agents using agent.ai Actions

This directory contains example Python scripts demonstrating how to use the `agent.ai` library to perform various tasks by combining different API actions.

**Before Running Examples:**

1.  **Install `requests`:** Make sure you have the `requests` library installed: `pip install requests`
2.  **Set Bearer Token:**  In each example script, replace `"YOUR_BEARER_TOKEN_HERE"` with your actual Bearer token from your [Agent.ai account settings](https://agent.ai/user/settings#credits).
3.  **Run Examples:** Navigate to the `examples/` directory in your terminal and run each script using `python example_script_name.py`.

---

## Example Scripts:

1.  **`competitor_analysis.py`**:
    *   **Description:** Analyzes a competitor by grabbing text from their website, retrieving their LinkedIn profile summary, and fetching recent tweets (optional).
    *   **Actions Used:** `grabWebText`, `getLinkedinProfile`, `getRecentTweets`
    *   **Use Case:** Marketing and competitive intelligence to understand a competitor's online presence and messaging.
    *   **To Run:** `python competitor_analysis.py`

2.  **`brand_news_monitor.py`**:
    *   **Description:** Monitors Google News for mentions of a specific brand over a defined date range and location.
    *   **Actions Used:** `getGoogleNews`
    *   **Use Case:** Brand monitoring, reputation management, staying updated on industry news related to your brand.
    *   **To Run:** `python brand_news_monitor.py`

3.  **`social_media_content.py`**:
    *   **Description:** Generates social media post text and an accompanying image for a given topic using LLM and image generation actions.
    *   **Actions Used:** `chat` (`invokeLlm` under the hood), `generateImage`
    *   **Use Case:** Social media marketing, content creation, generating engaging posts quickly.
    *   **To Run:** `python social_media_content.py`

4.  **`lead_enrichment.py`**:
    *   **Description:** Enriches lead data by fetching company information from Breeze Intelligence (using `getCompanyObject`) and optionally retrieves LinkedIn profile details.
    *   **Actions Used:** `getCompanyObject`, `getLinkedinProfile`
    *   **Use Case:** Sales and marketing, lead qualification, gathering more information about potential customers.
    *   **To Run:** `python lead_enrichment.py`

5.  **`sales_email_subject.py`**:
    *   **Description:** Generates multiple engaging subject lines for sales emails using an LLM.
    *   **Actions Used:** `chat` (`invokeLlm`)
    *   **Use Case:** Sales outreach, improving email open rates, creating compelling email subject lines.
    *   **To Run:** `python sales_email_subject.py`

6.  **`faq_chatbot.py`**:
    *   **Description:** Creates a basic interactive chatbot that answers questions based on FAQ content crawled from a website.
    *   **Actions Used:** `grabWebText` (crawl mode), `chat` (`invokeLlm`)
    *   **Use Case:** Customer service, providing automated answers to common questions, website support.
    *   **To Run:** `python faq_chatbot.py`

7.  **`youtube_summary.py`**:
    *   **Description:** Summarizes the transcript of a YouTube tutorial video using an LLM.
    *   **Actions Used:** `getYoutubeTranscript`, `chat` (`invokeLlm`)
    *   **Use Case:** Customer service, quick learning, content summarization, support documentation.
    *   **To Run:** `python youtube_summary.py`

8.  **`website_monitor.py`**:
    *   **Description:** Monitors a website for content changes at regular intervals and stores the website content in the agent's database. Detects and reports changes.
    *   **Actions Used:** `grabWebText`, `getVariableFromDatabase`, `storeVariableToDatabase`
    *   **Use Case:** Operations, website monitoring, content change detection, competitor website tracking.
    *   **To Run:** `python website_monitor.py` (Note: Runs continuously until you stop it with Ctrl+C)

9.  **`file_conversion.py`**:
    *   **Description:** Converts a file from a URL to a different format (e.g., PDF to TXT), validating the conversion options first.
    *   **Actions Used:** `convertFileOptions`, `convertFile`
    *   **Use Case:** Operations, document processing, file format conversion workflows.
    *   **To Run:** `python file_conversion.py`

10. **`interactive_chat.py`**:
    *   **Description:** Starts a simple interactive chat shell where you can have a back-and-forth conversation with an LLM.
    *   **Actions Used:** `chat` (`invokeLlm`)
    *   **Use Case:** General chat, quick prototyping, exploring LLM capabilities interactively.
    *   **To Run:** `python interactive_chat.py`

---

**Note:** These examples are for demonstration purposes and provide basic functionality. For production use cases, you would likely need to add more robust error handling, input validation, and potentially more complex logic within the scripts.
