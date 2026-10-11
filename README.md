# NHANES Data Engineering Pipeline

## 📌 Project Overview

This project implements an end-to-end data engineering pipeline using public health data from the National Health and Nutrition Examination Survey (NHANES).

The pipeline ingests raw data, transforms and cleans it using Python and Pandas, creates aggregated datasets, loads them into PostgreSQL, and supports visualization through Power BI.

Apache Airflow orchestrates the pipeline workflow.

## 🏗️ Project Architecture

```text
NHANES Dataset
      |
      v
Python Data Ingestion
      |
      v
Raw Data Layer
      |
      v
Silver Layer
(Pandas Transformation)
      |
      v
Data Quality Tests (pytest)
      |
      v
Gold Layer
(Aggregated Parquet Files)
      |
      v
PostgreSQL Database
      |
      v
Power BI Dashboard

Apache Airflow orchestrates the pipeline tasks.
```

## 🛠️ Technologies Used

- **Python** — Data ingestion and pipeline logic
- **Pandas** — Data cleaning and transformation
- **Apache Airflow** — Workflow orchestration
- **Parquet** — Storage of transformed and aggregated datasets
- **PostgreSQL** — Analytical data storage
- **Power BI** — Data visualization and reporting
- **pytest** — Silver-layer data quality testing
- **Git and GitHub** — Version control and project hosting

## 🔄 Pipeline Workflow

### 1. Data Ingestion

Downloads the NHANES demographic dataset and stores the original file in the raw data layer.

### 2. Data Transformation

Processes the raw dataset using Pandas, selects relevant demographic and socioeconomic attributes, creates readable categories, and prepares a structured Silver dataset.

The transformed dataset is stored in Parquet format.

### 3. Data Quality Testing

Uses pytest to validate the Silver dataset.

The tests check that:
- Participant IDs are unique.
- Participant IDs are not missing.
- Required columns are present.
- Ages are within the expected range and are not missing.

### 4. Gold Layer

Creates aggregated datasets for analysis:

- Participant counts by age group and gender
- Average income-to-poverty ratio by age group

The aggregated datasets are stored as Parquet files.

### 5. PostgreSQL Integration

Loads the Gold datasets into PostgreSQL tables for downstream analysis.

### 6. Workflow Orchestration

Apache Airflow coordinates the pipeline through four tasks:

1. `download_nhanes`
2. `transform_nhanes`
3. `create_gold`
4. `load_postgresql`

### 7. Data Visualization

Power BI connects to the analytical data to present demographic and socioeconomic insights through a dashboard.

## 📁 Project Structure

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
├── tests/
│   └── test_silver_data.py
└── README.md
```

## 📊 Gold Datasets

### Participant Count by Age and Gender

Summarizes participant counts across age groups and gender categories.

### Average Income-to-Poverty Ratio by Age

Summarizes the average income-to-poverty ratio across age groups.

## 🎯 Learning Outcomes

Through this project, I practiced:

- Building a multi-stage data pipeline
- Ingesting public datasets using Python
- Cleaning and transforming data with Pandas
- Organizing data into raw, Silver, and Gold layers
- Working with Parquet files
- Writing data quality tests with pytest
- Loading analytical datasets into PostgreSQL
- Orchestrating data workflows with Apache Airflow
- Preparing processed data for Power BI visualization
- Managing project code with Git and GitHub

## 📚 Data Source

**National Health and Nutrition Examination Survey (NHANES)**

NHANES is a program of the US National Center for Health Statistics that collects information about the health and nutritional status of people in the United States.

The project uses NHANES demographic data for demographic and socioeconomic analysis.

Official website: https://www.cdc.gov/nchs/nhanes/

## 🚀 Future Improvements

Potential extensions include:

- Integrating additional NHANES datasets
- Improving data validation and pipeline monitoring
- Adding more analytical datasets and reports
- Expanding automated testing

## ⚠️ Disclaimer

This project is intended for educational and portfolio purposes. It demonstrates data engineering techniques using public health survey data and is not intended for clinical or medical decision-making.