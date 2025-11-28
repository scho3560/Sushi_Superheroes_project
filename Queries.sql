
-- Queries for the questions in our project definition 
-- ============================================================================
-- Query 1: High pollution areas
-- ============================================================================
SELECT 
    location,
    pollutant_type,
    concentration_ppm,
    reading_timestamp
FROM pollution_readings
WHERE concentration_ppm >= 500
ORDER BY concentration_ppm DESC;

-- ============================================================================
-- Query 2: Pollution cleanup needed (Question 1)
-- ============================================================================
SELECT 
    location,
    pollutant_type,
    AVG(concentration_ppm) AS current_ppm,
    100 AS goal_ppm,
    AVG(concentration_ppm) - 100 AS removal_needed_ppm
FROM pollution_readings
WHERE reading_timestamp >= '2024-01-01'
GROUP BY location, pollutant_type
HAVING removal_needed_ppm > 0
ORDER BY removal_needed_ppm DESC;

-- ============================================================================
-- Query 3: Safe diving depths (Question 2)
-- ============================================================================
SELECT 
    s.deployment_location,
    sr.depth_meters,
    sr.temperature_celsius,
    sr.measured_at
FROM sensor_readings sr
JOIN sensors s ON sr.sensor_id = s.sensor_id
WHERE sr.depth_meters <= 40
    AND sr.temperature_celsius BETWEEN 10 AND 25
    AND sr.measured_at >= '2024-01-01'
ORDER BY sr.depth_meters;

-- ============================================================================
-- Query 4: Safe locations summary (Question 2)
-- ============================================================================
SELECT 
    s.deployment_location,
    AVG(sr.depth_meters) AS avg_depth,
    AVG(sr.temperature_celsius) AS avg_temp,
    COUNT(*) AS reading_count
FROM sensors s
JOIN sensor_readings sr ON s.sensor_id = sr.sensor_id
WHERE s.active = 1
    AND sr.measured_at >= '2024-01-01'
GROUP BY s.deployment_location
HAVING avg_depth <= 100
ORDER BY avg_depth;

-- ============================================================================
-- Query 5: Endangered species count by ocean (Question 3)
-- ============================================================================
SELECT 
    hz.ocean_name,
    COUNT(DISTINCT s.species_id) AS total_species,
    COUNT(DISTINCT CASE WHEN s.population_count < 500 THEN s.species_id END) AS endangered_species
FROM habitable_zones hz
LEFT JOIN species_zones sz ON hz.zone_id = sz.zone_id
LEFT JOIN species s ON sz.species_id = s.species_id
GROUP BY hz.ocean_name
ORDER BY endangered_species DESC;

-- ============================================================================
-- Query 6: Endangered species details (Question 3)
-- ============================================================================
SELECT 
    hz.ocean_name,
    s.common_name,
    s.population_count,
    sz.observation_date
FROM habitable_zones hz
JOIN species_zones sz ON hz.zone_id = sz.zone_id
JOIN species s ON sz.species_id = s.species_id
WHERE s.population_count < 5000
ORDER BY s.population_count;

-- ============================================================================
-- Query 7: Critical protection zones (Question 3)
-- ============================================================================
SELECT 
    hz.zone_name,
    hz.ocean_name,
    COUNT(DISTINCT s.species_id) AS species_count,
    COUNT(DISTINCT CASE WHEN s.population_count < 500 THEN s.species_id END) AS endangered_count
FROM habitable_zones hz
LEFT JOIN species_zones sz ON hz.zone_id = sz.zone_id
LEFT JOIN species s ON sz.species_id = s.species_id
GROUP BY hz.zone_name, hz.ocean_name
HAVING endangered_count > 0
ORDER BY endangered_count DESC;

-- ============================================================================
-- Query 8: Plastic pollution by location (Question 4)
-- ============================================================================
SELECT 
    location,
    AVG(concentration_ppm) AS avg_plastic_ppm,
    MAX(concentration_ppm) AS max_plastic_ppm,
    COUNT(*) AS sample_count
FROM pollution_readings
WHERE pollutant_type IN ('plastic', 'microplastic')
    AND reading_timestamp >= '2024-01-01'
GROUP BY location
ORDER BY avg_plastic_ppm DESC;

-- ============================================================================
-- Query 9: Plastic pollution by ocean (Question 4)
-- ============================================================================
SELECT 
    CASE 
        WHEN location LIKE '%Pacific%' THEN 'Pacific Ocean'
        WHEN location LIKE '%Atlantic%' THEN 'Atlantic Ocean'
        WHEN location LIKE '%Indian%' THEN 'Indian Ocean'
        WHEN location LIKE '%Arctic%' THEN 'Arctic Ocean'
        ELSE 'Other'
    END AS ocean,
    COUNT(*) AS samples,
    AVG(concentration_ppm) AS avg_plastic_ppm
FROM pollution_readings
WHERE pollutant_type IN ('plastic', 'microplastic')
    AND reading_timestamp >= '2024-01-01'
GROUP BY ocean
ORDER BY avg_plastic_ppm DESC;

-- ============================================================================
-- Query 10: Volunteer activity (Bonus)
-- ============================================================================
SELECT 
    v.first_name,
    v.last_name,
    COUNT(va.activity_id) AS activities,
    SUM(va.hours_contributed) AS total_hours
FROM volunteers v
LEFT JOIN volunteer_activities va ON v.volunteer_id = va.volunteer_id
GROUP BY v.volunteer_id, v.first_name, v.last_name
ORDER BY total_hours DESC;


