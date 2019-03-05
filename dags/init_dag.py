import datetime as dt

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from airflow.macros.data_lake_presidential_visitors import (
    format_date_scrape)

from get_calendar_data import get_calendar_data

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2017, 6, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
    'user_defined_macros': {
        'format_date_scrape': format_date_scrape
    },
}

with DAG('get_president_agenda',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:

    get_calendar_data = PythonOperator(task_id='get_calendar_data',
                                       python_callable=get_calendar_data,
                                       provide_context=True,
                                       )
