import requests
from datetime import datetime

# API URL to fetch the hourly weather forecast for London
API_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'


def get_forecast_data():
    # Fetch forecast data from the API
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return data['list']
    else:
        print("Failed to fetch data from the API.")
        return []


def get_weather_data():
    # Prompt the user to enter the date for which weather data is needed
    date_input = input("Enter the date (YYYY-MM-DD): ")
    date_obj = datetime.strptime(date_input, "%Y-%m-%d")

    # Get the forecast data from the API
    forecast_data = get_forecast_data()
    if forecast_data:
        closest_forecast = min(forecast_data,
                               key=lambda x: abs(date_obj - datetime.strptime(x['dt_txt'], "%Y-%m-%d %H:%M:%S")))
        return closest_forecast['main']['temp']
    else:
        print("Data not found for the given date.")
        return None


def get_wind_speed():
    # Prompt the user to enter the date for which wind speed data is needed
    date_input = input("Enter the date (YYYY-MM-DD): ")
    date_obj = datetime.strptime(date_input, "%Y-%m-%d")

    # Get the forecast data from the API
    forecast_data = get_forecast_data()
    if forecast_data:
        # Find the forecast data closest to the specified date
        closest_forecast = min(forecast_data, key=lambda x: abs(date_obj - datetime.strptime(x['dt_txt'], "%Y-%m-%d %H:%M:%S")))
        return closest_forecast['wind']['speed']
    else:
        print("Data not found for the given date.")
        return None


def get_pressure():
    # Prompt the user to enter the date for which pressure data is needed
    date_input = input("Enter the date (YYYY-MM-DD): ")
    date_obj = datetime.strptime(date_input, "%Y-%m-%d")

    # Get the forecast data from the API
    forecast_data = get_forecast_data()
    if forecast_data:
        # Find the forecast data closest to the specified date
        closest_forecast = min(forecast_data,key=lambda x: abs(date_obj - datetime.strptime(x['dt_txt'], "%Y-%m-%d %H:%M:%S")))
        return closest_forecast['main']['pressure']
    else:
        print("Data not found for the given date.")
        return None


def main():
    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            temp = get_weather_data()
            if temp is not None:
                print(f"The temperature on the specified date is: {temp}°C")
        elif choice == '2':
            wind_speed = get_wind_speed()
            if wind_speed is not None:
                print(f"The wind speed on the specified date is: {wind_speed} m/s")
        elif choice == '3':
            pressure = get_pressure()
            if pressure is not None:
                print(f"The pressure on the specified date is: {pressure} hPa")
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
