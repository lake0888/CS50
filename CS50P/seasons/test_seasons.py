from seasons import _minutes, convert


def test_minutes():
    assert _minutes(365) == 525600
    assert _minutes(730) == 1051200
    assert _minutes(731) == 1052640
    assert _minutes(12410) == 17870400

def test_convert():
    assert convert(525600) == "five hundred twenty-five thousand, six hundred minutes"
    assert convert(1051200) == "one million, fifty-one thousand, two hundred minutes"
    assert convert(17942400) == "seventeen million, nine hundred forty-two thousand, four hundred minutes"