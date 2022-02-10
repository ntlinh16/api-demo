from datetime import datetime
from api_demo.mydate import countdown



def test_countdown_default():
    days = countdown()
    assert isinstance(days, int)
    assert 0 <= days <= 365


def test_countdown_with_correct_date():
    days = countdown(datetime.now())
    assert isinstance(days, int)
    assert 0 <= days <= 365


def test_countdown_with_wrong_date():
    today = datetime.now()
    date = datetime(today.year + 1, today.month, today.day)
    days = countdown(date)
    assert isinstance(days, int)
    assert 0 <= days <= 365


