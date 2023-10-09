import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Define your Spotify API credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'  # This should be a URL you've registered with your Spotify Developer application

# Initialize the Spotify client with OAuth2 authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read'))

# Example: Get the current user's playlists
def get_user_playlists():
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        print(playlist['name'])

# Example: Search for a track
def search_track(query):
    results = sp.search(q=query, type='track', limit=10)
    for track in results['tracks']['items']:
        print(f"Track: {track['name']} - Artist(s): {', '.join([artist['name'] for artist in track['artists']])}")

# Example: Add a track to a playlist
def add_track_to_playlist(playlist_id, track_uri):
    sp.playlist_add_items(playlist_id, [track_uri])

# Example: Create a playlist
def create_playlist(name):
    playlist = sp.user_playlist_create(sp.current_user()['id'], name)
    return playlist['id']

# Example: Get a user's top tracks
def get_top_tracks(time_range='short_term', limit=10):
    top_tracks = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    for idx, track in enumerate(top_tracks['items'], start=1):
        print(f"{idx}. {track['name']} - {', '.join([artist['name'] for artist in track['artists']])}")

# Example usage
if __name__ == "__main__":
    get_user_playlists()
    search_track("Bohemian Rhapsody")
    create_playlist("My New Playlist")
    get_top_tracks()
