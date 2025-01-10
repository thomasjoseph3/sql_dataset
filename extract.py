import json

# Load the JSON data from a file
with open("sql_dataset/correcteddata/ship3_data_corrected.json", "r") as file:
    data = json.load(file)

# Extract the prompts
if isinstance(data, list):  # If your JSON file contains a list of objects
    prompts = [item["prompt"] for item in data]
else:  # If it's a single object
    prompts = [data["prompt"]]

# Save prompts to another file
with open("prompts.txt", "w") as output_file:
    for prompt in prompts:
        output_file.write(prompt + "\n")

print("Prompts saved to prompts.txt")
