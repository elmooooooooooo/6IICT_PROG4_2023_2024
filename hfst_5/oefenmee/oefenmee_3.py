# Op welke regels print deze code iets?
# Er za ook een fout ontstaan. Leg uit waarom.
class Kat:
    naam = "Borysz"

    def miauw(self):
        print(f"{kitten.naam} zegt miauw") #FOUT MELDING kitten moet self zijn.

kater = Kat()
kater.miauw() 

kitten = Kat()
kitten.miauw()