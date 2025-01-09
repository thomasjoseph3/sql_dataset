import cx_Oracle

# Database connection details
dsn_tns = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
connection = cx_Oracle.connect(user="C##ship", password="123", dsn=dsn_tns)
cursor = connection.cursor()

# Drop existing tables
drop_table_queries = [
    "DROP TABLE workflows CASCADE CONSTRAINTS",
    "DROP TABLE employee_training CASCADE CONSTRAINTS",
    "DROP TABLE ai_insights CASCADE CONSTRAINTS",
    "DROP TABLE cost_tracking CASCADE CONSTRAINTS",
    "DROP TABLE machinery CASCADE CONSTRAINTS",
    "DROP TABLE sensors CASCADE CONSTRAINTS",
    "DROP TABLE drones CASCADE CONSTRAINTS",
    "DROP TABLE ai_cameras CASCADE CONSTRAINTS",
    "DROP TABLE trolleys CASCADE CONSTRAINTS",
    "DROP TABLE cradles CASCADE CONSTRAINTS",
    "DROP TABLE departments CASCADE CONSTRAINTS",
    "DROP TABLE employees CASCADE CONSTRAINTS",
    "DROP TABLE repair_tasks CASCADE CONSTRAINTS",
    "DROP TABLE repairs CASCADE CONSTRAINTS",
    "DROP TABLE ships CASCADE CONSTRAINTS"
]

for query in drop_table_queries:
    try:
        cursor.execute(query)
        print(f"Table dropped successfully: {query.split()[2]}")
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code != 942:  # Ignore table not found error
            print(f"Error dropping table: {query.split()[2]} - {error.message}")

# List of table creation queries in the correct order
table_creation_queries = [
    # Create independent tables first
    """
    CREATE TABLE ships (
        ship_id NUMBER PRIMARY KEY,
        name VARCHAR2(100),
        owner VARCHAR2(100),
        type VARCHAR2(50),
        build_year NUMBER,
        status VARCHAR2(50),
        location VARCHAR2(100),
        ai_enabled CHAR(5),
        inspection_score NUMBER,
        last_maintenance_date DATE
    )
    """,
    """
    CREATE TABLE employees (
        employee_id NUMBER PRIMARY KEY,
        first_name VARCHAR2(100),
        last_name VARCHAR2(100),
        department_id NUMBER,
        salary NUMBER,
        availability_status VARCHAR2(50),
        hire_date DATE,
        certifications VARCHAR2(200),
        increment_rate NUMBER,
        last_training_date DATE
    )
    """,
    """
    CREATE TABLE departments (
        department_id NUMBER PRIMARY KEY,
        department_name VARCHAR2(100),
        budget NUMBER,
        head_id NUMBER REFERENCES employees(employee_id)
    )
    """,

    # Dependent tables
    """
    CREATE TABLE repairs (
        repair_id NUMBER PRIMARY KEY,
        ship_id NUMBER REFERENCES ships(ship_id),
        start_date DATE,
        end_date DATE,
        status VARCHAR2(50),
        total_cost NUMBER,
        supervisor_id NUMBER REFERENCES employees(employee_id),
        priority_level NUMBER
    )
    """,
    """
    CREATE TABLE repair_tasks (
        task_id NUMBER PRIMARY KEY,
        repair_id NUMBER REFERENCES repairs(repair_id),
        task_name VARCHAR2(100),
        description VARCHAR2(500),
        estimated_time NUMBER,
        actual_time NUMBER,
        cost NUMBER,
        assigned_employee_id NUMBER REFERENCES employees(employee_id),
        status VARCHAR2(50)
    )
    """,
    """
    CREATE TABLE cradles (
        cradle_id NUMBER PRIMARY KEY,
        ship_id NUMBER REFERENCES ships(ship_id),
        status VARCHAR2(50),
        inspection_date DATE,
        repair_cost NUMBER
    )
    """,
    """
    CREATE TABLE trolleys (
        trolley_id NUMBER PRIMARY KEY,
        status VARCHAR2(50),
        last_maintenance_date DATE,
        repair_cost NUMBER
    )
    """,
    """
    CREATE TABLE ai_cameras (
        camera_id NUMBER PRIMARY KEY,
        ship_id NUMBER REFERENCES ships(ship_id),
        location VARCHAR2(100),
        status VARCHAR2(50),
        last_service_date DATE,
        repair_cost NUMBER,
        task_assigned_id NUMBER REFERENCES repair_tasks(task_id)
    )
    """,
    """
    CREATE TABLE drones (
        drone_id NUMBER PRIMARY KEY,
        type VARCHAR2(50),
        status VARCHAR2(50),
        last_service_date DATE,
        battery_status NUMBER,
        repair_cost NUMBER,
        inspection_count NUMBER
    )
    """,
    """
    CREATE TABLE sensors (
        sensor_id NUMBER PRIMARY KEY,
        type VARCHAR2(50),
        ship_id NUMBER REFERENCES ships(ship_id),
        location VARCHAR2(100),
        status VARCHAR2(50),
        data_collected CLOB,
        last_calibration_date DATE
    )
    """,
    """
    CREATE TABLE machinery (
        machinery_id NUMBER PRIMARY KEY,
        name VARCHAR2(100),
        type VARCHAR2(50),
        location VARCHAR2(100),
        status VARCHAR2(50),
        last_service_date DATE,
        repair_cost NUMBER,
        expected_lifetime NUMBER
    )
    """,
    """
    CREATE TABLE cost_tracking (
        cost_id NUMBER PRIMARY KEY,
        type VARCHAR2(50),
        description VARCHAR2(500),
        amount NUMBER,
        cost_date DATE,
        related_id NUMBER,
        related_type VARCHAR2(50)
    )

    """,
    """
    CREATE TABLE ai_insights (
        insight_id NUMBER PRIMARY KEY,
        ship_id NUMBER REFERENCES ships(ship_id),
        generated_date DATE,
        category VARCHAR2(100),
        prediction VARCHAR2(500),
        confidence_score NUMBER
    )
    """,
    """
    CREATE TABLE employee_training (
        training_id NUMBER PRIMARY KEY,
        employee_id NUMBER REFERENCES employees(employee_id),
        training_name VARCHAR2(100),
        certification VARCHAR2(100),
        completion_date DATE
    )
    """,
    """
    CREATE TABLE workflows (
        workflow_id NUMBER PRIMARY KEY,
        repair_id NUMBER REFERENCES repairs(repair_id),
        current_stage VARCHAR2(100),
        next_stage VARCHAR2(100),
        status VARCHAR2(50),
        start_date DATE,
        end_date DATE
    )
    """,
    """
    CREATE TABLE employee_tasks (
        employee_task_id NUMBER PRIMARY KEY,
        employee_id NUMBER REFERENCES employees(employee_id),
        task_id NUMBER,
        assigned_date DATE,
        completion_date DATE
    )
    """,
    """
    CREATE TABLE lifts (
    lift_id NUMBER PRIMARY KEY,
    type VARCHAR2(50),
    status VARCHAR2(50),
    capacity NUMBER,
    last_inspection_date DATE,
    inspection_cost NUMBER
    )
    """
]

# Execute each query
for query in table_creation_queries:
    try:
        cursor.execute(query)
        print(f"Table created successfully: {query.split()[2]}")
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"Error creating table: {query.split()[2]}")
        print(f"Oracle error code: {error.code}")
        print(f"Oracle error message: {error.message}")

# Close the connection
cursor.close()
connection.close()
