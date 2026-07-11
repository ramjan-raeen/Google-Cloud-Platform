from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook


def validate(gcp_conn_id, project_id, dataset_id, table_name):
    hook = BigQueryHook(
        gcp_conn_id=gcp_conn_id,
        use_legacy_sql=False
    )
    client = hook.get_client(project_id=project_id)
    query = f"""
    SELECT COUNT(*) as row_count FROM `{project_id}.{dataset_id}.{table_name}`
    """
    result = client.query(query).result()
    for row in result:
        print(f"BigQuery Rows: {row.row_count}")
