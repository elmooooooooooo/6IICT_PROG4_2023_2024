import requests

data = {
    'grant_type': 'client_credentials',
    'client_id': '4cc048fb419440f5951860cf0a9f9db0',
    'client_secret': '763a491995ce4b1cad73ecccd6bb9ade',
}



response_json = requests.post('https://accounts.spotify.com/api/token', data=data).json()
access_token = response_json["access_token"]

headers = {
    'Authorization': f'Bearer {access_token}',
}

album_name = input("typ een album: ")

get_album = requests.get(
    f'https://api.spotify.com/v1/search?q={album_name}&type=album&limit=1', headers=headers).json()["albums"]["items"]

print(get_album[0]["artists"][0]["name"])

album_track = input("wil je een track van deze album? ja of nee: ")

if album_track == "ja":

    get_album_tracks = requests.get(
        f'https://api.spotify.com/v1/albums/{get_album[0]["id"]}/tracks?offset=0&limit=20', headers=headers).json()["items"][0]["name"]

    print(get_album_tracks)
            
