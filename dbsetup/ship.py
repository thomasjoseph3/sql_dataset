import cx_Oracle

# Database connection details
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
connection = cx_Oracle.connect(user="ship_maintenance", password="password", dsn=dsn)

try:
    cursor = connection.cursor()

    # Check current data in the ships table
    cursor.execute("SELECT ship_id FROM ships")
    existing_ids = {row[0] for row in cursor.fetchall()}  # Get existing IDs as a set

    # New ships data to insert
    new_ships = [
        (1, 'Sea Explorer', 'Cargo', 2015, 'In Service'),
        (2, 'Ocean Voyager', 'Passenger', 2018, 'Under Maintenance'),
        (3, 'Horizon Carrier', 'Container', 2020, 'In Service'),
        (4, 'Atlantic Mariner', 'Oil Tanker', 2016, 'In Service'),
    ]

    # Filter out ships with duplicate IDs
    filtered_ships = [ship for ship in new_ships if ship[0] not in existing_ids]

    # Insert data into the ships table
    if filtered_ships:
        cursor.executemany("""
            INSERT INTO ships (ship_id, ship_name, type, build_year, status)
            VALUES (:1, :2, :3, :4, :5)
        """, filtered_ships)
        print(f"Inserted {len(filtered_ships)} new ships.")
    else:
        print("No new ships to insert. All IDs already exist.")

    # Commit the changes
    connection.commit()

except cx_Oracle.DatabaseError as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    connection.close()
