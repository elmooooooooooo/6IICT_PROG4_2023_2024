# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}
#f"Aardappelen: {recept['Aardappelen']} gram"
hoeveelheid = int(input("Met hoeveel mensen gaat u eten: "))
uitkomst = recept * hoeveelheid
print("Recept voor worst met wortelen en erwten: ")
for sleutel, waarde in recept.items():
    print(sleutel, waarde/4 * uitkomst)

