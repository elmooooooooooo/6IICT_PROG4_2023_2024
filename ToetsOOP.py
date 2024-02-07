class Account():

    def __init__(self, naam, balans, type):
        self.naam = naam
        self.balans = balans
        self.type = type

    def overzicht(self):
        print(f"naam = {self.naam}, type = {self.type}, balans = {self.balans}")

    def storten(self, bedrag):
        if type(bedrag) != int:
            raise ValueError("Typ een getal!")
        
        self.balans = self.balans + bedrag
        print(f"neuwe saldo: {self.balans} euro.")
        pass

    def afhalen(self, bedrag):
        if bedrag < 0:
            print("geen bedragen kleiner dan 0!")
        self.balans = self.balans - bedrag
        print(f"neuwe saldo: {self.balans} euro.")
        

class Bank():

    def __init__(self, KBC, bonus):
        self.KBC = KBC
        self.accounts = []
        self.bonus = bonus

    def toevoegen(self, account: 'Account'):
        if type(account) == Account:
            self.account = account
            self.accounts.append(account)
            print(f"account van {account.naam} is toegevoegd.")
        else:
            print("Geen geldig account opgegeven!")

    def overzicht(self):
        print(f"De bank {self.KBC} heeftv volgende accounts: ")
        for klanten in self.accounts:
            print(Account.overzicht())

    def bonus_uitkeren(self):
        pass
