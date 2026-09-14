from fetch_weather import get_forecast
from fetch_weather import get_history
from tabulate import tabulate
from datetime import date, timedelta
from database import get_latest_observation_date
from database import (
    insert_data,
    get_max_temperature,
    get_min_temperature,
    get_wettest_month,
    todays_forecast,
    todays_avg,
    windiest_month
)

def main():
    latest = get_latest_observation_date()

    if latest is None:
        start_date = date(2026, 1, 1)
    else:
        start_date = latest.date() + timedelta(days=1)

    end_date = date.today() - timedelta(days=1)

    if start_date <= end_date:
        history = get_history(
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d")
        )

        insert_data(history)


    forecast = get_forecast()
    insert_data(forecast, update_existing = True)
    
    while(True):
        decision = input("-------------------- \nWhat would you like to find?\n0. End \n1. Max Temperature \n2. Min Temperature \n3. Wettest Month \n4. Todays Forecast\n5. Windiest Month\n-------------------- \n")
        
        if decision == "0":
            print("\nHave a good day!")
            break
        elif decision == "1":
            day, temp = get_max_temperature()
            print(F"\nMax temperature of the Year: {day.strftime("%B %d, %Y")}: {temp}°F")
        elif decision == "2":
            day, temp = get_min_temperature()
            print(F"\nMin temperature of the Year: {day.strftime("%B %d, %Y")}: {temp}°F")
        elif decision == "3":
            day, amount = get_wettest_month()
            print(F"\nWettest month: {day.strftime("%B %Y")}: Total Precipitation: {amount} Inches")
        elif decision == "4":
            print("Todays Hourly Forecast")
            today = todays_forecast()
            print(tabulate(
                today,
                headers=[
                    "ID", "Location", "Time", "Temperature (°F)",
                    "Precipitation(In)", "Humidity (%)", "Wind Speed(mph)",
                    "Weather Code", "Cloud Cover(%)", "Pressure"
                ],
                tablefmt="grid"
                ))
            print("Todays Averages")
            avg = todays_avg()
            print(tabulate(
                avg,
                headers=[
                    "Date", "Avg_Temperature (°F)", "Avg_Humidity (%)",
                    "Total_Precipitation(In)", "Avg_Wind Speed(mph)",
                    "Weather Code", "Cloud Cover(%)", "Pressure"
                ],
                tablefmt="grid"
            ))
        elif decision == "5":
            month = windiest_month()
            print(F"\nWindest Month: {month.strftime("%B %Y")}")


if __name__ == "__main__":
    main()
 