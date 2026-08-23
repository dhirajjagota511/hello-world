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
        # wttr.in returns an error message key or lacks current_condition when it fails to find a city
        if "current_condition" not in data:
            print("Please enter a valid city name.")
            return

        current = data["current_condition"][0]
        temp_c = current["temp_C"]
        description = current["weatherDesc"][0]["value"]
        print(f"Weather in {city}: {temp_c}°C, {description}")
    except Exception as e:
        print("Sorry, something went wrong. Please try again.")
        return

get_weather()