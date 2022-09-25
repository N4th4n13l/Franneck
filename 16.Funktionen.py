# Funktionen | Eigen Funktionen erstellen
# immer mit def beginnen und mit: beenden

def func(a=None, b=None, c=None):  # Attributen übergeben in der Funktion
    print('A :', a)  # None gleich nichts und der Compiler erwartet auch nichts
    print('B :', b)
    print('C :', c)


func(a=2, c=1)  # Attribute können mit irgendwas gefüllt werden - Hier wird bestimmt was print ausgibt

func(b=3, c=2) # Wir können oder müssen definieren welches Attribut welcher ist


def func01(a=10, b=0, c=None):
    print('A :', a)
    print('B :', b)
    print('C :', c)

func01()  # nix angeben gibt default Werte von oben aus.

func01(b=3, c=2) # aist default von oben b und c sind unten definiert
#--------------------------------------------------------------------
# Werte zurück/-Ausgeben
def func02(a=10, b=2, c=None):
    print('A :', a)
    print('B :', b)
    val = a * b
    return val
wert = func02(3, 12)
print(wert)



