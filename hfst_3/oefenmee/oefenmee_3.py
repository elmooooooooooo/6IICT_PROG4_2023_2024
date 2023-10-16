"""
Maak de app na volgens de foto bij oefen mee 3.
Je hebt maar 3 labels nodig om deze app te maken.
"""

import tkinter as tk

app = tk.Tk()

label_1 = tk.Label(master=app, text="hallo")
label_1.grid(row=0,column=0)

label2 = tk.Label(master= app, text="klas" )
label2.grid(row=0, column=1)

label3 = tk.Label(master= app, text="6IICT" )
label3.grid(row=1, column=1,pady=0)

app.mainloop()