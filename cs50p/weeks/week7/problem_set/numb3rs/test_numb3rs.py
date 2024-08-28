from numb3rs import validate

def test_blanks():
    assert validate("1.5.36.") == False
    assert validate("") == False
    assert validate("1.3..36") == False
    assert validate(".1.4.54") == False
def test_alphas():
    assert validate("cat") == False
    assert validate("cat.1.4.54") == False
    assert validate("1.3.cat.36") == False
    assert validate("1.5.36.cat") == False
def test_invalid():
    assert validate("0.275.4.54") == False
    assert validate("0.0.1.4.54") == False
    assert validate("512.512.4.54") == False
def test_valid():
    assert validate("0.0.0.0") == True
    assert validate("0.0.1.255") == True
    assert validate("255.255.255.255") == True