from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from ingestion.download_nhanes import download_nhanes
from silver.transform_nhanes import transform_nhanes
from gold.create_gold import create_gold
from database.load_gold import load_gold


with DAG(
    dag_id="nhanes_brfss_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    download = PythonOperator(
        task_id="download_nhanes",
        python_callable=download_nhanes,
    )

    transform = PythonOperator(
        task_id="transform_nhanes",
        python_callable=transform_nhanes,
    )

    create_gold = PythonOperator(
        task_id="create_gold",
        python_callable=create_gold,
    )

    load_database = PythonOperator(
        task_id="load_postgresql",
        python_callable=load_gold,
    )

    download >> transform >> create_gold >> load_database