import json
import re

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

schema_mapping = {
    "ships": {
        "ship_id": "shipId",
        "name": "name",
        "owner": "owner",
        "type": "type",
        "build_year": "buildYear",
        "status": "status",
        "location": "location",
        "ai_enabled": "aiEnabled",
        "inspection_score": "inspectionScore",
        "last_maintenance_date": "lastMaintenanceDate"
    },
    "repairs": {
        "repair_id": "repairId",
        "ship_id": "shipId",
        "start_date": "startDate",
        "end_date": "endDate",
        "status": "status",
        "total_cost": "totalCost",
        "supervisor_id": "supervisorId",
        "priority_level": "priorityLevel"
    },
    "repair_tasks": {
        "task_id": "taskId",
        "repair_id": "repairId",
        "task_name": "taskName",
        "description": "description",
        "estimated_time": "estimatedTime",
        "actual_time": "actualTime",
        "cost": "cost",
        "assigned_employee_id": "assignedEmployeeId",
        "status": "status"
    },
    "employees": {
        "employee_id": "employeeId",
        "first_name": "firstName",
        "last_name": "lastName",
        "department_id": "departmentId",
        "salary": "salary",
        "availability_status": "availabilityStatus",
        "hire_date": "hireDate",
        "certifications": "certifications",
        "increment_rate": "incrementRate",
        "last_training_date": "lastTrainingDate"
    },
    "departments": {
        "department_id": "departmentId",
        "department_name": "departmentName",
        "budget": "budget",
        "head_id": "headId"
    },
    "cradles": {
        "cradle_id": "cradleId",
        "ship_id": "shipId",
        "status": "status",
        "inspection_date": "inspectionDate",
        "repair_cost": "repairCost"
    },
    "trolleys": {
        "trolley_id": "trolleyId",
        "status": "status",
        "last_maintenance_date": "lastMaintenanceDate",
        "repair_cost": "repairCost"
    },
    "ai_cameras": {
        "camera_id": "cameraId",
        "ship_id": "shipId",
        "location": "location",
        "status": "status",
        "last_service_date": "lastServiceDate",
        "repair_cost": "repairCost",
        "task_assigned_id": "taskAssignedId"
    },
    "drones": {
        "drone_id": "droneId",
        "type": "type",
        "status": "status",
        "last_service_date": "lastServiceDate",
        "battery_status": "batteryStatus",
        "repair_cost": "repairCost",
        "inspection_count": "inspectionCount"
    },
    "sensors": {
        "sensor_id": "sensorId",
        "type": "type",
        "ship_id": "shipId",
        "location": "location",
        "status": "status",
        "data_collected": "dataCollected",
        "last_calibration_date": "lastCalibrationDate"
    },
    "machinery": {
        "machinery_id": "machineryId",
        "name": "name",
        "type": "type",
        "location": "location",
        "status": "status",
        "last_service_date": "lastServiceDate",
        "repair_cost": "repairCost",
        "expected_lifetime": "expectedLifetime"
    },
    "cost_tracking": {
        "cost_id": "costId",
        "type": "type",
        "description": "description",
        "amount": "amount",
        "date": "date",
        "related_id": "relatedId",
        "related_type": "relatedType"
    },
    "ai_insights": {
        "insight_id": "insightId",
        "ship_id": "shipId",
        "generated_date": "generatedDate",
        "category": "category",
        "prediction": "prediction",
        "confidence_score": "confidenceScore"
    },
    "employee_training": {
        "training_id": "trainingId",
        "employee_id": "employeeId",
        "training_name": "trainingName",
        "certification": "certification",
        "completion_date": "completionDate"
    },
    "workflows": {
        "workflow_id": "workflowId",
        "repair_id": "repairId",
        "current_stage": "currentStage",
        "next_stage": "nextStage",
        "status": "status",
        "start_date": "startDate",
        "end_date": "endDate"
    }
}


def replace_snake_with_camel_oracle(text, schema):
    # Replace field names
    for table, fields in schema.items():
        for snake, camel in fields.items():
            # Replace snake_case field names with camelCase field names only if not already quoted
            text = re.sub(r'(?<!")\b' + re.escape(snake) + r'\b(?!")', f'"{camel}"', text)
    
    # Replace table names
    for table in schema.keys():
        camel_table = to_camel_case(table)
        # Replace snake_case table names with camelCase table names only if not already quoted
        text = re.sub(r'(?<!")\b' + re.escape(table) + r'\b(?!")', f'"{camel_table}"', text)
    
    return text


def update_entry(entry, schema):
    if "context" in entry:
        for table, details in entry["context"].items():
            if table in schema:
                entry["context"][table]["columns"] = [
                    schema[table].get(column, column) for column in details.get("columns", [])
                ]
    if "query" in entry:
        entry["query"] = replace_snake_with_camel_oracle(entry["query"], schema)
    return entry

input_file = "datasets/snake_case/ship3.json"
output_file = "datasets/camel_case/ship3_camel_case.json"

with open(input_file, 'r') as file:
    data = json.load(file)

updated_data = [update_entry(entry, schema_mapping) for entry in data]

with open(output_file, 'w') as file:
    json.dump(updated_data, file, indent=4)

print(f"Updated JSON file saved to {output_file}")
