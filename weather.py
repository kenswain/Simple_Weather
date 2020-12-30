#!/usr/local/bin/python3

import requests, json

api_key = "9ba6fc1b788596955f9cda5396fb080a"

base_url = "https://api.openweathermap.org/data/2.5/weather?"

city = "4668054"

URL = base_url + "id=" + city + "&appid=" + api_key + "&units=imperial"

response = requests.get(URL)
#print(URL)
if response.status_code == 200:
    data = response.json()
    main = data['main']
    temp = main['temp']
    max = main['temp_max']
    min = main['temp_min']
    feels = main['feels_like']
    humidity =  main['humidity']
    pressure = main['pressure']
    report = data['weather']
    print(f"{city:-^30}")
    print(f"Current Temperature: {temp}")
    print(f"Feels Like: {feels}")
    print(f"Max Temperature: {max}")
    print(f"Current Temperature: {min}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")
else:
    print(f"Error Accessing Site Status code: {response.status_code}")