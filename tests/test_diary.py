from lib.diary import *

"""
Can return the contents of diary
"""
def test_returns_contents_of_diary():
    diary = Diary('Hello, this is a diary.')
    assert diary.read() == 'Hello, this is a diary.'


"""
If diary contents empty
Returns empty string
"""
def test_returns_empty_string_if_contents_empty():
    diary = Diary('')
    assert diary.read() == ''