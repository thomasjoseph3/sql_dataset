import cx_Oracle

# Database connection details
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
connection = cx_Oracle.connect(user="ship_maintenance", password="password", dsn=dsn)

try:
    cursor = connection.cursor()

    # Helper function to fetch existing IDs from a table
    def fetch_existing_ids(table_name, id_column):
        cursor.execute(f"SELECT {id_column} FROM {table_name}")
        return {row[0] for row in cursor.fetchall()}

    # Insert data into the Cradles table
    existing_cradle_ids = fetch_existing_ids("cradles", "cradle_id")
    cradles = [
        (1, 1, 'Operational', 'No', '2024-01-15'),
        (2, 1, 'Under Repair', 'Yes', '2024-02-10'),
        (3, 2, 'Operational', 'No', '2024-03-05'),
        (4, 3, 'Under Repair', 'Yes', '2024-04-20')
    ]
    new_cradles = [cradle for cradle in cradles if cradle[0] not in existing_cradle_ids]
    if new_cradles:
        cursor.executemany("""
            INSERT INTO cradles (cradle_id, ship_id, status, requires_maintenance, last_inspection_date)
            VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))
        """, new_cradles)

    # Insert data into the Trolleys table
    existing_trolley_ids = fetch_existing_ids("trolleys", "trolley_id")
    trolleys = [
        (1, 1, 'Operational', 'No', '2024-01-10'),
        (2, 2, 'Under Repair', 'Yes', '2024-02-15'),
        (3, 3, 'Operational', 'No', '2024-03-10'),
        (4, 4, 'Under Repair', 'Yes', '2024-04-25')
    ]
    new_trolleys = [trolley for trolley in trolleys if trolley[0] not in existing_trolley_ids]
    if new_trolleys:
        cursor.executemany("""
            INSERT INTO trolleys (trolley_id, ship_id, status, requires_maintenance, last_inspection_date)
            VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))
        """, new_trolleys)

    # Insert data into the Lifts table
    existing_lift_ids = fetch_existing_ids("lifts", "lift_id")
    lifts = [
        (1, 1, 'Operational', 'No', '2024-01-12'),
        (2, 2, 'Under Repair', 'Yes', '2024-02-20'),
        (3, 3, 'Operational', 'No', '2024-03-15'),
        (4, 4, 'Under Repair', 'Yes', '2024-04-30')
    ]
    new_lifts = [lift for lift in lifts if lift[0] not in existing_lift_ids]
    if new_lifts:
        cursor.executemany("""
            INSERT INTO lifts (lift_id, ship_id, status, requires_maintenance, last_inspection_date)
            VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))
        """, new_lifts)

    # Insert data into the Maintenance Tasks table
    existing_task_ids = fetch_existing_ids("maintenance_tasks", "task_id")
    maintenance_tasks = [
        (1, 'Engine Check', 'Cradle', 120, 'Routine engine maintenance'),
        (2, 'Safety Inspection', 'Trolley', 90, 'Monthly safety check'),
        (3, 'Electrical Testing', 'Lift', 180, 'Comprehensive electrical check-up'),
        (4, 'Paint Touch-Up', 'Ship Hull', 240, 'Minor paint maintenance')
    ]
    new_tasks = [task for task in maintenance_tasks if task[0] not in existing_task_ids]
    if new_tasks:
        cursor.executemany("""
            INSERT INTO maintenance_tasks (task_id, task_name, task_type, average_time_minutes, description)
            VALUES (:1, :2, :3, :4, :5)
        """, new_tasks)

    # Insert data into the Maintenance Assignments table
    existing_assignment_ids = fetch_existing_ids("maintenance_assignments", "assignment_id")
    maintenance_assignments = [
        (1, 1, 1, '2024-01-15 09:00:00', '2024-01-15 11:00:00'),
        (2, 2, 2, '2024-02-10 08:30:00', '2024-02-10 10:00:00'),
        (3, 3, 3, '2024-03-05 14:00:00', '2024-03-05 16:30:00'),
        (4, 4, 4, '2024-04-20 10:00:00', '2024-04-20 14:00:00')
    ]
    new_assignments = [assignment for assignment in maintenance_assignments if assignment[0] not in existing_assignment_ids]
    if new_assignments:
        cursor.executemany("""
            INSERT INTO maintenance_assignments (assignment_id, task_id, employee_id, start_time, end_time)
            VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD HH24:MI:SS'), TO_DATE(:5, 'YYYY-MM-DD HH24:MI:SS'))
        """, new_assignments)

    # Commit changes
    connection.commit()
    print("Data inserted successfully.")

except cx_Oracle.DatabaseError as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    connection.close()
