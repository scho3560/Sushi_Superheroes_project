SUSHI SUPERHERO DATABASE

CREATE TABLE POLLUTION LEVELS (
  id BIGSERIAL PRIMARY KEY,
  area_name VARCHAR(200) NOT NULL,
  sensor_id VARCHAR(100),
  reading_ts TIMESTAMP NOT NULL,            -- UTC recommended
  pollutant VARCHAR(50) NOT NULL,           -- e.g., PM2.5, PM10, NO2, O3, CO, SO2
  value NUMERIC(8,3) NOT NULL,
  unit VARCHAR(20) NOT NULL,                -- e.g., µg/m3, ppm
  latitude DECIMAL(9,6),
  longitude DECIMAL(9,6),
  quality_flag SMALLINT DEFAULT 0,          -- 0=good,1=suspect,2=invalid
  source VARCHAR(200),                      
  created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE OPERATION DEPTHS (
  id BIGSERIAL PRIMARY KEY,
  operation_name VARCHAR(200) NOT NULL,
  device_id VARCHAR(100),
  depth_ts TIMESTAMP NOT NULL,              -- UTC recommended
  depth_meters NUMERIC(6,2) NOT NULL,
  latitude DECIMAL(9,6),
  longitude DECIMAL(9,6),
  source VARCHAR(200),                      
  created_at TIMESTAMP DEFAULT now()
);