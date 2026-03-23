import time
from api import *
import requests

base_url = "https://api.weatherapi.com/v1"
history = [] # List to store user activity in the program

def send_request(city):
    """Send requests to the API and get data. The url variable combines all necessary features
       for the request to work. It will try to get data, with 3 exceptions. The first is if it
       takes too long to connect to the API and it times out. The second is if the API takes
       too long to return data, again returning a time out error. The final exception is if the
       api connects, but returns an error code. If none of these exceptions are raised, the api
       will return the database to be stored in a variable and be used later in the program.
       If they are, the code will either run again, or quit if timed out"""
    url = f"{base_url}/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url, timeout=(3, 3))
        try: 
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to get weather data. Status code: {response.status_code}")
                history.append(f"Failed to retrieve weather data for {city}. Returned error code {response.status_code}")
                ui()
        except:
            print("An error occurred while retrieving weather data.")
            history.append(f"Failed to retrieve weather data for {city}. No error code returned.")
            ui()
    except requests.exceptions.ConnectTimeout as e:
        print(f"Connection to API timed out. Try again later, ({e})")
        history.append(f"Connection timed out. Returned error {e}")
        quit()
    except requests.exceptions.ReadTimeout as e2:
        print(f"Data sent to API timed out: {e2}")
        history.append(f"Data retrieval timed out. Returned error {e2}")
        quit()

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
        history.append("Entered help menu")
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
            history.append("Viewed help on using the app")
        elif choice == "2":
            print("\nYou will be automatically presented with basic information, such as temperature, condition, and what the temperature feels like. \n" \
            "You can then choose to view more specific information, such as that for wind, rain, along with some additional data. \n" \
            "Wind data includes wind speed, direction, chill, and gust data. \n" \
            "Rain data includes precipitation, cloud cover, and dew point. \n" \
            "You can also view additional information on humidity, pressure, visibility, and uv index.\n")
            history.append("Viewed help on what information they can view")
        elif choice == "3":
            print("\nNavigation tips:")
            print("- Use the numeric keys to select options from the menu.")
            print("- You can navigate back to the main menu at any time by selecting the appropriate option.\n")
            history.append("Viewed help on navigation tips")
        elif choice == "4":
            history.append("Exited help menu")
            return
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.\n")
            history.append("Messed up real time")
        time.sleep(2)

def save_history():
    with open("history.txt", "a") as f:
        f.write("\n".join(history))

def view_history():
    """This function allows the user to view their history in the program, showing them what they have done in the program"""
    history.append("Viewed current session history")
    print("\nYour history in the program:")
    print("\n".join(history))
    choice = input("\nWould you like to see full history from previous sessions? (y/n) ").lower()
    if choice == "y":
        try:
            with open("history.txt", "r") as f:
                full_history = f.read()
                print("\nFull history from previous sessions:")
                print("\n".join(full_history.splitlines()))
                history.append("Viewed history from previous sessions")
        except FileNotFoundError:
            print("\nNo history file found. This may be your first time using the program.")
            history.append("Tried to view history from previous sessions, but no history file found")
    elif choice == "n":
        return
    else:
        print("\nInvalid choice. Please enter 'y' or 'n'.")

def additional_data_menu(data):
    while True:
        history.append("Entered additional data menu")
        print("\nWhat type of data would you like to view?")
        print("1. Wind data")
        print("2. Rain data")
        print("3. Extra data (pressure, humidity, UV index, visibility)")
        print("4. View a different city")
        print("5. Help")
        print("6. View history")
        print("7. Exit")
        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            get_wind_data(data)
            history.append("Viewed wind data")
        elif choice == "2":
            get_rain_data(data)
            history.append("Viewed rain data")
        elif choice == "3":
            get_extra_data(data)
            history.append("Viewed extra data")
        elif choice == "4":
            history.append("Exited additional data menu to view a different city")
            ui()
        elif choice == "5":
            help()
        elif choice == "6":
            view_history()
        elif choice == "7":
            history.append("Exited program after viewing additional data")
            save_history()
            print("\nExiting the program.")
            quit()
        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.\n")
        time.sleep(2)

def ui():
    """Main user interface for the program. This handles gathering data and presenting it to the user, getting help, and exiting the program.
    This will not be used in startup, as the help function should be accessible before presenting data. It will stay here so the user can 
    still get help if they need it whilst using the data"""
    city_to_analyse = input("What city would you like to view data on? ").lower()
    weather_data = send_request(city_to_analyse)
    gather_main_data(weather_data)
    history.append(f"Requested and viewed main data on {city_to_analyse}")
    continue_choice = input("\nWould you like to view more data? (y/n) ").lower()
    if continue_choice == "n":
        history.append("Exited program after viewing main data")
        save_history()
        print("\nExiting the program.")
        quit()
    else:
        additional_data_menu(weather_data)

def startup():
    """This function is used to start the program. It will present the user with a welcome message and ask if they want to view help or start the program. 
    If they choose to start the program, they will be taken to the main user interface.
    If they choose to view help, they will be taken to the help menu, where they can choose what they want to view. """
    print("Welcome to the Weather App!")
    while True:
        print("\nWould you like to continue, or get some help before starting?")
        print("1. Start program")
        print("2. View help")
        print("3. Exit")
        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            ui()
        elif choice == "2":
            help()
        elif choice == "3":
            history.append("Exited program at startup")
            save_history()
            print("\nExiting the program.")
            quit()
        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.\n")
        time.sleep(2)
