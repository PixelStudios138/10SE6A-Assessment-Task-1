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
        print(f"\nThe temperature in {location}, {region}, {country} is {temperature}°C. It feels like {feels_like}°C.")
        print(f"It is {condition}")

def get_wind_data(data):
    """Presents wind data, such as speed, direction, chill, and gust data"""
    if data:
        wind_speed = data["current"]["wind_kph"]
        wind_direction = data["current"]["wind_dir"]
        wind_chill = data["current"]["windchill_c"]
        gust = data["current"]["gust_kph"]
        print(f"\nThe wind is {wind_speed}kph {wind_direction}, with a chill of {wind_chill}°C")
        print(f"There is a gust of {gust}kph")

def get_rain_data(data):
    """Gets data related to rain, such as precipitation, cloud cover, and dew point."""
    if data:
        precipitation = data["current"]["precip_mm"]
        cloud = data["current"]["cloud"]
        dew_point = data["current"]["dewpoint_c"]
        print(f"\nThe precipitation is {precipitation}mm")
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
        print(f"\nThe pressure is {pressure}mb")
        print(f"The humidity is {humidity}%")
        print(f"The UV index is {uv_index}")
        print(f"The visibility is {visibility}km")

def help():
    """This function provides help to the user, teaching them how to use the app, what information they can view, and navigation tips. 
    The user can choose which of these they want to view, or return to the main menu when finished."""
    while True:
        print("\nWhat do you need help with?")
        print("1. How to use the app")
        print("2. What information you can view")
        print("3. Navigation tips")
        print("4. Back to main menu")
        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            print("\nAfter running the file, you will be prompted to enter a city. You will be presented with basic weather data, such as temperature, " \
            "condition, and what the temperature feels like. \nYou can then choose to view more specific data, such as wind data, rain data, or extra data. " \
            "You can also choose to view help or exit the program.\n")
        elif choice == "2":
            print("\nYou will be automatically presented with basic information, such as temperature, condition, and what the temperature feels like. \n" \
            "You can then choose to view more specific information, such as that for wind, rain, along with some additional data. \n" \
            "Wind data includes wind speed, direction, chill, and gust data. \n" \
            "Rain data includes precipitation, cloud cover, and dew point. \n" \
            "You can also view additional information on humidity, pressure, visibility, and uv index.\n")
        elif choice == "3":
            print("\nNavigation tips:")
            print("- Use the numeric keys to select options from the menu.")
            print("- You can navigate back to the main menu at any time by selecting the appropriate option.\n")
        elif choice == "4":
            return
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.\n")
        time.sleep(2)

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
        print("4. Help")
        print("5. Exit")
        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            get_wind_data(weather_data)
        elif choice == "2":
            get_rain_data(weather_data)
        elif choice == "3":
            get_extra_data(weather_data)
        elif choice == "4":
            help()
        elif choice == "5":
            print("\nExiting the program.")
            quit()
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.\n")
        time.sleep(2)
