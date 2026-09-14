import requests

def get_forecast():
    forecast = requests.get(
        'https://api.open-meteo.com/v1/forecast?latitude=40.2737&longitude=-76.8844&hourly=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m,weather_code,cloud_cover,surface_pressure&timezone=auto&past_days=20&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch',
    )

    forecast_data = forecast.json()

    return forecast_data["hourly"]

def get_history(start_date, end_date):
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": 40.2737,
        "longitude": -76.8844,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "wind_speed_10m",
            "weather_code",
            "cloud_cover",
            "surface_pressure"
        ],
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "timezone": "auto"
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    return response.json()["hourly"]





