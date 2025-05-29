# Health Data ETL Pipeline (FHIR-lite Formatter)

This project demonstrates a simple data integration and transformation pipeline inspired by real-world electronic health record (EHR) data workflows.

## Overview

We use a sample open healthcare dataset to:
- Parse and clean raw clinical data (CSV format)
- Normalize lab values (e.g., unit conversion)
- Output structured JSON representing a simplified FHIR-like resource format

## Data Source

- [CMS Chronic Conditions Public Use File (PUF)](https://www.cms.gov/data-research/statistics-trends-and-reports/basic-stand-alone-medicare-claims-public-use-files/chronic-conditions-puf)
- Example CSV included in `data/` folder for quick execution

## Technologies

- Python 3
- Pandas
- JSON
- Command line execution

## Use Case

This project simulates how raw healthcare data can be standardized and structured for integration into a central EHR system. It demonstrates data pipeline design, field mapping, and format conversion.

## To Run

```bash
python etl_pipeline.py
```

Outputs will be stored in the `output/` folder.
