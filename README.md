# Nimbus
## What is this?
Nimbus is a simple CLI-based weather app made in Python intended for underpowered devices based on OpenWeatherMap.
## How do I set this up?
This is INSANELY important to follow or else the app will not work at all.

1. Upon opening the app, you should see a location option. Select it.
2. Put in your city name. Sometimes you might need to be more specific, for instance, 'CITYNAME,STATE/COUNTRY.'
3. You should be back at the main menu. Select the settings option.
4. You should see an API key option. Select that.
5. Put in your OWM API key. If you don't have one, sign up for OWM and get a free API key.
## What features are there?
### Forecast
Prints a basic forecast. Temperature, humidity, and the weather.
### Unit Selection
Select your preferred temperature unit, imperial or metric. By default, metric is the default.
### Idle
Prints out the forecast and when it printed, then refreshes after some time. By default, it will refresh every 300 seconds or 5 minutes. You can change this in settings.
## How much resources does this app consume?
### Windows
According to Task Manager, CPU usage is 0% (not exactly 0%, but definitely low,) and RAM usage starts off at 25MB. Can go up to 50 after a while. 
### Linux
According to htop, CPU usage is 0.0-0.4% (could be more,) and RAM usage is around 30MB.
