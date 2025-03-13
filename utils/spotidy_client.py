import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Environment variables yükleme
load_dotenv()

# Spotify bağlantısı
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    redirect_uri=os.getenv('REDIRECT_URI'),
    scope='playlist-modify-private playlist-read-private user-read-currently-playing user-read-playback-state'
))

# Kullanıcı bilgilerini alalım
user = sp.current_user()
print(f"Spotify'a bağlandin: {user['display_name']}")

