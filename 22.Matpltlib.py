# Matplotlib |
# Daten grafisch darstellen

import matplotlib.pyplot as plt

# -----------------------------
data = [1, 3, 5, 7]

# Schritt 1 welche daten werden geplottet
plt.plot(data, c='r')
# Weitere Mögliche Plot Befehle - Nur Punkte Anzeigen
plt.scatter(range(len(data)), data, c='b') # <<<<<<<<<<<<<<<< Weitere Möglichkeit
# Anzeige als x und y Koordinaten
plt.xlabel('X Werte')
plt.ylabel('Y Werte')
# Ausgabe als verbundene Linien
plt.show()
plt.savefig('Dateien/01.png')
