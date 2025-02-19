import requests
import json

class AgentDotAiClient:
    """
    A Python client for the Agent.ai Actions API (Action-Based Interface).
    """
    BASE_URL = "https://api-lr.agent.ai/v1"

    ACTION_ENDPOINTS = {
        "grabWebText": "/action/grab_web_text",
        "grabWebScreenshot": "/action/grab_web_screenshot",
        "getYoutubeTranscript": "/action/get_youtube_transcript",
        "getYoutubeChannel": "/action/get_youtube_channel",
        "getTwitterUsers": "/action/get_twitter_users",
        "getGoogleNews": "/action/get_google_news",
        "runYoutubeSearch": "/action/run_youtube_search",
        "getSearchResults": "/action/get_search_results",
        "getRecentTweets": "/action/get_recent_tweets",
        "getLinkedinProfile": "/action/get_linkedin_profile",
        "getLinkedinActivity": "/action/get_linkedin_activity",
        "getCompanyObject": "/action/get_company_object",
        "getBlueskyPosts": "/action/get_bluesky_posts",
        "searchBlueskyPosts": "/action/search_bluesky_posts",
        "getInstagramProfile": "/action/get_instagram_profile",
        "getInstagramFollowers": "/action/get_instagram_followers",
        "outputAudio": "/action/output_audio",
        "invokeLlm": "/action/invoke_llm",
        "generateImage": "/action/generate_image",
        "storeVariableToDatabase": "/action/store_variable_to_database",
        "getVariableFromDatabase": "/action/get_variable_from_database",
        "invokeAgent": "/action/invoke_agent",
        "restCall": "/action/rest_call",
        "convertFile": "/action/convert_file",
        "convertFileOptions": "/action/convert_file_options",
    }

    def __init__(self, bearer_token):
        """
        Initializes the AgentDotAiClient with a Bearer token.

        Args:
            bearer_token (str): The Bearer token for API authentication.
        """
        self.bearer_token = bearer_token
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }

    def _handle_response(self, response):
        """
        Handles API responses, checks for errors, and returns a consistent dictionary.

        Args:
            response (requests.Response): The response object from requests.

        Returns:
            dict: A dictionary containing 'status', 'error', 'results', and 'metadata'.
                  'status' (int): HTTP status code.
                  'error' (str or None): Error message if status is not 200, None otherwise.
                  'results' (dict or str or None): API response data if successful, None otherwise.
                  'metadata' (dict or None): Metadata from the API response, if available.

        """
        response_data = {
            "status": response.status_code,
            "error": None,
            "results": None,
            "metadata": None
        }

        try:
            json_response = response.json()
            if response.status_code == 200:
                response_data["results"] = json_response.get('response')
                response_data["metadata"] = json_response.get('metadata')
            else:
                response_data["error"] = json_response.get('error', response.text) # Get error from JSON or text
        except json.JSONDecodeError:
            if response.status_code != 200: # Only set error if not successful
                response_data["error"] = f"JSON Decode Error: {response.text}"
            else:
                response_data["results"] = response.text # if 200 but not json, return text as result


        return response_data


    def _post(self, endpoint, data):
        """
        Internal method to make a POST request to the API.

        Args:
            endpoint (str): The API endpoint path.
            data (dict): The request body data as a dictionary.

        Returns:
            dict: A dictionary containing 'status', 'error', 'results', and 'metadata'.
        """
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            return {
                "status": None,
                "error": f"Request Exception: {e}",
                "results": None,
                "metadata": None
            }


    def action(self, action_id, params):
        """
        Generic method to execute an AI action by its ID.

        Args:
            action_id (str): The ID of the action to execute (operationId from OpenAPI spec).
            params (dict):  Parameters for the action as a dictionary.

        Returns:
            dict: A dictionary containing 'status', 'error', 'results', and 'metadata'.
        """
        endpoint_path = self.ACTION_ENDPOINTS.get(action_id)
        if not endpoint_path:
            return {
                "status": 400, # Or another appropriate error code
                "error": f"Invalid action_id: {action_id}",
                "results": None,
                "metadata": None
            }
        return self._post(endpoint_path, params)


    def chat(self, prompt, model="gpt4o", **kwargs):
        """
        Use the invokeLlm action to generate text based on a prompt.

        Args:
            prompt (str): The text prompt for the LLM.
            model (str, optional): LLM model to use. Defaults to "gpt4o".
            **kwargs:  Additional parameters to pass to the invokeLlm action.

        Returns:
            dict: A dictionary containing 'status', 'error', 'results', and 'metadata'.
        """
        params = {"instructions": prompt, "llm_engine": model, **kwargs} # Include kwargs
        return self.action(action_id="invokeLlm", params=params)
