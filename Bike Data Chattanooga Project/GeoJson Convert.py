"""
@author: Jayson & Tiago
"""

import pandas as pd
import json

# Load CSV data into a DataFrame
csv_file = 'Bike_Chattanooga_Trip_Data.csv'  
df = pd.read_csv(csv_file)

# Create a GeoJSON FeatureCollection
features = []
for index, row in df.iterrows():
    # Check for NaN values in 'End Location'
    if pd.notna(row['End Location']):
        # Extracting coordinates from 'End Location' column
        coordinates_str = row['End Location'].replace('POINT (', '').replace(')', '')
        coordinates = list(map(float, coordinates_str.split()))

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": coordinates
            },
            "properties": {
                "memberType": row['Member Type'],
                "bikeID": row['BikeID'],
                "startTime": pd.to_datetime(row['Start Time']).isoformat(),
                "startStationName": row['Start Station Name'],
                "startStationID": row['Start Station ID'],
                "startLocation": row['Start Location'],
                "endTime": pd.to_datetime(row['End Time']).isoformat(),
                "endStationName": row['End Station Name'],
                "endStationID": row['End Station ID'],
                "endLocation": row['End Location'],
                "tripDurationMin": row['TripDurationMin']
            }
        }
        features.append(feature)

geojson_data = {
    "type": "FeatureCollection",
    "features": features
}

# Save GeoJSON to a file
output_file = 'output.geojson'  # Replace with the desired output file path
with open(output_file, 'w') as geojson_file:
    json.dump(geojson_data, geojson_file, indent=2)

print(f"Conversion complete. GeoJSON file saved to {output_file}")