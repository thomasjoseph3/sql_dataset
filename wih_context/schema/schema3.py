schema={
    "ships": {
        "columns": [
            "ship_id",
            "name",
            "owner",
            "type",
            "build_year",
            "status",
            "location",
            "ai_enabled",
            "inspection_score",
            "last_maintenance_date"
        ]
    },
    "repairs": {
        "columns": [
            "repair_id",
            "ship_id",
            "start_date",
            "end_date",
            "status",
            "total_cost",
            "supervisor_id",
            "priority_level"
        ],
        "foreign_keys": {
            "ship_id": "ships",
            "supervisor_id": "employees"
        }
    },
    "repair_tasks": {
        "columns": [
            "task_id",
            "repair_id",
            "task_name",
            "description",
            "estimated_time",
            "actual_time",
            "cost",
            "assigned_employee_id",
            "status"
        ],
        "foreign_keys": {
            "repair_id": "repairs",
            "assigned_employee_id": "employees"
        }
    },
    "employees": {
        "columns": [
            "employee_id",
            "first_name",
            "last_name",
            "department_id",
            "salary",
            "availability_status",
            "hire_date",
            "certifications",
            "increment_rate",
            "last_training_date"
        ],
        "foreign_keys": {
            "department_id": "departments"
        }
    },
    "departments": {
        "columns": [
            "department_id",
            "department_name",
            "budget",
            "head_id"
        ],
        "foreign_keys": {
            "head_id": "employees"
        }
    },
    "cradles": {
        "columns": [
            "cradle_id",
            "ship_id",
            "status",
            "inspection_date",
            "repair_cost"
        ],
        "foreign_keys": {
            "ship_id": "ships"
        }
    },
    "trolleys": {
        "columns": [
            "trolley_id",
            "status",
            "last_maintenance_date",
            "repair_cost"
        ]
    },
    "ai_cameras": {
        "columns": [
            "camera_id",
            "ship_id",
            "location",
            "status",
            "last_service_date",
            "repair_cost",
            "task_assigned_id"
        ],
        "foreign_keys": {
            "ship_id": "ships",
            "task_assigned_id": "repair_tasks"
        }
    },
    "drones": {
        "columns": [
            "drone_id",
            "type",
            "status",
            "last_service_date",
            "battery_status",
            "repair_cost",
            "inspection_count"
        ]
    },
    "sensors": {
        "columns": [
            "sensor_id",
            "type",
            "ship_id",
            "location",
            "status",
            "data_collected",
            "last_calibration_date"
        ],
        "foreign_keys": {
            "ship_id": "ships"
        }
    },
    "machinery": {
        "columns": [
            "machinery_id",
            "name",
            "type",
            "location",
            "status",
            "last_service_date",
            "repair_cost",
            "expected_lifetime"
        ]
    },
    "cost_tracking": {
        "columns": [
            "cost_id",
            "type",
            "description",
            "amount",
            "date",
            "related_id",
            "related_type"
        ]
    },
    "ai_insights": {
        "columns": [
            "insight_id",
            "ship_id",
            "generated_date",
            "category",
            "prediction",
            "confidence_score"
        ],
        "foreign_keys": {
            "ship_id": "ships"
        }
    },
    "employee_training": {
        "columns": [
            "training_id",
            "employee_id",
            "training_name",
            "certification",
            "completion_date"
        ],
        "foreign_keys": {
            "employee_id": "employees"
        }
    },
    "workflows": {
        "columns": [
            "workflow_id",
            "repair_id",
            "current_stage",
            "next_stage",
            "status",
            "start_date",
            "end_date"
        ],
        "foreign_keys": {
            "repair_id": "repairs"
        }
    }
}
