# 10SE6A Assessment Task 1

## Project Development - Part B

This markdown file will go over the stages of the Software Development life Cycle (SDLC) for this assessment task, from requirements to implementation.

## Requirements Outline

### Functional Requirements
**User Requirements:**  
- The user must input into a string the city they wish to view weather data on
- It cannot be a country, state, or other form of location
- This must also be a legitimate place name

**Inputs & Outputs:**  
- The system must take in a string inputted by the user of the city they would like to view data on
- It should output an image of the condition (e.g partly cloudy, sunny, etc), along with:
  - location
  - temperature
  - and condition.
- It may also display what the temperature feels like, the pressure, precipitation, humidity, and percentage of clouds.

**Core Features:**  
- The system must be an app
- A user can input a city in the world, and the weather for that location will be displayed, such as:
  - temperature
  - condition
  - precipitaiton
  - humidity
  - and other things

**User Interaction:**  
- The system will be displayed as an app
- Text will help show the user what to do
- It must be easy to navigate.

**Error Handling:**  
- A user could potentially input an incorrect value into the city field, meaning that no data will be returned
  - A `try:` and `except:` block will be used to check if it works, and gently give an error prompting the user to try again if it doesn't
- Another possible error is if the api can't return data, whether or not the user inputs correct information.
  - Like the previous error, a `try:` and `except:` block will be used to check if the data loads correctly, and if it doesn't, an error will be presented without the system crashing.

### Non-Functional Requirements
**Performance:**  
- The system should load data in no more than 3 seconds
- This will be checked by using the `timeout()` function, if it doesn't load within 3 seconds, the system will timeout and return an error without crashing the system telling the user to try again later

**Useability/Accessibility:**  
- To help with accessibility, the system will be easy to navigate by having text telling people what to do
- The text will also be fairly large to help those with slight visual impairments

**Reliability:**  
- A major crash that could occur is if the api can't properly retrieve data
  - By combining the `timeout()` function with a `try:` and `except:` block, this should avoid crashing the system
  - This will prevent the system to work without any data
- Another major problem is if the api key is leaked
  - This will be prevented by storing it in a `.gitignore` file that prevents it from being public, but still allowing the system to work fine
 
### Use Cases

**Use Case 1: Data Retrieval:**  
**Actor:** User (Person checking the Weather)  
**Preconditions:** Internet connection, available API key  

1. Search City
   - User enters a city name into the system  
2. API Retrieval
   - The system sends the city name to the api to retrieve data  
3. Error Handling  
   - The system checks if the api sent back data or an error was returned

**Postconditions:** Data is successfully retrieved for later use, or an error was presented without crashing the system

**Use Case 2: Data Display:**  
**Actor:** User  
**Preconditions:** Data successfully retrieved from API

1. Find Data
   - Load data from api key into dataframe to be used
2. Filter Data
   - Find the specific data to be used and store it in variables, and remove any unwanted information
3. Present Data
   - System displays data as text with some images

**Postconditions:** Data is successfully displayed to the user

## Determining Specifications

The following specifications are required for the project to run properly:
- A laptop with an internet connection and sufficient ram (~25-30 MB)
- Github
- Python 3.11 with requests and time library installed

## Design

The following diagrams were made to demonstrate how the code will function before it was made.

### Gantt Chart

This chart shows the timing for programming this task. It will begin in Week 5 and finish just before the due date in Week 9. 

![Gantt Chart describing the timing of the development of the assessment task](/Images/GanttChart.png "Gantt Chart of Development Stage")  

### Data Dictionaries

These charts show all the data and variables that are used in the program. The first shows the data from the api, the second shows the variables used by the program.

![Data dictionary describing the data from the database](/Images/api_data_dictionary.png "Data Dictionary from API")  

![Data dictionary describing the variables used in the program](/Images/Data_Dict.png "Data Dictionary of variables in the program")  

### Flowcharts

The following flowcharts cover all functions in the program, including the main file

![Flowchart describing how the main function will work](/Images/main_flowchart.png "Flowchart of main.py")  

![Flowchart describing how the startup function will work](/Images/startup_flowchart.png "Flowchart of startup function")  

![Flowchart describing how the ui function will work](/Images/ui_flowchart.png "Flowchart of ui function")  

![Flowchart describing how the additional data menu function will work](/Images/additionaldatamenu_flowchart.png "Flowchart of data menu")  

![Flowchart describing how the send request function will work](/Images/sendrequest_flowchart.png "Flowchart of send request function")  

![Flowchart describing how the gather main data function will work](/Images/gathermaindata_flowchart.png "Flowchart of main data function")  

![Flowchart describing how the wind data function will work](/Images/getwinddata_flowchart.png "Flowchart of wind function")  

![Flowchart describing how the rain function will work](/Images/getraindata_flowchart.png "Flowchart of rain function")  

![Flowchart describing how the extra data function will work](/Images/getextradata_flowchart.png "Flowchart of getting extra data function")  

![Flowchart describing how the help function will work](/Images/help_flowchart.png "Flowchart of help function")  

![Flowchart describing how the save history function will work](/Images/savehistory_flowchart.png "Flowchart of save history function")  

![Flowchart describing how the view history function will work](/Images/viewhistory_flowchart.png "Flowchart of view history function") 

### Pseudocode

Alongside the flowcharts, I have also made pseudocode for each function. These will be in order of the flowcharts from top to bottom: main, startup, ui, additional data menu, send request, gather main data, get wind data, get rain data, get extra data, help, save history, and view history.

```
BEGIN main
DECLARE String history
startup(history)
END main
```

```
BEGIN startup (history)
OUTPUT "Welcome to the Weather App!"
DECLARE int choice
WHILE true
    OUTPUT "Would you like to continue, or get help before starting?"
    OUTPUT "1) Start Program"
    OUTPUT "2) Get Help"
    OUTPUT "3) Exit"
    OUTPUT "Enter the number for your choice: "
    INPUT choice
    IF choice == 1
        ui(history)
    ELSE IF choice == 2
        Call help()
    ELSEIF choice == 3
        Open history mode write
        Write "Exited program at startup"
        Output "Exiting the program"
        QUIT
    ELSE
        Output "Invalid choice. Enter a number between 1 and 3"
    ENDIF
ENDWHILE
END startup
```

```
BEGIN ui (history)
DECLARE string continuechoice
DECLARE int choice
DECLARE string city_to_analyse
DECLARE String Array weatherdata[17]
OUTPUT "What city would you like to view data on?"
INPUT city_to_analyse
sendrequest(city_to_analyse, weatherdata)
gather_main_data(weatherdata)
savehistory("Requested and viewed main data", history)
OUTPUT "Would you like to view more? (y/n)"
INPUT continuechoice
IF continuechoice = "y"
    additionaldatamenu(weatherdata)
ELSEIF continuechoice = "n"
    savehistory("Exited program after viewing main data", history)
    OUTPUT "Exiting the program"
    QUIT
ELSE
    OUTPUT "Invalid choice. Please enter either 'y' or 'n'"
ENDIF
END ui
```

```
BEGIN additional_data_menu(data)
    DECLARE Integer choice
    WHILE true
        savehistory("Entered additional data menu", history)
        OUTPUT "What would you like to do?"
        OUTPUT "1) View Wind Data"
        OUTPUT "2) View Rain Data"
        OUTPUT "3) View Extra Data (pressure, uv, etc)"
        OUTPUT "4) Choose A Different City"
        OUTPUT "5) Get Help"
        OUTPUT "6) View History"
        OUTPUT "7) Exit"
        OUTPUT "Enter the number for your choice:"
        INPUT choice
        IF choice = 1
            get_wind_data(data)
        ELSEIF choice = 2
            get_rain_data(data)
        ELSEIF choice = 3
            get_extra_data(data)
        ELSEIF choice = 4
            ui()
        ELSEIF choice = 5
            help()
        ELSEIF choice = 6
            viewhistory()
        ElLSEIF choice = 7
            savehistory("Exited the program after viewing additional data", history)
            OUTPUT "Exiting the program"
	QUIT
         ELSE
            OUTPUT "Invalid choice. Enter a number between 1 and 7"
        ENDIF
    ENDWHILE
END additional_data_menu
```

```
BEGIN sendrequest (city, data)
DECLARE string url = "https://api.weatherapi.com/v1/current.json?key=(apiKey)&q=city"
DECLARE string response = requests.get(url, timeout=(3, 3))
IF response == "200"
    OUTPUT return.json
ELSE
    OUTPUT "An error occurred when retrieving data"
ENDIF
END sendrequest
```

```
BEGIN gather_main_data (data)
IF data
    OUTPUT "The temperature in " 
    OUTPUT data[“location”]
    OUTPUT data[“region”]
    OUTPUT data[“country”]
    OUTPUT "is"
    OUTPUT data[“temperature_c”]
    OUTPUT ". It feels like "
    OUTPUT data[“feelslike_c”]
    OUTPUT ". It is "
    OUTPUT data[“condition”]
ENDIF
END gather_main_data()
```

```
BEGIN get_wind_data (data{})
IF data
    OUTPUT "The wind is "
    OUTPUT data[“wind_speed”]
    OUTPUT"kph"
    OUTPUT data[“wind_direction”]
    OUTPUT " with a chill of "
    OUTPUT data[“wind_chill”]
    OUTPUT " degrees celsius. There is a gust of"
    OUTPUT data[“gust_speed”]
    OUTPUT" kph."
ENDIF
END get_wind_data
```

```
BEGIN get_rain_data (data)
IF data
    OUTPUT "The precipitation is "
    OUTPUT data[precipitation”]
    OUTPUT "mm. The cloud cover is "
    OUTPUT data[“cloud”]
    OUTPUT "%. The dew point is "
    OUTPUT data[“dew_point”]
    OUTPUT " degrees celsius."
ENDIF
END get_rain_data()
```

```
BEGIN get_extra_data (data)
IF data
    OUTPUT "The pressure is "
    OUTPUT data[“pressure”]
    OUTPUT "mb. The humidity is "
    OUTPUT data[“humidity”]
    OUTPUT "%. The UV Index is "
    OUTPUT data[“uv”]
    OUTPUT ". The visibility is "
    OUTPUT data[“visibility”]
    OUTPUT "km."
ENDIF
END get_extra_data()
```

```
BEGIN help
DECLARE int choice
While true
    savehistory("Entered help menu")
    OUTPUT "What do you want help with?"
    OUTPUT "1) How to use the app"
    OUTPUT "2) What information you can view"
    OUTPUT "3) Navigation tips"
    OUTPUT"4) Back to main menu"
    IF choice == 1
        OUTPUT "After running the file, you will be prompted to enter a city. You will be presented with basic weather data, such as temperature, condition, and what the temperature feels like. You can then choose to view more specific data, such as wind data, rain data, or extra data. You can also choose to view help or exit the program."
        savehistory("Viewed help on using the app", history)
    ELSEIF choice == 2
        OUTPUT "You will be automatically presented with basic information, such as temperature, condition, and what the temperature feels like. You can then choose to view more specific information, such as that for wind, rain, along with some additional data. Wind data includes wind speed, direction, chill, and gust data. Rain data includes precipitation, cloud cover, and dew point. You can also view additional information on humidity, pressure, visibility, and uv index."
        savehistory("Viewed help on information that can be viewed", history)
    ELSEIFchoice == 3
        OUTPUT "Navigation tips: - Use the numeric keys to select options from the menu. - You can navigate back to the main menu at any time by selecting the appropriate option."
        savehistory("Viewed help on navigation tips", history)
    ELSEIF choice == 4
         savehistory("Exited help menu", history)
         ui()
    ELSE
         OUTPUT "Invalid input. Enter number between 1 and 4"
    ENDIF
ENDWHILE
END help
```

```
BEGIN savehistory (message, history)
OPEN history (write mode)
WRITE message
CLOSE
END
```

```
BEGIN viewhistory (history)
OPEN history mode read
READ history
OUTPUT history
END viewhistory
```

### System Chart

The final diagram for the design stage is the following system chart. It shows the flow of information within modules, and how those modules relate to each other.

![Structure chart describing the flow of information within modules](/Images/structure_chart.png "Structure chart of system")

## Maintenance 

Maintenance will be a major factor of the future of this project, as leaving it alone will cause it to eventually cease functioning, preventing future users from being able to use it. 
