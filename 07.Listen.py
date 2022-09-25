# Listen <<important>>

# a0a + b oder a + a = b
# extend oder append  --  erweitern oder anhängen
# insert, pop, count, iterieren

einkaufs_liste = ['milch', 'wasser', 'eier', 'apfel']
zusatz_liste = ['packpulver', 'bananen']
zusatz_liste_neu = 'brot'
print(einkaufs_liste)

"""einkaufs_liste  = einkaufs_liste + zusatz_liste #gar nicht cool - nie machen
einkaufs_liste += zusatz_liste # etwas cooler - kann man"""

einkaufs_liste.extend(zusatz_liste) # Beste Variante für extend
print(einkaufs_liste)

einkaufs_liste.append(zusatz_liste_neu) # nach append
print(einkaufs_liste)

einkaufs_liste.pop()  # POP  --  letztes Element löschen oder Zahl eingeben um Anzahl der letzten ? zu löschen
print(einkaufs_liste)

print(einkaufs_liste.count('milch')) # COUNT  -- !!  zählen was wie viel in Liste

"""for i in range(len(einkaufs_liste)): # möglich aber nicht sehr cooler Code
    print(einkaufs_liste[i])"""

for val in einkaufs_liste:  # Beste Variante um die einzelnen Elemente einer Liste anzuzeigen
    print(val)
    

