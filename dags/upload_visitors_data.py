import os
import requests
import tempfile

from airflow.exceptions import AirflowException

import values
from utils import format_date_scrape, get_s3_client

client = get_s3_client()

def upload_visitors_data(prev_ds, *args, **kwargs):
    formatted_date = format_date_scrape(prev_ds)
    VISITS_URL = values.VISITS_URL
    data = {'valorCaja1': formatted_date}
    response = requests.post(VISITS_URL, data=data)
    if response.ok:
        key_name = f"{prev_ds}_visits"
        with tempfile.NamedTemporaryFile(mode='w+b') as temp:
            temp.write(response.content)
            temp.seek(0)
            client.upload_file(temp.name, os.environ.get('AWS_DATA_LAKE_BUCKET'), key_name)
    else:
        raise AirflowException("Request failed.")
