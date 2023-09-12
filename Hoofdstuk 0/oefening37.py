""" Maak het spel galgje na.

    Gebruik hiervoor een willekeurig woord uit 
    onderstaande lijst (uitbreiden mag).

    Vraag de gebruiker naar een letter of
    om het woord te raden. Het spel stopt
    als het woord correct is of na 7 vragen.

    Print in het eerste geval "gewonnen!".
    In het tweede geval "verloren!". 

        Tip! stel een lijst op met erin de
             gevonden letters. Vul deze eerst
             volledig met _ . Als de gebruiker een 
             letter geeft die in het woord zit, 
             vervang de overeenkomstige _ door deze 
             letter.

    >>> Gok letter / Raad woord (1/7): a
    Woord:  _  _  _  _
    >>> Gok letter / Raad woord (2/7): e
    Woord:  e  _  e  _
    >>> Gok letter / Raad woord (3/7): t
    Woord:  e  _  e  _
    >>> Gok letter / Raad woord (4/7): v
    Woord:  e  v  e  _
    >>> Gok letter / Raad woord (5/7): even
    gewonnen!
"""
import random
woorden = ["uier", "even", "stuk", "volk"]
vraag = 0
hoeveelheidvragen = 0

woord = random.choice(woorden)
gevondenletters = ["_","_","_","_"]
while hoeveelheidvragen < 7:
    hoeveelheidvragen += 1
    geradenletter = input(f"Gok letter / Raad woord ({hoeveelheidvragen}/7): ")
    for index, letter in enumerate(woord):
        if geradenletter == letter:
            gevondenletters[index] = letter
    print(gevondenletters)
    if geradenletter == woord:
        print(f'woord: {geradenletter}')
        print("je hebt gewonnen!")
        break
if geradenletter in woorden:
        print(f'woord: {geradenletter} {geradenletter} {geradenletter} {geradenletter}')
if gevondenletters == 4:
     print("je hebt gewonnen!")
     