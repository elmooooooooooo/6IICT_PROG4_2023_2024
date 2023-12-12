""" Oefening 3 (  / 8): klikker app.

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


counter = 0
def teller():
  global counter
  invoer.get()
  counter += 1
  invoer.set(str(counter))

  if counter % 2 == 0:
    veld.config(fg="green")
  else:
    veld.config(fg="red")



invoer = tk.StringVar()
invoer.set(str(counter))
veld = tk.Entry(master=app, background="white", width=100, textvariable=invoer)
veld.grid(row=0, column=0)
veld.config(fg="green")

knop1 = tk.Button(master=app, text="klik", command=teller)
knop1.grid(column=0, row=1)

app.mainloop()