from unittest.mock import Mock
from lib.music_library import *
from lib.track import *

"""
When tracks added
can list tracks correctly
"""
track_1 = Track("Come Back to Earth", 'Mac Miller')
track_2 = Track("2009", 'Mac Miller')
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
    track_1 = Track("So It Goes", "Mac Miller")
    library.add(track_1)
    assert library.search('Ladders') == []


"""
If search matches tracks
returns tracks in list
"""
def test_returns_tracks_in_list_if_matching():
    library = MusicLibrary()
    track_1 = Track("Jet Fuel", "Mac Miller")
    track_2 = Track("OUTTA MY MIND", "Monsune")
    track_3 = Track("Dunno", "Mac Miller")
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    assert library.search('Mac Miller') == [track_1, track_3]