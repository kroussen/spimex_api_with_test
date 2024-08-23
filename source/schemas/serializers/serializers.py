from datetime import date, datetime


def datetime_to_string(obj):
    if isinstance(obj, (date, datetime)):
        return obj.strftime('%Y-%m-%d')
