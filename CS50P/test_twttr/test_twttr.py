from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("WhAt's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"