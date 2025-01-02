import cx_Oracle

# Database connection details
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
connection = cx_Oracle.connect(user="ship_maintenance", password="password", dsn=dsn)

try:
    cursor = connection.cursor()

    # Query to list all tables in the current schema
    cursor.execute("SELECT table_name FROM user_tables ORDER BY table_name")
    tables = cursor.fetchall()

    print("Tables in the schema:")
    for table in tables:
        print(table[0])
    print("=" * 50)

    # Query and display data from each table
    for table in tables:
        table_name = table[0]
        print(f"Data from table {table_name}:")
        
        try:
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            
            if rows:
                for row in rows:
                    print(row)
            else:
                print(f"No data found in table {table_name}.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error querying table {table_name}: {e}")
        
        print("-" * 50)

except cx_Oracle.DatabaseError as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    connection.close()
