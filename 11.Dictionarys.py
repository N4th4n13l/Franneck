# Dictionarys {key: value} | https://www.youtube.com/watch?v=5cdQdSl41M8&list=PLt_1e8h-E5Lb3shyy92ry-HcW-kKCXMXy&index=12

tagebuch = { 'Montag:' 'Doofer Tag', 'Dienstag:' 'War schon besser' }
tagebuch = {'Montag': ['Schule doof', 'ganzer Tat Regen', 'alles doof'], 'Dienstag': ['war schon besser', 'ich war aber cool']}

tagebuch = {'Montag': {'Morgen': 'doof', 'Mittag': 'noch doofer', 'Abend': 'am doofsten'},
            'Dienstag': ['war schon besser', 'ich war aber cool']}

print(  tagebuch['Montag']['Morgen']   )
print(   tagebuch ['Montag']['Abend']  )
print(tagebuch)


dog = { 'name': 'Roger', 'age': 8}
print(dog.get('name'))  # Gib mir den Namen aus dem Dic Dog aus

print(list(dog.keys())) # Was sind in Dogs für Keywörter
print(list(dog.values())) # WAs sind für Value Wörter drin
print(list(dog.items()))
print(list(dog.items()))
print(len(dog))
dog['Essen'] = 'Fleisch' # Finde ich och wichtig!!!<<<<<<<<<<<<<<<<<<<<<<<<<<<
print(dog)
del dog['age']  # Key Value Paare löschen
print(dog)
dogCopy = dog.copy() # Dictionary kopieren

#
#
#
