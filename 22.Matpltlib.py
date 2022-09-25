# Matplotlib |
# Daten grafisch darstellen
import random
import matplotlib.pyplot as plt

# -----------------------------
#data = [1, 3, 5, 7]
data = random.randint(1,10)in range (10)
for i in data:
      print(i)
# Schritt 1 welche daten werden geplottet
plt.plot(data, c='r')
#Weitere Mögliche Plot Befehle - Nur Punkte Anzeigen
#plt.scatter(range(len(data)), data, c='b') # <<<<<<<<<<<<<<<< Weitere Möglichkeit
# Anzeige als x und y Koordinaten
plt.xlabel('X Werte')
plt.ylabel('Y Werte')
# Ausgabe als verbundene Linien
plt.show()
