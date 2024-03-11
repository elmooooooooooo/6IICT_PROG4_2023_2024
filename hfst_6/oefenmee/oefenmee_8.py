# Bepaal de som van alle elementen (en sub-elementen) in een (geneste) lijst.
def som_lijst():
    return

print( som_lijst([1,2,3,4]) )           # 10
print( som_lijst([1, [2,3], 4]) )       # 10
print( som_lijst([1,2,[3,[4]]]) )       # 10
print( som_lijst([1, [2, [3, [4]]]]) )  # 10