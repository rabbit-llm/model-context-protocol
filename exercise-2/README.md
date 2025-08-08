# Exercise 2: MCP Core Capabilities — Tools, Resources, and Prompts

This exercise demonstrates the three core capabilities of the Model Context Protocol (MCP): **Tools**, **Resources**, and **Prompts** using a simple weather service example.

## Project Structure

```
exercise-2/
├── mcp_capabilities/
│   ├── server.py      # Defines MCP capabilities (tools, resources, prompts)
│   └── client.py      # Demonstrates client usage
├── requirements.txt   # fastmcp dependency
```

## Setup

1. Ensure you have Python 3.8+ installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

Start the MCP server:

```bash
python mcp_capabilities/server.py
```

## Using the Client

Run the client to interact with the MCP server:

```bash
python mcp_capabilities/client.py
```

The client will:
- Test server connectivity
- List available tools, resources, and prompts
- Fetch the locations resource
- Call the `get_weather` tool
- Generate a prompt for an LLM

## Code Overview

### Tools

Server-side functions that perform actions.  
Example: `get_weather` returns weather info for a city.

### Resources

Static or dynamic data collections.  
Example: `locations` lists available cities.

### Prompts

Templates for generating conversational context.  
Example: `get_weather_prompt` creates a prompt for asking about the weather.

## Extending the Example

- Add new tools, resources, or prompts in `server.py`.
- Test your changes using `client.py`.

##