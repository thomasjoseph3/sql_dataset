import json

# Load the original JSON data
with open("library.json", "r") as json_file:
    original_data = json.load(json_file)

# Load the error prompts from the error_results.txt file
with open("error_results.txt", "r") as error_file:
    error_prompts = [line.replace("Prompt: ", "").strip()
                     for line in error_file if line.startswith("Prompt: ")]

# Separate the matching and non-matching JSON objects
matching_data = [item for item in original_data if item["prompt"] in error_prompts]
remaining_data = [item for item in original_data if item["prompt"] not in error_prompts]

# Save the matching data to a new JSON file for fixing
with open("matched_errors.json", "w") as matched_file:
    json.dump(matching_data, matched_file, indent=4)

# Save the remaining data back to a new JSON file
with open("remaining_data.json", "w") as remaining_file:
    json.dump(remaining_data, remaining_file, indent=4)

print("Matched errors saved to 'matched_errors.json'.")
print("Remaining data saved to 'remaining_data.json'.")
