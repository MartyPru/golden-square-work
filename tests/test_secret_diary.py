from unittest.mock import Mock
from lib.secret_diary import *
import pytest

"""
Initially
diary is locked
"""
def test_diary_initially_locked():
    diary = Mock()
    diary.contents = "This is a diary."
    secret_diary = SecretDiary(diary)
    assert secret_diary.locked == True

"""
If diary is locked
Returns "Go Away"
"""
def test_raises_go_away_when_locked():
    diary = Mock()
    diary.contents = "This is a diary."
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == 'Go away!'


"""
Can unlock diary
"""
def test_can_unlock_diary():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.locked == False

"""
Can lock diary
"""
def test_can_lock_diary():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.locked == True



"""
If diary is unlocked
Returns diary contents
"""
def test_returns_contents_if_unlocked():
    diary = Mock()
    diary.contents = "This is a diary."
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'This is a diary.'