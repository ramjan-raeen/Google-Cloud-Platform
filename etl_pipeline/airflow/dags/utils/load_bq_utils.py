# @task

from google.cloud import bigquery
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook




def load_bigquery(gcp_conn_id, project_id, dataset_id, table_name, file_name):

    hook = BigQueryHook(
        gcp_conn_id=gcp_conn_id,
        use_legacy_sql=False,

    )
    client = hook.get_client(project_id=project_id)


    table_id = f"{project_id}.{dataset_id}.{table_name}"
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        source_format = bigquery.SourceFormat.PARQUET,
        autodetect = True
    )
    with open(file_name, 'rb') as source:
        job = client.load_table_from_file(
            source,
            table_id,
            job_config=job_config

        )
        job.result()
        table = client.get_table(table_id)
        target_count =table.num_rows
        print(f"Loaded {target_count} rows into BigQuery table: {table} Successfully !!")
        return target_count
