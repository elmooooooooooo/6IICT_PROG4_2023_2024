# Bepaal recursief of een getal voldoet aan het luhn-criteria.

def luhn(reeks):
    reeks = str(reeks)
    if len(reeks) == 0:
        return 0
    
    getal = int(reeks[0])
    if len(reeks)%2 == 0: getal *= 2
    if getal > 9: getal -= 9
    return getal + luhn(reeks[1:])

print( luhn(4687612962034330) ) # 70 --> geldig
print( luhn(6728003096702784) ) # 70 --> geldig
print( luhn(2727903413621029) ) # 66 --> ongeldig
print( luhn(9727009535679498) ) # 92 --> ongeldig