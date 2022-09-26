# Sets | (Mengen)
# ähnlich wie Tuples können aber nicht geändert werden. Keine Keys

familie_mutter = {'angelika', 'monika', 'barbara'}
familie_vater = {'dieter', 'anne', 'lothar', 'monika'}

print('dieter' in familie_mutter)
print('dieter' in familie_vater)


familie =  familie_mutter | familie_vater # wir bilden ein Set mit Namen aus beiden Familien
print(familie)

gleiche_namen = familie_mutter & familie_vater  # welcher Name ist in beiden Listen?
print(gleiche_namen)

gleiche_namen1 = familie_mutter - familie_vater  # unwichtig :-)
print(gleiche_namen1)

gleiche_namen2 = familie_mutter ^ familie_vater  # nur die NAmen welche nicht doppelt sind
print(gleiche_namen2)

# set comprehension
famielie02 = {person for person in familie_mutter + familie_vater }
print(famielie02)