# JSON | JavaScript Object Notation
# um mmit excel etx LIsten zu arbeiten ist Pasndas gut
import json
# import pandas

personen = ['Jan', 'Max', 'Horst']

pref = {'Jan': ['AI', 'ITS', 'Mathe'],
        'Max': ['ITS', 'ET', 'Physik'],
        'Horst': ['Pysik', 'Mathe', 'Chemie']}

noten = {'Jan': [1, 3, 5],
         'Max': [2, 3, 2],
         'Horst': [3, 2, 1]}

personen_dict = {pers: [(fach, note) for fach, note in
                        zip(pref[pers], noten[pers])]
                 for pers in personen}

print(personen_dict)

with open('studenten_noten.txt', 'w') as f:
    json.dump(personen_dict, f, indent=4, separators=(',', ':'), sort_keys=True)
