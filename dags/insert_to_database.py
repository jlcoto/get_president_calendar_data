import os

from bs4 import BeautifulSoup

from utils import format_date_scrape, get_s3_client

client = get_s3_client()


def insert_into_database():
    s3_object = client.get_object(Bucket=os.environ.get('AWS_DATA_LAKE_BUCKET'), Key='2019-02-05_visits')
    raw_data = s3_object['Body'].read()
    process_data = BeautifulSoup(raw_data, 'lxml')
    columns = [column.text.strip() for column in process_data.findAll('th')]
    column_dict = {number: column for number, column in enumerate(columns)}
    list_of_rows = [row.findAll('td') for row in process_data.findAll('tr')]

    results = []
    for row in list_of_rows:
        results_dictionary = {}
        if len(row) == 0:
            pass
        else:
            results_dictionary = {column_dict[number]:
                                  col_content.text.strip() for number, col_content in enumerate(row)}
            results.append(results_dictionary)
