import asyncio
import pprint

from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

SERVER_URL = "http://localhost:8000/mcp"
pp = pprint.PrettyPrinter(indent=2, width=100)

def is_ml_query(query: str) -> bool:
    """
    Checks if the query is related to machine learning by searching for ML-specific keywords.
    Returns True if any keyword is found in the query.
    """
    ml_keywords = ["machine learning", "gradient", "transformer", "bias-variance", "qdrant", "RAG", "vector db"]
    return any(k.lower() in query.lower() for k in ml_keywords)


async def main():
    # Set up the transport and client for communicating with the MCP server
    transport = StreamableHttpTransport(url=SERVER_URL)
    client = Client(transport)

    print("\n🚀 Connecting to FastMCP server at:", SERVER_URL)
    async with client:
        # 1. Ping to test connectivity
        print("\n🔗 Testing server connectivity...")
        await client.ping()
        print("✅ Server is reachable!\n")

        # 2. List server tool
        print("🛠️  Available tools:")
        tools = await client.list_tools()  # Fetches the list of available tools from the server
        pp.pprint(tools)
 
        # 3. Get your query: 
        query = input("Your query: ")  # User inputs their query

        # 4. Call tool
        ml_query = is_ml_query(query)  # Determine if the query is ML-related
        print(f"Machine learning related query? {'Yes' if ml_query else 'No'}")

        # Extract tool names for routing logic
        tool_names = [tool.name for tool in tools]

        # Route the query to the appropriate tool based on its type and availability
        if ml_query and "vector_rag" in tool_names:
            print("🧠 Routing to vector_rag …")
            result = await client.call_tool("vector_rag", {"query": query})
        
        elif "web_search" in tool_names:
            print("🌐 Routing to web_search …")
            result = await client.call_tool("web_search", {"query": query})
        else:
            result = {"error": "No suitable tool found."}

        # Pretty print the result from the tool
        pp.pprint(result)

if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
