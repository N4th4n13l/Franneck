# Matplotlib |
# Daten grafisch darstellen

import matplotlib.pyplot as plt

# -----------------------------
data = [1, 3, 5, 2]

# Schritt 1 welche daten werden geplottet
plt.plot(data, c='r')
# Weitere Mögliche Plot Befehle - Nur Punkte Anzeigen
plt.scatter(range(len(data)), data, c='b') # <<<<<<<<<<<<<<<< Weitere Möglichkeit
# Anzeige als x und y Koordinaten
plt.xlabel('X Werte')
plt.ylabel('Y Werte')
# Ausgabe als verbundene Linien
# z.b. Mittellinie als Schwellwert in gelb
x1 = 0
x2 = 5
y1 = 3
y2 = 3
plt.plot((x1, x2), (y1, y2), c='y')

plt.show()
plt.savefig('Dateien/01.png')
