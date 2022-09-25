# Klassen |
# Erstellen von eigenen Klassen

class Tier:
    rasse = ''
    geschlecht = ''
    alter = 0

    def __init__(self, rasse, geschlecht, alter):  # Braucht es immer - wieso k.A.
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.alter = alter

    def printRasse(self):
        print('Name:', self.rasse)


# Grund Klasse >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Vererbung von Tier zu Hund - als Untergattung
class Hund(Tier):
    tazen_groesse = 0

    def __init__(self, tazen_groesse, rasse, geschlecht, alter):  # immer Attribute der Mutterklasse angeben
        super().__init__(rasse, geschlecht, alter)  # mit dem super-Befehl beziehen wir uns auf die Mutterklasse Tier
        self.tazen_groesse = tazen_groesse


h1 = Hund(10, 'Dackel', 'Männlich', 5)
h1.printRasse()  # Funktion aus der Eltern Klasse aufgerufen
