import requests


def get_weather(latitude, longitude):
    """
    Get current weather information using Open-Meteo.
    No API key is required.
    """

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,weather_code"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    current = data.get("current", {})

    return {
        "temperature": current.get("temperature_2m"),
        "weather_code": current.get("weather_code")
    }