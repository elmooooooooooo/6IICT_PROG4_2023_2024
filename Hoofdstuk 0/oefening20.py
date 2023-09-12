""" Stel een trainingsschema op voor een marathon.

    Een simpele aanpak ziet er als volgt uit.
    Loop op dag 1 een aantal km. Loop de volgende 
    dag 10% meer, de dag daarop opnieuw 10% meer, 
    ... . Herhaal dit tot je aan 42 km zit.

    Vraag de gebruiker hoeveel km deze kan lopen 
    op dag 1. Bereken vervolgens hoeveel deze op 
    dag 2, 3, 4, ... moet lopen.

    Het programma stopt wanneer de totaal gelopen
    afstand groter is dan 42 km.

    >>> Hoeveel km kan je op dag 1 lopen: 6
    Op dag 1 loop je 6 km
    Op dag 2 loop je 6.6 km
    Op dag 3 loop je 7.99 km
    ...
    Op dag 22 loop je 44.45 km
"""
aantalkm = int(input("Hoeveel km kan je lopen op dag 1:"))
hoogstegetal = 42
countdag = 1
while aantalkm < hoogstegetal:
    countdag = countdag + 1
    aantalkm = aantalkm*1.1
    print(f'Op dag {countdag} loop je {aantalkm} km. ')

    
    

