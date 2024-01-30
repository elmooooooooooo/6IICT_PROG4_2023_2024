""" Maak een simpel raad-spel. Een deel van de code is reeds gegeven. (  / 5) """

""" Niveau 1 (  / 1):
De huidige code genereert willekeurig het getal 0 of 1 in een while-loop.
Hiernaast zijn er twee tellers aangemaakt. De variabelen rondes & correct.

Voeg volgende zaken toe IN de while-loop, 
    vraag de gebruiker wat het random getal is (0 of 1).
    Als dit juist is: print 'Dat klopt!' en verhoog variabele correct met 1.
    Anders als dit fout is: print 'Foute keuze!'.
    Verhoog tenslotte ALTIJD de variabele rondes met 1.

De while-loop stopt als de gebruiker -1 ingeeft.
Print voor het programma te eindigen nog volgende zin:
"Bedankt voor het spelen. Je score is: *correct* / *rondes*"
"""
import random

""" Niveau 2 (  / 1.5)
Raise volgende custom exceptions in de code van niveau 1.
De naam is gegeven, de uitleg bij het raisen mag je zelf kiezen.

    1. OutOfBoundsError: raise als de gebruiker een getal kleiner dan -1
                         of groter dan 1 ingeeft.
    2. ForceQuitError: raise als er 5 rondes geweest zijn.
                       (Het spel bestaat dus maximaal uit 5 rondes).
"""
    
""" Niveau 3 (  / 1.5)
Handel IN de while-loop volgende specifieke exceptions af. Voor iedere exception 
print je wat het probleem is, hiernaast voer je ook de aangegeven actie uit.

    1. Gebruiker geeft GEEN getal in: verhoog variabele rondes met 1.
    2. Gebruiker drukt CTRL+C in: stop de while-loop (doet dus hetzelfde als -1 ingeven).
    3. Er zijn 5 rondes geweest: stop de while-loop (je vangt hier dus de custom ForceQuitError op).

Tip! Plaats de try-except over de code IN de while-loop. Bepaal voor deze te
     plaatsen eerst welke specifieke Errors er optreden in volgende 3 situaties.

     while True:
        try:
            *Code van Niveau 1 & Niveau 2*
        except ...

"""

""" Niveau 4 (  / 1)
Pas het spel aan. Print na iedere ronde de huidige score van de gebruiker.
"Je huidige score is *correct*/*aantal*."

Deze print moet ALTIJD optreden. 
Dus ook als het programma een exception afhandelt, of als het programma crasht.

"""

class OutOfBoundsError(Exception):
    pass

class ForceQuitError(Exception):
    pass

while True:
    try:
        getal = random.randint(0,1)
        vraag = int(input("wat is het random getal 0 of 1: "))
        if vraag < -1 or vraag > 1:
            raise OutOfBoundsError("Geen nummers onder -1, kies iets anders.")
        if vraag > 5:
            raise ForceQuitError("Er zijn al 5 rondes geweest!")
        if vraag == getal:
            print("Dat klopt!")
            rondes, correct = rondes + 1, correct + 1
            print(rondes, correct)
        else:
            print("Foute keuze!")
            rondes = rondes + 1
            print(rondes, correct)
        if vraag == -1:
            break
    except ForceQuitError:
        print("Er zijn al 5 rondes geweest!")
        break
    except OutOfBoundsError:
        print("Geen nummers onder -1, kies iets anders.")
        break
    except ValueError:
        print("Geen woorden of andere dingen toegestaan, alleen getallen 0 of 1!")
    except KeyboardInterrupt:
        print("geen ctrl c toegestaan")
    finally:
        print(rondes, correct)