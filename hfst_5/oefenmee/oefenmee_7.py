# Werk verder met de klasse Hond van oefen mee 6.
class Hond:
    def __init__(self, naam, gewicht):
        self.naam = naam
        self.gewicht = gewicht

    def weegschaal(self):
        print(f"{self.naam} weegt {self.gewicht}kg.")

    def wijzig_naam(self, naam):
        print(f"{self.naam} heet nu {naam}.")
        self.naam = naam
    
    def eten(self, massa):
        self.gewicht = self.gewicht + (massa * 0.3)
        print(f"{self.naam} is nu {self.gewicht}kg.")

" Via onderstaande code kan je niveau 1 testen. "
hond = Hond("Lucky", 5)
hond.wijzig_naam("Bolly")

" Via onderstaande code kan je niveau 2 testen. "
hond.eten(0.5)
hond.eten(0.5)
hond.eten(0.5)

" Stel de test voor niveau 3 zelf op. "

# *0.3