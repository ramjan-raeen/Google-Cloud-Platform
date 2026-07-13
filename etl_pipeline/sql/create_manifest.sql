select current_database();
CREATE TABLE etl_manifest
(
    run_id             VARCHAR(100),
    dag_id             VARCHAR(100),

    source_system      VARCHAR(30),
    source_table       VARCHAR(100),
    source_row_count   BIGINT,

    target_system      VARCHAR(30),
    target_table       VARCHAR(200),
    target_row_count   BIGINT,

    status             VARCHAR(20),

    start_time         TIMESTAMP,
    end_time           TIMESTAMP,

    error_message      TEXT,

    PRIMARY KEY(run_id, source_table)
);


