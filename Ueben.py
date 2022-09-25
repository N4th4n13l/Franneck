tagebuch = {'Montag:' 'Doofer Tag', 'Dienstag:' 'War schon besser'}

tagebuch = {'Montag': ['Schule doof', 'ganzer Tat Regen', 'alles doof'],
            'Dienstag': ['war schon besser', 'ich war aber cool']}


# Die 3 Arten von Augabe für Dictinarys die man kenne sollte

for k in tagebuch.keys():
    print(k)

for v in tagebuch.values(): # Ausgabe der Values
    print(v)

for k, v in tagebuch.items(): # Ausgabe von beidem
    print(k, v)

"""for k, liste in tagebuch2.items(): # wir holen den Key mit der Liste der Values
    print('key: ', k)
    for val in liste:
        print(val)"""
