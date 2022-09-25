# Listen <<comprehensions>> |  Das richtige anlegen von Listen

vector = [0 for _ in range(4)]
print(vector)

vector = [i for i in range(10)]
print(vector)
# 2 d Matrix - Listen
matrix = [ [0 for j in range(3)] for i in range(4)]   # Aussen die 4 sind die Zeilen - die inneren die Spalten (3)

print(matrix)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]] Zeilen und Spalten in der Ausgabe

matrix = [ [i * j for j in range(3)] for i in range(4)] #das Erste ist die Operation bei jeder Runde zält es 1 dazu
print(matrix)