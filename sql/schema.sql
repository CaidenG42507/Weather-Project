-- View of daily averages
CREATE VIEW daily_weather_summary AS
SELECT
    observation_time::date AS day,
    ROUND(AVG(temperature)::numeric, 2) AS avg_temperature,
    ROUND(AVG(humidity)::numeric, 2) AS avg_humidity,
    ROUND(SUM(precipitation)::numeric, 2) AS total_precipitation,
    ROUND(AVG(wind_speed)::numeric, 2) AS avg_wind_speed,
    ROUND(AVG(cloud_cover)::numeric, 2) AS avg_cloud_cover,
    ROUND(AVG(surface_pressure)::numeric, 2) AS avg_surface_pressure
FROM weather_observations
GROUP BY observation_time::date;