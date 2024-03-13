# Bepaal de som van alle elementen (en sub-elementen) in een (geneste) lijst.
def som_lijst(lijst):
    aantal = 0
    for element in lijst:
        if type(element) != int:
            aantal = aantal + som_lijst(element)
        else:
            aantal += element   
    return aantal


print( som_lijst([1,2,3,4]) )           # 10
print( som_lijst([1, [2,3], 4]) )       # 10
print( som_lijst([1,2,[3,[4]]]) )       # 10
print( som_lijst([1, [2, [3, [4]]]]) )  # 10