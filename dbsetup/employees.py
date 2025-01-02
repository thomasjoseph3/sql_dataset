import cx_Oracle

# Database connection details
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
connection = cx_Oracle.connect(user="ship_maintenance", password="password", dsn=dsn)

try:
    cursor = connection.cursor()

    # Check current data in the employees table
    cursor.execute("SELECT employee_id FROM employees")
    existing_ids = {row[0] for row in cursor.fetchall()}  # Get existing IDs as a set

    # Employees data to insert
    all_employees =[
        (11, 'Michael', 'Lee', 1, '2022-11-10', 'Junior Engineer', 60000.0, 'Available'),
        (12, 'Isabella', 'White', 2, '2021-07-25', 'Operations Analyst', 55000.0, 'Available'),
        (13, 'Daniel', 'Harris', 3, '2020-03-18', 'Maintenance Tech', 40000.0, 'Unavailable'),
        (14, 'Emily', 'Thompson', 4, '2019-09-05', 'Logistics Planner', 58000.0, 'Available'),
        (15, 'Liam', 'Robinson', 5, '2022-01-20', 'HR Manager', 65000.0, 'Available'),
        (16, 'Noah', 'Lewis', 1, '2020-05-15', 'Engineer', 72000.0, 'Unavailable'),
        (17, 'Charlotte', 'Walker', 2, '2018-08-11', 'Senior Operator', 90000.0, 'Available'),
        (18, 'Lucas', 'Hall', 3, '2021-12-30', 'Maintenance Planner', 48000.0, 'Available'),
        (19, 'Harper', 'Allen', 4, '2023-04-14', 'Logistics Assistant', 46000.0, 'Available'),
        (20, 'Amelia', 'Young', 5, '2023-06-22', 'Admin Coordinator', 51000.0, 'Available'),
    ]

    # Filter out employees with duplicate IDs
    new_employees = [emp for emp in all_employees if emp[0] not in existing_ids]

    # Insert data into the employees table
    if new_employees:
        cursor.executemany("""
            INSERT INTO employees (employee_id, first_name, last_name, department_id, hire_date, job_title, salary, availability_status)
            VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), :6, :7, :8)
        """, new_employees)
        print(f"Inserted {len(new_employees)} new employees.")
    else:
        print("No new employees to insert. All IDs already exist.")

    # Commit the changes
    connection.commit()

except cx_Oracle.DatabaseError as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    connection.close()
