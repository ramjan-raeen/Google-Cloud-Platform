# Author    :   Ramjan Raeen
# Date      :   2026-07-13
# Modified  :   2026-07-13
# Purpose   :   migrate large volumnes of data from mysql to BigQuery using paging

from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator



from utils.extract_mysql_utils_paging import extract_mysql_pagged
from utils.load_bq_utils_paging import load_batch_to_bigquery


PROJECT_ID = Variable.get("gcp_project_id")
DATASET_ID = Variable.get("dataset_id")
TABLE_ID = Variable.get("table_name")
SOURCE_TABLE_ID = Variable.get("source_table")
SOURCE_PRIMARY_KEY = Variable.get("source_table_primary_key")

default_args = {
    'owner':'Ramjan',
    'depends_on_past':False,
    'email_on_failure':False,
    'email_on_retry':False,
    'retry_delay':timedelta(minutes=1),
    'retries':1
}
def extract_and_load(mysql_conn_id,
                     source_table,
                     primary_key,
                     gcp_conn_id,
                     project_id,
                     dataset_id,
                     target_table
                     ):
    total_source = 0
    total_target = 0

    first_batch = True
    for df in extract_mysql_pagged(mysql_conn_id,
                            source_table,
                            primary_key,
                            batch_size=100):
        total_source +=len(df)

        write_mode = ("WRITE_TRUNCATE" if first_batch else "WRITE_APPEND")
        loaded_rows = load_batch_to_bigquery(gcp_conn_id,
                               project_id,
                               dataset_id,
                               target_table,
                               data_frame=df,
                               write_disposition=write_mode)
        total_target +=loaded_rows
        first_batch = False
        print(f"Loaded Batched Rows: {loaded_rows}")
    return {
        "source_count":total_source,
        "target_count":total_target
    }


        



with DAG(dag_id="batch_mysql_to_bq_paging",
         description="migrate large volumnes of data from mysql to BigQuery using paging",
         default_args=default_args,
         start_date=datetime(2026, 7, 12),
         schedule_interval='@Daily',
         catchup=False
         ) as dag:
    start = EmptyOperator(
        task_id="start"
    )
    end = EmptyOperator(
        task_id="end"
    )

    extract_and_load_task = PythonOperator(
        task_id="extract_and_load",
        python_callable=extract_and_load,
        op_kwargs={
            "mysql_conn_id":"mysql_conn_id",
            "source_table":SOURCE_TABLE_ID,
            "primary_key":SOURCE_PRIMARY_KEY,
            "gcp_conn_id":"google_cloud_default",
            "project_id":PROJECT_ID,
            "dataset_id":DATASET_ID,
            "target_table":TABLE_ID

        }
    )


start >> extract_and_load_task >>  end