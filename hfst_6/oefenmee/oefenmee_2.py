# Los de vragen uit oefen mee 2 op.

def optellen(getal):
    if getal == 3:
        print(getal)
        return
    
    #print(getal) # 123
    optellen(getal+1)
    print(getal) # 321
optellen(1)