import json

file_paths = ["./Fires_Dataset/Fire_Dataset_Cleaned/fire_batch_1.geojson",
              "./Fires_Dataset/Fire_Dataset_Cleaned/fire_batch_2.geojson",
              "./Fires_Dataset/Fire_Dataset_Cleaned/fire_batch_3.geojson",
              "./Fires_Dataset/Fire_Dataset_Cleaned/fire_batch_4.geojson",
              "./Fires_Dataset/Fire_Dataset_Cleaned/fire_batch_5.geojson",
              "./Fires_Dataset/Fire_Dataset_Cleaned/fire_batch_6.geojson",
              "./Fires_Dataset/Fire_Dataset_Cleaned/fire_batch_7.geojson",
              "./Fires_Dataset/Fire_Dataset_Cleaned/fire_batch_8.geojson",
              "./Fires_Dataset/Fire_Dataset_Cleaned/fire_batch_9.geojson",
              "./Fires_Dataset/Fire_Dataset_Cleaned/fire_batch_10.geojson"]

all_event_ids = set()
sum = 0

# Iterate over each file to extract and combine event_ids
for file_path in file_paths:
    with open(file_path, 'r') as file:
        geo_data = json.load(file)

    # Extract eventid values from the current file and add to the combined set
    event_ids = {feature['severity'] for feature in geo_data['features']}
    sum += len([x for x in geo_data['features']])
    all_event_ids.update(event_ids)

    print(len(event_ids))

print(sum)
print(len(all_event_ids))
if len(all_event_ids) == sum:
    print("All files have different entries.")
else:
    print("Files have duplicate entries.")
