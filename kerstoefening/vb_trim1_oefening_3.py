""" Oefening 3 (  / 8): klikker-app

Baseer je op oefening_3.exe om de klikkerapp op te bouwen.
Onderstaande vereisten bevatten de zaken waar je zeker op moet letten.

Grafische vereisten:
    - Bouw de app na zoals in de exe (de widgets moeten allemaal op dezelfde plaats staan).
    - De titel van de app is "klikker-spel".
    - De Entry bovenaan heeft bij de start van de app een waarde 0 reeds ingevuld.
    - De knop heeft een breedte van 15.
    - Het label dat de teller toont heeft als font "Helvetica" met een grootte 14.
    - Het label dat de teller toont heeft een padding van 10 boven en onder zich.

Functionele vereisten:
    - Op de knop duwen moet een teller verhogen met de waarde die momenteel in de Entry staat.
      Bevat de Entry GEEN geheel getal op dat moment? Reset de teller dan naar 0.
    - Na het verhogen van de teller moet ook het label onderaan wijzigen.
      ---> Het getal rechts in het label moet dezelfde waarde zijn als de teller.
      ---> Is de teller even, dan is het label groen. Is de teller oneven, dan is het label rood.

"""
import tkinter as tk

app = tk.Tk()
app.title("Klikker-spel")

teller = 0
def verhoog_teller():
    global teller

    hoeveelheid = hoeveelheid_entry.get()

    if not hoeveelheid.isnumeric():
        teller = 0
    else:
        teller += int(hoeveelheid)

    if teller % 2 == 0:
        teller_label.config(fg="green", text=f"Teller: {teller}")
    else:
        teller_label.config(fg="red", text=f"Teller: {teller}")

uitleghoeveelheid_label = tk.Label(app, text="Teller verhogen met: ")
uitleghoeveelheid_label.grid(row=0,column=0)
hoeveelheid_entry       = tk.Entry(app)
hoeveelheid_entry.insert(0,"0")
hoeveelheid_entry.grid(row=0,column=1)

verhoog_button = tk.Button(app, text="Verhoog de teller!", command=verhoog_teller, width=15)
verhoog_button.grid(row=1, column=0, columnspan=2)

teller_label = tk.Label(app, text="Teller: 0", fg="green", font=("Helvetica",15))
teller_label.config(fg="green")
teller_label.grid(row=2, column=0, columnspan=2, pady=(10,10))

app.mainloop()