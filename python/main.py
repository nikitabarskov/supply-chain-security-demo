import requests

def fetch_weather(woeid):
    url = f"https://www.metaweather.com/api/location/{woeid}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Failed to fetch weather data. Status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None

def main():
    woeid = 44418  # Example WOEID for London
    weather_data = fetch_weather(woeid)
    if weather_data:
        # Do something with the fetched weather data
        print("Fetched weather data for WOEID", woeid, ":")
        print(weather_data)
    else:
        print("No weather data fetched. Exiting...")

if __name__ == "__main__":
    main()
