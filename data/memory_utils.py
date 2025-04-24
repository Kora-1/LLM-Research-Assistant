import os
import json
from datetime import datetime

# Path to the memory store file where previous queries are stored
MEMORY_PATH = "data/memory_store.json"


def load_from_memory(query: str):
    """
    Loads a previous query's data from memory if it exists.

    This function checks if the memory file exists, and if so, attempts to load the
    data associated with the given query. If the query exists in memory, it returns
    the data. Otherwise, it returns None.

    Parameters:
    - query (str): The query string whose associated data is to be fetched.

    Returns:
    - dict or None: The data corresponding to the query if it exists, otherwise None.

    Example:
    >>> load_from_memory("What are the benefits of AI in healthcare?")
    {"query": "What are the benefits of AI in healthcare?", "results": [...], "summaries": [...]}
    """
    # Check if the memory file exists
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r") as f:
            # Load the content of the memory file as a dictionary
            memory = json.load(f)
            # Return the data corresponding to the query if it exists, else None
            return memory.get(query)
    return None


def save_to_memory(state: dict):
    """
    Saves the current state of a query to memory.

    This function stores the state of a query (including the query itself and its timestamp)
    in the memory file. If the memory file already exists, it loads the current data,
    updates it with the new query, and then saves it back. If the file doesn't exist,
    it creates a new memory file.

    Parameters:
    - state (dict): A dictionary containing the query and relevant data (e.g., results, summaries).

    Example:
    >>> state = {"query": "What are the benefits of AI in healthcare?", "results": [...], "summaries": [...]}
    >>> save_to_memory(state)
    """
    # Check if the memory file exists
    if os.path.exists(MEMORY_PATH):
        # If the file exists, load the current memory data
        with open(MEMORY_PATH, "r") as f:
            memory = json.load(f)
    else:
        # If the file doesn't exist, initialize an empty dictionary
        memory = {}

    # Add the current timestamp to the state
    state["timestamp"] = datetime.now().isoformat()

    # Store the state in memory using the query as the key
    memory[state["query"]] = state

    # Save the updated memory data back to the file
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=4)


# Path to the JSON file for saving query results
FILEPATH = "data/queries_results.json"


def save_to_json(data):
    """
    Saves the results and summaries of a query to a JSON file.

    This function checks if the results file exists. If it does, it loads the existing
    data and appends the new query's data. If the file doesn't exist, it creates a new file
    with the query data.

    Parameters:
    - data (dict): A dictionary containing the query, results, and summaries to be saved.

    Example:
    >>> data = {"query": "What are the benefits of AI in healthcare?", "results": [...], "summaries": [...]}
    >>> save_to_json(data)
    """
    # Check if the results file exists
    if os.path.exists(FILEPATH):
        # If it exists, load the current data from the file
        with open(FILEPATH, 'r') as file:
            existing_data = json.load(file)
    else:
        # If it doesn't exist, create an empty dictionary
        existing_data = {}

    # Add the new query data (results and summaries) to the existing data
    query = data["query"]
    existing_data[query] = {
        "results": data["results"],
        "summaries": data["summaries"]
    }

    # Save the updated data back to the JSON file
    with open(FILEPATH, 'w') as file:
        json.dump(existing_data, file, indent=4)
