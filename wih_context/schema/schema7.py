{
    "companies": {
        "columns": ["company_id", "name", "address", "industry", "contact_email", "contact_phone"]
    },
    "departments": {
        "columns": ["department_id", "name", "company_id", "head_id", "budget"],
        "foreign_keys": {
            "company_id": "companies",
            "head_id": "employees"
        }
    },
    "employees": {
        "columns": ["employee_id", "first_name", "last_name", "department_id", "role", "salary", "availability", "hire_date"],
        "foreign_keys": {"department_id": "departments"}
    },
    "teams": {
        "columns": ["team_id", "name", "department_id", "lead_id"],
        "foreign_keys": {
            "department_id": "departments",
            "lead_id": "employees"
        }
    },
    "projects": {
        "columns": ["project_id", "name", "description", "department_id", "start_date", "end_date", "budget", "status"],
        "foreign_keys": {"department_id": "departments"}
    },
    "project_assignments": {
        "columns": ["assignment_id", "project_id", "employee_id", "role", "start_date", "end_date", "status"],
        "foreign_keys": {
            "project_id": "projects",
            "employee_id": "employees"
        }
    },
    "vehicles": {
        "columns": ["vehicle_id", "name", "type", "owner_id", "status", "location"],
        "foreign_keys": {"owner_id": "employees"}
    },
    "maintenance_records": {
        "columns": ["maintenance_id", "vehicle_id", "start_date", "end_date", "cost", "status"],
        "foreign_keys": {"vehicle_id": "vehicles"}
    },
    "maintenance_tasks": {
        "columns": ["task_id", "maintenance_id", "task_name", "description", "estimated_cost", "actual_cost", "worker_id", "status"],
        "foreign_keys": {
            "maintenance_id": "maintenance_records",
            "worker_id": "employees"
        }
    },
    "equipment": {
        "columns": ["equipment_id", "name", "type", "status", "department_id", "last_serviced_date"],
        "foreign_keys": {"department_id": "departments"}
    },
    "equipment_usage": {
        "columns": ["usage_id", "equipment_id", "worker_id", "start_time", "end_time", "purpose"],
        "foreign_keys": {
            "equipment_id": "equipment",
            "worker_id": "employees"
        }
    },
    "spare_parts": {
        "columns": ["part_id", "name", "type", "quantity", "status", "supplier_id"],
        "foreign_keys": {"supplier_id": "suppliers"}
    },
    "equipment_parts": {
        "columns": ["id", "equipment_id", "part_id", "quantity_used"],
        "foreign_keys": {
            "equipment_id": "equipment",
            "part_id": "spare_parts"
        }
    },
    "suppliers": {
        "columns": ["supplier_id", "name", "contact_email", "contact_phone", "address"]
    },
    "safety_audits": {
        "columns": ["audit_id", "vehicle_id", "audit_date", "auditor_id", "remarks"],
        "foreign_keys": {
            "vehicle_id": "vehicles",
            "auditor_id": "employees"
        }
    },
    "tasks": {
        "columns": ["task_id", "name", "description", "priority", "assigned_to", "project_id", "start_date", "due_date", "completion_date", "status"],
        "foreign_keys": {
            "assigned_to": "employees",
            "project_id": "projects"
        }
    },
    "documents": {
        "columns": ["document_id", "title", "file_path", "uploaded_by", "related_id", "related_type", "upload_date"],
        "foreign_keys": {"uploaded_by": "employees"}
    },
    "expenses": {
        "columns": ["expense_id", "type", "amount", "date", "description", "department_id", "project_id"],
        "foreign_keys": {
            "department_id": "departments",
            "project_id": "projects"
        }
    },
    "training_sessions": {
        "columns": ["session_id", "name", "description", "trainer_id", "start_date", "end_date", "status"],
        "foreign_keys": {"trainer_id": "employees"}
    },
    "training_attendance": {
        "columns": ["attendance_id", "session_id", "employee_id", "attendance_status"],
        "foreign_keys": {
            "session_id": "training_sessions",
            "employee_id": "employees"
        }
    },
    "notifications": {
        "columns": ["notification_id", "message", "recipient_id", "related_id", "related_type", "timestamp", "status"],
        "foreign_keys": {"recipient_id": "employees"}
    },
    "events": {
        "columns": ["event_id", "name", "description", "start_date", "end_date", "location", "organizer_id"],
        "foreign_keys": {"organizer_id": "employees"}
    }
}
