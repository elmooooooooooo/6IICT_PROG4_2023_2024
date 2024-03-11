# Tel alle cijfers in een getal op.
def optellen(getal):
    getal = str(getal)

    if len(getal) == 1:
        return int(getal)
    
    #vorige_woord = draaiom( woord )
    return int(getal[-1]) + optellen(int(getal[0:-1]))


print( optellen(12345) )            # 15
print( optellen(5) )                # 5
print( optellen(4687612962034330) ) # 64
print( optellen(6728003096702784) ) # 69