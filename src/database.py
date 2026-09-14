import psycopg
from fetch_weather import get_forecast
from fetch_weather import get_history




def insert_data(hourly, update_existing=False):
    connection = None

    try:
        connection = psycopg.connect(
            dbname="weatherdata",
            user="postgres",
            password="YOUR_PASSWORD",
            host="localhost",
            port="5432"
        )

        cursor = connection.cursor()

        if update_existing:
            insert_query = """
                INSERT INTO weather_observations (
                    location_id,
                    observation_time,
                    temperature,
                    humidity,
                    precipitation,
                    wind_speed,
                    weather_code,
                    cloud_cover,
                    surface_pressure
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)

                ON CONFLICT (location_id, observation_time)
                DO UPDATE SET
                    temperature = EXCLUDED.temperature,
                    precipitation = EXCLUDED.precipitation,
                    humidity = EXCLUDED.humidity,
                    wind_speed = EXCLUDED.wind_speed,
                    weather_code = EXCLUDED.weather_code,
                    cloud_cover = EXCLUDED.cloud_cover,
                    surface_pressure = EXCLUDED.surface_pressure
            """
        else:
            insert_query = """
                INSERT INTO weather_observations (
                    location_id,
                    observation_time,
                    temperature,
                    humidity,
                    precipitation,
                    wind_speed,
                    weather_code,
                    cloud_cover,
                    surface_pressure
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)

                ON CONFLICT (location_id, observation_time)
                DO NOTHING
            """

        for i in range(len(hourly["time"])):
            record_to_insert = (
                1,
                hourly["time"][i],
                hourly["temperature_2m"][i],
                hourly["relative_humidity_2m"][i],
                hourly["precipitation"][i],
                hourly["wind_speed_10m"][i],
                hourly["weather_code"][i],
                hourly["cloud_cover"][i],
                hourly["surface_pressure"][i]
            )

            cursor.execute(insert_query, record_to_insert)

        connection.commit()
        cursor.close()

    except Exception as error:
        print(f"Error connecting to database: {error}")

    finally:
        if connection is not None:
            connection.close()

def get_latest_observation_date():
    connection = None

    try:
        connection = psycopg.connect(
            dbname="weatherdata",
            user="postgres",
            password="YOUR_PASSWORD",
            host="localhost",
            port="5432"
        )

        cursor = connection.cursor()

        cursor.execute("""
            SELECT observation_time
            FROM weather_observations
            WHERE observation_time < CURRENT_date AND location_id = 1
            ORDER BY observation_time DESC
            LIMIT 1;
        """)

        latest = cursor.fetchone()[0]

        cursor.close()

        return latest

    except Exception as error:
        print(f"Error getting latest observation date: {error}")
        return None

    finally:
        if connection is not None:
            connection.close()


def get_max_temperature():
    connection = psycopg.connect(
        dbname="weatherdata",
        user="caidengardner",
        password="your_password",
        host="localhost",
        port="5432"
    )

    with connection.cursor() as cursor:
        query = """
            SELECT observation_time, temperature
            FROM weather_observations
            ORDER BY temperature DESC;
        """

        cursor.execute(query)

        result = cursor.fetchall()

    connection.close()

    return result[0]
    
def get_min_temperature():
    connection = psycopg.connect(
        dbname="weatherdata",
        user="caidengardner",
        password="your_password",
        host="localhost",
        port="5432"
    )

    with connection.cursor() as cursor:
        query = """
            SELECT observation_time, temperature
            FROM weather_observations
            ORDER BY temperature ASC;
        """

        cursor.execute(query)

        result = cursor.fetchall()

    connection.close()

    return result[0]
            
def get_wettest_month():
    connection = psycopg.connect(
        dbname="weatherdata",
        user="caidengardner",
        password="your_password",
        host="localhost",
        port="5432"
    )

    with connection.cursor() as cursor:
        query = """
            SELECT DATE_TRUNC('month', observation_time) AS month, SUM(precipitation) AS Total_precipitation
            FROM weather_observations
            GROUP BY DATE_TRUNC('month', observation_time)
            ORDER BY Total_precipitation DESC
            LIMIT 1;
        """

        cursor.execute(query)

        result = cursor.fetchall()

    connection.close()

    return result[0]   

def todays_forecast():
    connection = psycopg.connect(
        dbname="weatherdata",
        user="caidengardner",
        password="your_password",
        host="localhost",
        port="5432"
    )

    with connection.cursor() as cursor:
        query = """
            SELECT * 
            FROM weather_observations 
            WHERE observation_time >= CURRENT_DATE and observation_time < CURRENT_DATE + 1;
        """

        cursor.execute(query)

        result = cursor.fetchall()

    connection.close()

    return result   

def todays_avg():
    connection = psycopg.connect(
        dbname="weatherdata",
        user="caidengardner",
        password="your_password",
        host="localhost",
        port="5432"
    )

    with connection.cursor() as cursor:
        query = """
            SELECT * 
            FROM daily_weather_summary 
            WHERE day = CURRENT_DATE;
        """

        cursor.execute(query)

        result = cursor.fetchall()

    connection.close()

    return result   

def windiest_month():
    connection = psycopg.connect(
        dbname = "weatherdata",
        user="caidengardner",
        password="your_password",
        host="localhost",
        port="5432"
    )

    with connection.cursor() as cursor:
        query = """
            SELECT DATE_TRUNC('month', observation_time) AS month, ROUND(AVG(wind_speed)::numeric, 2) AS avg_wind_speed
            FROM weather_observations
            GROUP BY DATE_TRUNC('month', observation_time)
            ORDER BY avg_wind_speed DESC
            LIMIT 1;
        """
        cursor.execute(query)
        result = cursor.fetchone()
    connection.close()
    return result[0]
