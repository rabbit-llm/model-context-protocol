# client.py
from server import get_weather

def call_tool(tool_name, **kwargs):
    if tool_name == "get_weather":
        # In a real client, this would be a network call
        return get_weather(**kwargs)
    return "Tool not found"