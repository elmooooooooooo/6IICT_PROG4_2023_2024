# Werk verder met de klasse Hond van oefen mee 2.

" Via onderstaande code kan je niveau 1 testen. "

class Hond:
    def benoem(self, benaming):
        self.naam = benaming

    def blaf(self):
        print(f"{self.naam} zegt blaf")

    def wegen(self, gewicht):
        self.massa = gewicht

    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa}kg.")

hond = Hond()
hond.benoem("Fleur")
print( hond.naam )
hond.blaf()

" Via onderstaande code kan je niveau 2 testen. "
dier = Hond()
dier.benoem("Fifi")
dier.wegen(3)
print( dier.massa )
dier.weegschaal()