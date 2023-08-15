import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your actual credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='3f732d0f1721483389e7fb7cd8dcd3a1',
                                               client_secret='07e49a4693894296b559cf17093cc503',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-modify-playback-state'))

# Replace 'SPOTIFY_URI_OF_SONG' with the URI of the song you want to play
sp.start_playback(uris=['spotify:track:2JzZzZUQj3Qff7wapcbKjc'])

