import requests, json

basisurl = "https://v2.jokeapi.dev/joke/"

while True:
    categorie = input("""Welke Categorie wil je:
        1-Programming
        2-Misc
        3-Dark
        4-Pun
        5-Spooky
        6-Christmas
        7-Any
        8-END  
    :             """)

    if categorie == "1":
       basisurl = "https://v2.jokeapi.dev/joke/Programming"
    elif categorie == "2":
       basisurl = "https://v2.jokeapi.dev/joke/Misc"
    elif categorie == "3":
       basisurl = "https://v2.jokeapi.dev/joke/Dark"
    elif categorie == "4":
       basisurl = "https://v2.jokeapi.dev/joke/Pun"
    elif categorie == "5":
       basisurl = "https://v2.jokeapi.dev/joke/Spooky"
    elif categorie == "6":
       basisurl = "https://v2.jokeapi.dev/joke/Christmas"
    elif categorie == "7":
       basisurl = "https://v2.jokeapi.dev/joke/Any"
    elif categorie == "8":
       break
    else:
       print("geef een geldig cijfer")
       continue
    
# url = basisurl+categorie

    response_json = requests.get(basisurl).json() # Haal JSON uit response.

    with open(f"hfst_2/opdrachten/opdracht1.json", "w") as fp:
        json.dump(response_json, fp)

    if "joke" in response_json:
        print(response_json["joke"])
    else:
        print(response_json["setup"])    # De setup
        print(response_json["delivery"]) # De punchline
