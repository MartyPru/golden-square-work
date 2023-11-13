from lib.string_builder import *

def test_builds_strings_given_and_returns_correct_length():
    builder = StringBuilder()
    builder.add("Hello, ")
    builder.add("World!")
    size = builder.size()
    assert size == 13
    final_string = builder.output()
    assert final_string == "Hello, World!"
