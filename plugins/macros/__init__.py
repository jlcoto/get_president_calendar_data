import datetime as dt

def format_date_scrape(date):
    return dt.datetime.strptime(date, '%Y-%m-%d') \
             .strftime('%d/%m/%Y')
