from datetime import datetime
from datetime import timedelta
from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.empty import EmptyOperator
# from airflow.utils.taskgroup import TaskGroup
# from airflow.sdk import TaskGroup
from airflow.utils.task_group import TaskGroup

from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

default_args={
    'owner':'airflow',
    'depends_on_past':False,
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)

}

with DAG(
    dag_id='gcs_to_bigquery',
    default_args = default_args,
    description='The purpose of this dag to transfer data from gcs to BigQuery',
    start_date = datetime(2026,2,24),
    schedule = '@daily'
) as dag:
    task_01 = EmptyOperator(
        task_id='start'
    )
    task_02 = GCSToBigQueryOperator(
        task_id='GCSToBigQuery',
        bucket='my-bucket',
        source_objects=['my-folder/my-files.csv'],
        destination_project_dataset_table='project.dataset.my-table',
        source_format='CSV',
        skip_leading_rows=1,
        write_disposition='WRITE_TRUNCATE',
        create_disposition='CREATE_IF_NEEDED',
        field_delimiter=',',
        autodetect=True

    )
    task_03 = BigQueryInsertJobOperator(
        task_id="BigQuery",
        configuration = {
            "query":{
                "query":"SELECT * FROM TABLE NAME",
            'useLegacySql':False
            }
        },
        location="us"
    )
task_01 >> task_02 >> task_03