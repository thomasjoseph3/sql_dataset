import re
from wih_context.schemas.schema import schema
def extract_keywords(prompt):
    # Remove punctuation and split into words
    words = re.findall(r'\b\w+\b', prompt.lower())
    
    # Stopwords to exclude common words
    stopwords = {"list", "all", "to", "assigned", "id", "of", "and", "for", "with", "the"}
    return [word for word in words if word not in stopwords]

# Example usage
prompt = "List all employees assigned to task ID 5"
keywords = extract_keywords(prompt)
print("Keywords:", keywords)  # Output: ['employees', 'task']


def find_relevant_tables(keywords, schema):
    relevant_tables = {}
    for table, details in schema.items():
        for keyword in keywords:
            if keyword in table.lower() or any(keyword in column.lower() for column in details["columns"]):
                relevant_tables[table] = details
    return relevant_tables

# Example usage
relevant_tables = find_relevant_tables(keywords, schema)
print("Relevant Tables:", relevant_tables.keys())  # Output: ['employees', 'repair_tasks']


def trace_relationships(relevant_tables, schema):
    related_tables = set(relevant_tables.keys())
    for table, details in relevant_tables.items():
        if "foreign_keys" in details:
            for fk_table in details["foreign_keys"].values():
                if fk_table in schema:
                    related_tables.add(fk_table)
    return related_tables

# Example usage
all_relevant_tables = trace_relationships(relevant_tables, schema)
print("All Relevant Tables:", all_relevant_tables)  # Output: {'employees', 'repair_tasks', 'departments'}


def generate_context(relevant_tables, schema):
    context = {}
    for table in relevant_tables:
        context[table] = {
            "columns": schema[table]["columns"],
            "foreign_keys": schema[table].get("foreign_keys", {})
        }
    return context

# Example usage
context = generate_context(all_relevant_tables, schema)
print("Context:", context)


def process_prompt(prompt, schema):
    # Extract keywords
    keywords = extract_keywords(prompt)
    
    # Find relevant tables
    relevant_tables = find_relevant_tables(keywords, schema)
    
    # Trace relationships
    all_relevant_tables = trace_relationships(relevant_tables, schema)
    
    # Generate context
    context = generate_context(all_relevant_tables, schema)
    return context

# Example prompt
prompt = "List all employees assigned to task ID 5"
context = process_prompt(prompt, schema)
print("Generated Context:", context)


