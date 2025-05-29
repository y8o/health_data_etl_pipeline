import pandas as pd
import json
import os

def convert_glucose(value, unit):
    if unit == "mmol/L":
        return round(value * 18.0182, 2), "mg/dL"
    return value, unit

df = pd.read_csv("data/sample_clinical_data.csv")
output = []

for _, row in df.iterrows():
    lab_value, unit = convert_glucose(row["lab_value"], row["unit"]) if row["lab_test"] == "Glucose" else (row["lab_value"], row["unit"])
    resource = {
        "resourceType": "Observation",
        "id": str(row["patient_id"]),
        "status": "final",
        "code": {
            "text": row["lab_test"]
        },
        "valueQuantity": {
            "value": lab_value,
            "unit": unit
        }
    }
    output.append(resource)

os.makedirs("output", exist_ok=True)
with open("output/observations.json", "w") as f:
    json.dump(output, f, indent=2)

print("ETL complete. Output written to output/observations.json")
