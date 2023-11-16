from unittest.mock import Mock
from lib.music_library import *

"""
When tracks added
can list tracks correctly
"""
track_1 = Mock()
track_2 = Mock()
library = MusicLibrary()
library.add(track_1)
library.add(track_2)
assert library.tracks == [track_1, track_2]


"""
If no tracks in track list
returns empty list when searching
"""
def test_returns_empty_list_when_no_tracks_in_list():
    library = MusicLibrary()
    assert library.search('Ladders') == []


"""
If search doesn't match any tracks
returns empty list
"""
def test_returns_empty_list_when_no_tracks_matching():
    library = MusicLibrary()
    track_1 = Mock()
    track_1.matches.return_value = False
    library.add(track_1)
    assert library.search('Ladders') == []


"""
If search matches tracks
returns tracks in list
"""
def test_returns_tracks_in_list_if_matching():
    library = MusicLibrary()
    track_1 = Mock()
    track_1.matches.return_value = True
    track_1.title = 'Ladders'
    track_1.artist = 'Mac Miller'
    track_2 = Mock()
    track_2.matches.return_value = True
    track_2.title = 'Small Worlds'
    track_2.artist = 'Mac Miller'
    library.add(track_1)
    library.add(track_2)
    assert library.search('Mac Miller') == [track_1, track_2]