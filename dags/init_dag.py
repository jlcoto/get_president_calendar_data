import datetime as dt
import os

from dotenv import load_dotenv

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from upload_visitors_data import upload_visitors_data

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

    get_calendar_data = PythonOperator(task_id='upload_visitors_data',
                                       python_callable=upload_visitors_data,
                                       provide_context=True,
                                       )
