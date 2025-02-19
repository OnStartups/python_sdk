class AgentDotAiError(Exception):
    """Base exception class for agentdotai library."""
    pass

class BadRequestError(AgentDotAiError):
    """Exception raised for 400 Bad Request errors."""
    pass

class AuthenticationError(AgentDotAiError):
    """Exception raised for 403 Authentication errors."""
    pass

class ServerError(AgentDotAiError):
    """Exception raised for 500 Server errors."""
    pass

class APIError(AgentDotAiError):
    """Generic exception for other API errors."""
    pass
