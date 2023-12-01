from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    i = 2
    while i < 99:
        assert gauge(i) == f"{i}%"
        i += 1