# Exercise 3: Hybrid RAG with MCP — Vector Search & Web Search

This exercise demonstrates how to build a hybrid Retrieval-Augmented Generation (RAG) system using the Model Context Protocol (MCP). The system combines a local vector database for ML FAQs with a web search tool, allowing you to route queries to the most appropriate source.

## Project Structure

```
exercise-3/
├── client.py           # Demonstrates client usage and query routing
├── server.py           # Defines MCP tools: vector search and web search
├── prepare_store.py    # Prepares and persists the vector store
```

## Setup

1. Ensure the general setup
2. Prepare the vector store (run this before starting the server):
   ```bash
   python prepare_store.py
   ```

## Running the Server

Start the MCP server:

```bash
python server.py
```

The server will:
- Load the ML FAQ vector database from `.venv/.rag_store`
- Provide two tools: `vector_rag` (for ML FAQ search) and `web_search` (for general queries)

## Using the Client

Run the client to interact with the MCP server:

```bash
python client.py
```

The client will:
- Connect to the MCP server and list available tools
- Prompt you for a query
- Automatically route ML-related queries to the local vector store (`vector_rag`)
- Route general queries to the web search tool (`web_search`)
- Display the results in a readable format

## Code Overview

### Tools

- **vector_rag**: Searches the local ML FAQ vector DB for relevant answers using semantic similarity.
- **web_search**: Uses DuckDuckGo to answer general queries from the web.

### Vector Store

- Prepared by `prepare_store.py` using `sentence-transformers` and persisted in `.venv/.rag_store`.
- Stores ML FAQ documents and their embeddings for fast retrieval.

### Query Routing

- The client uses simple keyword matching to decide whether to use the vector DB or web search.
- You can extend this logic for more advanced routing.

## Extending the Example

- Add more ML FAQ documents in `prepare_store.py` and re-run it to update the vector store.
- Improve the query routing logic in `client.py`.
- Add new tools or resources to the MCP server as needed.