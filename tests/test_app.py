from helloworld.app import greeting


def test_first():
    "An initial test for the app"
    assert 1 + 1 == 2


def test_greeting():
    """Check that the greeting function works"""
    assert greeting("Toga") == "Hello, Toga"
    """Check that the greeting function works with an empty string"""
    assert greeting("") == "Hello, stranger"
    """If the name is Brutus, the greeting should be different"""
    assert greeting("Brutus") == "All hail Beeware!"
