import json
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
artist_name = input("typ een artist: ")
url = "https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"

result= requests.get(url, headers)
json_result = json.loads(result.content)
print(json_result)

response_json = requests.get(f'https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg', headers=headers).json()

print(response_json)
print(access_token, artist_name)