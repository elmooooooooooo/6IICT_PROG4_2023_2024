import requests, json
url = 'https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg'
response = requests.get(url)
response_json = response.json()

with open("hfst_2/project/nig.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")