""" Voorbeelden (API geeft enkel Engelse zinnen terug):

Advies 1:
    Input || Topic for advice: spiders
    Print || Remember that spiders are more afraid of you, than you are of them.
Advies 2:
    Input || Topic for advice: teeth
    Print || You don't need to floss all of your teeth. Only the ones you want to keep.
Advies 3:
    Input || Topic for advice: programming
    Print || No advice slips found matching that search term.

"""

import requests, json


slip_id = input("Topic for advice: ")

url = f"https://api.adviceslip.com/advice/search/{slip_id}"
response_json = requests.get(url).json()
#print(response_json)

with open("hfst_2/oefenmee/APImokerst.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")

if "message" in response_json:
    print("No advice slips found matching that search term")
else:
    advice = response_json["slips"][0]["advice"]
    print(advice)