from data.memory_utils import save_to_json
from tools.tavily_search import get_tavily_tool
from tools.summarizer import summarize_content
import requests
from bs4 import BeautifulSoup


def fetch_web_content(url):
    """
    Fetches the raw text content from a given URL.

    This function makes an HTTP request to the provided URL, parses the HTML content,
    and extracts the raw text using BeautifulSoup. It handles any exceptions that
    may arise during the request or parsing process and returns an empty string if
    an error occurs.

    Parameters:
    - url (str): The URL of the web page to fetch content from.

    Returns:
    - str: The raw text content from the web page, or an empty string if an error occurs.

    Example:
    >>> fetch_web_content("http://example.com")
    "Example Domain"
    """
    try:
        # Send a GET request to the URL with a timeout of 10 seconds
        html = requests.get(url, timeout=10).text
        # Parse the HTML using BeautifulSoup and extract the text content
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()  # Return the raw text content
    except Exception as e:
        # If an error occurs during the request or parsing, return an empty string
        return ""


def research_agent(state):
    """
    Performs research based on the provided query, gathers results, and summarizes the content from web sources.

    This function receives a research query and utilizes the TavilySearch tool to get search results.
    It then fetches the web content from the URLs in the search results, summarizes the content,
    and stores the data in a JSON file.

    Parameters:
    - state (dict): A dictionary containing the following key:
        - "query" (str): The research query that needs to be answered.

    Returns:
    - dict: A dictionary containing:
        - "query" (str): The original research query.
        - "summaries" (list): A list of summaries, each containing a URL and its corresponding summary.

    Example:
    >>> state = {"query": "What are the benefits of AI in healthcare?"}
    >>> result = research_agent(state)
    >>> print(result["summaries"])
    [{"url": "http://example.com/ai-healthcare", "summary": "AI helps with diagnostics."}]
    """
    # Extract the research query from the provided state dictionary
    query = state["query"]

    # Get an instance of the TavilySearch tool (to search for research results)
    tavily_tool = get_tavily_tool()

    # Run the search with the provided query
    results = tavily_tool.run(query)

    # Initialize an empty list to store the summaries
    summaries = []

    # Iterate through the search results and process each item
    for item in results:
        url = item.get("url")  # Extract the URL from the result
        # Fetch the raw text content of the web page at the provided URL
        raw_text = fetch_web_content(url)
        # Summarize the content based on the research query
        summary = summarize_content(raw_text, query)
        # Append the URL and its summary to the summaries list
        summaries.append({"url": url, "summary": summary})

    # Prepare the data to save, including the query, results, and summaries
    data_to_save = {
        "query": query,
        "results": results,
        "summaries": summaries
    }

    # Save the data to a JSON file using the save_to_json function
    save_to_json(data_to_save)

    # Return the query and the summaries as a dictionary
    return {
        "query": query,
        "summaries": summaries
    }
