import json
import random
import time
import os
from functools import wraps

# Decorator to repeat the playlist
def repeat_playlist(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        while True:
            for song in self.songs:
                yield song
    return wrapper

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.current_index = 0

    def add_song(self, song):
        """Add a song to the playlist."""
        self.songs.append(song)

    def shuffle(self):
        """Shuffle the playlist."""
        random.shuffle(self.songs)

    def save_to_json(self, filename):
        """Save the playlist to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([song.__dict__ for song in self.songs], file)
        except IOError as e:
            print(f"Error saving to {filename}: {e}")

    def load_from_json(self, filename):
        """Load the playlist from a JSON file."""
        try:
            with open(filename, 'r') as file:
                songs_data = json.load(file)
                self.songs = [Song(**song) for song in songs_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from {filename}: {e}")

    @repeat_playlist
    def play(self):
        """Play the playlist."""
        while True:
            yield self.songs[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.songs)

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __repr__(self):
        return f"{self.title} by {self.artist} ({self.duration} mins)"

# Example usage
if __name__ == "__main__":
    # Create songs
    song1 = Song("Song 1", "Artist 1", 3.5)
    song2 = Song("Song 2", "Artist 2", 4.0)
    song3 = Song("Song 3", "Artist 3", 2.8)

    # Create playlist and add songs
    playlist = Playlist("My Playlist")
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)

    # Shuffle playlist
    playlist.shuffle()

    # Save playlist to JSON
    playlist.save_to_json("playlist.json")

    # Load playlist from JSON
    new_playlist = Playlist("Loaded Playlist")
    new_playlist.load_from_json("playlist.json")

    # Play the playlist
    for song in new_playlist.play():
        print(song)
        # Simulate playing song for its duration
        time.sleep(song.duration * 60)
