import csv
import cx_Oracle

# Database connection details
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
connection = cx_Oracle.connect(user="ship_maintenance", password="password", dsn=dsn)

try:
    cursor = connection.cursor()

    # Open the CSV file
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            prompt = row["prompt"]
            query = row["query"]
            print(f"Executing query for prompt: {prompt}")
            
            try:
                # Execute the SQL query
                cursor.execute(query)
                results = cursor.fetchall()
                
                # Display results
                print(f"Results for '{prompt}':")
                if results:
                    for result in results:
                        print(result)
                else:
                    print("No data found.")
            except cx_Oracle.DatabaseError as e:
                print(f"Error executing query for '{prompt}': {e}")
            
            print("-" * 50)

except cx_Oracle.DatabaseError as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    connection.close()
