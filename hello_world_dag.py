from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

# Define the Python function to be executed
def helloWorld():
    print("Hello, Airflow!")

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}
def helloWorld():
    print("TEST")
# Define the DAG
with DAG(dag_id="hello_world_dag",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:
      
      task1 = PythonOperator(
        task_id="hello_world",
        python_callable=helloWorld)

task1
