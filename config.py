import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API keys from environment variables
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # For Gemini via Google GenerativeAI SDK

# Check if the Tavily API Key is loaded correctly
if TAVILY_API_KEY is None:
    print("Enter Tavily API Key")  # Prompt to enter Tavily API Key if it's missing
else:
    # Print the last 6 characters of the Tavily API Key to confirm it's loaded
    print("Tavily API Key found", TAVILY_API_KEY[-6:])

# Check if the Gemini API Key is loaded correctly
if GEMINI_API_KEY is None:
    print("Enter Gemini API Key")  # Prompt to enter Gemini API Key if it's missing
else:
    # Print the last 6 characters of the Gemini API Key to confirm it's loaded
    print("Gemini API Key found", GEMINI_API_KEY[-6:])
