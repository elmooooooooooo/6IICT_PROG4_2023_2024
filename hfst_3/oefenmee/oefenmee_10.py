"""
Volg de instructies van oefen mee 10.
Je zal een app maken waarmee je de eerste/laatste letter uit een entry kan verwijderen.
De app bestaat uit 1 entry & 2 buttons.

"""
import tkinter as tk
app = tk.Tk()

# Functie maakt & plaatst een label.
veld = tk.Entry(master=app)
veld.grid(row=0, column=0, columnspan=2)

def lettereerst():
    veld.delete(0,1)

def letterlaatst():
    inhoud = veld.get() # Haal huidige inhoud op. 
    inhoud = inhoud[:-1] # Verwijder laatste letter uit variabele. 
    veld.delete(0,tk.END) # Maak volledige Entry leeg. 
    veld.insert(0,inhoud) # Voeg gewijzigde inhoud terug toe. 


# 1) Knop aanmaken.
knop = tk.Button(master=app, text="verwijder eerste", command=lettereerst)
# 2) Knop plaatsen.
knop.grid(row=1, column=1)

knop2 = tk.Button(master=app, text="verwijder laatste", command=letterlaatst)
# 2) Knop plaatsen.
knop2.grid(row=1, column=0)

app.mainloop()
