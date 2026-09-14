# PA Environmental Explorer
```
PA Environmental Explorer is a Python and PostgreSQL weather data project that collects historical and forecast weather data for Harrisburg, Pennsylvania using the Open-Meteo API.

The project stores hourly weather observations in PostgreSQL, creates daily summaries, and allows users to explore weather statistics through a command-line interface and SQL analysis.
```
## Features
```
- Fetches historical weather data from the Open-Meteo Archive API
- Fetches current forecast data from the Open-Meteo Forecast API
- Stores hourly weather observations in PostgreSQL
- Prevents duplicate observations using unique location and time records
- Updates existing forecast rows when newer forecast data becomes available
- Automatically determines which historical dates are missing before requesting more data
- Creates daily weather summaries
- Provides a command-line interface for exploring weather data
- Includes additional SQL analysis queries and documented findings
```
## Weather Variables Collected
```
The project currently stores:

- Temperature
- Relative humidity
- Precipitation
- Wind speed
- Weather code
- Cloud cover
- Surface pressure
```
## Command-Line Features
```
The current command-line interface allows users to view:

- Maximum temperature
- Minimum temperature
- Wettest month
- Today's hourly forecast
- Today's weather averages
- Windiest month
```
## Analysis

The project also includes SQL queries used to explore weather patterns such as:
```
- Overall weather averages
- Hottest and coldest days
- Monthly average temperature
- Monthly precipitation totals
- Monthly average wind speed
- Daily temperature ranges
- Weather code frequency
- Temperature and humidity correlation
- Wind speed and surface pressure correlation
- Precipitation frequency under high cloud cover
- Pressure differences between calm and windy conditions

Some findings from the analysis include:

- July was the hottest month in the analyzed period
- January was the coldest month
- August had the highest total precipitation
- January had the highest average wind speed
- Higher summer temperatures tended to be associated with lower humidity
- Precipitation occurred much more frequently when cloud cover was at least 70%
```


## Tech Stack
```
- Python
- PostgreSQL
- SQL
- Open-Meteo API
- requests
- psycopg
- tabulate
```
## Project Structure
```
Weather_Project/
│
├── src/
│   ├── main.py
│   ├── database.py
│   └── fetch_weather.py
│
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
│
├── notes/
│   └── finding.md
│
├── requirements.txt
├── README.md
└── .gitignore
```
## Pipeline
```
Open-Meteo API
      ↓
Python data collection
      ↓
PostgreSQL database
      ↓
SQL analysis
      ↓
Command-line interface
```
## Setup
```
1. Clone the repository
    -git clone YOUR_REPOSITORY_URL
    -cd Weather_Project
2. create a postgre SQL data base called weatherdata
3. Create the data base schema
    - sql/schema.sql
4. install dependencies
    -pip install -r requirements.txt
5. configure postgres data base credentials
6. run the program
    -python src/main.py
```

## Data Source
```
Weather data is provided by the Open-Meteo API.

The project uses:

Open-Meteo Forecast API
Open-Meteo Historical Weather API

Weather data is currently collected for Harrisburg, Pennsylvania.
```
## Purpose
```
The purpose of this project is to build an end-to-end environmental data pipeline while practicing real-world data engineering and data analysis skills.

The project demonstrates experience with:

REST APIs
Python
PostgreSQL
SQL
Database design
Data ingestion
Data aggregation
Data analysis
Error handling
Command-line application development
```