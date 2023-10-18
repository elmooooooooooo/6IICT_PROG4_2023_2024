"""
Volg de instructies van oefen mee 8.
Je zal een simpel rekenmachine maken met behulp van 2 Entries, 1 label & 1 button.
    
    Tip! De methode .get() van entries geeft altijd een string.
         Je kan hier natuurlijk niet mee rekenen.
"""

import tkinter as tk
app = tk.Tk()

# Functie maakt & plaatst een label.

veld1 = tk.Entry(master=app)
veld1.grid(row=0, column=0)

veld2 = tk.Entry(master=app)
veld2.grid(row=0, column=1)

def som():
    getal1 = int(veld1.get())
    getal2 = int(veld2.get())

    print(getal1 + getal2)
    uitkomst.config(text=f"De som van de bovenstaande getallen is: {getal1 + getal2}")

uitkomst = tk.Label(master=app, text=f"De som van de bovenstaande getallen is: ",)
uitkomst.grid(row=1, column=0, columnspan=2)

# 1) Knop aanmaken.
knop = tk.Button(master=app, text="bereken", command=(som))
# 2) Knop plaatsen.
knop.grid(row=2, column=0, columnspan=2)

app.mainloop()