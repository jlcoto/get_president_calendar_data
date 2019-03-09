import datetime as dt
import os

import boto3

def format_date_scrape(date):
    return dt.datetime.strptime(date, '%Y-%m-%d') \
             .strftime('%d/%m/%Y')

def get_s3_client():
    session = boto3.Session(profile_name=os.environ.get('AWS_USER'))

    client = session.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
    )
    return client
