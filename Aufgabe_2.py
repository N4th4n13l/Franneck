# Aufgabe
# Anlegen eine Dict für mehrere Personen
# Vertiefung-Gebiete und Noten
# Dictionary abgespeichert und einzelne Werte jeden Perso ausgeben
# Zusatzaufgabe -- gleiche Person mit gleichen Interessen ausgeben

personen = ['Jan', 'Max', 'Horst']

pref = {'Jan': ['AI', 'ITS', 'Mathe'],
        'Max': ['ITS', 'ET', 'Physik'],
        'Horst': ['Pysik', 'Mathe', 'Chemie']}

noten = {'Jan':[1, 3, 5],
         'Max':[2, 3 ,2],
         'Horst': [3, 2, 1]}

zusammen = {pers: [(fach, note) for fach, note in
                   zip(pref[pers], noten[pers])]
               for pers in personen}

for person, daten in zusammen.items():
    print('Student: ', person)
    for fach in daten:
        print('Fach: ', fach[0], 'Note: ', fach[1])
