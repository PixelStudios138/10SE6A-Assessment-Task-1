import time
from api import *
import requests

base_url = "https://api.weatherapi.com/v1"
api_type = "" # String to determine what type of data to request, e.g. general weather, forecasts, alerts, etc.

def send_request(city, api_type):
    """Send requests to the API and get data. The url variable combines all necessary features
       for the request to work. It will try to get data, with 3 exceptions. The first is if it
       takes too long to connect to the API and it times out. The second is if the API takes
       too long to return data, again returning a time out error. The final exception is if the
       api connects, but returns an error code. If none of these exceptions are raised, the api
       will return the database to be stored in a variable and be used later in the program."""
    url = f"{base_url}/{api_type}?key={api_key}&q={city}"
    try:
        response = requests.get(url, timeout=(3, 3))
        try: 
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to get weather data. Status code: {response.status_code}")
                return None
        except:
            print("An error occurred while retrieving weather data.")
            return None
    except requests.exceptions.ConnectTimeout as e:
        print(f"Connection to API timed out. Try again later, ({e})")
    except requests.exceptions.ReadTimeout as e2:
        print(f"Data sent to API timed out: {e2}")

def gather_main_data(data):
    """This function gathers basic weather data, which will be immediately displayed to the user.
       The data that will be displayed is the temperature, condition, and what the temperature feels
       like for the given location."""
    if data:
        location = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        condition = data["current"]["condition"]["text"].lower()
        print(f"The temperature in {location}, {region}, {country} is {temperature}°C. It feels like {feels_like}°C.")
        print(f"It is {condition}")

def get_wind_data(data):
    """Presents wind data, such as speed, direction, chill, and gust data"""
    if data:
        wind_speed = data["current"]["wind_kph"]
        wind_direction = data["current"]["wind_dir"]
        wind_chill = data["current"]["windchill_c"]
        gust = data["current"]["gust_kph"]
        print(f"The wind is {wind_speed}kph {wind_direction}, with a chill of {wind_chill}°C")
        print(f"There is a gust of {gust}kph")

def get_rain_data(data):
    """Gets data related to rain, such as precipitation, cloud cover, and dew point."""
    if data:
        precipitation = data["current"]["precip_mm"]
        cloud = data["current"]["cloud"]
        dew_point = data["current"]["dewpoint_c"]
        print(f"The precipitation is {precipitation}mm")
        print(f"The cloud cover is {cloud}%")
        print(f"The dew point is {dew_point}°C")

def get_extra_data(data):
    """This function gets additional information that the user may wish to view, such as humidity,
       pressure, visibility, and uv index and presents it to the user"""
    if data:
        humidity = data["current"]["humidity"]
        pressure = data["current"]["pressure_mb"]
        uv_index = data["current"]["uv"]
        visibility = data["current"]["vis_km"]
        print(f"The pressure is {pressure}mb")
        print(f"The humidity is {humidity}%")
        print(f"The UV index is {uv_index}")
        print(f"The visibility is {visibility}km")

def temp_ui():
    """Temporary UI to test functions. This will eventually be replaced with a tkinter app-interface.
        This will prompt the user to choose the type of data they wish to view.
        This will simulate how the final app will work, but in the terminal instead of a graphical interface."""
    city_to_analyse = input("What city would you like to view data on? ").lower()
    weather_data = send_request(city_to_analyse, "current.json")
    gather_main_data(weather_data)
    while True:
        print("\nWhat type of data would you like to view?")
        print("1. Wind data")
        print("2. Rain data")
        print("3. Extra data (pressure, humidity, UV index, visibility)")
        print("4. Exit")
        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            get_wind_data(weather_data)
        elif choice == "2":
            get_rain_data(weather_data)
        elif choice == "3":
            get_extra_data(weather_data)
        elif choice == "4":
            print("Exiting the program.")
            quit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        time.sleep(2)
