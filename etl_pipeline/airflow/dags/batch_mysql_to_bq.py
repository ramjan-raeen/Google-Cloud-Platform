from datetime import datetime
from datetime import timedelta

import pandas as pd
from sqlalchemy import create_engine

from airflow import DAG
from airflow.models import Variable
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator


from utils.extract_mysql_utils import extract_mysql
from utils.load_bq_utils import load_bigquery
from utils.validation import validate

default_args={
    'owner':'airflow',
    'depends_on_past':False,
    'email_on_failures':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

PROJECT_ID = Variable.get("gcp_project_id")
DATASET_ID = Variable.get("dataset_id")
TABLE_NAME = Variable.get("table_name")

MYSQL_USER = Variable.get("mysql_user")
MYSQL_PASSWORD = Variable.get("mysql_pass")
MYSQL_HOST = Variable.get("mysql_host")
MYSQL_PORT = Variable.get("mysql_port")
MYSQL_DB = Variable.get("mysql_db")

TEMP_FILE = "/tmp/customers.parquet"


def insert_manifest(**kwargs):
    ti = kwargs['ti']

    pass

def update_manifest():
    pass


with DAG(dag_id='batch_mysql_to_bq',
         description='migrate data from Mysql to BigQuery',
         default_args=default_args,
         schedule_interval='@daily',
         start_date=datetime(2026,7,9),
         catchup=False
          ) as dag:
    start = EmptyOperator(
        task_id='start'
    )
    end = EmptyOperator(
        task_id='end'
    )

    extracted = PythonOperator(
        task_id="extracted",
        python_callable=extract_mysql,
        op_kwargs = {
            "mysql_user":MYSQL_USER,
            "mysql_pass":MYSQL_PASSWORD,
            "mysql_host":MYSQL_HOST,
            "mysql_port":MYSQL_PORT,
            "mysql_db":MYSQL_DB,
            "temp_file":TEMP_FILE
        }
    )
    insert_manifest_task = PythonOperator(
        task_id="insert_manifest",
        python_callable=insert_manifest
    )

    load_to_bigquery = PythonOperator(
        task_id="load_to_bigquery",
        python_callable=load_bigquery,
        op_kwargs={
            "project_id":PROJECT_ID,
            "gcp_conn_id":"google_cloud_default",
            "dataset_id":DATASET_ID,
            "table_name":TABLE_NAME,
            "file_name":TEMP_FILE
        }
    )
    updata_manifest_task = PythonOperator(
        task_id="update_manifest",
        python_callable=update_manifest
    )
    
    validation = PythonOperator(
        task_id="validation",
        python_callable=validate,
        op_kwargs={
            "gcp_conn_id":"google_cloud_default",
            "project_id":PROJECT_ID,
            "dataset_id":DATASET_ID,
            "table_name":TABLE_NAME
        }
    )

        


start >> extracted >> insert_manifest_task >> load_to_bigquery >> updata_manifest_task >> validation >> end
