import requests

data = {
    'grant_type': 'client_credentials',
    'client_id': '4cc048fb419440f5951860cf0a9f9db0',
    'client_secret': 'your-client-secret',
}

response = requests.post('https://accounts.spotify.com/api/token', data=data)