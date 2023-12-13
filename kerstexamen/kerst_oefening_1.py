import random

""" Oefening 1 (  / 6): quiz-script 

Vul het script verder aan onder keuze == "1", keuze == "2" en keuze == "3".
Baseer je hiervoor op de uitleg die bij TODO geschreven is.
"""

# Dictionary quiz start reeds gevuld om snel te testen.
# Sleutel: Vraag || Waarde: Antwoord op vraag
quiz = {"hoofdstad belgie": "brussel", "2+2": "4", "kleuren in regenboog": "7"}

while True:

    print(f"\nKeuzes:")
    print("    1) Vraag toevoegen")
    print("    2) Aantal vragen printen")
    print("    3) Vraag stellen")
    print("    4) Stoppen")
    keuze = input(f"\nWat wil je doen: ")

    if keuze == "1":
        """ TODO (voorbeelden gaan uit van de dictionary quiz bovenaan het programma):
        
        Vraag de gebruiker om een vraag (str) en vraag de gebruiker om een antwoord (str).
        Voeg met vraag & antwoord een nieuw element toe aan de dictionary quiz.
        Print na het toevoegen de zin: "Nieuwe quizvraag toegevoegd."

            Voorbeeld 1:
            Input || Wat is de vraag: groen+rood
            Input || Wat is het antwoord: geel
            Print || Nieuwe quizvraag toegevoegd.

        Een nieuw element toevoegen mag enkel als de vraag nog niet bestaat in de quiz.
        Indien dit wel het geval is, voeg vraag & antwoord niet toe. 
        Print enkel de zin: "De quizvraag *vraag* bestaat reeds, kan deze niet opnieuw toevoegen!"

            Voorbeeld 2:
            Input || Wat is de vraag: 2+2
            Input || Wat is het antwoord: 6
            Print || De quizvraag '2+2' bestaat reeds, kan deze niet opnieuw toevoegen!

        Na deze twee voorbeelden ziet de dictionary quiz er als volgt uit:
        {"hoofdstad belgie": "brussel", "2+2": "4", "kleuren in regenboog": "7", "groen+rood": "geel"}

        """

        nieuwevraag = input("Wat is de vraag: ")
        antwoordToegevoegdeVraag = input("Wat is het antwoord: ")

        if nieuwevraag in quiz:
            print(f"De quizvraag {nieuwevraag} bestaat reeds, kan deze niet opnieuw toevoegen!")
        else:
            waarde = {nieuwevraag : antwoordToegevoegdeVraag}
            quiz.update(waarde)
            print("vraag toegevoegd") 
            print(quiz)


    elif keuze == "2":
        """ TODO (voorbeelden gaan uit van de dictionary quiz bovenaan het programma):

        Print hoeveel vragen de quiz momenteel bezit.
        Geef hierna een opsomming van deze vragen (antwoord hoeft niet).

            Voorbeeld:
            Print || De quiz bevat momenteel 3 vragen:
            Print ||    - hoofdstad belgie
            Print ||    - 2+2
            Print ||    - kleuren in regenboog
            Print ||    - ... (voor ieder element in de quiz)
        
        """
        for index, aantalvragen in enumerate(quiz):
            print(f"De quiz bevat momenteel {index + 1} vragen:")

        for vragen in quiz:
            print(f"- {vragen}")


    elif keuze == "3":
        """ TODO (voorbeelden gaan uit van de dictionary quiz bovenaan het programma):

        Selecteer een willekeurige vraag uit de dictionary quiz. Vraag het antwoord aan de gebruiker.
        Heeft deze het antwoord goed, print dan "correct!". Anders, print dan "fout!".
        Je mag ervanuitgaan dat alles met kleine letters geschreven wordt.
        Tip! gebruik de module random.

        Indien het niet lukt om een willekeurige vraag te stellen, mag je altijd de vraag
        "2+2" stellen. Je krijgt dan wel geen volledig punt op dit onderdeel.

            Voorbeeld 1:
            Input || kleuren in regenboog: 6
            Print || fout!

            Voorbeeld 2:
            Input || 2+2: 4
            Print || correct!

        """
        randomvraag = print(random.choice(list(quiz())))
        antwoord = input("Geef je antwoord")
        
        if antwoord in randomvraag:
            print("correct!")
        else:
            print("fout!")
        

    elif keuze == "4":
        break

    else:
        print("Geef een geldige keuze!")