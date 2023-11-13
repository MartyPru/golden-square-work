import pytest
from lib.present import *

def test_present_unwrap_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message  = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_present_wrap_error():
    present = Present()
    present.wrap("Hello, this is a present.")
    with pytest.raises(Exception) as e:
        present.wrap("This is another present, will it fit in the same box?")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."