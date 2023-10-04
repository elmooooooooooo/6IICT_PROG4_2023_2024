shrek_movie = {
    "titel": "Shrek",
    "regiceurs": ["Andrew Adamson", "Vicky Jenson"],
    "hoofdpersonages": {
        "shrek": {
            "stemacteur": "Mike Myers",
            "soort": "Oger",
        },
        "ezel": {
            "stemacteur": "Eddie Murphy",
            "soort": "Sprekende Ezel",
        },
    },
    "cijfers": {"opbrengst": "$48 miljoen", "kosten": "$50 miljoen"},
    "prijzen": {"academy awards": 1, "BAFTA awards": 1}
}

""" 1)
Print de zin "Sprekende Ezel" door deze op te halen uit de dictionary.
"""
print(shrek_movie["hoofdpersonages"]["ezel"]["soort"])

""" 2)
De waarde van sleutel "opbrengst" bevat een fout. Corrigeer deze.
Ze geven hier een opbrengst van $48 miljoen, dit zou $480 miljoen moeten zijn.
"""
shrek_movie["cijfers"] = {"opbrengst": "$480 miljoen", "kosten": "$50 miljoen"}
print(shrek_movie["cijfers"]["opbrengst"])

""" 3)
De sleutel "regiceurs" is verkeerd gespeld. Vervang deze door de sleutel "regisseurs". 
De waarde verbonden aan deze sleutel moeten hetzelfde blijven.
    Opgelet! Dit moet werken, ongeacht welke waarde verbonden is aan de sleutel.
"""
shrek_movie.pop("regiceurs")
shrek_movie.update({
    "regisseurs": ["Andrew Adamson", "Vicky Jenson"]})
print(shrek_movie["regisseurs"])

""" 4)
Print een overzicht van de prijzen die de film gewonnen heeft.
De code moet blijven werken, ook als er later meer prijzen worden toegevoegd.
De print moet er als volgt uitzien.

    Prijzen voor de film Shrek:
        - academy awards: 1
        - BAFTA awards: 2

Tip! Maak eerst een nieuwe variabele met de waarde van sleutel "prijzen".
     Overloop deze met een for-loop.
"""
# prijzenlijst = {"prijzen": {"academy awards": 1, "BAFTA awards": 1}}

# for s, prijzen in prijzenlijst.items():
#     print(f"""Prijzen voor de film Shrek:
#     -{prijzen}
# """)

for award, aantal in shrek_movie["prijzen"].items():
    print(award,aantal)