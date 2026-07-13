# Author    :   Ramjan Raeen
# Date      :   2026-07-13
# Modified  :   2026-07-13
# Purpose   :   Extract large volume of data from source system using paging.


import pandas as pd
from airflow.providers.mysql.hooks.mysql import MySqlHook

def extract_mysql_pagged(mysql_conn_id,
                         source_table,
                         primary_key,
                         batch_size=10000):
    hook = MySqlHook(mysql_conn_id=mysql_conn_id)
    engine = hook.get_sqlalchemy_engine()
    last_id = 0
    total_rows = 0

    while True:

        query = f"""
        SELECT * FROM {source_table} WHERE {primary_key} > {last_id} ORDER BY {primary_key} LIMIT {batch_size}
        """
        df = pd.read_sql(query,
                         engine
                        )
        print(f"Query: {query}")
        if df.empty:
            break

        total_rows +=len(df)

        yield df

        last_id = df[primary_key].max()
        print(f"max last_id : {last_id}")
    print(f"Total Extracted Rows: {total_rows}")


