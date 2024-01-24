# Werk verder met de klasse Hond van oefen mee 4.
class Hond:
    def __init__(self, naam, gewicht):
        self.naam = naam
        self.gewicht = gewicht

    def weegschaal(self):
        print(f"{self.naam} weegt {self.gewicht}kg.")

hond_1 = Hond("Floris", 8)

hond_2 = Hond("Fido", 3)

" Via onderstaande code kan je niveau 2 testen. "
hond_1.weegschaal()
hond_2.weegschaal()
