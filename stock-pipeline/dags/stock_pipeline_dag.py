import sys
sys.path.append('/opt/airflow')
from airflow import DAG  # pyright: ignore[reportMissingImports]
from airflow.operators.python import PythonOperator  # pyright: ignore[reportMissingImports]
from datetime import datetime, timedelta
from scripts.fetch_and_store import fetch_and_store_stock_data  # pyright: ignore[reportMissingImports]

with DAG(
    dag_id='stock_pipeline_dag',
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
    }
) as dag:

    fetch_and_store_data = PythonOperator(
        task_id='fetch_and_store_data',
        python_callable=fetch_and_store_stock_data,
    )

    fetch_and_store_data