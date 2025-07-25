class CircularPlaylist:
    def __init__(self, items):
        self.items = items
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if not self.items:
            raise StopIteration
        item = self.items[self.index]
        self.index = (self.index + 1) % len(self.items)
        return item

songs = ["Track A", "Track B", "Track C"]
player = CircularPlaylist(songs)
print("Playlist (10 items):")
for i, song in enumerate(player):
    print(song, end=" | ")
    if i >= 9:
        break
# Output: Track A | Track B | Track C | Track A | Track B | Track C | Track A | Track B | Track C | Track A |
