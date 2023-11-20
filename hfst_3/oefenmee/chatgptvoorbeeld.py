import tkinter as tk

def bereken():
    try:
        invoer = invoerveld.get()
        resultaat = eval(invoer)
        resultaat_label.config(text="Resultaat: " + str(resultaat))
    except Exception as e:
        resultaat_label.config(text="Fout: Ongeldige invoer")

# Maak het hoofdvenster
venster = tk.Tk()
venster.title("Rekenmachine")

# Invoerveld
invoerveld = tk.Entry(venster, width=20)
invoerveld.grid(row=0, column=0, columnspan=4)

# Resultaatlabel
resultaat_label = tk.Label(venster, text="Resultaat: ")
resultaat_label.grid(row=1, column=0, columnspan=4)

# Knoppen
knoppen = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 2
col_val = 0

for knop in knoppen:
    tk.Button(venster, text=knop, padx=20, pady=20, command=lambda knop=knop: invoerveld.insert(tk.END, knop) if knop != '=' else bereken()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

venster.mainloop()
