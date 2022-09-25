#Aufgabe aus import random https://www.youtube.com/watch?v=_I46-DLj5Zg&list=PLt_1e8h-E5Lb3shyy92ry-HcW-kKCXMXy&index=11
# Tuto 11
import random
# Zwei leere Lisen anlegen
smaller = []
bigger = []
#Zufallsliste generieren
data = [random.randint(0, 10) for _ in range(10)]
# User Input
zahl = int(input("Bitte Zahl eingeben"))

for var in data:
    if var < zahl:
        smaller.append(var)
    elif var > zahl:
        bigger.append(var)

print(data)
print(smaller)
print(bigger)

