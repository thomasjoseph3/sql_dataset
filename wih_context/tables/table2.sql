CREATE TABLE vehicles (
    vehicle_id NUMBER PRIMARY KEY,
    name VARCHAR2(100),
    type VARCHAR2(50),
    owner VARCHAR2(100),
    status VARCHAR2(50)
);

CREATE TABLE maintenance_records (
    maintenance_id NUMBER PRIMARY KEY,
    vehicle_id NUMBER REFERENCES vehicles(vehicle_id),
    start_date DATE,
    end_date DATE,
    cost NUMBER,
    status VARCHAR2(50)
);

CREATE TABLE maintenance_tasks (
    task_id NUMBER PRIMARY KEY,
    maintenance_id NUMBER REFERENCES maintenance_records(maintenance_id),
    task_name VARCHAR2(100),
    description VARCHAR2(500),
    estimated_cost NUMBER,
    actual_cost NUMBER
);

CREATE TABLE workers (
    worker_id NUMBER PRIMARY KEY,
    first_name VARCHAR2(100),
    last_name VARCHAR2(100),
    team_id NUMBER REFERENCES teams(team_id),
    salary NUMBER,
    availability_status VARCHAR2(50),
    join_date DATE
);

CREATE TABLE teams (
    team_id NUMBER PRIMARY KEY,
    team_name VARCHAR2(100),
    manager_id NUMBER REFERENCES workers(worker_id)
);

CREATE TABLE equipment (
    equipment_id NUMBER PRIMARY KEY,
    name VARCHAR2(100),
    type VARCHAR2(50),
    status VARCHAR2(50),
    last_serviced_date DATE
);

CREATE TABLE equipment_usage (
    usage_id NUMBER PRIMARY KEY,
    equipment_id NUMBER REFERENCES equipment(equipment_id),
    worker_id NUMBER REFERENCES workers(worker_id),
    start_time DATE,
    end_time DATE,
    purpose VARCHAR2(200)
);

CREATE TABLE spare_parts (
    part_id NUMBER PRIMARY KEY,
    name VARCHAR2(100),
    type VARCHAR2(50),
    quantity NUMBER,
    status VARCHAR2(50)
);

CREATE TABLE equipment_parts (
    id NUMBER PRIMARY KEY,
    equipment_id NUMBER REFERENCES equipment(equipment_id),
    part_id NUMBER REFERENCES spare_parts(part_id),
    quantity_used NUMBER
);

CREATE TABLE maintenance_invoices (
    invoice_id NUMBER PRIMARY KEY,
    maintenance_id NUMBER REFERENCES maintenance_records(maintenance_id),
    amount NUMBER,
    issue_date DATE,
    payment_status VARCHAR2(50)
);

CREATE TABLE safety_audits (
    audit_id NUMBER PRIMARY KEY,
    vehicle_id NUMBER REFERENCES vehicles(vehicle_id),
    audit_date DATE,
    auditor_id NUMBER REFERENCES workers(worker_id),
    remarks VARCHAR2(500)
);

CREATE TABLE project_assignments (
    assignment_id NUMBER PRIMARY KEY,
    project_id NUMBER REFERENCES projects(project_id),
    worker_id NUMBER REFERENCES workers(worker_id),
    assigned_date DATE,
    completion_date DATE,
    status VARCHAR2(50)
);

CREATE TABLE projects (
    project_id NUMBER PRIMARY KEY,
    name VARCHAR2(100),
    start_date DATE,
    end_date DATE,
    status VARCHAR2(50)
);
