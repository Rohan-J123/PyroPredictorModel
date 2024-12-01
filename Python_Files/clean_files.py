import json

file_paths = ["./Fire_Dataset_19_20/fire_batch_1.geojson",
              "./Fire_Dataset_19_20/fire_batch_2.geojson",
              "./Fire_Dataset_19_20/fire_batch_3.geojson",
              "./Fire_Dataset_19_20/fire_batch_4.geojson",
              "./Fire_Dataset_19_20/fire_batch_5.geojson",
              "./Fire_Dataset_19_20/fire_batch_6.geojson",
              "./Fire_Dataset_19_20/fire_batch_7.geojson",
              "./Fire_Dataset_19_20/fire_batch_8.geojson",
              "./Fire_Dataset_19_20/fire_batch_9.geojson",
              "./Fire_Dataset_19_20/fire_batch_10.geojson",
              "./Fire_Dataset_19_20/fire_batch_11.geojson",
              "./Fire_Dataset_19_20/fire_batch_12.geojson",
              "./Fire_Dataset_19_20/fire_batch_13.geojson",
              "./Fire_Dataset_19_20/fire_batch_14.geojson",
              "./Fire_Dataset_19_20/fire_batch_15.geojson"]

seen_event_ids = set()

# Iterate over each file
for file_path in file_paths:
    with open(file_path, 'r') as file:
        geo_data = json.load(file)

    unique_features = []
    
    # Iterate over each feature and keep only unique eventids
    for feature in geo_data['features']:
        event_id = feature['properties']['severity']
        if event_id not in seen_event_ids:
            unique_features.append(feature)
            seen_event_ids.add(event_id)

    # Update the features with the unique ones
    geo_data['features'] = unique_features

    # Rewrite the file with updated data
    with open(file_path, 'w') as file:
        json.dump(geo_data, file, indent=4)

    print(f"Updated {file_path}: {len(geo_data['features'])} unique features")
