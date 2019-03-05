import datetime as dt

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from get_calendar_data import get_calendar_data

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2017, 6, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('get_president_agenda',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:

    get_calendar_data = PythonOperator(task_id='get_calendar_data',
                                       python_callable=get_calendar_data,
                                       provide_context=True,
                                       )
