import json
import requests

API_KEY = '6a9680b9c80b45b47bc5c5a2ed051e17'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """Fetches weather data for a given city."""
    api_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def save_weather_data(data, filename="weather_data.json"):
    """Saves JSON data to a file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_weather_data(filename="weather_data.json"):
    """Loads JSON data from a file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"error": "File not found or invalid JSON"}

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    weather_data = get_weather(city_name)

    if "weather" in weather_data:
        print(f"Weather description: {weather_data['weather'][0]['description']}")
        save_weather_data(weather_data)
    else:
        print("Error fetching weather data.")
