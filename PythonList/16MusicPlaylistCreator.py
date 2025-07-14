# Music Playlist Creator

# Initial playlist
playlist = ["Shape of You", "Levitating", "Blinding Lights"]

# Add new song
new_song = input("Enter a song to add: ").strip().title()
playlist.append(new_song)

# Remove a song
remove_song = input("Enter a song to remove: ").strip().title()
if remove_song in playlist:
    playlist.remove(remove_song)
else:
    print("Song not found in playlist.")

# Repeat the playlist 2 times
print("\nYour Playlist Repeated Twice:")
print(playlist * 2)

# Display all songs
print("\nCurrent Playlist:")
for song in playlist:
    print("-", song)

# Search for a song
search = input("\nEnter a song to search: ").strip().title()
if search in playlist:
    print(f"'{search}' is in your playlist.")
else:
    print(f"'{search}' is not in the playlist.")
