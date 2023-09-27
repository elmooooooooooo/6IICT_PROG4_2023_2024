# Maak een eigen JSON-bestand aan met behulp van onderstaande code.
import requests, json

url = "https://api.adviceslip.com/advice/search/api"
response_json = requests.get(url).json()

with open("hfst_2/oefenmee/bericht_advice.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")

print(response_json["slips"][0]["advice"])