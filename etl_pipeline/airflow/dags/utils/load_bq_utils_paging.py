# Author    :   Ramjan Raeen
# Date      :   2026-07-13
# Modified  :   2026-07-13
# Purpose   :   Load batch data to gcp bigquery table.

from google.cloud import bigquery
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook


def load_batch_to_bigquery(gcp_conn_id,
                           project_id,
                           dataset_id,
                           target_table,
                           data_frame,
                           write_disposition="WRITE_APPEND"):
    hook = BigQueryHook(gcp_conn_id=gcp_conn_id,
                        use_legacy_sql=False)
    
    client = hook.get_client(project_id=project_id)

    job_config = bigquery.LoadJobConfig(write_disposition=write_disposition,
                                        autodetect=True)
    table_id = f"{project_id}.{dataset_id}.{target_table}"
    job = client.load_table_from_dataframe(
        data_frame,
        table_id,
        job_config=job_config
    )
    job.result()
    return len(data_frame)