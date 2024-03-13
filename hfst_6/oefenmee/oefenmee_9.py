# Bepaal het aantal bestanden in een map (en alle submappen).
import os

def doorzoek_map(pad):
    items = os.listdir(pad)  # Zet de inhoud van de map in een lijst.

    teller = 0
    for item in items: # Overloop ieder item.
        item_pad = os.path.join(pad, item)  # Haal pad van item op.

        if os.path.isfile(item_pad):        # Is item een bestand?
            teller = teller + 1
            # print(f"{item} is een bestand.")
        elif os.path.isdir(item_pad):       # Is item een map?
            # print(f"{item} is een map.")
            teller = doorzoek_map(item_pad) + teller

    return teller

" Opgelet! uitkomsten geven aantal bestanden aan. Mappen zelf zijn niet meegeteld. "
print( doorzoek_map("hfst_1") )    # 40 
print( doorzoek_map("hfst_5") )    # 553 
print( doorzoek_map("hfst_6") )    # 43
