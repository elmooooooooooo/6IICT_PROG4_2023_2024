import requests

data = {
    'grant_type': 'client_credentials',
    'client_id': '4cc048fb419440f5951860cf0a9f9db0',
    'client_secret': '763a491995ce4b1cad73ecccd6bb9ade',
}

response_json = requests.post('https://accounts.spotify.com/api/token', data=data).json()
access_token = response_json["access_token"]

headers = {
    'Authorization': 'Bearer 1POdFZRZbvb...qqillRxMr2z',
}

response = requests.get('https://api.spotify.com/v1/me', headers=headers).json()
information = response

print(access_token)
print(information)