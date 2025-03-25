import requests




def fetch_weather(data):
    params={"q":data,"appid":API_KEY,"units":"metric"}

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def display_weather(city):

    if "error" in city:
        print(f"Error:{city['error']}")
        return
    
    if city.get("cod")!=200:
        print(f"Error:{city.get('message','Invalid city')}")
        return
    

    print(f"\nWeather in {city['name']}:")
    print(f" Temperature: {city['main']['temp']}°C")
    print(f" Condition: {city['weather'][0]['description'].title()}")
    print(f" Wind Speed: {city['wind']['speed']} m/s")
    print(f" Humidity: {city['main']['humidity']}%\n")


    if __name__=="__main__":
        cityname=input("enter city name:")
        weather_data= fetch_weather(city)
        display_weather(weather_data)


    