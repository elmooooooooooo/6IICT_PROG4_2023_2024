"""
Volg de instructies van oefen mee 9.
Je zal een app maken om letters toe te voegen aan een entry op een specifieke positie?
De app bestaat uit 3 entries & 1 button.

"""

import tkinter as tk
app = tk.Tk()

# Functie maakt & plaatst een label.

veld1 = tk.Entry(master=app)
veld1.grid(row=0, column=0)

veld2 = tk.Entry(master=app)
veld2.grid(row=0, column=1)

veld3 = tk.Entry(master=app)
veld3.grid(row=2, column=0, columnspan=2)

def lettersom():
    getal = int(veld1.get())
    letter = veld2.get()
    
    veld3.insert(getal, letter)

# 1) Knop aanmaken.
knop = tk.Button(master=app, text="bereken", command=(lettersom))
# 2) Knop plaatsen.
knop.grid(row=1, column=0, columnspan=2)

app.mainloop()