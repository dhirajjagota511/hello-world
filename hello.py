import requests

def get_weather():
    city = input("Enter a city: ").strip()
    if not city:
        print("Please enter a valid city name.")
        return

    # Call the weather API
    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Parse the current conditions
        current = data["current_condition"][0]
        temp_c = current["temp_C"]
        temp_f = current["temp_F"]
        desc = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]
        
        print(f"\n--- Current Weather in {city.capitalize()} ---")
        print(f"Condition:   {desc}")
        print(f"Temperature: {temp_c}°C / {temp_f}°F")
        print(f"Humidity:    {humidity}%")
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve weather data: {e}")

get_weather()