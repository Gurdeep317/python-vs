import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL="https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city):
    if not API_KEY:
        return {"error": "API key not found. Check your .env file."}
    
    params={"q":city,"appid":API_KEY,"units":"metric"}

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def display_weather(data):

    if "error" in data:
        print(f"Error:{data['error']}")
        return
    
    if data.get("cod")!=200:
        print(f"Error:{data.get('message','Invalid city')}")
        return
    

    print(f"\nWeather in {data['name']}:")
    print(f" Temperature: {data['main']['temp']}°C")
    print(f" Condition: {data['weather'][0]['description'].title()}")
    print(f" Wind Speed: {data['wind']['speed']} m/s")
    print(f" Humidity: {data['main']['humidity']}%\n")


if __name__=="__main__":
    cityname=input("enter city name:")
    weather_data= fetch_weather(cityname)
    display_weather(weather_data)


    