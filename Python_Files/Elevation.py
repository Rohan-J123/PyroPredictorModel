import requests
import json

def elevation(LATITUDE, LONGITUDE):
    url = "https://api.open-meteo.com/v1/elevation"

    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        if 'elevation' in data:
            print(f"Elevation: {data['elevation']} meters")
            return data['elevation'][0]
        else:
            print("Elevation data not found in the response.")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

import time
import random

file_paths = [  
                "./Non_Fire_Dataset_Vegetation/non_fire_batch_1.geojson",
                "./Non_Fire_Dataset_Vegetation/non_fire_batch_2.geojson",
                "./Non_Fire_Dataset_Vegetation/non_fire_batch_3.geojson",
                "./Non_Fire_Dataset_Vegetation/non_fire_batch_4.geojson",
                "./Non_Fire_Dataset_Vegetation/non_fire_batch_5.geojson",
                "./Non_Fire_Dataset_Vegetation/non_fire_batch_6.geojson",
                "./Non_Fire_Dataset_Vegetation/non_fire_batch_7.geojson",
                "./Non_Fire_Dataset_Vegetation/non_fire_batch_8.geojson",
                "./Non_Fire_Dataset_Vegetation/non_fire_batch_9.geojson",
                "./Non_Fire_Dataset_Vegetation/non_fire_batch_10.geojson"]

i = 1
for file_path in file_paths:
    with open(file_path, 'r') as file:
        geo_data = json.load(file)
        output_data = []
        for feature in geo_data['features']:
            [LONGITUDE, LATITUDE] = feature['geometry']['coordinates']
            time.sleep(random.uniform(0, 0.5))
            feature["Elevation"] = elevation(LATITUDE, LONGITUDE)
            output_data.append(feature)
        geo_data['features'] = output_data
    with open(f"Non_Fire_Dataset_Elevation/non_fire_batch_{i}.geojson", 'w') as out_file:
          json.dump(geo_data, out_file, indent=4)
    i += 1