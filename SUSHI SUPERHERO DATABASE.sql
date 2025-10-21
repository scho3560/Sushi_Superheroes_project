SUSHI SUPERHERO DATABASE

CREATE TABLE POLLUTION_LEVELS (
  id VARCHAR(100) PRIMARY KEY,
  area_name VARCHAR(200) NOT NULL,
  sensor_id VARCHAR(100),
  reading_ts TIMESTAMP NOT NULL,            -- UTC time of reading
  pollutant VARCHAR(50) NOT NULL,           -- found contaminent NO2, O3, CO, SO2
  amount NUMERIC(8,3) NOT NULL,
  unit VARCHAR(20) NOT NULL,                -- e.g., µg/m3, ppm
  latitude DECIMAL(9,6),
  longitude DECIMAL(9,6),
  quality_flag SMALLINT DEFAULT 0,          
  source VARCHAR(200),                      -- Source of the data
  created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE OPERATION_DEPTHS (
  id PRIMARY KEY,
  operation_name VARCHAR(200) NOT NULL,     -- Name of the operation or task
  device_id VARCHAR(100),                   -- Identifier for the vessel or device getting depth
  depth_ts TIMESTAMP NOT NULL,              -- UTC time of depth measurement
  depth_meters NUMERIC(6,2) NOT NULL,
  latitude DECIMAL(9,6),
  longitude DECIMAL(9,6),
  created_at TIMESTAMP DEFAULT now()        -- Timestamp when the record was created  
);

CREATE TABLE AT_RISK_SPECIES (
  id PRIMARY KEY,
  species_name VARCHAR(200) NOT NULL,       -- Common name of the species
  scientific_name VARCHAR(200),              -- Scientific name of the species
  risk_level VARCHAR(50) NOT NULL,          -- e.g., Endangered, Vulnerable
  habitat VARCHAR(200),                      -- Natural habitat of the species
  population_estimate INTEGER,               -- Estimated population count
  last_survey_date DATE,                     -- Date of the last population survey
  conservation_measures TEXT,                -- Description of conservation efforts
  created_at TIMESTAMP DEFAULT now()        -- Timestamp when the record was created  
);

CREATE TABLE VOLUNTEERS (
  id PRIMARY KEY,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(200) UNIQUE NOT NULL,
  phone VARCHAR(20),
  join_date DATE NOT NULL,
  areas_of_interest TEXT,                    -- Areas where the volunteer is interested in working
  availability TEXT,                         -- Volunteer availability details
  created_at TIMESTAMP DEFAULT now()        -- Timestamp when the record was created  
);