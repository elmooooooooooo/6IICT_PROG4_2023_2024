# Pas de URL aan zoals aangegeven in de verschillende niveau's.
import requests
import json
counter = 0
url = "https://v2.jokeapi.dev/joke/Christmas?a"
response_json = requests.get(url).json() # Haal JSON uit response.
while True:
   counter = counter + 1
   str(counter)
   with open(f"hfst_2/oefenmee/hoppa{counter}.json", "w") as fp:
    json.dump(response_json, fp)
    # Bepaal of de grap uit 1 of 2 delen bestaat.
    if ("joke" in response_json):
        print(response_json["joke"])     # De grap
    else:
        print(response_json["setup"])    # De setup
        print(response_json["delivery"]) # De punchline
