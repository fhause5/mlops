from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator

default_arg = {'owner': 'airflow', 'start_date': '2020-02-28'}

dag = DAG('simple-mysql-dag',
          default_args=default_arg,
          schedule_interval='0 0 * * *')

mysql_task = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql_default',
                           task_id='mysql_task',
                           sql='sample_sql.sql',
                           params={'test_user_id': -99})

mysql_task