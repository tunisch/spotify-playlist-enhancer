import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Environment variables yükleme
load_dotenv()

# Spotify bağlantısı
sp_oauth = SpotifyOAuth(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    redirect_uri=os.getenv('REDIRECT_URI'),
    scope='playlist-modify-private playlist-read-private user-read-currently-playing user-read-playback-state user-library-read user-top-read'
)

token_info = sp_oauth.get_cached_token()
if not token_info:
    print(f"Enter the URL you were redirected to: ")
    redirect_url = input()
    code = sp_oauth.parse_response_code(redirect_url)
    token_info = sp_oauth.get_access_token(code=code)

if token_info:
    sp = spotipy.Spotify(auth=token_info['access_token'])
    user = sp.current_user()
    print(f"Spotify'a bağlandın: {user['display_name']}")
else:
    print("Yetkilendirme başarısız.")
