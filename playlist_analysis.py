import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# token.json dosyasından token'ı okuma
with open('token.json', 'r') as file:
    token_info = json.load(file)

access_token = token_info['access_token']

# Spotipy ile Spotify'a bağlanalım
sp = spotipy.Spotify(auth=access_token)

# Kullanıcı bilgilerini alalım
user = sp.current_user()
print(f"Spotify'a bağlandın: {user['display_name']}")

# Playlist ID (Spotify'dan bir playlist URL'sinden alabilirsin)
playlist_id = '0SYZIeRqDQGsbCvWkdoFLD'  # Burayı kendi playlist ID'nizle değiştirin

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
