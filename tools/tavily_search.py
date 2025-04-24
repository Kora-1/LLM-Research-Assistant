from langchain_community.tools.tavily_search.tool import TavilySearchResults

def get_tavily_tool(k=5):
    """
    Returns an instance of the TavilySearchResults tool with a specified number of search results.

    This function initializes the TavilySearchResults tool with the specified number of search results to be returned.
    It is useful for performing search operations using the Tavily search functionality. If an error occurs during the
    initialization, it catches the exception and prints an error message.

    Parameters:
    - k (int): The number of search results to return. Defaults to 5. This controls the number of search results
      that will be fetched by the tool.

    Returns:
    - TavilySearchResults: An instance of the TavilySearchResults tool, configured with the specified number of results.
      If an error occurs during initialization, returns None.

    Example:
    >>> tavily_tool = get_tavily_tool(10)
    >>> search_results = tavily_tool.run("What are the benefits of AI?")
    >>> print(search_results)
    """
    try:
        # Attempt to initialize the TavilySearchResults tool with the specified number of search results
        return TavilySearchResults(k=k)
    except Exception as e:
        # If an error occurs during the initialization, print the error and return None
        print(f"Error initializing TavilySearchResults: {e}")
        return None
