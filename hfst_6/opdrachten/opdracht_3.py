# Bepaal recursief de grootte van een map.
import os

def grootte_map(pad):
    items = os.listdir(pad)  # Zet de inhoud van de map in een lijst.
    grootte = 0

    for item in items: # Overloop ieder item.
        item_pad = os.path.join(pad, item)  # Haal pad van item op.

        if os.path.isfile(item_pad):        # Is item een bestand?
            #grootte = os.path.getsize(item_pad) / (1024**2) + grootte # Grootte in MB.
            print(f"{item} is een bestand.")
        elif os.path.isdir(item_pad):       # Is item een map?
            # grootte van een map is verwaarloosbaar.
            grootte = os.path.getsize(item_pad) / (1024**2) + grootte # Grootte in MB.
            #print(f"{item} is een map.")

    return grootte



    
# Cijfers zijn in MB.
print(grootte_map("hfst_1")) # 0.013
print(grootte_map("hfst_5")) # 101.96
print(grootte_map("hfst_6")) # 0.03