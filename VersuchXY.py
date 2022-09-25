personalien = []

vorname = input('Bitte Vornamen eingeben: ')
nachname = input('Bitte Nachname eingeben: ')
wohnort = input('Bitte Wohnort eingeben: ')

personalien.append([vorname, '\n', nachname, '\n', wohnort])

with open('personalien.txt', 'a') as p:
    p.write(vorname + ' ' + nachname + ', ' + wohnort + '\n')
with open('personalien.txt', 'r') as p:
    for line in p:
        print(line + 'zur Kontrolle direkt in der Ausgabe')

print(personalien)
