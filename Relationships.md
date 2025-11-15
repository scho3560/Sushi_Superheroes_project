Relationships in schema

This document explains likely one-to-many and one-to-one relationships that can be implemented given the current schema in `Data_Dictionary.sql`.

Files considered:
- Data_Dictionary.sql (schema)

Current tables (from Data_Dictionary.sql):
- pollutants (id, pollutant, pollution_level, pollution_level_percentage, avg_plastic_ppm, goal_ppm, est_cubic_kilometers_plastic, reading_ts)
- sensor_readings (id, sensor_id, sensor_location, sensor_depth_meters, sensor_temp_celsius, sensor_measurement_temp, measured_at)
- satellites (id, satellite_name, satellite_location, satellite_measurement_temp, observed_at)
- habitable_zones (id, zone_name, ocean_location, habitable, noted_at)
- environment_data (id, data_key, data_value, is_endangered, recorded_at)
- species (id, species_name, species_info, endangered_status, last_observed)

Recommended / natural relationships

1) One-to-many: sensors -> sensor_readings
   - Rationale: `sensor_readings.sensor_id` is an identifier for a sensor. One sensor will generate many readings over time.
   - Implementation notes:
     - Create a `sensors` table with primary key `sensor_id` (VARCHAR(128)).
     - Add FK constraint on `sensor_readings(sensor_id)` -> `sensors(sensor_id)`.
   - Example SQL:
     ```sql
     CREATE TABLE sensors (
       sensor_id VARCHAR(128) PRIMARY KEY,
       description TEXT
     );

     ALTER TABLE sensor_readings
       ADD CONSTRAINT fk_sensor_readings_sensor
       FOREIGN KEY (sensor_id) REFERENCES sensors(sensor_id);
     ```

2) One-to-many: habitable_zones -> species
   - Rationale: A single habitable zone can contain many species.
   - Implementation notes:
     - Add `zone_id BIGINT` column to `species`, populate it, and add FK to `habitable_zones(id)`.
   - Example SQL:
     ```sql
     ALTER TABLE species ADD COLUMN zone_id BIGINT;
     -- Backfill zone_id values appropriately using your domain rules
     ALTER TABLE species
       ADD CONSTRAINT fk_species_zone
       FOREIGN KEY (zone_id) REFERENCES habitable_zones(id);
     ```

3) One-to-one (optional): pollutants -> environment_data
   - Rationale: If each pollutant has exactly one environment_data metadata row (e.g., canonical volume estimate), you can enforce 1:1 by adding a pollutant_id FK on environment_data and making it UNIQUE.
   - Implementation notes:
     - Add `pollutant_id BIGINT` to `environment_data`, backfill mapping, then add UNIQUE + FK constraints.
   - Example SQL:
     ```sql
     ALTER TABLE environment_data ADD COLUMN pollutant_id BIGINT;
     -- Backfill pollutant_id using domain-specific mapping
     ALTER TABLE environment_data
       ADD CONSTRAINT uq_environment_data_pollutant UNIQUE (pollutant_id);
     ALTER TABLE environment_data
       ADD CONSTRAINT fk_environment_data_pollutant
       FOREIGN KEY (pollutant_id) REFERENCES pollutants(id);
     ```

Checks and migration guidance
- Before adding FK/UNIQUE constraints, run queries to detect violations or missing mappings. Example checks:
  - sensor_readings rows without sensors:
    ```sql
    SELECT DISTINCT sensor_id FROM sensor_readings WHERE sensor_id IS NOT NULL
      AND sensor_id NOT IN (SELECT sensor_id FROM sensors);
    ```
  - species rows without matching zone:
    ```sql
    SELECT s.id FROM species s WHERE s.zone_id IS NULL; -- after adding column
    ```
  - duplicate pollutant mappings in environment_data:
    ```sql
    SELECT pollutant_id, COUNT(*) FROM environment_data GROUP BY pollutant_id HAVING COUNT(*)>1;
    ```

Notes and alternatives
- The current schema is flexible and contains no explicit FK columns; relationships require adding columns or adopting conventions (e.g., store pollutant name in data_key). If you prefer not to change schema, use application-level joins by matching strings (less safe).
- If you want me to implement one of the above relationships (including safe backfill scripts and pre-check queries), tell me which one and I will prepare a migration plan and the exact SQL.

EOF
