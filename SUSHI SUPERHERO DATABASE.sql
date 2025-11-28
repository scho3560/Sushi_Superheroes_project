Sushi Super Hero Database
--
CREATE TABLE IF NOT EXISTS pollution_levels (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    area_name VARCHAR(200),
    sensor_id VARCHAR(100),
    reading_ts DATETIME NOT NULL,
    pollutant VARCHAR(50) NOT NULL,
    amount DECIMAL(10,3) NOT NULL,
    unit VARCHAR(20),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    quality_flag SMALLINT DEFAULT 0,
    source VARCHAR(200),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table: pollutants (plastic / environmental metrics)
CREATE TABLE IF NOT EXISTS pollutants (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    pollutant VARCHAR(100) NOT NULL,
    pollution_level VARCHAR(50),
    pollution_level_percentage DECIMAL(5,2),
    avg_plastic_ppm INT,
    goal_ppm INT,
    est_cubic_kilometers_plastic DECIMAL(18,6),
    reading_ts DATETIME NOT NULL
) ENGINE=InnoDB;

-- Table: sensor_readings (general-purpose sensor measurements)
CREATE TABLE IF NOT EXISTS sensor_readings (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    sensor_id VARCHAR(128),
    sensor_location VARCHAR(256),
    sensor_depth_meters DECIMAL(8,3),
    sensor_measurement_temp DECIMAL(8,3),
    measured_at DATETIME NOT NULL
) ENGINE=InnoDB;

-- Table: satellites (satellite observations)
CREATE TABLE IF NOT EXISTS satellites (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    satellite_name VARCHAR(128),
    satellite_location VARCHAR(256),
    satellite_measurement_temp DECIMAL(8,3),
    observed_at DATETIME
) ENGINE=InnoDB;

-- Table: operation_depths (vessel/device depth logs)
CREATE TABLE IF NOT EXISTS operation_depths (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    operation_name VARCHAR(200) NOT NULL,
    device_id VARCHAR(100),
    depth_ts DATETIME NOT NULL,
    depth_meters DECIMAL(8,3) NOT NULL,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table: species (includes at-risk / conservation fields)
CREATE TABLE IF NOT EXISTS species (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    species_name VARCHAR(200) NOT NULL,
    scientific_name VARCHAR(200),
    species_info TEXT,
    risk_level VARCHAR(50),
    habitat VARCHAR(200),
    population_estimate INT,
    last_observed DATETIME,
    conservation_measures TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table: habitable_zones
CREATE TABLE IF NOT EXISTS habitable_zones (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    zone_name VARCHAR(256),
    ocean_location VARCHAR(256),
    habitable BOOLEAN,
    noted_at DATETIME
) ENGINE=InnoDB;

-- Table: environment_data (flexible key/value or JSON blob)
CREATE TABLE IF NOT EXISTS environment_data (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    data_key VARCHAR(256),
    data_value TEXT,
    is_endangered BOOLEAN,
    recorded_at DATETIME
) ENGINE=InnoDB;


