--Average Temperature of Past Month
SELECT AVG(temperature)
FROM weather_observations
WHERE observation_time < CURRENT_DATE and observation_time > (CURRENT_DATE - INTERVAL '1 month');

-- Top 15 windiest days
SELECT
    observation_time::date AS day,
    ROUND(AVG(wind_speed)::numeric, 2) AS avg_wind_speed
FROM weather_observations
GROUP BY observation_time::date
ORDER BY avg_wind_speed DESC
LIMIT(15);

-- Highest surface pressure
SELECT *
FROM weather_observations
ORDER BY surface_pressure DESC
LIMIT (50);

-- Total Averages
SELECT
ROUND(AVG(avg_temperature)::numeric, 2) AS overall_avg_temperature,
ROUND(AVG(avg_humidity)::numeric, 2) AS overall_avg_humidity,
ROUND(AVG(total_precipitation)::numeric, 2) AS avg_daily_precipitation,
ROUND(AVG(avg_wind_speed)::numeric, 2) AS overall_avg_wind_speed,
ROUND(AVG(avg_cloud_cover)::numeric, 2) AS overall_avg_cloud_cover,
ROUND(AVG(avg_surface_pressure)::numeric, 2) AS overall_avg_surface_pressure
 FROM daily_weather_summary;

-- Top 10 Hottest days
SELECT *
FROM daily_weather_summary
ORDER BY avg_temperature DESC
LIMIT (10);

-- Hottest 10 temperatures by the hour
SELECT * 
FROM weather_observations
ORDER BY temperature 
DESC LIMIT (10);

-- Top 10 coldest days
SELECT *
FROM daily_weather_summary
ORDER BY avg_temperature ASC
LIMIT (10);

-- Coldest 10 temperatures by the hour
SELECT * 
FROM weather_observations
ORDER BY temperature 
ASC LIMIT (10);


-- Count amount of each weather code
SELECT weather_code, COUNT(weather_code)
FROM weather_observations 
GROUP BY weather_code
ORDER BY count ASC;

-- Max temperature by day
SELECT DATE(observation_time) AS day, MAX(temperature) AS max_temperature
FROM weather_observations
GROUP BY DATE(observation_time)
ORDER BY day;

-- Highest temperature ranges by day
SELECT 
DATE(observation_time) AS day, 
    MAX(temperature) AS max_temperature, 
    MIN(temperature) AS min_temperature,
    (MAX(temperature) - MIN(temperature)) AS temperature_range
 FROM weather_observations
 GROUP BY DATE(observation_time)
 ORDER BY temperature_range DESC;


-- highest temperature from the summer months
SELECT * FROM weather_observations
WHERE observation_time < '2026-09-01' AND observation_time > '2026-05-31'
ORDER BY temperature DESC;

-- Lowest temperature from the winter months
SELECT * FROM weather_observations
WHERE observation_time >= '2026-01-01' AND observation_time < '2026-04-1'
ORDER BY temperature ASC;

-- correlation exploration
=======================================================================
 -- Correlation between humidty and temperature during summer months
SELECT CORR(temperature, humidity) 
FROM weather_observations
WHERE observation_time < '2026-09-01' AND observation_time > '2026-05-31';

 -- Correlation between temperature and surface pressure during winter months
SELECT CORR(temperature, surface_pressure)
FROM weather_observations
WHERE observation_time >= '2026-01-01' AND observation_time < '2026-04-1';

 -- Correlation between wind speed and surface pressure during winter months
SELECT CORR(wind_speed, surface_pressure)
FROM weather_observations
WHERE observation_time >= '2026-01-01' AND observation_time < '2026-04-1';

 -- Correlation between precipitation and cloud cover during summer months
SELECT CORR(precipitation, cloud_cover) 
FROM weather_observations
WHERE observation_time < '2026-09-01' AND observation_time > '2026-05-31';

 -- Correlation between humidty and preipitation during summer months
SELECT CORR(precipitation, humidity) 
FROM weather_observations
WHERE observation_time < '2026-09-01' AND observation_time > '2026-05-31';

-- Correlation between surface_pressure and cloud_cover during summer months
SELECT CORR(surface_pressure, cloud_cover)
FROM weather_observations
WHERE observation_time < '2026-09-01' AND observation_time > '2026-05-31';

--Correlation between wind_speed and surfrace pressure during summer months
SELECT CORR(wind_speed, surface_pressure)
FROM weather_observations
WHERE observation_time < '2026-09-01' AND observation_time > '2026-05-31';
=======================================================================

-- Average surface pressure on calm days
SELECT AVG(avg_surface_pressure)
FROM daily_weather_summary
WHERE avg_wind_speed < 4;

-- Average surface pressure on windier days
SELECT AVG(avg_surface_pressure)
FROM daily_weather_summary
WHERE avg_wind_speed > 6;

-- Avg precipitation when cloud_coverage > 65
SELECT AVG(precipitation)
FROM weather_observations
WHERE cloud_cover > 65;

-- precipitation % when cloud coverage atleast 70
SELECT 100.0 * COUNT(*) FILTER (WHERE precipitation > 0) / COUNT(*) AS precipitation_percent
FROM weather_observations
WHERE cloud_cover >= 70;

-- Average temperature by month
SELECT DATE_TRUNC('month', observation_time) AS month, ROUND(AVG(temperature)::numeric, 2) AS avg_temperature
FROM weather_observations
GROUP BY DATE_TRUNC('month', observation_time)
ORDER BY month;

-- Total precipitation by month
SELECT DATE_TRUNC('month', observation_time) AS month, SUM(precipitation) AS Total_precipitation
FROM weather_observations
GROUP BY DATE_TRUNC('month', observation_time)
ORDER BY month;

-- Average wind by month
SELECT DATE_TRUNC('month', observation_time) AS month, ROUND(AVG(wind_speed)::numeric, 2) AS avg_wind_speed
FROM weather_observations
GROUP BY DATE_TRUNC('month', observation_time)
ORDER BY month;

SELECT DATE_TRUNC('month', observation_time) AS month, SUM(precipitation) AS Total_precipitation
FROM weather_observations
GROUP BY DATE_TRUNC('month', observation_time)
ORDER BY month DESC
LIMIT 1;