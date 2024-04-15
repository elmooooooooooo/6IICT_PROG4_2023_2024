""" OEFENING 2: (  / 10)
Ontwikkel onderstaande klassen. Ze worden gebruikt in paas_oef_2_game.py.
Je kan de code controleren door deze game uit te voeren.
  ! OPGELET: spel zal crashen tot __init__ van Fruit & FruitSpel opgesteld zijn !

Je kan het spel opsplitsen in een aantal onderdelen.
Wat volgt is een overzicht van de methoden die je moet ontwikkelen per onderdeel.
    (1) Spel starten:  __init__ Fruit & __init__ FruitSpel.
    (2) Fruit tonen op scherm: methoden (1), maak_fruit & teken_fruiten.
    (3) Fruit bewegen op scherm: methoden (2), beweeg & beweeg_fruiten.
    (4) Fruit klikken & scoren: methoden (3), bepaal_score, reset_kan_klikken, klikken & raakt_fruit.
    
"""

import pygame, random

class Fruit:
    def __init__(self, x, y, straal, snelheid, kleur, breedte_scherm:int, hoogte_scherm:int): # (  / 2)
        """ Geef objecten van Fruit volgende eigenschappen.
          - x: x-positie van het fruit. Deze heeft als startwaarde altijd 0.
          - y: y-positie van het fruit. Een willekeurig getal tussen 0 en hoogte_scherm.
               Lukt dit niet? Geef deze dan altijd waarde 300. Je krijgt in dit geval minder punten.
          - straal:   straal van het fruit. Een willekeurig getal tussen 0.01*breedte_scherm & 0.05*breedte_scherm.
                      Lukt dit niet? Geef deze dan altijd waarde 15. Je krijgt in dit geval minder punten.
          - snelheid: Snelheid van het fruit. Een willekeurig getal tussen 0.005*breedte_scherm & 0.02*breedte_scherm.
                      Lukt dit niet? Geef deze dan altijd waarde 5. Je krijgt in dit geval minder punten.
          - kleur:    kleur van het fruit. Neem rechtstreeks over uit bovenstaande parameter.
        """
        self.x = 0
        self.y = random.randint(0, hoogte_scherm)
        self.straal = random.randint(0.01*breedte_scherm , 0.05*breedte_scherm)
        self.snelheid = random.randint(0.005*breedte_scherm & 0.02*breedte_scherm)
        self.kleur = kleur

    
    def beweeg(self): # (  / 1)
        " Beweeg de positie van het fruit naar rechts met de eigenschap snelheid van het fruit. "
        if self.snelheid:
            self.x + 1


    def bepaal_score(self): # (  / 1)
        """ RETURN de score die het fruit waard is.
        Deze score is gelijk aan de snelheid*8 min de straal*2.
        """
        return (self.snelheid * 8 - self.straal * 2)


    def teken(self,screen:pygame.Surface): # REEDS GEMAAKT.
        " Teken fruit op screen. "
        pygame.draw.circle(screen,self.kleur,(self.x,self.y),self.straal)


    def raakt_muis(self,muis_pos):         # REEDS GEMAAKT.
        " Raakt de muis dit stuk fruit? Indien ja, return True. "
        return (self.x - muis_pos[0]) ** 2 + (self.y - muis_pos[1]) ** 2 <= self.straal ** 2

        

class FruitSpel:
    def __init__(self, fruiten, score, kan_klikken): # (  / 1)
        """ Geef objecten van FruitSpel volgende eigenschappen.
          - fruiten: alle fruiten in het spel. Start als een lege lijst.
          - score:   de score die behaald is in het spel. Start met waarde 0.
          - kan_klikken: kan de speler in het spel 'klikken'. Start True.         
        """
        self.fruiten = []
        self.score = 0
        if kan_klikken:
            True



    def maak_fruit(self,scherm:list,kleur:tuple): # (  / 1)
        """ Maak een stuk fruit aan (gebruik klasse Fruit) en voeg toe aan de lijst.
        De kleur kan je rechtstreeks overnemen uit bovenstaande parameters.
        
        De parameter scherm moet je eerst opsplitsen in breedte_scherm & hoogte_scherm.
        Je weet dat scherm als volgt is opgebouwd: scherm = [breedte_scherm, hoogte_scherm]
            Tip! Gebruik de index om het te splitsen.
        """
        Fruit(hoogte_scherm = 2, breedte_scherm = 2, kleur=tuple)
        self.fruiten.append(Fruit)


    def teken_fruiten(self,screen:pygame.Surface): # (  / 0.5)
        """ Teken ieder fruit in de lijst fruiten.
        Gebruik hiervoor de methode teken in Fruit.
        """
        for fruit in self.fruiten:
            #teken(fruit)
            pygame.draw.circle(screen,self.kleur,(self.x,self.y),self.straal)


    def beweeg_fruiten(self): # (  / 0.5)
        """ Beweeg ieder fruit in de lijst fruiten.
        Gebruik hiervoor de methode beweeg in Fruit.
        """


    def reset_kan_klikken(self,muis_ingedrukt:bool): # (  / 1)
        """ Reset de eigenschap kan_klikken.
        De eigenschap kan_klikken, moet True worden als...
        kan_klikken momenteel False is EN de muis NIET ingedrukt is (zie muis_ingedrukt).
        """


    def klikken(self,muis_ingedrukt:bool,muis_pos:tuple): # (  / 1)
        """ Als de muis ingedrukt is en de speler kan klikken. Dan...
              1) Zet eigenschap kan_klikken naar False.
              2) Voer de methode raakt_fruiten uit (dit is de methode hieronder).
            Anders gebeurt er niets.
        """


    def raakt_fruiten(self,muis_pos:tuple): # (  / 1)
        """ Scoor & verwijder fruiten die met de muis overlappen.
        Overloop ieder fruit in de lijst fruiten.
            Als de muis het stuk fruit raakt (gebruik hiervoor methode raakt_muis in Fruit).
              1) Verhoog de eigenschap scoren met het resultaat van de methode bepaal_score in Fruit.
              2) Verwijder hierna het stuk fruit uit de lijst fruiten.
        """


    def teken_score(self,screen:pygame.Surface,font:pygame.font.Font): # Reeds gemaakt.
        " Teken de score op screen. "
        score_afb = font.render( f"Score: {self.score}", True, (255,255,255) )
        screen.blit(score_afb,(20,20))