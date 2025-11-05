import requests, json
import os
import time

## OpenWeatherMap Settings

API_KEY = "none"
CITY = "none"
UNIT = "metric"

## Variables

idleTime = 300

## Functions

def fetchWeather():
    global API_KEY, CITY, UNIT
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNIT}"
    try:
        response = requests.get(URL)
        data = response.json()
    except:
        print("Error connecting to the API. Try checking internet connection or API key.")
    
    if data["cod"] == 200:
        main = data["main"]
        temp = main["temp"]
        humidity = main["humidity"]
        weather = data["weather"][0]["description"]
        print(f"{CITY}: {temp} degrees, {humidity}% humidity, {weather}", flush=True)
    else:
        print("Error fetching weather.")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fetchSettings():
    global API_KEY, idleTime
    print("A - API Key\nR - Refresh Time for Idle")
    soptions = input("Choose an option.")
    
    if soptions.upper() == "A":
        API_KEY = input("Input your API key.\n")
        clear()
        mainMenu()
    
    elif soptions.upper() == "R":
        idleTime = int(input("How long should the forecast be refreshed in idle? Input in seconds, default is 300."))
        clear()
        mainMenu()
        
    else:
        print('Not found.')
        time.sleep(1)
        clear()
        mainMenu()
  
def idle():
    while True:
        clear() ## clear screen to make it nicer
        fetchWeather() ## fetch weather
        
        ## time 
        current_time = time.localtime()
        formatted = time.strftime("%H:%M:%S", current_time)
        print('Last updated at', formatted, flush=True)
        
        time.sleep(idleTime) ## auto refresh

## Menu

def mainMenu():
    print('Welcome to Nimbus')
    print("F - Forecast\nL - Location\nU - Unit\nS - Settings\nI - Idle\nE - Exit")

    option = input("Choose an option.")

    if option.upper() == "F":
        clear()
        fetchWeather()
        input("\nPress Enter to return to menu...")
        clear()
        mainMenu()
    elif option.upper() == "L":
        global CITY
        clear()
        CITY = input("Input your city name.\n")
        clear()
        mainMenu()
    elif option.upper() == "U":
        global UNIT
        clear()
        UNIT = input("Input your preferred temperature unit (metric, imperial)\n")
        clear()
        mainMenu()
    elif option.upper() == "S":
        clear()
        fetchSettings()
    elif option.upper() == "I":
        idle()
    elif option.upper() == "E":
        sys.exit()
    else:
        print('Not found.')
        time.sleep(1)
        clear()
        mainMenu()
        
mainMenu()