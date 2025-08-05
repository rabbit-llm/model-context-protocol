# capabilities.py
from fastmcp import FastMCP
from typing import Dict, List


mcp = FastMCP(name="WeatherService")

@mcp.tool(name="get_weather", description="Returns weather for a given city.")
def get_weather(city: str):
    current_weather = {
        "Helsinki": "The weather is sunny. The temperature is 27°C. No rain expected.",
        "Tampere": "The weather is cloudy. The temperature is 25°C. Light rain expected.",
        "Oulu": "The weather is rainy. The temperature is 22°C. Heavy rain expected.",
        "Vaasa": "The weather is windy. The temperature is 24°C. No rain expected."
    }
    print(f"Fetching weather for {city}...")

    return {"city": city, "weather": current_weather.get(city, "Unknown")}


@mcp.resource("resource://ai/locations")
def locations() -> List[str]:
    return [
        "Helsinki",
        "Tampere",
        "Oulu",
        "Vaasa"
    ]


@mcp.prompt("get_weather")
def get_weather_prompt(location: str):
    return [
        {"role": "system", "content": "You are a weather assistant"},
        {"role": "user", "content": "Please give me the weather of the city {location}."}
    ]

if __name__ == "__main__":
    print("\n🚀 Starting weather Server...")
    mcp.run(transport="http")