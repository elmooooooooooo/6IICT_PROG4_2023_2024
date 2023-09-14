 # Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
gastenaanwezig = []

while True:
    vraag = input("wat is je naam: ")
    if vraag.upper() == "STOP":
        break
    if vraag in gastenaanwezig:
        print(f'{vraag} is al binnen')

    elif vraag in gasten:
        #gasten.get(vraag, "niet aanwezig") 2de optie
        print(f'welkom {gasten[vraag]} {vraag}. Kom binnen.')
        gasten.pop(vraag)
        gastenaanwezig.append(vraag)
    else:
        print(f"De naam {vraag} staat niet op de lijst.")



   