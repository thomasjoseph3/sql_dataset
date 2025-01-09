{
    "vehicles": {
        "columns": ["vehicle_id", "name", "type", "owner", "status"]
    },
    "maintenance_records": {
        "columns": ["maintenance_id", "vehicle_id", "start_date", "end_date", "cost", "status"],
        "foreign_keys": {"vehicle_id": "vehicles"}
    },
    "maintenance_tasks": {
        "columns": ["task_id", "maintenance_id", "task_name", "description", "estimated_cost", "actual_cost"],
        "foreign_keys": {"maintenance_id": "maintenance_records"}
    },
    "workers": {
        "columns": ["worker_id", "first_name", "last_name", "team_id", "salary", "availability_status", "join_date"],
        "foreign_keys": {"team_id": "teams"}
    },
    "teams": {
        "columns": ["team_id", "team_name", "manager_id"],
        "foreign_keys": {"manager_id": "workers"}
    },
    "equipment": {
        "columns": ["equipment_id", "name", "type", "status", "last_serviced_date"]
    },
    "equipment_usage": {
        "columns": ["usage_id", "equipment_id", "worker_id", "start_time", "end_time", "purpose"],
        "foreign_keys": {"equipment_id": "equipment", "worker_id": "workers"}
    },
    "spare_parts": {
        "columns": ["part_id", "name", "type", "quantity", "status"]
    },
    "equipment_parts": {
        "columns": ["id", "equipment_id", "part_id", "quantity_used"],
        "foreign_keys": {"equipment_id": "equipment", "part_id": "spare_parts"}
    },
    "maintenance_invoices": {
        "columns": ["invoice_id", "maintenance_id", "amount", "issue_date", "payment_status"],
        "foreign_keys": {"maintenance_id": "maintenance_records"}
    },
    "safety_audits": {
        "columns": ["audit_id", "vehicle_id", "audit_date", "auditor_id", "remarks"],
        "foreign_keys": {"vehicle_id": "vehicles", "auditor_id": "workers"}
    },
    "project_assignments": {
        "columns": ["assignment_id", "project_id", "worker_id", "assigned_date", "completion_date", "status"],
        "foreign_keys": {"project_id": "projects", "worker_id": "workers"}
    },
    "projects": {
        "columns": ["project_id", "name", "start_date", "end_date", "status"]
    }
}
