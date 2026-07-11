from airflow.providers.postgres.hooks.postgres import PostgresHook



def create_manifest(
        postgres_conn_id,
        run_id,
        dag_id,
        source_system,
        source_table,
        source_row_count
):
    hook = PostgresHook(postgres_conn_id=postgres_conn_id)
    sql = """
    INSERT INTO etl_manifest
    (
    run_id,
    dag_id,
    source_system,
    source_table,
    source_row_count,
    status,
    start_time
    )
    VALUES
    (
        %s,
        %s,
        %s,
        %s,
        %s,
        'RUNNING',
        NOW()
    );
    """

    hook.run(
        sql,
        parameters=(
            run_id,
            dag_id,
            source_system,
            source_table,
            source_row_count,
        ),
    )




def complete_manifest(
        postgres_conn_id,
        run_id,
        source_table,
        target_system,
        target_table,
        target_row_count,
        status,
        error_message=None,
):
    hook = PostgresHook(postgres_conn_id=postgres_conn_id)

    sql="""
    UPDATE etl_manifest
    SET
        target_system=%s,
        target_table=%s,
        target_row_count=%s,
        status=%s,
        error_message=%s,
        end_time = NOW()
   WHERE run_id=%s
   AND source_table=%s
    """

    hook.run(
        sql,
        parameters=(
            target_system,
            target_table,
            target_row_count,
            status,
            error_message,
            run_id,
            source_table
        ),
    )