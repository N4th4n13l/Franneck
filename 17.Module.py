# Module | laden und eigene erstellen
# __init__.py

import numpy # Befehl zum importieren
import numpy as np # Modul importieren und mit anderem Namen weiterverwenden.
import EigenesModul

print(numpy.mean([1,2])) # Modul anwählen Punkt und dann was es machen soll
print(np.mean([2,4]))


from numpy import mean # alles reinladen von dem Modul - Nicht unbedingt benutzen da viel Speicher
print(mean([1,2]))

EigenesModul.func01()

# ------------------ Eine Software besteht aus diversen Modulen! Eigenen oder externen -------------------
# Wir brauchen einen Einstiegspunkt
# from MODUL import FUNKTION - so können wir gezielt auswählen was wir wollen

# wenn wir einen Unterordner haben braucht es eine leere python Datei mit dem Code >>>>>>>>>>>>>>>>
# __init__.py   <<<<<<<<< nur wenn wir Klassen und Funktionen nutzen wollen

# dann muss es heissen >>> from ORDNER import Modul und aufgerufen wir es mit MODUL.FUNKTION
# oder from ORDNER.MODUL import FUNKTION
