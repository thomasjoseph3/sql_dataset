import cx_Oracle

# Database connection details
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
connection = cx_Oracle.connect(user="ship_maintenance", password="password", dsn=dsn)

try:
    cursor = connection.cursor()

    # Check current data in the departments table
    cursor.execute("SELECT department_id FROM departments")
    existing_ids = {row[0] for row in cursor.fetchall()}  # Get existing IDs as a set

    # Departments data to insert
    all_departments = [
        (1, 'Engineering', 'Dockyard A'),
        (2, 'Operations', 'Dockyard B'),
        (3, 'Maintenance', 'Dockyard C'),
        (4, 'Logistics', 'Dockyard D'),
        (5, 'Administration', 'Headquarters')
    ]

    # Filter out departments with duplicate IDs
    new_departments = [dept for dept in all_departments if dept[0] not in existing_ids]

    # Insert data into the departments table
    if new_departments:
        cursor.executemany("""
            INSERT INTO departments (department_id, department_name, location)
            VALUES (:1, :2, :3)
        """, new_departments)
        print(f"Inserted {len(new_departments)} new departments.")
    else:
        print("No new departments to insert. All IDs already exist.")

    # Commit the changes
    connection.commit()

except cx_Oracle.DatabaseError as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    connection.close()
