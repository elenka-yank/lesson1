from airflow import DAG
from airflow.operators import PythonOperator
from datetim import datetime

default_args = {
  'owner':'eyank',
  'depends_on_past': False,
  'start_date': 'datetime(2018, 1, 1)',
  'retries': 0
}

dag = DAG('python_hello_world_dag',
         default_args=default_args,
         catchup=False,
         schedule_interval='00 20 * * *')

def hello():
  return print('hello, world')

def sum_int():
  return print(2+2)

# def my_name():
#   return print ('i am Elena')

# def sys_path():
#   return print(pathlib.Path(__file__).parent.absolute())

t1 = PythonOperator(
  task_id = 'print_hello_world',
  python_callable = hello,
  dag = dag)

t2 = PythonOperator(
  task_id = 'sum_task',
  python_callable = sum_int,
  dag = dag)
t1 >> t2
