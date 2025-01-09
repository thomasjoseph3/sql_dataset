schema = {
    "ships": {
        "columns": ["ship_id", "name", "owner", "type", "build_year", "status"]
    },
    "repairs": {
        "columns": ["repair_id", "ship_id", "start_date", "end_date", "status"],
        "foreign_keys": {"ship_id": "ships"}
    },
    "repair_tasks": {
        "columns": ["task_id", "repair_id", "task_name", "description", "estimated_time", "actual_time"],
        "foreign_keys": {"repair_id": "repairs"}
    },
    "employees": {
        "columns": ["employee_id", "first_name", "last_name", "department_id", "salary", "availability_status", "hire_date"],
        "foreign_keys": {"department_id": "departments"}
    },
    "departments": {
        "columns": ["department_id", "department_name"]
    },
    "cradles": {
        "columns": ["cradle_id", "ship_id", "status"],
        "foreign_keys": {"ship_id": "ships"}
    },
    "trolleys": {
        "columns": ["trolley_id", "status"]
    },
    "wheels": {
        "columns": ["wheel_id", "trolley_id", "condition"],
        "foreign_keys": {"trolley_id": "trolleys"}
    },
    "lifts": {
        "columns": ["lift_id", "type", "status", "capacity"]
    },
    "employee_tasks": {
        "columns": ["employee_task_id", "employee_id", "task_id", "assigned_date"],
        "foreign_keys": {"employee_id": "employees", "task_id": "repair_tasks"}
    },
    "invoices": {
        "columns": ["invoice_id", "repair_id", "amount", "issued_date", "status"],
        "foreign_keys": {"repair_id": "repairs"}
    },
    "inspection_records": {
        "columns": ["inspection_id", "ship_id", "inspection_date", "inspector_id", "remarks"],
        "foreign_keys": {"ship_id": "ships", "inspector_id": "employees"}
    }
}
