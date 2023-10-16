import requests

data = {
    'grant_type': 'client_credentials',
    'client_id': '4cc048fb419440f5951860cf0a9f9db0',
    'client_secret': '763a491995ce4b1cad73ecccd6bb9ade',
}


response_json = requests.post(
    'https://accounts.spotify.com/api/token', data=data).json()
access_token = response_json["access_token"]

headers = {
    'Authorization': f'Bearer {access_token}',
}

response_json = requests.get(
    f'https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg', headers=headers).json()

while True:

    keuze_gebruiker = int(input("""kies een optie: 
    1: Top-Tracks
    2: Album
    3: STOP
                : """))

    if keuze_gebruiker == 1:

        artist_name = input("type an artist: ")
        get_artist = requests.get(
            f'https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1', headers=headers).json()["artists"]["items"]

        if len(get_artist) == 0:
            print("no artist found with this name")
            continue

        top_tracks = requests.get(
            f'https://api.spotify.com/v1/artists/{get_artist[0]["id"]}/top-tracks?country=US', headers=headers).json()["tracks"]

        for index, track in enumerate(top_tracks):
            print(f'{index + 1}: {track["name"]}')

        related_artist = input("gerelateerden artiesten bekijken? ja of nee: ")

        if related_artist == "nee":
            continue
        if related_artist == "ja":
            related_artists = requests.get(
                f'https://api.spotify.com/v1/artists/{get_artist[0]["id"]}/related-artists', headers=headers).json()["artists"][0]["name"]

            print(related_artists)

        related_artists_id = requests.get(
            f'https://api.spotify.com/v1/artists/{get_artist[0]["id"]}/related-artists', headers=headers).json()["artists"][0]["id"]

        toptracks_relatedartist = input(
            "wil je de top tracks van deze artist ook weten? Ja of nee: ")

        if toptracks_relatedartist == "nee":
            continue
        if toptracks_relatedartist == "ja":
            top_tracks_related_artist = requests.get(
                f'https://api.spotify.com/v1/artists/{related_artists_id}/top-tracks?country=US', headers=headers).json()["tracks"]

            for index, track in enumerate(top_tracks_related_artist):
                print(f'{index + 1}: {track["name"]}')

    if keuze_gebruiker == 2:

        artist_name = input("type an artist: ")
        get_artist = requests.get(
            f'https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1', headers=headers).json()["artists"]["items"]

        if len(get_artist) == 0:
            print("no artist found with this name")
            continue

        albums = requests.get(
            f'https://api.spotify.com/v1/artists/{get_artist[0]["id"]}/albums?&country=US&limit=50', headers=headers).json()["items"][0]["name"]

        print(albums)

    if keuze_gebruiker == 3:
        break
