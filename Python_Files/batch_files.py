import json
import random
from datetime import datetime, timedelta


file_paths = ["./GDAC_Dataset_Batched/Dataset1.geojson",
              "./GDAC_Dataset_Batched/Dataset2.geojson",
              "./GDAC_Dataset_Batched/Dataset3.geojson",
              "./GDAC_Dataset_Batched/Dataset4.geojson",
              "./GDAC_Dataset_Batched/Dataset5.geojson",
              "./GDAC_Dataset_Batched/Dataset6.geojson",
              "./Fire_Dataset_Batched/fire_batch_1.geojson",
              "./Fire_Dataset_Batched/fire_batch_2.geojson",
              "./Fire_Dataset_Batched/fire_batch_3.geojson",
              "./Fire_Dataset_Batched/fire_batch_4.geojson",
              "./Fire_Dataset_Batched/fire_batch_5.geojson",
              "./Fire_Dataset_Batched/fire_batch_6.geojson",
              "./Fire_Dataset_Batched/fire_batch_7.geojson",]

unique_features = []
batch_size = 200
file_counter = 1

# Iterate over each file
for file_path in file_paths:
    with open(file_path, 'r') as file:
        geo_data = json.load(file)
    
    # Iterate over each feature and keep only unique eventids
    for feature in geo_data['features']:
        temp = {}
        temp['type'] = feature['type']
        temp['geometry'] = feature['geometry']
        temp['properties'] = {}
        temp['properties']['fromdate'] = feature['properties']['fromdate']
        if 'severity' in feature['properties']:
            temp['properties']['severity'] = feature['properties']['severity']
        else:
            temp['properties']['severity'] = feature['properties']['severitydata']['severity']
        unique_features.append(temp)

        if len(unique_features) >= batch_size:
            output_data = {'type': 'FeatureCollection', 'features': unique_features}
            output_file = f"./Non_Fire_Dataset_Combined/non_fire_batch_{file_counter}.geojson"
            with open(output_file, 'w') as out_file:
                json.dump(output_data, out_file, indent=4)
            
            print(f"Updated {output_file}: {len(unique_features)} unique features")
            file_counter += 1
            unique_features = []

# Write any remaining features to the last file
if unique_features:
    output_data = {'type': 'FeatureCollection', 'features': unique_features}
    output_file = f"./Fire_Dataset_Combined/fire_batch_{file_counter}.geojson"
    with open(output_file, 'w') as out_file:
        json.dump(output_data, out_file, indent=4)
    
    print(f"Updated {output_file}: {len(unique_features)} unique features")
