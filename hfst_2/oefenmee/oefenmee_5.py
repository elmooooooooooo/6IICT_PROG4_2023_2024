# Pas de URL aan zoals aangegeven in de verschillende niveau's.
import requests
import json


kerstgrap = 0
grap = 1


while kerstgrap < 3:
   
   url = "https://v2.jokeapi.dev/joke/Christmas?amount=3"
   response_json = requests.get(url).json() # Haal JSON uit response.

   with open(f"oefenmee_1.json", "w") as fp:
    json.dump(response_json, fp)


    # Bepaal of de grap uit 1 of 2 delen bestaat.
    if ("joke" in response_json):
        print(response_json["joke"])     # De grap
    else:
        print(f'grap{grap}: {response_json["jokes"][kerstgrap]["setup"]}')  # De setup
        print(response_json["jokes"][kerstgrap]["delivery"]) # De punchline
    kerstgrap = kerstgrap + 1
    grap = grap + 1
