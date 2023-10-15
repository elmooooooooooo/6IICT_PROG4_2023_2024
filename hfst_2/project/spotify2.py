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

    artist_name = input("type an artist: ")


    get_artist = requests.get(
        f'https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1', headers=headers).json()["artists"]["items"]

    if len(get_artist) == 0:
        print("no artist found with this name")

    keuze_gebruiker = int(input("""kies een optie: 
    1: Top-Tracks
    2: nog niks
    3: nog niks
    4: STOP
                : """))

    if keuze_gebruiker == 1:
        top_tracks = requests.get(
            f'https://api.spotify.com/v1/artists/{get_artist[0]["id"]}/top-tracks?country=US', headers=headers).json()["tracks"]

        for index, track in enumerate(top_tracks):
            print(f'{index + 1}: {track["name"]}')

    if keuze_gebruiker == 2:
        pass

    if keuze_gebruiker == 3:
        pass

    if keuze_gebruiker == 4:
        break

