# Spotify Playlist Enhancer

Spotify Playlist Enhancer is a Python project designed to automatically suggest and add songs with a similar vibe, rhythm, and feel to your existing Spotify playlist. Using the Spotify API, it analyzes your playlist’s tracks and queues similar songs for your approval before adding them.

## Features

🎵 Analyze the vibe and characteristics of your existing playlist tracks.

🔍 Suggest songs with a similar feel based on rhythm, energy, and genre.

✅ Queue songs for real-time listening before adding them.

➕ Automatically add approved songs to your playlist.

## Project Structure

spotify-playlist-enhancer/
|-- .env                   # Environment variables (Spotify API credentials)
|-- config.py              # Configuration settings
|-- main.py                # Main script for running the enhancer
|-- requirements.txt       # Project dependencies
|-- utils/
|   |-- spotify_client.py  # Spotify API interaction functions
|   |-- song_analyzer.py   # Functions for song analysis and comparison
|-- README.md              # Project documentation

## Setup

### Clone the repository:

git clone https://github.com/yourusername/spotify-playlist-enhancer.git
cd spotify-playlist-enhancer

### Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install dependencies:

pip install -r requirements.txt

### Set up your environment variables:

Create a .env file and add your Spotify API credentials:

SPOTIPY_CLIENT_ID='your-client-id'
SPOTIPY_CLIENT_SECRET='your-client-secret'
SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

### Run the script:

python main.py

## Usage

The script will analyze your playlist and suggest similar songs.

You’ll be able to listen to suggested songs in a queue.

Approve or skip songs to automatically update your playlist.

## Future Plans

Implement machine learning for better song recommendation.

Add a web-based interface for easier interaction.

## Contributing

Feel free to fork this repository and contribute! Open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License.
