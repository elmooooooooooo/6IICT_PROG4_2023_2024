# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
grootste_steden = {
    'Frankrijk': {
        'Parijs': 2140526,
        'Marseille': 869815,
    },
    'Belgi?': {
        'Brussel': 1209000,
        'Antwerpen': 523248,
    },
    'Duitsland': {
        'Berlijn': 3769495,
        'Hamburg': 1841179,
    }
}

for land, steden in grootste_steden.items():
    print(land)
    for stad, aantal in steden.items():
        print(f'{stad} heeft {aantal} inwoners.')