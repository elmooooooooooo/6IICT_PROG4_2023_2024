""" Oefening 2 (   / 6): API -- CO2 uitstoot van websites 

API: https://api.websitecarbon.com/

Voorbeelden (CO2 uitstoot afgerond op 3 cijfers na de komma):
    Opgelet! De API geeft 2 soorten CO2 terug. Kies voor de optie 'grid'.

    Als jouw script dezelfde prints heeft als onderstaande voorbeelden,
    dan mag je ervanuit gaan dat het script correct gemaakt is.

    Website 1:
        Input || Welke website opzoeken: https://www.w3schools.com/
        Print || Deze website is 1578905 bytes groot, en veroorzaakt 0.397 gram CO2 uitstoot.
    Website 2:
        Input || Welke website opzoeken: https://github.com/
        Print || Deze website is 1948243 bytes groot, en veroorzaakt 0.490 gram CO2 uitstoot.
    Website 3:
        Input || Welke website opzoeken: abc
        Print || Geen geldige site opgegeven.

"""


import requests, json


website = input("Welke website opzoeken: ")

url = f"https://api.websitecarbon.com/site?url={website}"
response_json = requests.get(url).json()
#print(response_json)

with open("hfst_2/oefenmee/CO2uitstoot.json", "w") as fp:
    json.dump(response_json, fp)
    print(f'Deze website is {response_json["bytes"]} bytes groot, en veroorzaakt {response_json["statistics"]["co2"]["grid"]["grams"]} gram CO2 uitstoot.')
