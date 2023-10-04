""" Oefening 5 (  / 6 )
Maak onderstaande app voor de olympische spelen verder af.
Het menu is reeds gemaakt. Jij zal de opties in dit menu verder uitwerken.

Er zijn 3 opties waaruit de gebruiker kan kiezen (meer info is verderop te vinden).
Alle opties maken gebruik van de dictionary olympische_spelen.
    1) Toon details van discipline.
    2) Voeg discipline toe (aan dictionary olympische_spelen).
    3) Geef overzicht van dictionary olympische_spelen.

"""

# Sleutels zijn de disciplines, waardes zijn lijsten met prijswinnaars.
# De lijsten bevat respectievelijk de eerste, tweede & derde plaats.
olympische_spelen = { 
    "100m sprint": ["Usain Bolt", "Yohan Blake", "Justin Gatlin"],
    "zwemmen": ["Michael Phelps", "Chad le Clos", "Conor Dwyer"],
    "gymnastiek": ["Simone Biles", "Aly Raisman", "Aliya Mustafina"],
}

while True: # Start de app.
    # Overzicht keuzemenu
    print("Menu: ")
    print("  1) Toon details van discipline.")
    print("  2) Voeg discipline toe.")
    print("  3) Toon discipline.")
    print("  4) Stop de app.")

    # Kies een van de 4 opties.
    optie = input("Selecteer wat je wilt doen: ")

    if optie == "1":   # Toon details van opgevraagde discipline.
        """ 1) Toon details van discipline.
        Vraag de gebruiker naar een discipline.

        Komt de discipline voor in de dictionary olympische_spelen, print dan volgende zin.
            >>>  Discipline *discipline* met als winnaars *plaats1*, *plaats2* & *plaats3*.

        Als de discipline niet voorkomt in de dictionary olympische_spelen, print dan het volgende.
            >>> Kan discipline *discipline* niet vinden.
        """
        keuze = input("""Geef een discipline: """)
        
        if keuze in olympische_spelen:
            print(olympische_spelen[keuze])
        else:
            print("kan de discipline niet vinden")



    elif optie == "2": # Voeg discipline toe aan de dictionary olympische_spelen.
        """ 2) Voeg discipline toe.
        Vraag de gebruiker om een *discipline*, *plaats1*, *plaats2* & *plaats3*.
        Voeg vervolgens een nieuw element toe aan de dictionary olympische_spelen. 
        Dit element heeft als sleutel de *discipline*, de waarde is een lijst met 
        de overige inputs.

        Het element ziet er dus in het algemeen als volgt uit.
            *discipline*: [*plaats1*, *plaats2*, *plaats3*]
        Een specifiek voorbeeld is.
            'fietsen': ["Richard Carapaz", "Wout van Aert", "Tadej Pogacar"]

        Het is toegelaten om een discipline die reeds bestaat in olympische_spelen te overschrijven.
        """
        sporttoevoegen= input("kies uit een sport:")
        plaats1 = input("kies een naam voor plaats 1:")
        plaats2 = input("kies een naam voor plaats 2:")
        plaats3 = input("kies een naam voor plaats 3:")

        olympische_spelen.update(sporttoevoegen[plaats1, plaats2, plaats3])

    elif optie == "3":
        """ 3) Geef overzicht van olympische_spelen.
        Print iedere discipline (met eerste plaats) die zich in de dictionary bevindt.
        De print moet er dus als volgt eruitzien.
            >>> Volgende disciplines vonden plaats in de olympische spelen:
            >>>     - 100m sprint (Usain Bolt)
            >>>     - zwemmen (Michael Phelps)
            >>>     - gymnastiek (Simone Biles)
            >>>     - enzoverder voor iedere andere discipline...
        """

        

    elif optie == "4": # Stop de app.
        print(f"\nBedankt voor het gebruiken van deze app.")
        break

    else: # Verkeerde input gegeven.
        print(f"\nDit is geen optie. Gelieve opnieuw te proberen.")