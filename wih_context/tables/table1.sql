CREATE TABLE ships (
    ship_id NUMBER PRIMARY KEY,
    name VARCHAR2(100),
    owner VARCHAR2(100),
    type VARCHAR2(50),
    build_year NUMBER,
    status VARCHAR2(50)
);

CREATE TABLE repairs (
    repair_id NUMBER PRIMARY KEY,
    ship_id NUMBER REFERENCES ships(ship_id),
    start_date DATE,
    end_date DATE,
    status VARCHAR2(50)
);

CREATE TABLE repair_tasks (
    task_id NUMBER PRIMARY KEY,
    repair_id NUMBER REFERENCES repairs(repair_id),
    task_name VARCHAR2(100),
    description VARCHAR2(500),
    estimated_time NUMBER,
    actual_time NUMBER
);

CREATE TABLE employees (
    employee_id NUMBER PRIMARY KEY,
    first_name VARCHAR2(100),
    last_name VARCHAR2(100),
    department_id NUMBER REFERENCES departments(department_id),
    salary NUMBER,
    availability_status VARCHAR2(50),
    hire_date DATE
);

CREATE TABLE departments (
    department_id NUMBER PRIMARY KEY,
    department_name VARCHAR2(100)
);

CREATE TABLE cradles (
    cradle_id NUMBER PRIMARY KEY,
    ship_id NUMBER REFERENCES ships(ship_id),
    status VARCHAR2(50)
);

CREATE TABLE trolleys (
    trolley_id NUMBER PRIMARY KEY,
    status VARCHAR2(50)
);

CREATE TABLE wheels (
    wheel_id NUMBER PRIMARY KEY,
    trolley_id NUMBER REFERENCES trolleys(trolley_id),
    condition VARCHAR2(50)
);

CREATE TABLE lifts (
    lift_id NUMBER PRIMARY KEY,
    type VARCHAR2(50),
    status VARCHAR2(50),
    capacity NUMBER
);

CREATE TABLE employee_tasks (
    employee_task_id NUMBER PRIMARY KEY,
    employee_id NUMBER REFERENCES employees(employee_id),
    task_id NUMBER REFERENCES repair_tasks(task_id),
    assigned_date DATE
);

CREATE TABLE invoices (
    invoice_id NUMBER PRIMARY KEY,
    repair_id NUMBER REFERENCES repairs(repair_id),
    amount NUMBER,
    issued_date DATE,
    status VARCHAR2(50)
);

CREATE TABLE inspection_records (
    inspection_id NUMBER PRIMARY KEY,
    ship_id NUMBER REFERENCES ships(ship_id),
    inspection_date DATE,
    inspector_id NUMBER REFERENCES employees(employee_id),
    remarks VARCHAR2(500)
);
