from hello import hello

def test_argument():
    for name in ["Hermoine", "Ron"]:
        assert hello(name) == "hello, {name}"
def test_default():
    assert hello() == "hello, world"