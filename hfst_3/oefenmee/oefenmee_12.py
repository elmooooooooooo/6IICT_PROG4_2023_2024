"""
Volg de instructies van oefen mee 12.
In deel 1 van de oefen mee maak je het uiterlijk van een rekenmachine.
In deel 2 zal je deze ook echt laten werken.

    Tip! Je kan instellingen van widgets ook inladen via een dictionary.
         Op deze manier kan je veel gelijkaardige widgets snel opstellen en aanpassen.
         Er is een voorbeeld onderaan de oefen mee voorzien.
"""

import tkinter as tk
app = tk.Tk()

veld = tk.Entry(master=app, background="green")
veld.grid(row=0, column=0, columnspan=3)

knop1 = tk.Button(master=app, text="1", width=5, height=2)
knop1.grid(row=2, column=0)

knop2 = tk.Button(master=app, text="2", width=5, height=2)
knop2.grid(row=2, column=1)

knop3 = tk.Button(master=app, text="3", width=5, height=2)
knop3.grid(row=2, column=2)

knop4 = tk.Button(master=app, text="4", width=5, height=2)
knop4.grid(row=3, column=0)

knop5 = tk.Button(master=app, text="5", width=5, height=2)
knop5.grid(row=3, column=1)

knop6 = tk.Button(master=app, text="6", width=5, height=2)
knop6.grid(row=3, column=2)

knop7 = tk.Button(master=app, text="7", width=5, height=2)
knop7.grid(row=4, column=0)

knop8 = tk.Button(master=app, text="8", width=5, height=2)
knop8.grid(row=4, column=1)

knop9 = tk.Button(master=app, text="9", width=5, height=2)
knop9.grid(row=4, column=2)

knop0 = tk.Button(master=app, text="0", width=5, height=2)
knop0.grid(row=5, column=0)

knopplus = tk.Button(master=app, text="+", width=5, height=2)
knopplus.grid(row=5, column=1)

knopmin = tk.Button(master=app, text="-", width=5, height=2)
knopmin.grid(row=5, column=2)

knopgelijk = tk.Button(master=app, text="=", width=5, height=2)
knopgelijk.grid(row=6, column=0)

knopgelijk = tk.Button(master=app, text="CLR", width=12, height=2)
knopgelijk.grid(row=6, column=1, columnspan=2)

def som():
    getal1 = int(veld1.get())
    getal2 = int(veld2.get())

    print(getal1 + getal2)
    #uitkomst.config(text=f"De som van de bovenstaande getallen is: {getal1 + getal2}")

app.mainloop()