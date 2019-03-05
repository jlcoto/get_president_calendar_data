from airflow.plugins_manager import AirflowPlugin

from macros import format_date_scrape


class DRTDataLakePlugin(AirflowPlugin):
    name = 'data_lake_presidential_visitors'
    macros = [format_date_scrape]
