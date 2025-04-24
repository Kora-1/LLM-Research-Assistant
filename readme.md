# Research Assistant with LLM

This project is an AI-powered research assistant built using **Streamlit**, **Langchain**, and **Google GenerativeAI SDK (Gemini)**. The app helps users to input research queries and get detailed answers based on available data. The system first tries to fetch the results from a cached memory and, if not available, runs the full agent pipeline to generate an answer, which is then cached for future queries.

## Features

- **Research Query Input**: Users can input a research query to get an answer.
- **Memory Caching**: The system stores answers to frequently asked queries to avoid redundant processing.
- **Streamlit UI**: A simple, user-friendly interface for interacting with the AI.
- **Downloadable Results**: Users can download the generated research results as a JSON file.
  
## Requirements

Before running the app, make sure you have the following dependencies installed:

- **Streamlit**: Web framework for building the app interface.
- **Langchain**: Python library for managing chains of language models.
- **Google GenerativeAI SDK (Gemini)**: Google’s API for language models.
- **Dotenv**: For managing environment variables like API keys.
  
### Install Dependencies

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

You can generate the `requirements.txt` file by running:

```bash
pip freeze > requirements.txt
```

Here’s the list of required dependencies:

```
streamlit
langchain-community
google-generativeai
python-dotenv
requests
beautifulsoup4
langchain
langgraph
tavily-python
```

## Setup

### 1. Create `.env` File

Create a `.env` file in the root directory of the project and add your API keys as follows:

```
TAVILY_API_KEY=your_tavily_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Ensure that your `.env` file contains the correct keys for **Tavily** and **Google GenerativeAI** (Gemini).

### 2. Setting Up Environment Variables

The `.env` file should store sensitive information like API keys. You can use the `dotenv` package to load these values into your environment.

```python
from dotenv import load_dotenv
load_dotenv()
```

### 3. Running the Streamlit App

Once you have installed all dependencies and set up the `.env` file, you can run the Streamlit app.

To start the app, navigate to the project directory in your terminal and run:

```bash
streamlit run main.py
```

This will start the app, and it will automatically open a new tab in your default web browser where you can interact with the research assistant.

### 4. Interacting with the App

- **Enter your query** in the input field.
- The system will first check if the result is cached. If it’s cached, it will use the cached answer.
- If no cached result is found, it will run the full research agent pipeline and generate an answer.
- Once the answer is generated, it will be displayed on the screen.
- You can also **download the result** as a JSON file.

## Project Structure

Here is the basic structure of the project:

```
research_assistant_ai/
│
├── .env                         # Environment variables (API keys)
├── requirements.txt             # List of dependencies
│
├── main.py                      # Entry point of the application
├── config.py                    # Configuration settings (e.g., constants, paths)
│
├── data/                        # Directory for data files
│   ├── memory_store.json        # Stores cached research results
│   ├── queries_results.json     # Stores results of queries
│   └── memory_utils.py          # Code for loading and saving memory
│
├── agents/                      # Contains agent-related logic
│   ├── research_agent.py        # Code to process research queries
│   ├── answer_agent.py          # Code to generate answers
│
├── graph/                       # Contains graph-related logic
│   ├── research_graph.py        # Code to build and manage the research graph
│
└── tool/                        # Tools used by the agents
    ├── summarizer.py            # Logic for summarizing research content
    └── tavily_search.py                # Tool for reading or researching content (using tavily)

```

## How the System Works

1. **User Query**: The user enters a research query in the Streamlit UI.
2. **Memory Check**: The system checks if the query has been previously processed and cached.
3. **Full Agent Pipeline**: If no cached result is found, the system runs the full agent pipeline. This pipeline fetches search results, generates summaries, and combines them into a final answer.
4. **Save to Memory**: The answer is saved to memory for future reference, avoiding the need to reprocess the same query.
5. **Final Answer**: The generated or cached answer is displayed to the user, with the option to download the results.


## Conclusion

This **Research Assistant with LLM** app leverages the power of AI models to answer complex research queries in a fast, efficient manner. It uses caching to avoid redundant computations and makes it easy to interact with the system using Streamlit.

---
