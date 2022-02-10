from datetime import datetime


def countdown(date=datetime.now()):
    new_year = datetime(date.year + 1, 1, 1)
    days_left = (new_year - date).days
    return days_left
