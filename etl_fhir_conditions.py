"""
FHIR (Fast Healthcare Interoperability Resources) is a standard for structuring and exchanging healthcare data electronically using consistent, modular 'resources' like Patient, Condition, Observation, etc.
"""

import pandas as pd
import json
import os

# Load data
df = pd.read_csv("data/2010_Chronic_Conditions_PUF.csv")

# Mapping from column names to readable condition labels
condition_map = {
    "CC_ALZHDMTA": "Alzheimer's Disease or Related Dementia",
    "CC_CANCER": "Cancer",
    "CC_CHF": "Congestive Heart Failure",
    "CC_CHRNKIDN": "Chronic Kidney Disease",
    "CC_COPD": "Chronic Obstructive Pulmonary Disease",
    "CC_DEPRESSN": "Depression",
    "CC_DIABETES": "Diabetes",
    "CC_ISCHMCHT": "Ischemic Heart Disease",
    "CC_OSTEOPRS": "Osteoporosis",
    "CC_RA_OA": "Rheumatoid Arthritis / Osteoarthritis",
    "CC_STRKETIA": "Stroke / Transient Ischemic Attack"
}

output = []

# Iterate over rows and extract active conditions
for idx, row in df.iterrows():
    patient_id = f"patient_{idx:05d}"

    for code, label in condition_map.items():
        if row.get(code) == 1:
            resource = {
                "resourceType": "Condition",
                "id": f"{patient_id}-condition-{code.lower()}",
                "subject": {
                    "reference": f"Patient/{patient_id}"
                },
                "code": {
                    "text": label
                },
                "clinicalStatus": "active"
            }
            output.append(resource)

# Write to JSON file
os.makedirs("output", exist_ok=True)
with open("output/fhir_conditions.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"✅ ETL complete. {len(output)} FHIR Condition resources written to output/fhir_conditions.json")
