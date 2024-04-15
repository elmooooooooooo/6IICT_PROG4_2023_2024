""" OEFENING 3: (  / 5)

!!! OPGELET: voor deze oefening mag je het internet NIET gebruiken. !!!

Gebruik recursie om te controleren hoe vaak een bepaalde letter voorkomt in een string.
je mag tijdens deze oefening geen gebruik maken van count, find, of soortgelijke functies.

TIP:
    hallo = h + allo
                allo = a + llo
                ...
"""


def aantal_letter(letter, woord):

    counter = 0
    if len(woord) == 0:
        return 0
    
    if letter == woord[-1]:
        counter = counter + 1
    

    return counter + aantal_letter(letter, woord[0:-1])


    # laatste = woord[-1] 
    # eerste = woord[0]

    # if laatste == eerste:
    #     return aantal_letter(woord[1:-1])
    # else:
    #     return False

print( aantal_letter("a", "hallo") )        # 1
print( aantal_letter("r", "programmeren") ) # 3
print( aantal_letter("b", "") )             # 0