from lib.report_length import *

"""
For given string, return correct length in characters
"""

def test_return_correct_length():
    result = report_length('Hello')
    assert result == 'This string was 5 characters long.'


"""
Returns 0 for empty string
"""

def test_return_0_for_empty_string():
    result = report_length('')
    assert result == 'This string was 0 characters long.'