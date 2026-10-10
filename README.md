# NHANES Data Engineering Pipeline

An end-to-end data engineering project that processes public health demographic data from the National Health and Nutrition Examination Survey (NHANES) using Python, Pandas, Apache Airflow, PostgreSQL, and Power BI.

## Project Overview

This project demonstrates how raw public health data can be transformed into structured datasets and analytical summaries for reporting.

The pipeline downloads NHANES data, transforms and cleans demographic information, creates aggregated datasets, loads the results into PostgreSQL, and supports visualization through Power BI.

## Architecture

```text
NHANES Dataset
      |
      v
Python Data Ingestion
      |
      v
Raw Layer
      |
      v
Silver Layer
(Pandas Transformation)
      |
      v
Gold Layer
(Aggregated Parquet Files)
      |
      v
PostgreSQL
      |
      v
Power BI Dashboard
```

Apache Airflow orchestrates the pipeline tasks.

## Technologies Used

* **Python** — Data ingestion and pipeline logic
* **Pandas** — Data cleaning and transformation
* **Apache Airflow** — Workflow orchestration
* **Parquet** — Storage of transformed and aggregated datasets
* **PostgreSQL** — Analytical data storage
* **Power BI** — Data visualization and reporting
* **Git and GitHub** — Version control and project management

## Pipeline Workflow

### 1. Data Ingestion

Downloads the NHANES demographic dataset and stores the original file in the raw data layer.

### 2. Data Transformation

Processes the raw dataset using Pandas, selects relevant demographic and socioeconomic attributes, creates readable categories, and prepares a structured Silver dataset.

### 3. Gold Layer

Creates aggregated datasets for analysis:

* Participant counts by age group and gender
* Average income-to-poverty ratio by age group

The aggregated datasets are stored in Parquet format.

### 4. PostgreSQL Loading

Loads the Gold datasets into PostgreSQL tables for downstream analysis.

### 5. Workflow Orchestration

Apache Airflow coordinates the pipeline through four tasks:

1. `download_nhanes`
2. `transform_nhanes`
3. `create_gold`
4. `load_postgresql`

### 6. Visualization

Power BI connects to the analytical data to present demographic and socioeconomic insights through a dashboard.

## Project Structure

```text
NHANES_BRFSS_Data_Engineering/
├── airflow/
│   └── dags/
│       └── nhanes_pipeline.py
├── database/
│   └── load_gold.py
├── gold/
│   ├── create_gold.py
│   ├── avg_income_poverty_by_age.parquet
│   └── participant_count_by_age_gender.parquet
├── ingestion/
│   ├── download_nhanes.py
│   └── inspect_nhanes.py
├── raw/
│   └── DEMO_L.xpt
├── silver/
│   ├── transform_nhanes.py
│   └── nhanes_demographics.parquet
└── README.md
```

## Data Source

**National Health and Nutrition Examination Survey (NHANES)**

NHANES is a program of the U.S. National Center for Health Statistics that collects information about the health and nutritional status of people in the United States.

The project uses the NHANES demographic dataset for demographic and socioeconomic analysis.

Official website: https://www.cdc.gov/nchs/nhanes/

## Key Learning Outcomes

* Building a multi-stage data pipeline
* Working with raw and transformed datasets
* Cleaning and transforming data using Pandas
* Creating analytical aggregations
* Storing structured data in Parquet
* Loading datasets into PostgreSQL
* Orchestrating data workflows with Apache Airflow
* Preparing data for business intelligence dashboards
* Managing project code with Git and GitHub

## Future Improvements

Potential extensions include improved data validation, automated pipeline monitoring, and additional analytical reporting.

## Disclaimer

This project is intended for educational and portfolio purposes. The analysis is based on public NHANES data and should not be interpreted as medical advice.
