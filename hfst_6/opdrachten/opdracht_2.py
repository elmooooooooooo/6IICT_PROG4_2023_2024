# Bepaal recursief of een woord een palindroom is.
def palindroom(woord):

    if len(woord) == 1 or len(woord) == 0:
        return True
    
    laatste = woord[-1] 
    eerste = woord[0]

    if laatste == eerste:
        return palindroom(woord[1:-1])
    else:
        return False


print( palindroom("lepel") ) # True
print( palindroom("mes")   ) # False
print( palindroom("otto")  ) # True
print( palindroom("auto")  ) # False
