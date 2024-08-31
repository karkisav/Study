from um import count


def test_normal():
    assert count("um") == 1
    assert count("hi, there") == 0
    assert count("Um, thanks, um...") == 2

def test_inbetween():
    assert count("hi there did i um, leave my umbrella perhaps") == 1
    assert count("Did you watch the latest album?") == 0
    assert count("  um    ") == 1

def test_end():
    assert count("Did you watch the latest album?") == 0