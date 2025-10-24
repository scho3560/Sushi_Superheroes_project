# MySQL Ocean Environmental Database Population Script
# Compatible with MySQL Workbench 8.0+ and version control (GitHub)
# 
# Installation:
# pip install mysql-connector-python
#
#\
import mysql.connector
from datetime import datetime, timedelta
import random
import sys

def get_db_connection():
    """
    Create and return a MySQL database connection.
    Update these values to match your MySQL Workbench connection settings.
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",        # Usually 'localhost' for MySQL Workbench
            port=3306,               # Default MySQL port
            user="your_username",    # Your MySQL username
            password="your_password", # Your MySQL password
            database="your_database", # Your database name
            charset='utf8mb4',       # UTF-8 encoding for compatibility
            use_unicode=True
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        sys.exit(1)

# STEP 1: Connect to MySQL
print("Connecting to MySQL database...")
conn = get_db_connection()
cursor = conn.cursor()
print("Connection successful!")

# STEP 2: Create all tables (MySQL Workbench compatible)
print("\nCreating tables...")

# Drop tables if they exist (useful for fresh starts)
# Comment out these lines if you want to keep existing data
cursor.execute('SET FOREIGN_KEY_CHECKS = 0')
cursor.execute('DROP TABLE IF EXISTS pollutants')
cursor.execute('DROP TABLE IF EXISTS sensor_readings')
cursor.execute('DROP TABLE IF EXISTS satellites')
cursor.execute('DROP TABLE IF EXISTS habitable_zones')
cursor.execute('DROP TABLE IF EXISTS environment_data')
cursor.execute('DROP TABLE IF EXISTS species')
cursor.execute('SET FOREIGN_KEY_CHECKS = 1')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pollutants (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        pollutant VARCHAR(100) NOT NULL,
        pollution_level VARCHAR(50),
        pollution_level_percentage DECIMAL(5,2),
        avg_plastic_ppm INT,
        goal_ppm INT,
        est_cubic_kilometers_plastic DECIMAL(18,6),
        reading_ts TIMESTAMP NOT NULL,
        INDEX idx_reading_ts (reading_ts),
        INDEX idx_pollution_level (pollution_level)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensor_readings (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        sensor_id VARCHAR(128),
        sensor_location VARCHAR(256),
        sensor_depth_meters DECIMAL(8,3),
        sensor_temp_celsius DECIMAL(6,3),
        sensor_measurement_temp DECIMAL(6,3),
        measured_at TIMESTAMP NOT NULL,
        INDEX idx_measured_at (measured_at),
        INDEX idx_sensor_depth (sensor_depth_meters)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS satellites (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        satellite_name VARCHAR(128),
        satellite_location VARCHAR(256),
        satellite_measurement_temp DECIMAL(6,3),
        observed_at TIMESTAMP,
        INDEX idx_observed_at (observed_at)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS habitable_zones (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        zone_name VARCHAR(256),
        ocean_location VARCHAR(256),
        habitable BOOLEAN,
        noted_at TIMESTAMP,
        INDEX idx_habitable (habitable)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS environment_data (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        data_key VARCHAR(256),
        data_value TEXT,
        is_endangered BOOLEAN,
        recorded_at TIMESTAMP,
        INDEX idx_data_key (data_key),
        INDEX idx_recorded_at (recorded_at)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS species (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        species_name VARCHAR(256) NOT NULL,
        species_info TEXT,
        endangered_status VARCHAR(64),
        last_observed TIMESTAMP,
        INDEX idx_endangered_status (endangered_status)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
''')

print("Tables created successfully!")

# STEP 3: Prepare mock data

# Pollutants data
pollutant_types = ['plastic', 'oil', 'chemical waste', 'microplastics', 'industrial runoff']
pollution_levels = ['low', 'moderate', 'high', 'severe']
pollutants_data = []

for i in range(50):
    pollutant = random.choice(pollutant_types)
    level = random.choice(pollution_levels)
    percentage = round(random.uniform(5.0, 95.0), 2)
    avg_ppm = random.randint(100, 5000)
    goal_ppm = random.randint(50, 500)
    est_plastic = round(random.uniform(0.001, 10.5), 6)
    reading_ts = datetime.now() - timedelta(days=random.randint(0, 365))
    
    pollutants_data.append((pollutant, level, percentage, avg_ppm, goal_ppm, est_plastic, reading_ts))

# Sensor readings data
sensor_locations = ['Pacific Ocean - North', 'Atlantic Ocean - South', 'Indian Ocean', 
                   'Mediterranean Sea', 'Caribbean Sea', 'Gulf of Mexico', 'Arctic Ocean']
sensor_readings_data = []

for i in range(100):
    sensor_id = f"SENSOR-{random.randint(1000, 9999)}"
    location = random.choice(sensor_locations)
    depth = round(random.uniform(5.0, 200.0), 3)
    temp = round(random.uniform(-2.0, 30.0), 3)
    measured_at = datetime.now() - timedelta(days=random.randint(0, 365))
    
    sensor_readings_data.append((sensor_id, location, depth, temp, temp, measured_at))

# Satellites data
satellite_names = ['AQUA-SAT-1', 'OCEAN-WATCH-2', 'MARINE-EYE-3', 'SEA-MONITOR-4', 'HYDRO-SAT-5']
satellites_data = []

for i in range(30):
    sat_name = random.choice(satellite_names)
    location = random.choice(sensor_locations)
    temp = round(random.uniform(15.0, 35.0), 3)
    observed_at = datetime.now() - timedelta(days=random.randint(0, 365))
    
    satellites_data.append((sat_name, location, temp, observed_at))

# Habitable zones data
zone_names = ['Reef Zone Alpha', 'Deep Trench Beta', 'Coastal Shelf Gamma', 
              'Open Water Delta', 'Shallow Bay Epsilon', 'Continental Slope Zeta']
habitable_zones_data = []

for i in range(20):
    zone = random.choice(zone_names)
    location = random.choice(sensor_locations)
    habitable = random.choice([True, True, False])  # More likely to be habitable
    noted_at = datetime.now() - timedelta(days=random.randint(0, 365))
    
    habitable_zones_data.append((zone, location, habitable, noted_at))

# Environment data
env_keys = ['floating_plastic_volume_km3', 'plastic_debris_count', 'oil_slick_area_km2',
            'water_quality_index', 'ph_level', 'dissolved_oxygen_ppm']
environment_data_list = []

for i in range(40):
    key = random.choice(env_keys)
    if 'plastic' in key:
        value = f"{round(random.uniform(0.1, 50.0), 2)} cubic kilometers"
    elif 'count' in key:
        value = str(random.randint(1000, 1000000))
    elif 'area' in key:
        value = f"{round(random.uniform(0.5, 100.0), 2)} km²"
    elif 'ph' in key:
        value = str(round(random.uniform(6.5, 8.5), 2))
    else:
        value = str(round(random.uniform(1.0, 100.0), 2))
    
    is_endangered = random.choice([True, False])
    recorded_at = datetime.now() - timedelta(days=random.randint(0, 365))
    
    environment_data_list.append((key, value, is_endangered, recorded_at))

# Species data
species_names = [
    'Blue Whale', 'Great White Shark', 'Sea Turtle', 'Coral (Staghorn)', 
    'Dolphin', 'Manatee', 'Seahorse', 'Clownfish', 'Hammerhead Shark',
    'Penguin (Emperor)', 'Seal (Harbor)', 'Octopus', 'Jellyfish', 
    'Starfish', 'Sea Otter', 'Walrus', 'Narwhal', 'Beluga Whale'
]
endangered_statuses = ['endangered', 'threatened', 'vulnerable', 'least concern', 'near threatened']
species_data = []

for species_name in species_names:
    location = random.choice(sensor_locations)
    info = f"Found in {location}. Population shows seasonal migration patterns."
    status = random.choice(endangered_statuses)
    last_observed = datetime.now() - timedelta(days=random.randint(0, 180))
    
    species_data.append((species_name, info, status, last_observed))

# STEP 4: Insert all data
print("Inserting pollutants data...")
cursor.executemany(
    'INSERT INTO pollutants (pollutant, pollution_level, pollution_level_percentage, avg_plastic_ppm, goal_ppm, est_cubic_kilometers_plastic, reading_ts) VALUES (%s, %s, %s, %s, %s, %s, %s)',
    pollutants_data
)

print("Inserting sensor readings data...")
cursor.executemany(
    'INSERT INTO sensor_readings (sensor_id, sensor_location, sensor_depth_meters, sensor_temp_celsius, sensor_measurement_temp, measured_at) VALUES (%s, %s, %s, %s, %s, %s)',
    sensor_readings_data
)

print("Inserting satellites data...")
cursor.executemany(
    'INSERT INTO satellites (satellite_name, satellite_location, satellite_measurement_temp, observed_at) VALUES (%s, %s, %s, %s)',
    satellites_data
)

print("Inserting habitable zones data...")
cursor.executemany(
    'INSERT INTO habitable_zones (zone_name, ocean_location, habitable, noted_at) VALUES (%s, %s, %s, %s)',
    habitable_zones_data
)

print("Inserting environment data...")
cursor.executemany(
    'INSERT INTO environment_data (data_key, data_value, is_endangered, recorded_at) VALUES (%s, %s, %s, %s)',
    environment_data_list
)

print("Inserting species data...")
cursor.executemany(
    'INSERT INTO species (species_name, species_info, endangered_status, last_observed) VALUES (%s, %s, %s, %s)',
    species_data
)

# STEP 5: Save changes and close connection
print("\nCommitting changes to database...")
conn.commit()

cursor.close()
conn.close()

print("\n" + "="*50)
print("DATABASE POPULATION COMPLETE!")
print("="*50)
print(f"✓ Pollutants: {len(pollutants_data)} records")
print(f"✓ Sensor Readings: {len(sensor_readings_data)} records")
print(f"✓ Satellites: {len(satellites_data)} records")
print(f"✓ Habitable Zones: {len(habitable_zones_data)} records")
print(f"✓ Environment Data: {len(environment_data_list)} records")
print(f"✓ Species: {len(species_data)} records")
print("="*50)
print("\nYou can now view the data in MySQL Workbench!")
print("Refresh your schema to see the populated tables.")