""" Oefening 1 (  / 6): shopping-script """

# Dictionary kar start reeds gevuld om snel te testen.
# Sleutel: Artikel || Waarde: hoeveelheid van artikel
kar = {"kaars": 4, "gehakt": 400, "ei": 6} 

while True:

    print(f"\nKeuzes:")
    print("    1) Overzicht kar")
    print("    2) artikal toevoegen")
    print("    3) app stoppen")
    keuze = input(f"\nWat wil je doen: ")

    if keuze == "1":
        """ TODO (voorbeelden gaan uit van de dictionary kar bovenaan het programma):

        Print iedere artikel en de hoeveelheid van dit artikel op een aparte regel.

            Voorbeeld:        
            Print || Momenteel heb je het volgende in je kar:
            Print ||    - appels: 3
            Print ||    - gehakt: 400
            Print ||    - ei: 6
            Print ||    - ... (voor ieder element in de quiz)
        
        """

        print("Momenteel heb je het volgende in je kar:")
        for artikel, hoeveelheid in kar.items():
            print(f"   - {artikel}: {hoeveelheid}")


    elif keuze == "2":
        """ TODO (voorbeelden gaan uit van de dictionary kar bovenaan het programma):

        Vraag de gebruiker om een artikel en hoeveelheid. Voeg deze toe aan de dictionary kar.
        Je mag ervanuit gaan dat de gebruiker altijd een int opgeeft voor hoeveelheid.
        
            Voorbeeld 1:
            Input || Welk artikel kopen: kaars
            Input || Hoeveel van dit artikel kopen: 4
            Print || Een nieuw artikel 'kaars' is toegevoegd aan de kar!

        Bestaat het artikel reeds in de dictionary kar, 
        tel dan de nieuwe hoeveelheid op bij de oude hoeveelheid.

            Voorbeeld 2:
            Input || Welk artikel toevoegen: ei
            Input || Hoeveel van dit artikel kopen: 6
            Print || Het artikel 'ei' bestaat reeds in de kar. De hoeveelheid werd verhoogd! 
        
        Na deze twee voorbeelden ziet de dictionary kar er als volgt uit:
        {"kaars": 4, "gehakt": 400, "ei": 12, "kaars": 4} 
            
        """

        artikel     = input("Welk artikel kopen: ") 
        hoeveelheid = int(input("Hoeveel van dit artikel kopen: "))

        if artikel in kar:
            print(f"Een nieuw artikel '{artikel}' is toegevoegd aan de kar!")
            kar[artikel] = kar[artikel] + hoeveelheid
        else:
            print(f"Het artikel '{artikel}' bestaat reeds in de kar. De hoeveelheid werd verhoogd!")
            kar[artikel] = hoeveelheid

        print(kar)

    elif keuze == "3":
        break

    else:
        print("Geef een geldige keuze!")