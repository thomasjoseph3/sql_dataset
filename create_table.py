import cx_Oracle

# Database connection details
dsn_tns = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
connection = cx_Oracle.connect(user="C##university", password="123", dsn=dsn_tns)
cursor = connection.cursor()

# Drop existing tables in reverse dependency order
drop_table_queries = [
    "DROP TABLE rail_details CASCADE CONSTRAINTS",
    "DROP TABLE wheel_data CASCADE CONSTRAINTS",
    "DROP TABLE recommendation_for_operational_improvements CASCADE CONSTRAINTS",
    "DROP TABLE prediction_for_failures CASCADE CONSTRAINTS",
    "DROP TABLE roi_metrics CASCADE CONSTRAINTS",
    "DROP TABLE predictive_maintenance CASCADE CONSTRAINTS",
    "DROP TABLE predicted_downtime CASCADE CONSTRAINTS",
    "DROP TABLE trolley_alert CASCADE CONSTRAINTS",
    "DROP TABLE vessel_alert CASCADE CONSTRAINTS",
    "DROP TABLE active_alerts CASCADE CONSTRAINTS",
    "DROP TABLE trolley_system_performance CASCADE CONSTRAINTS",
    "DROP TABLE lift_system_performance CASCADE CONSTRAINTS",
    "DROP TABLE component_lifecycle CASCADE CONSTRAINTS",
    "DROP TABLE upcoming_maintenance CASCADE CONSTRAINTS",
    "DROP TABLE transfer_progress CASCADE CONSTRAINTS",
    "DROP TABLE vessel_details CASCADE CONSTRAINTS",
    "DROP TABLE cradle_details CASCADE CONSTRAINTS",
    "DROP TABLE trolley_details CASCADE CONSTRAINTS",
    "DROP TABLE lift_maintenance_tracker CASCADE CONSTRAINTS",
    "DROP TABLE load_distribution CASCADE CONSTRAINTS",
    "DROP TABLE ship_lift_status CASCADE CONSTRAINTS",
    "DROP TABLE operational_status CASCADE CONSTRAINTS",
    "DROP TABLE key_metrics CASCADE CONSTRAINTS"
]

for query in drop_table_queries:
    try:
        cursor.execute(query)
        print(f"Table dropped successfully: {query.split()[2]}")
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code != 942:  # Ignore table not found error
            print(f"Error dropping table: {query.split()[2]} - {error.message}")

# Create tables in dependency order
table_creation_queries = [
    # Independent tables
    """
    CREATE TABLE key_metrics (
        id VARCHAR2(50) PRIMARY KEY,
        operational_trolleys NUMBER,
        ships_in_transfer NUMBER,
        operational_lifts NUMBER
    )
    """,
    """
    CREATE TABLE operational_status (
        id VARCHAR2(50) PRIMARY KEY,
        status_summary VARCHAR2(255),
        CONSTRAINT fk_operational_status_key_metrics FOREIGN KEY (id) REFERENCES key_metrics(id)
    )
    """,
    """
    CREATE TABLE ship_lift_status (
        id VARCHAR2(50),
        lift_name VARCHAR2(100),
        status VARCHAR2(50),
        current_load NUMBER,
        max_capacity NUMBER,
        historical_usage_hours NUMBER,
        PRIMARY KEY (id, lift_name),
        CONSTRAINT fk_ship_lift_key_metrics FOREIGN KEY (id) REFERENCES key_metrics(id)
    )
    """,
    """
    CREATE TABLE load_distribution (
        id VARCHAR2(50),
        lift_name VARCHAR2(100),
        current_load NUMBER,
        max_capacity NUMBER,
        PRIMARY KEY (id, lift_name),
        CONSTRAINT fk_load_distribution_ship_lift FOREIGN KEY (id, lift_name) REFERENCES ship_lift_status(id, lift_name)
    )
    """,
    """
    CREATE TABLE lift_maintenance_tracker (
        id VARCHAR2(50),
        lift_name VARCHAR2(100),
        last_maintenance_date TIMESTAMP,
        next_maintenance_due TIMESTAMP,
        PRIMARY KEY (id, lift_name),
        CONSTRAINT fk_lift_maintenance_ship_lift FOREIGN KEY (id, lift_name) REFERENCES ship_lift_status(id, lift_name)
    )
    """,
    """
    CREATE TABLE trolley_details (
        id VARCHAR2(50) PRIMARY KEY,
        trolley_name VARCHAR2(100) UNIQUE,
        status VARCHAR2(50),
        current_load NUMBER,
        wheel_count NUMBER,
        speed NUMBER,
        max_capacity NUMBER,
        location VARCHAR2(255)
    )
    """,
    """
    CREATE TABLE cradle_details (
        id VARCHAR2(50) PRIMARY KEY,
        cradle_name VARCHAR2(100) UNIQUE,
        status VARCHAR2(50),
        occupancy VARCHAR2(100),
        wear_level VARCHAR2(50),
        current_load NUMBER,
        structural_stress VARCHAR2(50)
    )
    """,
    """
    CREATE TABLE vessel_details (
        id VARCHAR2(50) PRIMARY KEY,
        vessel_name VARCHAR2(100) UNIQUE,
        vessel_type VARCHAR2(50),
        status VARCHAR2(50),
        weight NUMBER,
        length NUMBER,
        width NUMBER,
        owner_company VARCHAR2(100),
        assigned_cradle VARCHAR2(100),
        birthing_area VARCHAR2(100)
    )
    """,
    """
    CREATE TABLE transfer_progress (
        id VARCHAR2(50),
        vessel_name VARCHAR2(100),
        transfer_completed VARCHAR2(50),
        estimated_time_to_destination VARCHAR2(50),
        PRIMARY KEY (id),
        CONSTRAINT fk_transfer_progress_vessel FOREIGN KEY (id) REFERENCES vessel_details(id)
    )
    """,
    """
    CREATE TABLE upcoming_maintenance (
        id VARCHAR2(50),
        next_due_date TIMESTAMP,
        asset_name VARCHAR2(100),
        PRIMARY KEY (id, asset_name)
    )
    """,
    """
    CREATE TABLE component_lifecycle (
        id VARCHAR2(50),
        asset_name VARCHAR2(100),
        remaining_lifespan_hours NUMBER,
        historical_usage_hours NUMBER,
        PRIMARY KEY (id, asset_name)
    )
    """,
    """
    CREATE TABLE lift_system_performance (
        id VARCHAR2(50),
        lift_name VARCHAR2(100),
        average_transfer_time NUMBER,
        utilization_rate NUMBER,
        PRIMARY KEY (id, lift_name)
    )
    """,
    """
    CREATE TABLE trolley_system_performance (
        id VARCHAR2(50),
        trolley_name VARCHAR2(100),
        average_transfer_time NUMBER,
        utilization_rate NUMBER,
        PRIMARY KEY (id, trolley_name)
    )
    """,
    """
    CREATE TABLE active_alerts (
        alert_id VARCHAR2(50) PRIMARY KEY,
        model_id VARCHAR2(50),
        remote_id VARCHAR2(50),
        path VARCHAR2(255),
        name VARCHAR2(100),
        acknowledge NUMBER,
        origin TIMESTAMP,
        message VARCHAR2(500),
        created_at TIMESTAMP,
        updated_at TIMESTAMP
    )
    """,
    """
    CREATE TABLE vessel_alert (
        alert_id VARCHAR2(50) PRIMARY KEY,
        vessel_id VARCHAR2(50),
        alert_type VARCHAR2(100),
        alert_message VARCHAR2(500),
        created_at TIMESTAMP,
        CONSTRAINT fk_vessel_alert_vessel FOREIGN KEY (vessel_id) REFERENCES vessel_details(id)
    )
    """,
    """
    CREATE TABLE trolley_alert (
        alert_id VARCHAR2(50) PRIMARY KEY,
        trolley_id VARCHAR2(50),
        alert_type VARCHAR2(100),
        alert_message VARCHAR2(500),
        created_at TIMESTAMP,
        CONSTRAINT fk_trolley_alert_trolley FOREIGN KEY (trolley_id) REFERENCES trolley_details(id)
    )
    """,
    """
    CREATE TABLE predicted_downtime (
        id VARCHAR2(50) PRIMARY KEY,
        asset_name VARCHAR2(100),
        predicted_downtime_hours NUMBER,
        confidence_level NUMBER,
        prediction_date TIMESTAMP
    )
    """,
    """
    CREATE TABLE predictive_maintenance (
        id VARCHAR2(50) PRIMARY KEY,
        asset_name VARCHAR2(100),
        maintenance_due_date TIMESTAMP,
        predicted_issue VARCHAR2(255),
        confidence_level NUMBER
    )
    """,
    """
    CREATE TABLE roi_metrics (
        id VARCHAR2(50) PRIMARY KEY,
        project_name VARCHAR2(100),
        cost_savings NUMBER,
        revenue_generated NUMBER,
        roi_percentage NUMBER
    )
    """,
    """
    CREATE TABLE prediction_for_failures (
        id VARCHAR2(50) PRIMARY KEY,
        asset_name VARCHAR2(100),
        failure_type VARCHAR2(100),
        confidence_level NUMBER,
        prediction_date TIMESTAMP
    )
    """,
    """
    CREATE TABLE recommendation_for_operational_improvements (
        id VARCHAR2(50) PRIMARY KEY,
        recommendation VARCHAR2(1000),
        asset_name VARCHAR2(100),
        potential_impact VARCHAR2(255),
        created_at TIMESTAMP
    )
    """,
    """
    CREATE TABLE wheel_data (
        id VARCHAR2(50),
        trolley_id VARCHAR2(50),
        wheel_position VARCHAR2(50),
        condition VARCHAR2(50),
        load_carried NUMBER,
        PRIMARY KEY (id, trolley_id, wheel_position),
        CONSTRAINT fk_wheel_data_trolley FOREIGN KEY (trolley_id) REFERENCES trolley_details(id)
    )
    """,
    """
    CREATE TABLE rail_details (
        id VARCHAR2(50) PRIMARY KEY,
        rail_name VARCHAR2(100),
        length NUMBER,
        capacity NUMBER,
        status VARCHAR2(50),
        last_inspection_date TIMESTAMP,
        next_inspection_due TIMESTAMP,
        operational_since TIMESTAMP,
        notes VARCHAR2(255)
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
