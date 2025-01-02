{
    "patients": {
        "columns": [
            "patient_id",
            "first_name",
            "last_name",
            "dob",
            "gender",
            "address",
            "phone",
            "email",
            "emergency_contact"
        ]
    },
    "appointments": {
        "columns": [
            "appointment_id",
            "patient_id",
            "doctor_id",
            "appointment_date",
            "status",
            "reason",
            "notes"
        ],
        "foreign_keys": {
            "patient_id": "patients",
            "doctor_id": "doctors"
        }
    },
    "doctors": {
        "columns": [
            "doctor_id",
            "first_name",
            "last_name",
            "specialization",
            "phone",
            "email",
            "hire_date",
            "department_id"
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
            "head_doctor_id"
        ],
        "foreign_keys": {
            "head_doctor_id": "doctors"
        }
    },
    "prescriptions": {
        "columns": [
            "prescription_id",
            "appointment_id",
            "medicine_name",
            "dosage",
            "frequency",
            "start_date",
            "end_date"
        ],
        "foreign_keys": {
            "appointment_id": "appointments"
        }
    },
    "labs": {
        "columns": [
            "lab_id",
            "appointment_id",
            "test_name",
            "test_date",
            "result",
            "technician_id"
        ],
        "foreign_keys": {
            "appointment_id": "appointments"
        }
    },
    "medical_records": {
        "columns": [
            "record_id",
            "patient_id",
            "record_date",
            "diagnosis",
            "treatment_plan"
        ],
        "foreign_keys": {
            "patient_id": "patients"
        }
    }
}
