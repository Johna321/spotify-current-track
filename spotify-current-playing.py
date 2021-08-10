#!/bin/python3

import requests

SPOTIFY_CURRENT_PLAYING_URL = "https://api.spotify.com/v1/me/player/currently-playing"
SPOTIFY_BEARER_TOKEN = ""

def fetchSpotifyData(spotifyUrl, bearerToken):
    res = requests.get(SPOTIFY_CURRENT_PLAYING_URL, headers={
        "Authorization": f"Bearer {SPOTIFY_BEARER_TOKEN}"
    })
    res = res.json()
    try:
        trackName = res['item']['name']
        artists = res['item']['artists']
        artistName = ", ".join([artist['name'] for artist in artists])
        print(f"{trackName} - {artistName}")
    except:
        print('')

def main():
    fetchSpotifyData(SPOTIFY_CURRENT_PLAYING_URL, SPOTIFY_BEARER_TOKEN)

if __name__ == '__main__':
    main()
