import pytest
from lib.password_checker import *

def test_password_checker_class_when_valid():
    checker = PasswordChecker()
    is_valid = checker.check('123456789')
    assert is_valid == True

def test_password_checker_class_error():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        is_valid = checker.check('123')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."