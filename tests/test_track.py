from lib.track import *

"""
If doesn't match to track
returns False
"""
def test_returns_false_for_no_match():
    track = Track('Self Care', 'Mac Miller')
    assert track.matches('Come Back to Earth') == False

"""
If doesn't match to artist
returns False
"""
def test_returns_false_for_no_match():
    track = Track('Self Care', 'Mac Miller')
    assert track.matches('Kendrick Lamar') == False

"""
Correctly matches title
"""
def test_matches_title_of_track():
    track = Track('Self Care', 'Mac Miller')
    assert track.matches('Self Care') == True


"""
Correctly matches artist
"""
def test_matches_artist_of_track():
    track = Track('Self Care', 'Mac Miller')
    assert track.matches('Mac Miller') == True


"""
Returns true for partial matches
"""
def test_returns_true_partial_match():
    track = Track('Self Care', 'Mac Miller')
    assert track.matches('Care') == True
