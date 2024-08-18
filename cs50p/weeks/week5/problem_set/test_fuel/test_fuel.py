import pytest
from fuel import convert, gauge

def test_convert_int():
    assert convert("1/2") == 50
    assert convert("3/4") == 75

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("cat/car")
    with pytest.raises(ValueError):
        convert("1/2/3")
    with pytest.raises(ValueError):
        convert("2/1")

def test_convert_ZeroError():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge_Full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    
def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"

