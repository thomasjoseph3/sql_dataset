from rapidfuzz import fuzz, process
import inflect

inflect_engine = inflect.engine()

# Define stop words to exclude
STOP_WORDS = {
    "is", "as", "list", "all", "get", "retrieve", "find", "to", "for", "on", "by", "in", "and", "of", "the", "from", "assigned"
}

# Helper function to generate singular/plural variations
def generate_variations(word):
    return {word, inflect_engine.singular_noun(word) or word, inflect_engine.plural(word)}

# Main function to find relevant tables
def find_relevant_tables(prompt, schema):
    import re

    # Preprocess the prompt and filter stop words
    prompt_words = [word for word in re.findall(r'\w+', prompt.lower()) if word not in STOP_WORDS]

    # Create a mapping of table and column names with variations
    table_map = {}
    column_map = {}
    for table, details in schema.items():
        for variation in generate_variations(table.lower()):
            table_map[variation] = table
        for column in details.get("columns", []):
            for variation in generate_variations(column.lower()):
                column_map[variation] = table

    # Perform fuzzy matching to find matching tables and columns
    matched_tables = set()
    for word in prompt_words:
        # Match tables
        table_match = process.extractOne(word, table_map.keys(), scorer=fuzz.token_set_ratio)
        if table_match and table_match[1] > 60:  # Threshold for matching
            matched_tables.add(table_map[table_match[0]])

        # Match columns
        column_match = process.extractOne(word, column_map.keys(), scorer=fuzz.token_set_ratio)
        if column_match and column_match[1] > 60:  # Threshold for matching
            matched_tables.add(column_map[column_match[0]])

    # Traverse relationships to include all related tables
    relevant_tables = set(matched_tables)
    for table in matched_tables:
        traverse_relationships(table, schema, relevant_tables)

    return relevant_tables

# Recursive function to find related tables
def traverse_relationships(table, schema, relevant_tables):
    if table not in schema:
        return
    foreign_keys = schema[table].get("foreign_keys", {})
    for related_table in foreign_keys.values():
        if related_table not in relevant_tables:
            relevant_tables.add(related_table)
            traverse_relationships(related_table, schema, relevant_tables)


from schemas.schema import schema

# Test the function
prompt = "List all employees assigned to task ID 5"
relevant_tables = find_relevant_tables(prompt, schema)
print(relevant_tables)
