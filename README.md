# NHANES Data Engineering Pipeline

## 📌 Project Overview

This project implements an end-to-end data engineering pipeline using public health data from the National Health and Nutrition Examination Survey (NHANES).

The pipeline ingests raw data, transforms it using Python and Pandas, creates aggregated datasets, loads them into PostgreSQL, and supports visualization through Power BI.

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
Gold Layer
(Aggregated Parquet Files)
      |
      v
PostgreSQL Database
      |
      v
Power BI Dashboard

Apache Airflow orchestrates the pipeline.
```

## 🛠️ Technologies Used

* **Python** — Data ingestion and processing
* **Pandas** — Data cleaning and transformation
* **Apache Airflow** — Workflow orchestration
* **Parquet** — Columnar data storage
* **PostgreSQL** — Relational database
* **Power BI** — Data visualization
* **Git and GitHub** — Version control and project hosting

## 🔄 Pipeline Workflow

### 1. Data Ingestion

Downloads the NHANES demographic dataset and stores the original file in the raw data layer.

### 2. Data Transformation

Uses Pandas to clean and transform the data, select relevant columns, and create useful demographic categories.

The transformed dataset is stored in Parquet format in the silver layer.

### 3. Gold Layer

Creates aggregated datasets for analysis, including:

* Participant counts by age group and gender
* Average income-to-poverty ratio by age group

These datasets are stored as Parquet files.

### 4. PostgreSQL Integration

Loads the aggregated gold datasets into PostgreSQL tables for downstream analysis.

### 5. Workflow Orchestration

Apache Airflow orchestrates the following tasks:

1. Download NHANES data
2. Transform the data
3. Create gold datasets
4. Load the gold datasets into PostgreSQL

### 6. Data Visualization

Power BI is used to visualize demographic and socioeconomic information from the processed datasets.

## 📁 Project Structure

```text
NHANES_BRFSS_Data_Engineering/
│
├── airflow/
│   └── dags/
│       └── nhanes_pipeline.py
│
├── database/
│   └── load_gold.py
│
├── gold/
│   ├── create_gold.py
│   ├── avg_income_poverty_by_age.parquet
│   └── participant_count_by_age_gender.parquet
│
├── ingestion/
│   ├── download_nhanes.py
│   └── inspect_nhanes.py
│
├── raw/
│   └── DEMO_L.xpt
│
├── silver/
│   └── transform_nhanes.py
│
└── README.md
```

## 📊 Gold Datasets

### Participant Count by Age and Gender

Summarizes participant counts across age groups and gender categories.

### Average Income-to-Poverty Ratio by Age

Summarizes the average income-to-poverty ratio across age groups.

## 🎯 Learning Outcomes

Through this project, I practiced:

* Building a data ingestion pipeline
* Cleaning and transforming data with Pandas
* Organizing data into raw, silver, and gold layers
* Working with Parquet files
* Loading analytical datasets into PostgreSQL
* Orchestrating data workflows with Apache Airflow
* Preparing processed data for Power BI visualization
* Managing a project with Git and GitHub

## 📚 Data Source

The dataset is sourced from the official NHANES program maintained by the US Centers for Disease Control and Prevention.

Official website: https://www.cdc.gov/nchs/nhanes/

## ⚠️ Disclaimer

This project is intended for educational and portfolio purposes. It demonstrates data engineering techniques using public health survey data and is not intended for clinical or medical decision-making.
