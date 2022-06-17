from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

our_first_dag = DAG(
    "first_dag",
    start_date=days_ago(0, 0, 0, 0, 0),
    tags=['bash']
)
operation_1 = BashOperator(
    bash_command="""echo "completed" """,
    dag=our_first_dag,
    task_id='operation_1'
)

operation_2 = BashOperator(
    bash_command="sleep 20",
    dag=our_first_dag,
    task_id='operation_2'
)

operation_1 >> operation_2
