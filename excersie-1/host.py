# host.py
from client import call_tool

user_input = "What's the weather in Paris?"

# Normally the LLM would decide which tool to use
tool_needed = "get_weather"
params = {"location": "Paris"}

# The Host uses the Client to call the tool
result = call_tool(tool_needed, **params)

print("AI Response:", result)