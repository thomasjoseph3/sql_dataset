import json

# Load your JSON file
input_file = "ship.json"  # Replace with your file name
output_file = "gpt2_train.txt"

with open(input_file, "r") as f:
    data = json.load(f)

with open(output_file, "w") as f:
    for entry in data:
        prompt = entry["prompt"]
        context = entry.get("context", {})
        query = entry["query"]

        # Flatten context
        context_text = []
        for table, details in context.items():
            columns = ", ".join(details.get("columns", []))
            context_text.append(f"{table} table has columns {columns}.")
        context_text = " ".join(context_text)

        # Combine into plain text
        formatted_example = (
            f"Prompt: {prompt}\n"
            f"Context: {context_text}\n"
            f"Query: {query}\n"
            f"<|endoftext|>\n"
        )
        f.write(formatted_example)

print(f"Preprocessed data saved to {output_file}")
