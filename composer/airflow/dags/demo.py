# Author        :   Ramjan Raeen
# Date          :   2026-04-04
# Last Modified :   2026-04-04
# Purpose       :   This dag is created to understand all possible essential operators and cross functions.





from datetime import datetime, timedelta

import random
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.trigger_rule import TriggerRule

default_args = {
    'owner':'Ramjan',
    'depends_on_past':False,
    'email_on_failure':False,
    'email_on_retry':False,
    'retry_delay':timedelta(minutes=1),
    'retries':1
    
}

def choose_arbitrary_number(a, b):
    return random.randint(a, b)

def classify_number(ti):
    num = ti.xcom_pull(task_ids='choose_arbitrary_number', key='return_value')
    print(f"num : {num},   type: {type(num)}")
    if num % 2 ==0:
        return 'even_number'
    else:
        return 'odd_number'
    
def even_number_list(ti):
    num = ti.xcom_pull(task_ids='choose_arbitrary_number', key='return_value')
    return [n for n in range(num) if n % 2 ==0]

def odd_number_list(ti):
    num = ti.xcom_pull(task_ids='choose_arbitrary_number', key='return_value')
    return [n for n in range(num) if n % 2 !=0]

def dags_context_vars(*args, **kwargs):
    print(f"args[0] : {args[0]} and args[1] : {args[1]}")
    print(f"orchestration               :   {kwargs['orchestration']}")
    print(f"airflow version             :   {kwargs['airflow_version']}")
    print(f"kwargs                      :   {kwargs}")
    print()
    print(f"DAG_RUN                     :   {kwargs['dag_run']}")
    print(f"DAG ID                      :   {kwargs['dag'].dag_id}")
    print(f"DAG ID                      :   {kwargs['dag_run'].dag_id}")
    print(f"RUN ID                      :   {kwargs['dag_run'].run_id}")
    print(f"LOGICAL DATE                :   {kwargs['dag_run'].logical_date}")
    print(f"DATA INTERVAL START DATE    :   {kwargs['dag_run'].data_interval_start}")
    print(f"DATA INTERVAL END DATE      :   {kwargs['dag_run'].data_interval_end}")
    print(f"START DATE                  :   {kwargs['dag_run'].start_date}")
    print(f"END DATE                    :   {kwargs['dag_run'].end_date}")
    print(f"RUN TYPE                    :   {kwargs['dag_run'].run_type}")
    print(f"TASK CLEAR NUMBER           :   {kwargs['dag_run'].clear_number}")
    print(f"TASK ID                     :   {kwargs['ti'].task_id}")
    print(f"TASK START DATE             :   {kwargs['ti'].start_date}")
    print(f"TASK END DATE               :   {kwargs['ti'].end_date}")



with DAG(
    dag_id="demo",
    default_args=default_args,
    description="demonstration of actual DAG implementation",
    start_date=datetime(2026,4,3),
    schedule="0 8,20 * * *", # Schedule at 8:00 AM and 8:00 PM UTC, Everyday!!
    catchup=False
) as dag:
    task_start = EmptyOperator(
        task_id = "start"
    )
    task_01 = PythonOperator(
        task_id = 'choose_arbitrary_number',
        python_callable = choose_arbitrary_number,
        op_args = [0, 10]
    )
    task_02 = BranchPythonOperator(
        task_id='classify_number',
        python_callable=classify_number
    )
    task_03 = PythonOperator(
        task_id='even_number',
        python_callable=even_number_list
    )
    task_04 = PythonOperator(
        task_id='odd_number',
        python_callable=odd_number_list
    )
    task_05 = PythonOperator(
        task_id='dags_context_vars',
        python_callable = dags_context_vars,
        op_args = [10, 100],
        op_kwargs = {'orchestration':'docker-compose', 'airflow_version':'3.0.1'},
        trigger_rule=TriggerRule.ONE_SUCCESS
    )

    task_end = EmptyOperator(
        task_id = 'end',
        trigger_rule =TriggerRule.ALL_SUCCESS 
    )

task_start >> task_01 >> task_02
task_02 >> [task_03, task_04] >> task_05 >> task_end
