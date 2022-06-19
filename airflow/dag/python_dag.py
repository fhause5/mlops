import os

import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from airflow.utils.dates import days_ago

our_second_dag = DAG(
    "second_dag",
    description='Python DAG example',
    schedule_interval="* * * * *",
    start_date=days_ago(0, 0, 0, 0, 0),
    tags=['python'],
    doc_md='*Python DAG doc* :)'
)


def download_titanic_dataset():
    df = pd.read_csv("https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")
    df.to_csv("df.csv")


download_dataframe = PythonOperator(
    task_id='download_titanic_dataset',
    python_callable=download_titanic_dataset,
    dag=our_second_dag
)


def transform_titanic_dataset():
    df = pd.read_csv("df.csv")
    del df['Unnamed: 0']
    gr = df.groupby("Pclass").agg({"Survived": "mean"})
    gr.to_csv("output.csv")


transform_dataframe = PythonOperator(
    task_id='transform_dataset',
    python_callable=transform_titanic_dataset,
    dag=our_second_dag
)

get_output = BashOperator(
    bash_command="""cat /tmp/output.csv """,
    dag=our_second_dag,
    task_id='operation_3'
)

os.chdir("/tmp")

download_dataframe >> transform_dataframe >> get_output