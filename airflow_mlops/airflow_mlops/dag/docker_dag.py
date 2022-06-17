from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

docker_dag = DAG(
    "docker_dag",
    start_date=days_ago(0, 0, 0, 0, 0),
    tags=['DockerOperator']
)

operation_1 = DockerOperator(
    task_id='docker_command',
    image='centos:latest',
    command="/bin/sleep 30",
    dag=docker_dag
)

operation_1
