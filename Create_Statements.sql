##Possible CREATE statements for our databases##

CREATE TABLE pollution_levels (
    pollution_Level_Percentage DECIMAL(5,2),         
    avg_Plastic_PPM INT,                             
    goal_PPM INT,                                    
    est_Cubic_Kilometers_Plastic DECIMAL(10,2)  
    %%to be removed Decimal (5,2)     
);

CREATE TABLE depth_and_temp_chart(
    sensor_location VARCHAR(12),
    sensor_depth(meters) Decimal(5,2),
    sensor_temp(F) Decimal(3,1)
);

Create Table satelliate(
    satelliate_location VARCHAR(12),
    measurement(temp) Decimal(5,2),
    
);

CREATE TABLE habitable_zones(
    ocean_location VARCHAR(10),
    habitable(YESorNO) VARCHAR(3),
);

CREATE TABLE environment_data (
    ocean_location VARCHAR(10),
    is_it_endangered(YESorNO) VARCHAR(3),
);

CREATE TABLE species_info(
    species_name VARCHAR(12),
    species_info(endangered_status) VARCHAR(14),
);
