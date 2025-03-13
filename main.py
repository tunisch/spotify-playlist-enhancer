from utils.spotify_client import sp

def get_playlist_tracks(sp, playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = []
    for item in results['items']:
        track = item['track']
        tracks.append(track)
    return tracks

def find_similar_tracks(sp, track_id):
    features = sp.audio_features([track_id])[0]
    query = f"genre:{features['key']} tempo:{features['tempo']} energy:{features['energy']} danceability:{features['danceability']}"
    
    results = sp.search(q=query, type='track', limit=10)
    similar_tracks = []
    for item in results['tracks']['items']:
        similar_tracks.append(item)
    return similar_tracks

# Çalma listesi ID'sini buraya ekle
playlist_id = 'ÇALMA_LISTESI_ID'

# Çalma listesindeki parçaları al
tracks = get_playlist_tracks(sp, playlist_id)
for idx, track in enumerate(tracks):
    print(f"{idx + 1} {track['name']} - {track['artists'][0]['name']}")

# Örnek şarkıya benzer şarkıları bul
track_id = tracks[0]['id']  # Çalma listesinden bir şarkının ID'sini al
similar_tracks = find_similar_tracks(sp, track_id)
for idx, track in enumerate(similar_tracks):
    print(f"Benzer {idx + 1} {track['name']} - {track['artists'][0]['name']}")
