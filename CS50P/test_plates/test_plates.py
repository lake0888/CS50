from plates import is_valid

def test_twoletters():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("50") == False

def test_sizelessthan2():
    assert is_valid("C") == False

def test_sizemorethan6():
    assert is_valid("CS50000") == False

def test_numberatend():
    assert is_valid("CS50P") == False
    assert is_valid("CS5000") == True

def test_firstnumber0():
    assert is_valid("CS05") == False

def test_alphanumeric():
    assert is_valid("PI3.14") == False
