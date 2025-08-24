from fastmcp import FastMCP
import chromadb
import os
from sentence_transformers import SentenceTransformer
from duckduckgo_search import DDGS

# Set up the path for persistent vector storage inside the .venv directory
venv_dir = os.path.join(os.path.dirname(__file__), "..", ".venv")
rag_store_path = os.path.join(venv_dir, ".rag_store")

# Initialize a persistent ChromaDB client at the specified path
client = chromadb.PersistentClient(path=rag_store_path)

# Get or create a collection named "ml_faq" for storing the documents and embeddings
collection = client.get_or_create_collection("ml_faq")

# Load the sentence transformer model for embedding queries
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Print the number of documents in the collection to verify successful loading
print("Document count:", collection.count())

# Initialize the FastMCP server with a service name
mcp = FastMCP(name="MLFAQService")

@mcp.tool(name="vector_rag", description="Query the local ML FAQ vector DB and return top-k matches.")
def vector_rag(query: str, k: int = 3):
    """
    Tool: Searches the local vector database for the most relevant ML FAQ documents.
    - Encodes the query to a vector.
    - Performs a similarity search in the collection.
    - Returns the top-k matching documents and their distances.
    """
    q_emb = embedder.encode([query]).tolist()[0]
    res = collection.query(query_embeddings=[q_emb], n_results=k)
    hits = [{"doc": d, "distance": dist} for d, dist in zip(res["documents"][0], res["distances"][0])]
    return {"source": "vector_db", "query": query, "results": hits}

@mcp.tool(name="web_search", description="Run a web search for general queries.")
def web_search(query: str, k: int = 3):
    """
    Tool: Uses DuckDuckGo to perform a web search for the query.
    - Returns the top-k search results as a list of dictionaries.
    """
    with DDGS() as ddg:
        results = list(ddg.text(query, max_results=k))
    return {"source": "web", "query": query, "results": results}

if __name__ == "__main__":
    # Start the FastMCP server using HTTP transport
    print("\n🚀 Starting Machine learning FAQ Server...")
    mcp.run(transport="http")