

-- Table: pollutants
CREATE TABLE pollutants (
        id BIGSERIAL PRIMARY KEY,
        pollutant VARCHAR(100) NOT NULL,            -- e.g., 'plastic', 'oil'
        pollution_level VARCHAR(50),                -- level/category
        pollution_level_percentage DECIMAL(5,2),    -- percent (0-100)
        avg_plastic_ppm INTEGER,                    -- average plastic parts per million
        goal_ppm INTEGER,                           -- target ppm
        est_cubic_kilometers_plastic DECIMAL(18,6), -- estimated cubic kilometers of plastic
        reading_ts TIMESTAMPTZ NOT NULL             -- timestamp of the reading (timezone-aware)
);

-- Table: sensor_readings
CREATE TABLE sensor_readings (
        id BIGSERIAL PRIMARY KEY,
        sensor_id VARCHAR(128),                     -- external sensor identifier (if available)
        sensor_location VARCHAR(256),               -- raw location string or geocode
        sensor_depth_meters DECIMAL(8,3),           -- depth in meters
        sensor_temp_celsius DECIMAL(6,3),           -- temperature in °C
        sensor_measurement_temp DECIMAL(6,3),       -- raw measurement value for temperature
        measured_at TIMESTAMPTZ NOT NULL            -- when sensor measurement was taken
);

-- Table: satellites
CREATE TABLE satellites (
        id BIGSERIAL PRIMARY KEY,
        satellite_name VARCHAR(128),                -- satellite name or id (kept generic)
        satellite_location VARCHAR(256),            -- location for satellite reading (e.g., lat/lon or region)
        satellite_measurement_temp DECIMAL(6,3),    -- temperature measurement reported by satellite
        observed_at TIMESTAMPTZ                     -- timestamp of the satellite observation
);

-- Table: habitable_zones
CREATE TABLE habitable_zones (
        id BIGSERIAL PRIMARY KEY,
        zone_name VARCHAR(256),                     -- name or description of the zone
        ocean_location VARCHAR(256),                -- ocean/location description
        habitable BOOLEAN,                          -- true if habitable, false otherwise
        noted_at TIMESTAMPTZ                        -- optional timestamp for when this was recorded
);

-- Table: environment_data
CREATE TABLE environment_data (
        id BIGSERIAL PRIMARY KEY,
        data_key VARCHAR(256),                      -- short key or label for the environment datum
        data_value TEXT,                            -- raw environment data or JSON/text
        is_endangered BOOLEAN,                      -- generic endangered flag (context-dependent)
        recorded_at TIMESTAMPTZ
);

-- Table: species
CREATE TABLE species (
        id BIGSERIAL PRIMARY KEY,
        species_name VARCHAR(256) NOT NULL,
        species_info TEXT,                          -- freeform information about the species
        endangered_status VARCHAR(64),              -- textual status (e.g., 'endangered', 'vulnerable')
        last_observed TIMESTAMPTZ
);
