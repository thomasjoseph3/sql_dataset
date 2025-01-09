import json
import re

# Snake_case to camelCase conversion function
def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Schema mapping from snake_case to camelCase
schema_mapping = {
    "members": {
        "member_id": "memberId",
        "first_name": "firstName",
        "last_name": "lastName",
        "email": "email",
        "phone": "phone",
        "address": "address",
        "join_date": "joinDate",
        "membership_status": "membershipStatus"
    },
    "books": {
        "book_id": "bookId",
        "title": "title",
        "author": "author",
        "genre": "genre",
        "publisher": "publisher",
        "publication_year": "publicationYear",
        "isbn": "isbn",
        "total_copies": "totalCopies",
        "available_copies": "availableCopies"
    },
    "borrowed_books": {
        "borrow_id": "borrowId",
        "member_id": "memberId",
        "book_id": "bookId",
        "borrow_date": "borrowDate",
        "due_date": "dueDate",
        "return_date": "returnDate",
        "fine_amount": "fineAmount"
    },
    "reservations": {
        "reservation_id": "reservationId",
        "member_id": "memberId",
        "book_id": "bookId",
        "reservation_date": "reservationDate",
        "status": "status"
    },
    "staff": {
        "staff_id": "staffId",
        "first_name": "firstName",
        "last_name": "lastName",
        "email": "email",
        "phone": "phone",
        "hire_date": "hireDate",
        "role": "role"
    },
    "publishers": {
        "publisher_id": "publisherId",
        "publisher_name": "publisherName",
        "contact_email": "contactEmail",
        "contact_phone": "contactPhone",
        "address": "address"
    }
}

# Replace all snake_case fields in text with camelCase and fix quotes
def replace_snake_with_camel(text, schema):
    for table, fields in schema.items():
        for snake, camel in fields.items():
            text = re.sub(r'\b' + re.escape(snake) + r'\b', f'"{camel}"', text)
    return text.replace('""', '"')

# Update the context, prompt, and queries to camelCase with proper quoting
def update_entry(entry, schema):
    # Update context
    if "context" in entry:
        for table, details in entry["context"].items():
            if table in schema:
                entry["context"][table]["columns"] = [
                    schema[table].get(column, column) for column in details.get("columns", [])
                ]
    # Update query
    if "query" in entry:
        entry["query"] = replace_snake_with_camel(entry["query"], schema)

    return entry

# Load the JSON file
input_file = "datasets/camel_case/library_oracle_camel_case.json"
output_file = "datasets/camel_case/library_oracle_camel_case_fixed.json"

with open(input_file, 'r') as file:
    data = json.load(file)

# Process each entry in the dataset
updated_data = [update_entry(entry, schema_mapping) for entry in data]

# Save the updated JSON file
with open(output_file, 'w') as file:
    json.dump(updated_data, file, indent=4)

print(f"Updated JSON file saved to {output_file}")
