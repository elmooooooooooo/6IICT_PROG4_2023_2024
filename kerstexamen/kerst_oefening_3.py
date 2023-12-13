""" oefening 3 (   / 8): Authenticatie app

Baseer je op kerst_oefening_3.exe om de authenticatie app op te bouwen.
Onderstaande vereisten bevatten de zaken waar je zeker op moet letten.

Grafische vereisten:
    - Bouw de app na zoals in de exe (de widgets moeten allemaal op dezelfde plaats staan).
    - De titel van de app is "Authenticator".
    - De gebruiker kan de grootte van de app niet wijzigen (Tip: gebruik resizable).
    - Het label bovenaan is onderlijnd en heeft als font "Euphemia" met grootte 16.
    - Het label bovenaan heeft een padding van 30 links en rechts van zich.
    - De Entry in het midden heeft een padding van 10 boven en onder zich.
    - Beide knoppen hebben een breedte (width) van 12.
    - Het label onderaan heeft een padding van 10 ENKEL boven zich.

Functionele vereisten:
    - Op de knop inloggen duwen moet nagaan of de huidige gebruiker bestaat.
      Doe dit door te controleren of de inhoud van de Entry in de lijst gebruikers voorkomt.
      ---> Dit is het geval: maak het label bovenaan groen en wijzig naar "Welkom, *gebruiker*!"
      ---> Dit is niet het geval: maak het label bovenaan rood en wijzig naar "Ongeldige login!"
    - Na het drukken op de knop inloggen moet de Entry volledig leeggemaakt worden, 
      dit ongeacht of de login gelukt is of niet.
    - Op de knop status drukken toont de status ENKEL als de admin is ingelogd.
      ---> De admin is ingelogd: wijzig label onderaan naar "Dit is de status..." in het groen.
      ---> De admin is niet ingelogd: wijzig label onderaan naar "Geen recht voor status..." in het rood.

      Tip! Hou de huidig ingelogd gebruiker bij in een globale variabele.
           Je kan deze gebruiken om te controleren of de admin is ingelogd.

"""
import tkinter as tk

app = tk.Tk()
app.title("Authenticator")

# Lijst met verschillede soorten gebruikers.
gebruikers = ["admin", "personeel"] 

inloggen_label = tk.Label(app, text="Gelieve in te loggen", fg="black", font=("Helvetica 15 underline"))
inloggen_label.config(fg="black")
inloggen_label.grid(row=0, column=0, columnspan=2)

accountnaam = tk.Label(app, text="Geef account op: ")
accountnaam.grid(row=1,column=0, pady=5)

Inloggegevens= tk.Entry(app)
Inloggegevens.grid(row=1,column=1, pady=5)

inloggenknop = tk.Button(app, text="Inloggen", width=10)
inloggenknop.grid(row=2, column=0, columnspan=1, pady=5)

toonStatusknop = tk.Button(app, text="Toon status",width=10)
toonStatusknop.grid(row=2, column=1, columnspan=1, pady=5)

status_label = tk.Label(app, text="Hier verschijnt de status...", fg="black", font=("Helvetica",8))
status_label.config(fg="black")
status_label.grid(row=3, column=0, columnspan=2)

# geen tijd meer om af te maken :(

app.mainloop()