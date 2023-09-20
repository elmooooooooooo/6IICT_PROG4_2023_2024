# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
spelinfo = {
    'speler1': {
        'naam': 'Alice',
        'positie': {
            'x': 10,
            'y': 5
        },
        'inventaris': {
            'bepantsering': 'schild',
            'wapen': 'zwaard',
            'goud': 50
        }
    },
    'speler2': {
        'naam': 'Bob',
        'positie': {
            'x': 2,
            'y': 8
        },
        'inventaris': {
            'wapen': 'boog',
            'goud': 9999999999
        }
    }
}

print(spelinfo['speler2']['naam'])
print(spelinfo['speler2']['positie']['x'])
print(spelinfo['speler2']['positie']['y'])
print(spelinfo['speler2']['inventaris']['wapen'])

spelinfo['speler2']['inventaris']['goud'] = 0
spelinfo['speler2']['hacker'] = True
spelinfo['speler1']['hacker'] = False

print(spelinfo)