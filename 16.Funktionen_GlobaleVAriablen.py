# Funktionen | Globale Variablen
#  Aufpassen wie man von wo in Funktionen, Variablen auslesen kann

name = input('Name?:')


def non():
    zahl = 0

    def hello():
        nonlocal zahl  # übernehmen aus andere Funktion
        zahl = zahl + 1
        print('hello ' + name + str(zahl))  # Übernahme aus Variable oberhalb der Funktion im Code

    hello()  # WICHTIG Matthias ist ein Argument zum Parameter oben


non()
