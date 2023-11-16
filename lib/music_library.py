class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def search(self, keyword):
        for track in self.tracks:
            track.matches(keyword)
        matching = [f"{track.title} by {track.artist}" for track in self.tracks if track.matches() == True]
        return matching
        