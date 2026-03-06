from api import *
import requests

base_url = "https://api.weatherapi.com/v1"

def send_request(city):
    url = f"{base_url}/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    
def display_weather_info(data):
    if data:
        location = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        condition = condition.lower()
        print(f"The temperature in {location}, {region}, {country} is {temperature}°C")
        print(f"It is {condition}")

city_to_analyse = input("What city would you like to view data on?")
weather_data = send_request(city_to_analyse)
print(weather_data)
#display_weather_info(weather_data)