# Module | laden und eigene erstellen

import numpy # Befehl zum importieren
import numpy as np # Modul importieren und mit anderem Namen weiterverwenden.
import EigenesModul

print(numpy.mean([1,2])) # Modul anwählen Punkt und dann was es machen soll
print(np.mean([2,4]))


from numpy import mean # alles reinladen von dem Modul - Nicht unbedingt benutzen da viel Speicher
print(mean([1,2]))

EigenesModul.func01()
