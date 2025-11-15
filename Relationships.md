2 relationships

1) Many-to-Many: species <-> habitable_zones
-------------------------------------------------
A species can appear in many zones and a zone can contain many species. Modeling that as a many-to-many relationship (via a small join table) avoids duplication and keeps the core `species` and `habitable_zones` records clean. The join rows can hold context such as first-observed dates without bloating either main table.

2) One-to-Many: sensors -> sensor_readings
-------------------------------------------------
Sensors produce many time-series readings while each reading is tied to a single sensor. Giving sensors their own small table for device metadata and having readings reference it keeps the time-series table compact and enforces that readings link to valid devices. This makes device management and metadata queries straightforward without slowing down time-series access.
