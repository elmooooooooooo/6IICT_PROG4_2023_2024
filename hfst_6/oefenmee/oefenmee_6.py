# Draai een woord om.
def draaiom(woord):

    if len(woord) == 1:
        return woord
    
    #vorige_woord = draaiom( woord )
    return woord[-1] + draaiom(woord[0:-1])


print( draaiom("Hallo") )       # ollaH
print( draaiom("Dag") )         # gaD
print( draaiom("f"))            # f
print( draaiom("Iedereen") )    # neeredeI