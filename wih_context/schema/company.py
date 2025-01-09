{
    "employees": {
        "columns": [
            "employee_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "hire_date",
            "job_id",
            "manager_id",
            "department_id",
            "salary",
            "bonus",
            "date_of_birth"
        ],
        "foreign_keys": {
            "job_id": "jobs",
            "manager_id": "employees",
            "department_id": "departments"
        }
    },
    "jobs": {
        "columns": [
            "job_id",
            "job_title",
            "min_salary",
            "max_salary"
        ]
    },
    "departments": {
        "columns": [
            "department_id",
            "department_name",
            "manager_id",
            "location"
        ],
        "foreign_keys": {
            "manager_id": "employees"
        }
    },
    "salaries": {
        "columns": [
            "salary_id",
            "employee_id",
            "base_salary",
            "bonus",
            "deductions",
            "pay_date"
        ],
        "foreign_keys": {
            "employee_id": "employees"
        }
    },
    "projects": {
        "columns": [
            "project_id",
            "project_name",
            "start_date",
            "end_date",
            "client_id",
            "project_manager_id",
            "budget"
        ],
        "foreign_keys": {
            "client_id": "clients",
            "project_manager_id": "employees"
        }
    },
    "project_assignments": {
        "columns": [
            "assignment_id",
            "project_id",
            "employee_id",
            "role",
            "start_date",
            "end_date"
        ],
        "foreign_keys": {
            "project_id": "projects",
            "employee_id": "employees"
        }
    },
    "clients": {
        "columns": [
            "client_id",
            "client_name",
            "contact_email",
            "contact_phone",
            "company_name"
        ]
    },
    "profits": {
        "columns": [
            "profit_id",
            "department_id",
            "project_id",
            "year",
            "revenue",
            "expenses",
            "net_profit"
        ],
        "foreign_keys": {
            "department_id": "departments",
            "project_id": "projects"
        }
    },
    "attendance": {
        "columns": [
            "attendance_id",
            "employee_id",
            "attendance_date",
            "status"
        ],
        "foreign_keys": {
            "employee_id": "employees"
        }
    },
    "performance_reviews": {
        "columns": [
            "review_id",
            "employee_id",
            "review_date",
            "performance_score",
            "review_comments",
            "reviewed_by"
        ],
        "foreign_keys": {
            "employee_id": "employees",
            "reviewed_by": "employees"
        }
    },
    "assets": {
        "columns": [
            "asset_id",
            "asset_name",
            "asset_type",
            "assigned_to",
            "purchase_date",
            "cost",
            "status"
        ],
        "foreign_keys": {
            "assigned_to": "employees"
        }
    }
}
