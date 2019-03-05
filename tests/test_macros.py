import datetime as dt

from plugins.macros import format_date_scrape

def test_format_date_scrape():
    formatted_date = format_date_scrape('2007-07-08')
    assert formatted_date == '08/07/2007'
