import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Environment variables yükleme
load_dotenv()

# Spotify bağlantısı için SpotifyOAuth kullanımı
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope='playlist-modify-private, playlist-modify-public, playlist-read-private, playlist-read-collaborative, user-library-read'
))

# Kullanıcıyı Spotify'a yönlendirip authorization code almak için URL oluşturuyoruz
auth_url = sp.auth_manager.get_authorize_url()
print(f"Spotify'a giriş yapmak için bu URL'yi ziyaret edin: {auth_url}")

# Kullanıcıdan gelen authorization code'u almak
auth_code = 'AQCtf052CKI95Iyw4oQPajFpKU7gDhICdGWLMXdV37whfch_s_0aiPpu3UNJvptqXDO_V88J-qyNwnyHeqWcG2GM7QlefJ9bIxBvCZtGi9IsSZIcF2snX9eMqxjPyH56Yh22zS76_Hmh1T87UBFxO-dT-PHDW_U7aTF1BnKQfrtZuQm1Xsigmd_3DM8zs7LyihKencVW-AWBomsljoIBvZBIRMRVGrTv_KC6cBLqd7mGN8fmO9bU1qAeil6vy_LQbKp4SgO0ZrFqXaBr5ddzJzrw2C9GM9PBsd4cnQYpIBUub-0uNAh1u7yfUhgNp24TwFnFsYtN10wArA'

# Authorization Code ile Access Token al
token_info = sp.auth_manager.get_access_token(auth_code)

# Access Token'ı yazdır
access_token = token_info['access_token']
print(f"Access Token: {access_token}")

# Spotify API ile veri çekebilirsiniz
sp = spotipy.Spotify(auth=access_token)

# Kullanıcı bilgilerini alalım
user = sp.current_user()
print(f"Spotify'a bağlandın: {user['display_name']}")

# Playlist ID (Spotify'dan bir playlist URL'sinden alabilirsin)
playlist_id = '0SYZIeRqDQGsbCvWkdoFLD'

# Playlist'teki şarkıları alalım
results = sp.playlist_tracks(playlist_id)
tracks = results['items']

print(f"Playlist'teki şarkı sayısı: {len(tracks)}\n")

# Şarkıların analiz özelliklerini alalım
track_ids = [track['track']['id'] for track in tracks]
features = sp.audio_features(track_ids)

# Her şarkı için analiz bilgilerini yazdıralım
for i, track in enumerate(tracks):
    track_info = track['track']
    track_feature = features[i]
    print(f"\n{track_info['name']} - {', '.join(artist['name'] for artist in track_info['artists'])}")
    print(f"Tempo: {track_feature['tempo']}")
    print(f"Energy: {track_feature['energy']}")
    print(f"Danceability: {track_feature['danceability']}")
    print(f"Valence: {track_feature['valence']}")
    print(f"Loudness: {track_feature['loudness']}")

# Playlist'e şarkı ekleme
track_uris = ['https://open.spotify.com/track/6ZFbXIJkuI1dVNWvzJzown?si=e072ab9f40ad48e0']  # Eklemek istediğiniz şarkının URI'si
try:
    sp.playlist_add_items(playlist_id, track_uris)
    print("Şarkı başarıyla eklendi!")
except Exception as e:
    print(f"Bir hata oluştu: {e}")

