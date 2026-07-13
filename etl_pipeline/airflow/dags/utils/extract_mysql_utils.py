# Author    :   Ramjan Raeen
# Date      :   2026-07-12
# Modified  :   2026-07-14
# Purpose   :   created utils package to extract source data from mysql database. 

import pandas as pd
from sqlalchemy import create_engine

def extract_mysql(mysql_user, mysql_pass, mysql_host, mysql_port, mysql_db, temp_file):
    engine = create_engine(
        f"mysql+pymysql://{mysql_user}:{mysql_pass}"
        f"@{mysql_host}:{mysql_port}/{mysql_db}"
    )
    sql = open("/opt/airflow/sql/dim_date.sql").read()
    df = pd.read_sql(sql, engine)
    print(df.head())
    df.to_parquet(temp_file, index=False)
    print(f"Extracted rows: {len(df)}")
    source_count = len(df)
    return source_count
