"""Todoo
"""
from pprint import pprint
import pendulum
from airflow import DAG
from airflow.decorators import task


with DAG(
    dag_id="weather_api_dag",
    schedule='@daily',
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["API", "ETL", "Postgres"],
) as dag:

    # [START howto_operator_python]
    @task(task_id="run_weather_etl_pipeline")
    def run_weather_etl_pipeline():
        """Todoo"""
        import weather_api

    ETL_TASK = run_weather_etl_pipeline()
