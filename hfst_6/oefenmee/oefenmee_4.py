# Bepaal de faculteit van een getal met behulp van een while-loop.
def facul(getal):

    uitkomst = 1
    while getal > 0:
        uitkomst = uitkomst * getal
        getal = getal - 1

    return uitkomst
        
        #for nummer in nummers:
            #print(nummer * nummer)
        #print(nummers["getal5"] * nummers["getal4"] * nummers["getal3"] * nummers["getal2"] * nummers["getal1"])
        #nummers.pop(1)
        #facul = facul + 1
    
print( facul(1) ) # 1
print( facul(2) ) # 2
print( facul(3) ) # 6
print( facul(4) ) # 24
print( facul(5) ) # 120