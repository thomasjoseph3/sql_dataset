{
    "students": {
        "columns": [
            "student_id",
            "first_name",
            "last_name",
            "dob",
            "email",
            "phone",
            "address",
            "enrollment_date",
            "program_id"
        ],
        "foreign_keys": {
            "program_id": "programs"
        }
    },
    "programs": {
        "columns": [
            "program_id",
            "program_name",
            "department_id",
            "duration_years",
            "credits_required"
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
            "head_id": "faculty"
        }
    },
    "faculty": {
        "columns": [
            "faculty_id",
            "first_name",
            "last_name",
            "title",
            "department_id",
            "email",
            "phone",
            "hire_date"
        ],
        "foreign_keys": {
            "department_id": "departments"
        }
    },
    "courses": {
        "columns": [
            "course_id",
            "course_name",
            "department_id",
            "credits",
            "faculty_id"
        ],
        "foreign_keys": {
            "department_id": "departments",
            "faculty_id": "faculty"
        }
    },
    "enrollments": {
        "columns": [
            "enrollment_id",
            "student_id",
            "course_id",
            "semester",
            "year",
            "grade"
        ],
        "foreign_keys": {
            "student_id": "students",
            "course_id": "courses"
        }
    },
    "exams": {
        "columns": [
            "exam_id",
            "course_id",
            "exam_date",
            "location",
            "total_marks"
        ],
        "foreign_keys": {
            "course_id": "courses"
        }
    },
    "exam_results": {
        "columns": [
            "result_id",
            "exam_id",
            "student_id",
            "marks_obtained"
        ],
        "foreign_keys": {
            "exam_id": "exams",
            "student_id": "students"
        }
    }
}
