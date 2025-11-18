This is the general information file for the Sushi Superheros Database programming project

Team Name: Sushi SuperHeros
Team Members: Sean, Allison, Tevin, Michael


General Information:
Our Topic: number 14, Life Below Water
Questions to answer:
  -At what depths are human operations (habitation, work, or recreation) considered safe, based on environmental and physiological constraints?
	- Throw people in a body of water experiment?

  -How many species within each body of water are currently classified as threatened or endangered?
	- Could pull from endangered species lists

  -What is the estimated volume (cubic feet or cubic meters) of floating plastic accumulations (“garbage islands”) in each body of water?
	- Drones & Buoy sensors?
  

Project Definition and Topic Selection:
Our project is based on Goal 14 from the United Nations Department of Economic and Social Affairs Sustainable Development, which is "Life Below Water". 
On the UN website, this goal focuses on the plan to 'Conserve and sustainably use the oceans, seas and marine resources for sustainable development'. This topic is important because the ocean and marine life are crucial to the ecosystems on our planet. The ocean itself acts as a necessity for nearly all forms of life, as well as a habitat for so many other forms of life with it. The lives that exist in the water are extremely important, as we utilize them so much in things like food and medicine. Lfie 

Our team has created a handful of questions we will attempt to answer, those questions being:
      
      - What amount of pollution must be removed from each ocean, sea, or river to generate meaningful restoration to underwater ecosystems?
      - At what depths are human operations (habitation, work, or recreation) considered safe, based on environmental and physiological constraints?
      - How many species within each body of water are currently classified as threatened or endangered?
      - What is the estimated volume (cubic feet or cubic meters) of floating plastic accumulations (“garbage islands”) in each body of water?

The data we will use to answer these questions will come from many sources, but some of them can include:
      - Temperature level readings from sensors placed in the ocean at different places
      - Depth test results from sensors
      - Pollution reports from different countries (EEA, UNEP, GPML, The Ocean Cleanup, NOAA, Nexus Plastic, etc.)
      - Animal Data from NOAA, IUCN, CMS, USFWS, and other foreign entities.
      - Government policies regarding conservation

This data will be collected by our team from the related organizations' websites and their own reports on topics related to our project, which we will use to populate our
database tables.


Project Definition Data:
The data for our project will be filed into appropriate SQL database tables, those being:

Tables: 
- Pollution Levels
- Pollutants
- Sensor Reading
- Satellialte
- habitat zone
- environmental data
- species 
- Operation Depths
- At_Risk_Species
- Volunteers

Data:
- average ppm
- pollutant type
- sensors IDs, locations, and temperature readings
- satellite name, location, and temperature measurements
- habitable zones in oceans
- general endangered species information
- estimated cubic meters of plastic 

The data that comes with these zones can be collected at
timestamps that will be included with each entry.

This data can tell us what parts of the ocean need the most attention when it comes to pollution cleaning, as well as what species in that area are endangered or not. 
We can use this data to find out about the temperature at different depths at different locations, to find the best places for possible underwater habitation  


Relationships:
2 relationships

Many-to-Many: species <-> habitable_zones
A species can appear in many zones and a zone can contain many species, which is a 
many-to-many relationship (via a small join table)

One-to-Many: sensors -> sensor_readings
Sensors produce many time-series readings while each reading is tied to a single sensor. 
Giving sensors their own small table for device metadata and having readings reference it keeps the time-series table small and enforces the readings to singular devices. 
This makes device management and metadata queries straightforward without slowing down access.
