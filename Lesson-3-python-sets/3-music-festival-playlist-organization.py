class MusicFestivalOrganizer:
    def __init__(self, artist_names=None, artists_genres=None, playlists=None):
        self.artist_names = artist_names or []
        self.artists_genres = artists_genres or {}
        self.playlists = playlists or []

    def compile_unique_lineup(self):
        unique_artists = set(self.artist_names)
        return unique_artists

    def categorize_by_genre(self):
        genre_categories = {}
        for artist, genre in self.artists_genres.items():
            if genre not in genre_categories:
                genre_categories[genre] = {artist}
            else:
                genre_categories[genre].add(artist)
        return genre_categories

    def check_playlist_duplication(self):
        unique_playlists = set(frozenset(playlist) for playlist in self.playlists)
        return len(unique_playlists) != len(self.playlists)

# Example data
artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock"
}
playlists = [
    {"Song A", "Song B", "Song C"},
    {"Song D", "Song E", "Song F"},
    {"Song A", "Song B", "Song C"}
]

# Creating an instance of the class
organizer = MusicFestivalOrganizer(artist_names, artists_genres, playlists)

# Task 1: Compile Unique Artist Lineup
unique_lineup = organizer.compile_unique_lineup()
print("Unique Artist Lineup:", unique_lineup)

# Task 2: Categorize Artists by Genre
genre_categories = organizer.categorize_by_genre()
for genre, artists in genre_categories.items():
    print(f"Genre: {genre}, Artists: {', '.join(artists)}")

# Task 3: Check for Playlist Duplication
duplication_found = organizer.check_playlist_duplication()
print("Duplicate Playlists Found:", duplication_found)
