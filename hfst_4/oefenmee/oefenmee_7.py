fruit_lijst = ["Appel", "Banaan", "Kers"]
try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )
except ZeroDivisionError:
    print( "Wie deelt door 0 is een snul. ")
except  ValueError:
    print( "geef een getal op: " )
except IndexError:
    print( "kleinere getal" ) 
except:
    print("Geen ctrl c")
    
print("Programma klaar") 