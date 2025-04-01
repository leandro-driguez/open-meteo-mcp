import requests
from mcp.server.fastmcp import FastMCP

server = FastMCP("Weather Server", "0.1.0")

OPEN_METEO_BASE_URL = "https://api.open-meteo.com/v1/forecast"

@server.tool(
    description="Consult everything about the weather in a given city. " \
    "Make weather forecast. " \
    "Get current weather data."
)
def get_weather(latitude: float, longitude: float):
    response = requests.get(
        f"{OPEN_METEO_BASE_URL}?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m,relative_humidity_2m,precipitation,cloud_cover,weather_code"
    )
    return response.json()

server.run()