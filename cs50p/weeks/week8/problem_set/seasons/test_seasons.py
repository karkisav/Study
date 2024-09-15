import pytest
from datetime import date
from seasons import DateToMins

def test_valid_date():
    dtm = DateToMins("2023-10-01")
    assert dtm.valid() == date(2023, 10, 1)
    dtm = DateToMins("1999-09-09")
    assert dtm.valid() == date(1999, 9, 9)

def test_invalid_date():
    with pytest.raises(SystemExit):
        dtm = DateToMins("0000-00-00")
        dtm.valid()
    with pytest.raises(SystemExit):
        dtm = DateToMins("Jan First 2021")
        dtm.valid()
