from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.get_size() == 0
    with pytest.raises(ValueError):
        jar.capacity = -1

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.get_size() == 5
    jar.deposit(5)
    assert jar.get_size() == 10
    with pytest.raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.get_size() == 7
    jar.withdraw(5)
    assert jar.get_size() == 2
    with pytest.raises(ValueError):
        jar.withdraw(5)