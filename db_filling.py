
# This program connects to a MySQL database and fills it with realistic sample data about
# ocean environments. It creates information about sensors that measure ocean conditions,
# different ocean zones where marine life lives, pollution levels, satellite observations,
# and records of different sea creatures and where they've been spotted. Before running
# this program, you need to update the database login credentials below, make sure you've
# created the database using the schema file, and install the mysql-connector-python package
# with the command: pip install mysql-connector-python

# Note: This script was generated through the use of an AI tool for time-saving reasons and was recently updated
# corrected, the prompts for that will be posted in an AI transcript

import mysql.connector
from datetime import datetime, timedelta
import random
import sys

def get_db_connection():
    
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="your_username",        # ⚠️ CHANGE THIS
            password="your_password",    # ⚠️ CHANGE THIS
            database="ocean_conservation", # ⚠️ CHANGE THIS if needed
            charset='utf8mb4',
            use_unicode=True
        )
        return conn
    except mysql. connector.Error as err:
        print(f"❌ Error connecting to MySQL: {err}")
        print("\n💡 Make sure to update the credentials in get_db_connection()")
        print("💡 Make sure the database exists (CREATE DATABASE ocean_conservation;)")
        sys.exit(1)

print("="*70)
print("🌊 OCEAN CONSERVATION DATABASE - MOCK DATA POPULATION")
print("="*70)

# Connect to MySQL
print("\n📡 Connecting to MySQL database...")
conn = get_db_connection()
cursor = conn.cursor()
print("✅ Connection successful!")

# Clear existing data (for fresh starts)
print("\n🧹 Clearing existing data...")
cursor.execute('SET FOREIGN_KEY_CHECKS = 0')
tables = ['species_zones', 'sensor_readings', 'pollution_readings', 
          'satellite_observations', 'species', 'habitable_zones', 'sensors']
for table in tables:
    cursor.execute(f'DELETE FROM {table}')
    print(f"   Cleared {table}")
cursor.execute('SET FOREIGN_KEY_CHECKS = 1')
print("✅ All tables cleared")

# ============================================================================
# STEP 1: Create base reference data (sensors, zones)
# ============================================================================

print("\n📍 Creating sensors...")

sensor_locations = [
    'Pacific Ocean - North',
    'Pacific Ocean - South', 
    'Atlantic Ocean - North',
    'Atlantic Ocean - South',
    'Indian Ocean',
    'Mediterranean Sea',
    'Caribbean Sea',
    'Gulf of Mexico',
    'Arctic Ocean',
    'Southern Ocean'
]

sensor_types = ['temperature', 'depth', 'chemical', 'multi-sensor']
sensors_data = []

for i in range(30):
    sensor_id = f"SENSOR-{1000 + i}"
    sensor_name = f"{random.choice(['Buoy', 'Station', 'Probe'])} {random.choice(['Alpha', 'Beta', 'Gamma', 'Delta'])} {i+1}"
    location = random.choice(sensor_locations)
    deployment_date = datetime.now() - timedelta(days=random.randint(30, 1000))
    sensor_type = random.choice(sensor_types)
    latitude = round(random.uniform(-80, 80), 6)
    longitude = round(random.uniform(-180, 180), 6)
    active = random.choice([True, True, True, False])  # 75% active
    
    sensors_data.append((
        sensor_id, sensor_name, location, deployment_date, 
        sensor_type, latitude, longitude, active
    ))

cursor.executemany('''
    INSERT INTO sensors 
    (sensor_id, sensor_name, deployment_location, deployment_date, 
     sensor_type, latitude, longitude, active)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
''', sensors_data)

print(f"✅ Created {len(sensors_data)} sensors")

# ============================================================================
print("\n🗺️  Creating habitable zones...")

zone_names = [
    'Reef Zone Alpha', 'Reef Zone Beta', 'Reef Zone Gamma',
    'Deep Trench Delta', 'Deep Trench Epsilon',
    'Coastal Shelf Omega', 'Coastal Shelf Sigma',
    'Open Water Zone 1', 'Open Water Zone 2', 'Open Water Zone 3',
    'Shallow Bay Area', 'Continental Slope Region',
    'Abyssal Plain Section', 'Seamount Cluster'
]

ocean_names = ['Pacific', 'Atlantic', 'Indian', 'Arctic', 'Southern']
habitable_zones_data = []

for i, zone_name in enumerate(zone_names):
    ocean = random.choice(ocean_names)
    latitude = round(random.uniform(-80, 80), 6)
    longitude = round(random.uniform(-180, 180), 6)
    area_sq_km = round(random.uniform(100, 50000), 2)
    avg_depth = round(random.uniform(10, 4000), 2)
    notes = f"Important biodiversity zone in the {ocean} Ocean"
    
    habitable_zones_data.append((
        zone_name, ocean, latitude, longitude, 
        area_sq_km, avg_depth, notes
    ))

cursor.executemany('''
    INSERT INTO habitable_zones 
    (zone_name, ocean_name, latitude, longitude, 
     area_square_km, avg_depth_meters, notes)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
''', habitable_zones_data)

print(f"✅ Created {len(habitable_zones_data)} habitable zones")

# Get zone IDs for later use
cursor.execute('SELECT zone_id FROM habitable_zones')
zone_ids = [row[0] for row in cursor.fetchall()]

# ============================================================================
# STEP 2: Create time-series and measurement data
# ============================================================================

print("\n🌡️  Creating sensor readings...")

sensor_readings_data = []

# Get list of sensor IDs
cursor.execute('SELECT sensor_id FROM sensors WHERE active = TRUE')
active_sensors = [row[0] for row in cursor.fetchall()]

for sensor_id in active_sensors:
    # Each sensor has 10-50 readings
    num_readings = random.randint(10, 50)
    
    for _ in range(num_readings):
        depth = round(random.uniform(0, 200), 3)
        temperature = round(random.uniform(-2, 30), 3)
        measured_at = datetime.now() - timedelta(
            days=random.randint(0, 365),
            hours=random.randint(0, 23)
        )
        quality_flag = random.choices([0, 1, 2], weights=[85, 10, 5])[0]
        
        sensor_readings_data.append((
            sensor_id, depth, temperature, measured_at, quality_flag
        ))

cursor.executemany('''
    INSERT INTO sensor_readings 
    (sensor_id, depth_meters, temperature_celsius, measured_at, quality_flag)
    VALUES (%s, %s, %s, %s, %s)
''', sensor_readings_data)

print(f"✅ Created {len(sensor_readings_data)} sensor readings")

# ============================================================================
print("\n🛰️  Creating satellite observations...")

satellite_names = [
    'AQUA-SAT-1', 'AQUA-SAT-2',
    'OCEAN-WATCH-1', 'OCEAN-WATCH-2',
    'MARINE-EYE-1', 'MARINE-EYE-2',
    'SEA-MONITOR-1',
    'HYDRO-SAT-1'
]

satellite_observations_data = []

for _ in range(100):
    satellite = random.choice(satellite_names)
    location = random.choice(sensor_locations)
    latitude = round(random.uniform(-80, 80), 6)
    longitude = round(random.uniform(-180, 180), 6)
    surface_temp = round(random.uniform(15, 35), 3)
    observed_at = datetime.now() - timedelta(
        days=random.randint(0, 365),
        hours=random.randint(0, 23)
    )
    
    satellite_observations_data.append((
        satellite, location, latitude, longitude, surface_temp, observed_at
    ))

cursor.executemany('''
    INSERT INTO satellite_observations 
    (satellite_name, observation_location, latitude, longitude, 
     surface_temperature_celsius, observed_at)
    VALUES (%s, %s, %s, %s, %s, %s)
''', satellite_observations_data)

print(f"✅ Created {len(satellite_observations_data)} satellite observations")

# ============================================================================
print("\n🏭 Creating pollution readings...")

pollutant_types = [
    'plastic', 'microplastic', 'oil', 'chemical waste', 
    'industrial runoff', 'agricultural runoff', 'heavy metals'
]

pollution_readings_data = []

for location in sensor_locations:
    # Each location has 5-15 pollution readings
    num_readings = random.randint(5, 15)
    
    for _ in range(num_readings):
        pollutant = random.choice(pollutant_types)
        
        # Generate realistic PPM values (some high, most moderate/low)
        if random.random() < 0.1:  # 10% severe pollution
            ppm = random.randint(1000, 5000)
        elif random.random() < 0.3:  # 30% high pollution
            ppm = random.randint(500, 1000)
        elif random.random() < 0.5:  # 50% moderate pollution
            ppm = random.randint(100, 500)
        else:  # 10% low pollution
            ppm = random.randint(10, 100)
        
        latitude = round(random.uniform(-80, 80), 6)
        longitude = round(random.uniform(-180, 180), 6)
        sample_volume = round(random.uniform(1, 100), 2)
        reading_ts = datetime.now() - timedelta(
            days=random.randint(0, 365),
            hours=random.randint(0, 23)
        )
        source_org = random.choice(['NOAA', 'UNEP', 'The Ocean Cleanup', 'GPML', 'Local Agency'])
        
        pollution_readings_data.append((
            location, latitude, longitude, pollutant, ppm, 
            sample_volume, reading_ts, source_org
        ))

cursor.executemany('''
    INSERT INTO pollution_readings 
    (location, latitude, longitude, pollutant_type, concentration_ppm,
     sample_volume_liters, reading_timestamp, source_organization)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
''', pollution_readings_data)

print(f"✅ Created {len(pollution_readings_data)} pollution readings")

# ============================================================================
# STEP 3: Create species and biodiversity data
# ============================================================================

print("\n🐋 Creating species...")

species_list = [
    ('Blue Whale', 'Balaenoptera musculus', 10000, 15000),
    ('Great White Shark', 'Carcharodon carcharias', 3000, 5000),
    ('Green Sea Turtle', 'Chelonia mydas', 80000, 120000),
    ('Hawksbill Turtle', 'Eretmochelys imbricata', 8000, 15000),
    ('Staghorn Coral', 'Acropora cervicornis', 50000, 100000),
    ('Common Dolphin', 'Delphinus delphis', 6000000, 7000000),
    ('West Indian Manatee', 'Trichechus manatus', 6000, 10000),
    ('Seahorse', 'Hippocampus spp.', 50000, 80000),
    ('Clownfish', 'Amphiprioninae', 500000, 1000000),
    ('Hammerhead Shark', 'Sphyrna spp.', 10000, 25000),
    ('Emperor Penguin', 'Aptenodytes forsteri', 200000, 400000),
    ('Harbor Seal', 'Phoca vitulina', 500000, 600000),
    ('Giant Pacific Octopus', 'Enteroctopus dofleini', 100000, 200000),
    ('Moon Jellyfish', 'Aurelia aurita', 10000000, 50000000),
    ('Common Starfish', 'Asterias rubens', 5000000, 10000000),
    ('Sea Otter', 'Enhydra lutris', 100000, 150000),
    ('Walrus', 'Odobenus rosmarus', 200000, 250000),
    ('Narwhal', 'Monodon monoceros', 75000, 120000),
    ('Beluga Whale', 'Delphinapterus leucas', 150000, 200000),
    ('Vaquita', 'Phocoena sinus', 10, 30),  # Critically endangered
    ('North Atlantic Right Whale', 'Eubalaena glacialis', 300, 400),  # Critically endangered
    ('Bluefin Tuna', 'Thunnus thynnus', 1500, 5000),  # Endangered
]

species_data = []

for common_name, scientific_name, pop_min, pop_max in species_list:
    # Use estimate range for most; exact count for some
    if random.random() < 0.3:
        population_count = random.randint(pop_min, pop_max)
        pop_est_min = None
        pop_est_max = None
    else:
        population_count = None
        pop_est_min = pop_min
        pop_est_max = pop_max
    
    last_survey = datetime.now().date() - timedelta(days=random.randint(30, 730))
    habitat = random.choice([
        'Coastal waters', 'Open ocean', 'Deep sea', 
        'Coral reefs', 'Kelp forests', 'Arctic waters'
    ])
    notes = f"Species found in {habitat}. Population monitoring ongoing."
    
    species_data.append((
        common_name, scientific_name, population_count,
        pop_est_min, pop_est_max, last_survey, habitat, notes
    ))

cursor.executemany('''
    INSERT INTO species 
    (common_name, scientific_name, population_count, 
     population_estimate_min, population_estimate_max, 
     last_survey_date, habitat_description, notes)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
''', species_data)

print(f"✅ Created {len(species_data)} species")

# Get species IDs for junction table
cursor.execute('SELECT species_id FROM species')
species_ids = [row[0] for row in cursor.fetchall()]

# ============================================================================
print("\n🔗 Creating species-zone relationships (many-to-many)...")

species_zones_data = []

# Each species lives in 1-5 zones
for species_id in species_ids:
    num_zones = random.randint(1, min(5, len(zone_ids)))
    selected_zones = random.sample(zone_ids, num_zones)
    
    for zone_id in selected_zones:
        observation_date = datetime.now().date() - timedelta(days=random.randint(0, 365))
        population_in_zone = random.randint(50, 10000) if random.random() < 0.7 else None
        notes = "Observed during regular monitoring" if random.random() < 0.5 else None
        
        species_zones_data.append((
            species_id, zone_id, observation_date, population_in_zone, notes
        ))

cursor.executemany('''
    INSERT INTO species_zones 
    (species_id, zone_id, observation_date, population_in_zone, notes)
    VALUES (%s, %s, %s, %s, %s)
''', species_zones_data)

print(f"✅ Created {len(species_zones_data)} species-zone relationships")

# ============================================================================
# STEP 4: Commit and report
# ============================================================================

print("\n💾 Committing all changes to database...")
conn.commit()

print("\n" + "="*70)
print("✅ DATABASE POPULATION COMPLETE!")
print("="*70)
print(f"\n📊 SUMMARY:")
print(f"   • Sensors: {len(sensors_data)} records")
print(f"   • Sensor Readings: {len(sensor_readings_data)} records")
print(f"   • Habitable Zones: {len(habitable_zones_data)} records")
print(f"   • Satellite Observations: {len(satellite_observations_data)} records")
print(f"   • Pollution Readings: {len(pollution_readings_data)} records")
print(f"   • Species: {len(species_data)} records")
print(f"   • Species-Zone Links: {len(species_zones_data)} records")
print("="*70)

# Close connection
cursor.close()
conn.close()

print("\n🎉 Success! You can now:")
print("   1. View the data in MySQL Workbench (refresh your schema)")
print("   2. Run queries.sql to test the analytical queries")
print("   3. Verify relationships are working correctly")
print("\n💡 Tip: Run 'SELECT COUNT(*) FROM table_name' for each table to verify data.")
