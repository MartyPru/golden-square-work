from lib.check_codeword import *

def test_check_codeword_for_horse_returns_correct():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'

def test_check_codeword_for_first_and_last_returns_close():
    result = check_codeword('house')
    assert result == 'Close, but nope.'

def test_check_codeword_returns_wrong():
    result = check_codeword('password')
    assert result == 'WRONG!'