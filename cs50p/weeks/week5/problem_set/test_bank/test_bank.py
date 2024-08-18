from bank import value

def test_default():
    assert value("hello !!!") == 0

def test_upper():
    assert value("Hello !!!") == 0
    assert value("Hi") == 20

def test_camel():
    assert value("HiiIiI") == 20
    assert value("What Are you doing today") == 100