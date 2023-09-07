import json

# Define the input and output file paths
input_file_path = "in.txt"
output_file_path = "out.json"

# Read the content of the input text file
with open(input_file_path, "r") as file:
    text = file.read()

# Split the text into lines
lines = text.split('\n')

# Initialize variables to store the data
data = {}
subtopics = []

# Process each line of the text
for line in lines:
    # Use regular expressions to extract topic and description
    if line.startswith("Topic: "):
        data["Topic"] = line.replace("Topic: ", "").strip()
    elif line.startswith("Description: "):
        data["Description"] = line.replace("Description: ", "").strip()
    elif line.strip() != "Subtopics:":
        subtopics.append(line.strip())

# Add the subtopics to the data dictionary
data["Subtopics"] = subtopics

# Convert the data to a JSON string
json_data = json.dumps(data, indent=4)

# Write the JSON data to a file
with open(output_file_path, "w") as json_file:
    json_file.write(json_data)

print(f"JSON data has been generated and written to '{output_file_path}'")
