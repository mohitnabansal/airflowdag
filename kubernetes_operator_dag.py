from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define the DAG
with DAG(
    'kubernetes_operator_dag',
    default_args=default_args,
    description='A simple KubernetesPodOperator DAG',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
) as dag:

    # Define the KubernetesPodOperator task
    k8s_task = KubernetesPodOperator(
        namespace='default',
        image="python:3.8-slim",
        cmds=["python", "-c"],
        arguments=["print('Hello from KubernetesPodOperator')"],
        labels={"foo": "bar"},
        name="k8s_task",
        task_id="k8s_task",
        get_logs=True,
    )

    k8s_task