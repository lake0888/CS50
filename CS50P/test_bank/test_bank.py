from bank import value

def test_hello():
    assert value("Hello") == 0

def test_h():
    assert value("Hi") == 20

def test_other():
    assert value("What's up") == 100