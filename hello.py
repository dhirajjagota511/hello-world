import requests

def get_weather_emoji(description):
    description = description.lower()
    if "thunder" in description:
        return "⛈️"
    elif "snow" in description or "blizzard" in description or "ice" in description:
        return "❄️"
    elif "rain" in description or "drizzle" in description or "shower" in description:
        return "🌧️"
    elif "fog" in description or "mist" in description or "haze" in description:
        return "🌫️"
    elif "overcast" in description:
        return "☁️"
    elif "cloud" in description:
        return "⛅"
    elif "sunny" in description or "clear" in description:
        return "☀️"
    else:
        return "🌡️"

def print_emoji_banner(emoji, rows=3, cols=5):
    for _ in range(rows):
        print(emoji * cols)

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
        emoji = get_weather_emoji(description)
        print_emoji_banner(emoji)
        print(f"Weather in {city}: {temp_c}°C, {description}")
    except Exception as e:
        print("Sorry, something went wrong. Please try again.")
        return

get_weather()