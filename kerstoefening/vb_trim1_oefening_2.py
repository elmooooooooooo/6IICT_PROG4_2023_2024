""" Oefening 2 (   / 6): API -- advies generator

Voorbeelden (API geeft enkel Engelse zinnen terug):

API: https://api.adviceslip.com/

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

import requests

query = input("Topic for advice: ")
response_json = requests.get(f"https://api.adviceslip.com/advice/search/{query}").json()
print(response_json)

if "message" in response_json:
    print(f"No advice slips found matching that search term.")
else:
    advice = response_json["slips"][0]["advice"]
    print(advice)