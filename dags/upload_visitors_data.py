import os
import requests
import tempfile

import boto3

import values
from utils import format_date_scrape

session = boto3.Session(profile_name=os.environ.get('AWS_USER'))

client = session.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
)

def upload_visitors_data(ts, ds, *args, **kwargs):
    formatted_date = format_date_scrape(ds)

    VISITS_URL = values.VISITS_URL
    data = {'valorCaja1': formatted_date}
    response = requests.post(VISITS_URL, data=data)
    data = response.content
    key_name = f"{ds}_visits"

    with tempfile.NamedTemporaryFile(mode='w+b') as temp:
        temp.write(data)
        temp.seek(0)
        client.upload_file(temp.name, os.environ.get('AWS_DATA_LAKE_BUCKET'), key_name)
