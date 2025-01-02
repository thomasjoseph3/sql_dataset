import cx_Oracle

# Database connection details (connect to the new schema)
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
connection = cx_Oracle.connect(user="ship_maintenance", password="password", dsn=dsn)

try:
    
    cursor = connection.cursor()
    # Drop tables if they exist
    cursor.execute("DROP TABLE maintenance_assignments CASCADE CONSTRAINTS")
    cursor.execute("DROP TABLE maintenance_tasks CASCADE CONSTRAINTS")
    cursor.execute("DROP TABLE lifts CASCADE CONSTRAINTS")
    cursor.execute("DROP TABLE trolleys CASCADE CONSTRAINTS")
    cursor.execute("DROP TABLE cradles CASCADE CONSTRAINTS")
    cursor.execute("DROP TABLE ships CASCADE CONSTRAINTS")
    cursor.execute("DROP TABLE employees CASCADE CONSTRAINTS")
    cursor.execute("DROP TABLE departments CASCADE CONSTRAINTS")


# Then proceed with creating tables

    # Create Departments Table
    cursor.execute("""
        CREATE TABLE departments (
            department_id NUMBER PRIMARY KEY,
            department_name VARCHAR2(100) NOT NULL,
            location VARCHAR2(100)
        )
    """)

    # Create Employees Table
    cursor.execute("""
        CREATE TABLE employees (
            employee_id NUMBER PRIMARY KEY,
            first_name VARCHAR2(50),
            last_name VARCHAR2(50),
            department_id NUMBER,
            hire_date DATE,
            job_title VARCHAR2(50),
            salary NUMBER(10, 2),
            availability_status VARCHAR2(20) CHECK (availability_status IN ('Available', 'Unavailable')),
            FOREIGN KEY (department_id) REFERENCES departments(department_id)
        )
    """)

    # Create Ships Table
    cursor.execute("""
        CREATE TABLE ships (
            ship_id NUMBER PRIMARY KEY,
            ship_name VARCHAR2(100),
            type VARCHAR2(50),
            build_year NUMBER(4),
            status VARCHAR2(50)
        )
    """)

    # Create Cradles Table
    cursor.execute("""
        CREATE TABLE cradles (
            cradle_id NUMBER PRIMARY KEY,
            ship_id NUMBER,
            status VARCHAR2(50),
            requires_maintenance VARCHAR2(20) CHECK (requires_maintenance IN ('Yes', 'No')),
            last_inspection_date DATE,
            FOREIGN KEY (ship_id) REFERENCES ships(ship_id)
        )
    """)

    # Create Trolleys Table
    cursor.execute("""
        CREATE TABLE trolleys (
            trolley_id NUMBER PRIMARY KEY,
            ship_id NUMBER,
            status VARCHAR2(50),
            requires_maintenance VARCHAR2(20) CHECK (requires_maintenance IN ('Yes', 'No')),
            last_inspection_date DATE,
            FOREIGN KEY (ship_id) REFERENCES ships(ship_id)
        )
    """)

    # Create Lifts Table
    cursor.execute("""
        CREATE TABLE lifts (
            lift_id NUMBER PRIMARY KEY,
            ship_id NUMBER,
            status VARCHAR2(50),
            requires_maintenance VARCHAR2(20) CHECK (requires_maintenance IN ('Yes', 'No')),
            last_inspection_date DATE,
            FOREIGN KEY (ship_id) REFERENCES ships(ship_id)
        )
    """)

    # Create Maintenance Tasks Table
    cursor.execute("""
        CREATE TABLE maintenance_tasks (
            task_id NUMBER PRIMARY KEY,
            task_name VARCHAR2(100),
            task_type VARCHAR2(50),
            average_time_minutes NUMBER,
            description VARCHAR2(500)
        )
    """)

    # Create Maintenance Assignments Table
    cursor.execute("""
        CREATE TABLE maintenance_assignments (
            assignment_id NUMBER PRIMARY KEY,
            task_id NUMBER,
            employee_id NUMBER,
            start_time DATE,
            end_time DATE,
            FOREIGN KEY (task_id) REFERENCES maintenance_tasks(task_id),
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
        )
    """)

    # Insert Sample Data
    cursor.execute("""
        INSERT INTO departments (department_id, department_name, location)
        VALUES (1, 'Engineering', 'Dockyard A')
    """)
    cursor.execute("""
        INSERT INTO employees (employee_id, first_name, last_name, department_id, hire_date, job_title, salary, availability_status)
        VALUES (1, 'John', 'Doe', 1, TO_DATE('2023-01-15', 'YYYY-MM-DD'), 'Engineer', 75000, 'Available')
    """)
    cursor.execute("""
        INSERT INTO ships (ship_id, ship_name, type, build_year, status)
        VALUES (1, 'Sea Explorer', 'Cargo', 2015, 'In Service')
    """)
    cursor.execute("""
        INSERT INTO cradles (cradle_id, ship_id, status, requires_maintenance, last_inspection_date)
        VALUES (1, 1, 'Operational', 'No', TO_DATE('2024-01-15', 'YYYY-MM-DD'))
    """)
    cursor.execute("""
        INSERT INTO maintenance_tasks (task_id, task_name, task_type, average_time_minutes, description)
        VALUES (1, 'Engine Check', 'Cradle', 120, 'Routine engine maintenance for cradles')
    """)
    cursor.execute("""
        INSERT INTO maintenance_assignments (assignment_id, task_id, employee_id, start_time, end_time)
        VALUES (1, 1, 1, TO_DATE('2024-01-15 08:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2024-01-15 10:00:00', 'YYYY-MM-DD HH24:MI:SS'))
    """)

    # Commit changes
    connection.commit()

    # Query Sample Data
    cursor.execute("""
        SELECT d.department_name, COUNT(e.employee_id) AS available_employees
        FROM employees e
        JOIN departments d ON e.department_id = d.department_id
        WHERE e.availability_status = 'Available'
        GROUP BY d.department_name
    """)
    for row in cursor.fetchall():
        print(f"Department: {row[0]}, Available Employees: {row[1]}")

except cx_Oracle.DatabaseError as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    connection.close()
