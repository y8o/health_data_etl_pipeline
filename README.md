
# Health Data ETL Pipeline (FHIR-lite Formatter)

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline that mimics real-world electronic health record (EHR) workflows. It processes public healthcare data and outputs structured JSON using a simplified version of the [FHIR](https://www.hl7.org/fhir/) (Fast Healthcare Interoperability Resources) standard.

---

## Overview

Using Medicare Chronic Conditions Public Use File (PUF) data, the pipeline:
- Parses raw CSV data representing chronic condition flags
- Transforms rows into standardized JSON "Condition" resources
- Outputs FHIR-like JSON suitable for EHR systems, APIs, or dashboards

---

## Data Source

- Dataset: [CMS Chronic Conditions Public Use File (PUF)](https://www.cms.gov/data-research/statistics-trends-and-reports/basic-stand-alone-medicare-claims-public-use-files/chronic-conditions-puf)
- Included: Example CSV file (`data/2010_Chronic_Conditions_PUF.csv`) with limited rows for demo use

---

## Technologies

- Python 3.x
- pandas
- JSON
- Command line

---

## Use Case

This project simulates how raw EHR data—especially binary condition indicators—can be cleaned, mapped, and structured into standard healthcare formats. It provides a hands-on example of healthcare data interoperability and preprocessing.

---

## ▶To Run

### 1. Install Python dependencies (if needed)
```bash
pip install pandas
```

### 2. Run the ETL script
```bash
python etl_fhir_conditions.py
```

### 3. Output

The pipeline will generate a JSON file:
```
output/fhir_conditions.json
```

Each record is a FHIR-style `Condition` resource, e.g.:

```json
{
  "resourceType": "Condition",
  "id": "patient_00001-condition-cc_diabetes",
  "subject": {
    "reference": "Patient/patient_00001"
  },
  "code": {
    "text": "Diabetes"
  },
  "clinicalStatus": "active"
}
```

---

## FHIR Note

FHIR (Fast Healthcare Interoperability Resources) is a standard created by HL7 for sharing healthcare data in modular, reusable formats like `Patient`, `Observation`, and `Condition`. This project uses a simplified version for demonstration purposes and educational analysis.

---

## Project Structure

```
.
├── data/
│   └── 2010_Chronic_Conditions_PUF.csv   # Sample input file
├── etl_fhir_conditions.py                # Main ETL script
├── output/
│   └── fhir_conditions.json              # Transformed output
├── LICENSE
└── README.md
```

---

## Condition Mapping

The script maps CMS columns like `CC_DIABETES`, `CC_CHF`, and `CC_RA_OA` into readable FHIR `Condition.code.text` values such as:

| Column Name    | Condition Label                          |
|----------------|-------------------------------------------|
| `CC_ALZHDMTA`  | Alzheimer’s Disease or Dementia           |
| `CC_CANCER`    | Cancer                                    |
| `CC_CHF`       | Congestive Heart Failure                  |
| `CC_CHRNKIDN`  | Chronic Kidney Disease                    |
| `CC_COPD`      | Chronic Obstructive Pulmonary Disease     |
| `CC_DEPRESSN`  | Depression                                |
| `CC_DIABETES`  | Diabetes                                  |
| `CC_ISCHMCHT`  | Ischemic Heart Disease                    |
| `CC_OSTEOPRS`  | Osteoporosis                              |
| `CC_RA_OA`     | Rheumatoid Arthritis / Osteoarthritis     |
| `CC_STRKETIA`  | Stroke / Transient Ischemic Attack        |

---

## Future Work

- Generate `Patient` resources alongside `Condition`
- Add timestamps (e.g., `onsetDateTime`)
- Support other FHIR resource types like `Observation`
- Convert full datasets or build REST endpoints

---

## License

MIT License. See `LICENSE` for details.
