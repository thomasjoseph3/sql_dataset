import cx_Oracle
import json

# Database connection details
dsn_tns = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
connection = cx_Oracle.connect(user="C##university", password="123", dsn=dsn_tns)

# Load dataset from JSON file
with open("library.json", "r") as file:
    dataset = json.load(file)

# Output files
success_file = "successful_results.txt"
error_file = "error_results.txt"

# Create a cursor
cursor = connection.cursor()

# Open both output files
with open(success_file, "w") as success_outfile, open(error_file, "w") as error_outfile:
    # Iterate through the dataset and execute queries
    for item in dataset:
        prompt = item['prompt']
        query = item["query"].strip().rstrip(';')  # Remove trailing spaces and semicolons

        print(f"Prompt: {prompt}")
        print(f"Processed Query: {query}")

        try:
            # Execute the query
            cursor.execute(query)
            results = cursor.fetchall()  # Fetch all results
            print(f"Number of results: {len(results)}")

            # Write to the success file
            success_outfile.write(f"Prompt: {prompt}\n")
            success_outfile.write(f"Processed Query: {query}\n")
            if results:
                print("Results:")
                for row in results:
                    success_outfile.write(f"{row}\n")
                    print(row)  # Print each row
            else:
                success_outfile.write("No results found.\n")
                print("No results found.")
            success_outfile.write("-" * 40 + "\n")
            print("-" * 40)  # Separator for console output

        except cx_Oracle.DatabaseError as e:
            # Capture and write errors to the error file
            error, = e.args
            error_outfile.write(f"Prompt: {prompt}\n")
            error_outfile.write(f"Processed Query: {query}\n")
            error_outfile.write(f"Oracle error code: {error.code}\n")
            error_outfile.write(f"Oracle error message: {error.message}\n")
            error_outfile.write("-" * 40 + "\n")
            print(f"Oracle error code: {error.code}")
            print(f"Oracle error message: {error.message}")
            print(f"Query causing issue: {query}")
            print("-" * 40)

# Close the connection
cursor.close()
connection.close()

print(f"Successful results saved to {success_file}.")
print(f"Errors saved to {error_file}.")
