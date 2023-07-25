from bank import value

def test_hello():
    assert value("Hello") == 100
    assert value("Hello!") == 100
    assert value("Hello, Damian") == 100

def test_h():
    assert value("Hi") == 20
    assert value("Hey.") == 20
    assert value("Hi, Mark!") == 20
    assert value("Hey, Mark!") == 20
    assert value("How's it going, Man?") == 20

def test_non_h():
    assert value("What's up?") == 0
    assert value("What's up?, Mark!") == 0
    assert value("Yo Mark!") == 0
    assert value("Wazza!") == 0