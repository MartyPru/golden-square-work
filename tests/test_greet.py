from lib.greet import *

def test_greet_returns_greeting_for_marty():
    result = greet('Marty')
    assert result == 'Hello, Marty!'