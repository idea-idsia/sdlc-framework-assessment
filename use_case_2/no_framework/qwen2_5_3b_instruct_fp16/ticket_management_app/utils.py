from datetime import date, timedelta

def format_date(date):
    return date.strftime('%Y-%m-%d %H:%M:%S')

def convert_date_to_datetime(datetime_str):
    return date.fromisoformat(datetime_str)