"""
CPTR 519-A Midterm Code:

@author: Jayson & Tiago
"""

import pymongo
from bson.son import SON


#Connection String
mongo_connection_string = "mongodb://localhost:27017"

# Connect to MongoDB
client = pymongo.MongoClient(mongo_connection_string)
db = client.Bike_Trip_Data
collection = db.Chattanooga_Trip_Data
    
# Query 1: Find the average trip duration for each member type.
pipeline = [
    {
        "$group": {
            "_id": "$properties.memberType",
            "averageTripDuration": {"$avg": "$properties.tripDurationMin"}
        }
    },
    {
        "$project": {
            "_id": 0,
            "memberType": "$_id",
            "averageTripDuration": 1
        }
    },
]

result = list(collection.aggregate(pipeline))

print("Query 1: Average trip duration for each member type:")
for entry in result:
    print(f"""Member Type: {entry['memberType']}
Average Trip Duration: {entry['averageTripDuration']}""")
    print()

# Query 2: Find the top 5 most popular start station names 
# for a specific time interval and list the number of trips.
start_date = "2021-10-22T17:50:00"
end_date = "2021-12-26T17:23:00"

pipeline = [
    {
        "$match": {
            "properties.startTime": {"$gte": start_date, "$lte": end_date}
        }
    },
    {
        "$group": {
            "_id": "$properties.startStationName",
            "totalTrips": {"$sum": 1}
        }
    },
    {
        "$sort": SON([("totalTrips", -1)])
    },
    {
        "$limit": 5
    }
]

results = list(collection.aggregate(pipeline))

print("Query 2: Top 5 most popular start station names from Oct 22 - Dec 26:")
for entry in results:
    print(f"""Start Station Name: {entry['_id']}
Total Trips: {entry['totalTrips']}""")
print()

# Query 3: Find the most popular location for subscribers based on the number of trips
pipeline = [
    {
        "$match": {
            "properties.memberType": "Subscriber"
        }
    },
    {
        "$group": {
            "_id": {
                "startLocation": "$properties.startLocation",
                "endLocation": "$properties.endLocation"
            },
            "totalTrips": {"$sum": 1}
        }
    },
    {
        "$sort": SON([("totalTrips", -1)])
    },
    {
        "$limit": 1
    }
]

result = list(collection.aggregate(pipeline))

print("Query 3:")
if result:
    most_popular_location = result[0]["_id"]
    total_trips = result[0]["totalTrips"]
    print("The most popular location for subscribers is:")
    print(f"Start Location: {most_popular_location['startLocation']}")
    print(f"End Location: {most_popular_location['endLocation']}")
    print(f"Total Trips: {total_trips}")
else:
    print("No data found for subscribers.")
    
#The address for the Location! (Found on: https://www.gps-coordinates.net/)
print("Location: The Tennessee Riverwalk, Riverside Park, Chattanooga, TN 37045, United States of America")
print()

# Query 4: Find bike trips that lasted longer than 30 minutes and
# project the station IDs and trip duration.
pipeline = [
    {
        "$match": {
            "properties.tripDurationMin": {"$gt": 120},
            "properties.memberType": "Dependent"
        }
    },
    {
        "$project": {
            "_id": 0,
            "startStationID": "$properties.startStationID",
            "endStationID": "$properties.endStationID",
          	"tripDurationMin": "$properties.tripDurationMin"
        }
    }
]
results = list(collection.aggregate(pipeline))

print("Query 4: Bike trips for 'dependent' subscribers greater than 2 hours:")

for trip in results:
    print(f"""Start Station ID:{trip['startStationID']}
End Station ID:{trip['endStationID']}
Trip Duration (min):{trip['tripDurationMin']} """)
    print()    

# Query 5: Find the top 6 bike IDs with the most trips
pipeline = [
    {
        "$group": {
            "_id": "$properties.bikeID",
            "totalTrips": {"$sum": 1}
        }
    },
    {
        "$sort": {"totalTrips": -1}
    },
    {
        "$limit": 6
    }
]

result = list(collection.aggregate(pipeline))

print("Query 5: Top 6 bike ids with the most trips.")
for bike in result:
    print(f"Bike ID: {bike['_id']}, Total Trips: {bike['totalTrips']}")
print()

# Query 6: Find the top 5 trip durations and display the member type along with
# start/end station name along with the trip duration.
pipeline = [
    {
        "$sort": {"properties.tripDurationMin": -1}
    },
    {
        "$limit": 5
    },
    {
        "$project": {
            "_id": 0,
            "memberType": "$properties.memberType",
            "startStationName": "$properties.startStationName",
            "endStationName": "$properties.endStationName",
            "tripDurationMin": "$properties.tripDurationMin"
        }
    }
]

result = list(collection.aggregate(pipeline))

print("Query 6: Top 5 trip durations")
for trip in result:
    print(f"""Member: {trip['memberType']},
Start: {trip['startStationName']},
End: {trip['endStationName']},
Trip Duration(min): {trip['tripDurationMin']}""")
    print()    
    
# Close MongoDB connection
client.close()
