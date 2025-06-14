import requests

def get_weather(city):
    api_key = "https://wttr.in/{}?format=3".format(city)
    try:
        response = requests.get(api_key)
        print(response.text)
    except:
        print("Error fetching weather info")

city = input("Enter city name: ")
get_weather(city)
