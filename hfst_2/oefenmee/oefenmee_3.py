# Voer onderstaande code uit & bekijk het resultaat.
import requests, json

url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
response = requests.get(url)
response_json = response.json()

with open("hfst_2/oefenmee/bericht_jokeAPI.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")
