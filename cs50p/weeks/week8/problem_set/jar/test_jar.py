import pytest
from jar import Jar

def test_deposit():
    n = Jar()
    n.deposit(2)
    assert n.size == 2

    n.deposit(10)
    assert n.size == 12

    with pytest.raises(ValueError):
        n.deposit(1)
    
def test_withdraw():
    n = Jar()
    n.deposit(12)

    n.withdraw(9)
    n.size == 3

    n.withdraw(3)
    n.size == 0

    with pytest.raises(ValueError):
        n.withdraw(1)

def test_string():
    n = Jar()

    n. deposit(3)
    assert str(n) == "🍪🍪🍪"

    n.withdraw(1)
    assert str(n) == "🍪🍪"

    n.withdraw(2)
    assert str(n) == ""

def test_invalid():
    n = Jar()
    with pytest.raises(ValueError):
        n.deposit("a")
    
    with pytest.raises(ValueError):
        n.deposit("1")
    
    with pytest.raises(ValueError):
        n.deposit("a")

    with pytest.raises(ValueError):
        n.deposit("3")