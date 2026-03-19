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
