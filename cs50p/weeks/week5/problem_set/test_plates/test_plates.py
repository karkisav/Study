from plates import is_valid

def test_length():
    assert is_valid("a") == False
    assert is_valid("OUTAIME") == False

def test_alpha():
    assert is_valid("50Cs") == False
    assert is_valid("50") == False

def test_numbers():
    assert is_valid("Cs50") == True
    assert is_valid("Cs50p") == False

def test_zero_placement():
    assert is_valid("Cs05") == False

def test_specialChars():
    assert is_valid("PI3.14") == False