from lib.time_error import *
from unittest.mock import Mock
"""
Correctly finds difference between external time and local time.
"""
def test_finds_difference_between_external_and_local_time():
    requester = Mock()
    requester.get().json.return_value = {"abbreviation":"GMT","client_ip":"82.163.117.26","datetime":"2023-11-16T14:28:48.199803+00:00",
                                         "day_of_week":4,"day_of_year":320,"dst":False,"dst_from":None,"dst_offset":0,"dst_until":None,"raw_offset":0,
                                         "timezone":"Europe/London","unixtime":1700144928,"utc_datetime":"2023-11-16T14:28:48.199803+00:00","utc_offset":"+00:00",
                                         "week_number":46}
    time = Mock()
    time.time.return_value = 1700144927
    error_find = TimeError(requester, time)
    assert error_find.error() == 1