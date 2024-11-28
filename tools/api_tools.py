import requests

def fetch_weather(city: str) -> str:
    """Fetch weather information for a given city."""
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}")
    if response.status_code == 200:
        data = response.json()
        return f"The current temperature in {city} is {data['current']['temp_c']}°C."
    return "Failed to fetch weather data."
