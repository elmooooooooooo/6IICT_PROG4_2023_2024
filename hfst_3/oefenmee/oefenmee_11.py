"""
Volg de instructies van oefen mee 11.
Je zal een app maken om de kleur van een label aan te passen.
De app bestaat uit 1 entry, 1 label & 1 button.

    Tip! Je zal de methode .config() moeten gebruiken.
         Hiermee kan je de onderdelen (kleur, tekst, ...) van een widget wijzigen.

"""

import tkinter as tk
app = tk.Tk()

# Maak label aan waarin tekst van Entry komt te staan
label = tk.Label(master=app, text="")
label.grid(row=0, column=0)

# Wijzig de tekst en kleur van het label.
label.config(text="Het label is nu rood", fg="red")

app.mainloop()
