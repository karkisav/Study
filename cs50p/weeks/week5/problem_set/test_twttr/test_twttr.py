from twttr import shorten

def test_default():
    for letter in ["a", "e", "i", "o", "u"]:
        assert shorten(letter) == ""

def test_str_small():
    assert shorten("saurav") == "srv"

def test_str_camel():
    assert shorten("sAuRav") == "sRv"

def test_str_punct():
    assert shorten("Hi this is, Cs50") == "H ths s, Cs50"