import os
import json

# Function to extract the first instance of "name" from JSON data
def extract_first_name(data, results):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "name":
                results.append(value)
                return  # Stop searching after the first instance is found
            elif isinstance(value, (dict, list)):
                extract_first_name(value, results)
    elif isinstance(data, list):
        for item in data:
            extract_first_name(item, results)

# Get the current working directory
folder_path = os.getcwd()

# List to store the found "name" values
found_names = []

# Iterate through files in the current directory
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            extract_first_name(data, found_names)

# Output the found "name" values to a text file
output_file_path = 'found_tag_values.txt'
with open(output_file_path, 'w') as output_file:
    for name in found_names:
        output_file.write(str(name) + '\n')

print(f"Found first names have been saved to {output_file_path}")
