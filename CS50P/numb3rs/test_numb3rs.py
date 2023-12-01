import pytest
import warnings
from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("192.168.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("255.255.255.300") == False
    assert validate("cat") == False
    assert validate("10.0.0.cat") == False

