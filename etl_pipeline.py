import pandas as pd
import json
import os

# Load CSV
df = pd.read_csv("data/2010_Chronic_Conditions_PUF.csv")

# Create output folder
os.makedirs("output", exist_ok=True)

# Select condition columns
condition_map = {
    "CC_ALZHDMTA": "Alzheimer's or Dementia",
    "CC_CANCER": "Cancer",
    "CC_CHF": "Congestive Heart Failure",
    "CC_CHRNKIDN": "Chronic Kidney Disease",
    "CC_COPD": "COPD",
    "CC_DEPRESSN": "Depression",
    "CC_DIABETES": "Diabetes",
    "CC_ISCHMCHT": "Ischemic Heart Disease",
    "CC_OSTEOPRS": "Osteoporosis",
    "CC_RA_OA": "Rheumatoid Arthritis / Osteoarthritis",
    "CC_STRKETIA": "Stroke / TIA"
}

resources = []

for idx, row in df.iterrows():
    patient_id = f"patient_{idx:05d}"

    for col, condition_name in condition_map.items():
        if row[col] == 1:
            condition = {
                "resourceType": "Condition",
                "id": f"{patient_id}-condition-{col.lower()}",
                "subject": { "reference": f"Patient/{patient_id}" },
                "code": { "text": condition_name },
                "clinicalStatus": "active"
            }
            resources.append(condition)

# Write output
with open("output/conditions.json", "w") as f:
    json.dump(resources, f, indent=2)

print(f"✅ ETL complete. {len(resources)} conditions written to output/conditions.json")
