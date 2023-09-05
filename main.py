import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = "0e47d4d5bcdd4663a77234431230409"

SPOTIPY_CLIENT_ID = '3be79b156f0b4bd0b86dc704806a104a'
SPOTIPY_CLIENT_SECRET = '4ea7ea71158241798590d3667a532b41'

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

vibes = {
    "sunny": ["upbeat", "happy", "pop", "summer", "tropical", "dance", "energetic", "justin timberlake"],
    "clear": ["calm", "relaxing", "acoustic", "folk", "chill"],
    "cloudy": ["indie", "alternative", "melancholic", "soft rock", "dreamy"],
    "rain": ["melancholic", "acoustic", "ballad", "sad", "reflective", "jazz", "blues"],
    "thunderstorm": ["intense", "rock", "electronic", "dramatic", "epic", "orchestral"],
    "snow": ["cozy", "jazz", "instrumental", "piano", "warm", "folk", "ambient"],
    "fog": ["mysterious", "ambient", "ethereal", "dream pop", "chillstep", "trip hop"],
    "windy": ["adventurous", "epic", "rock", "indie folk", "cinematic", "trance"],
    "hail": ["hard rock", "metal", "intense", "electronic", "industrial"],
    "overcast": ["mellow", "indie", "alternative", "chill", "lo-fi", "trip hop"],
    "drizzle": ["soft", "relaxing", "jazz", "r&b", "soul", "lo-fi"],
    "hot": ["latin", "reggaeton", "dancehall", "afrobeats", "funk", "disco"],
    "cold": ["ambient", "chill", "instrumental", "classical", "post-rock"],
    "mist": ["mysterious", "ambient", "ethereal", "dream pop", "chillstep", "trip hop"],
    "partly cloudy": ["mellow", "indie", "alternative", "chill", "lo-fi", "trip hop"],
    "light rain": ["melancholic", "acoustic", "ballad", "sad", "reflective", "jazz", "blues"],
}


def get_weather(zip_code):
    response = requests.get(f"{WEATHER_API_URL}?key={API_KEY}&q={zip_code}")
    data = response.json()
    return data['current']['condition']['text'].lower()


def get_songs_for_weather(weather_condition):
    keywords = vibes.get(weather_condition, [])
    if not keywords:
        return []
        print("No key words for this weather")

    # Combine two random keywords for a broader search
    keyword_combo = random.sample(keywords, 2)
    search_query = " ".join(keyword_combo)

    # Fetch more songs for variety
    results = sp.search(q=search_query, limit=20)

    # Randomly select 5 songs from the results
    selected_tracks = random.sample(results['tracks']['items'], 5)

    # Extract song titles and their respective artists
    songs_with_artists = []
    for track in selected_tracks:
        song_title = track['name']
        artist_names = ", ".join([artist['name'] for artist in track['artists']])
        songs_with_artists.append(f"{song_title} by {artist_names}")

    return songs_with_artists


def main():
    zip_code = input("Enter your zip code: ")
    weather_condition = get_weather(zip_code)
    print(f"Weather condition: {weather_condition}")

    songs = get_songs_for_weather(weather_condition)
    print("Songs for the mood:")
    for song in songs:
        print(song)


if __name__ == '__main__':
    main()