import chromadb
from sentence_transformers import SentenceTransformer
import os

# List of ML FAQ documents to be embedded and stored in the vector DB
docs = [
    "Gradient descent is an optimization algorithm used to minimize loss functions.",
    "The bias-variance tradeoff explains model generalization.",
    "Transformers use attention mechanisms to model long-range dependencies.",
    "Qdrant is a popular open-source vector database.",
    "Retrieval-Augmented Generation (RAG) augments LLMs with external context."
]

# Generate unique IDs for each document
ids = [f"doc-{i}" for i in range(len(docs))]

# Load the sentence transformer model for embedding the documents
model = SentenceTransformer("all-MiniLM-L6-v2")

# Set up the path for persistent vector storage inside the .venv directory
venv_dir = os.path.join(os.path.dirname(__file__), "..", ".venv")
rag_store_path = os.path.join(venv_dir, ".rag_store")

# Initialize a persistent ChromaDB client at the specified path
client = chromadb.PersistentClient(path=rag_store_path)

# Get or create a collection named "ml_faq" for storing the documents and embeddings
collection = client.get_or_create_collection("ml_faq")

# Convert documents to vector embeddings using the model
embeddings = model.encode(docs).tolist()

# Insert (or update) the documents, their IDs, and embeddings into the collection
collection.upsert(documents=docs, ids=ids, embeddings=embeddings)

# Print the number of documents in the collection to verify successful insertion
print(f"Number of documents in collection: {collection.count()}")

# Confirmation message showing where the vector store is persisted
print(f"✅ Vector store ready and persisted at {rag_store_path}")