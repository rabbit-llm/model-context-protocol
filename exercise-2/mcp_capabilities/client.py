import asyncio
import pprint

from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

SERVER_URL = "http://localhost:8000/mcp"
pp = pprint.PrettyPrinter(indent=2, width=100)



async def main():
    transport = StreamableHttpTransport(url=SERVER_URL)
    client = Client(transport)

    print("\n🚀 Connecting to FastMCP server at:", SERVER_URL)
    async with client:
        # 1. Ping to test connectivity
        print("\n🔗 Testing server connectivity...")
        await client.ping()
        print("✅ Server is reachable!\n")

        # 2. Discover server capabilities
        print("🛠️  Available tools:")
        pp.pprint(await client.list_tools())
        print("\n📚 Available resources:")
        pp.pprint(await client.list_resources())
        print("\n💬 Available prompts:")
        pp.pprint(await client.list_prompts())

        # 3. Fetch locations resource
        print("\n📍 Fetching locations...")
        locations = await client.read_resource("resource://ai/locations")
        pp.pprint(locations)

        # 4. Call the get_weather tool
        print("\n🌤️  Calling get_weather tool for Helsinki...")
        weather_result = await client.call_tool("get_weather", {"city": "Helsinki"})
        pp.pprint(weather_result)

        # 5. Use a prompt to get weather information
        print("\n📝 Using prompt to get weather information for Tampere...")
        prompt_result = await client.get_prompt("get_weather", {"location": "Tampere"})
        pp.pprint(prompt_result)
        

if __name__ == "__main__":
    asyncio.run(main())
