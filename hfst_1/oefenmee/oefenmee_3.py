# Start de oefen mee met onderstaande dictionary.
persoonsinfo = { # info over een persoon
    "naam": "Jan",
    "leeftijd": 32,
    "massa": 79
}

print(f'{persoonsinfo["naam"]} is {persoonsinfo["leeftijd"]} jaar oud en weegt {persoonsinfo["massa"]} kg')

print( len( persoonsinfo ) )
#len is een opsomming persoonsinfo = 3

nieuw_oogkleur = "oogkleur" 
nieuw_kleur = "blauw"
persoonsinfo[nieuw_oogkleur] = nieuw_kleur
print(f"Deze persoon heeft {persoonsinfo} ogen.")

naam = "Jan"
print(persoonsinfo[naam])
#jan heeft geen waarde
