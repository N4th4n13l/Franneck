# Aufgabe 4
# Anlegen eine Dict für mehrere Personen
# https://www.youtube.com/watch?v=gjNhv3_Liw8&list=PLt_1e8h-E5Lb3shyy92ry-HcW-kKCXMXy&index=27
# Erstelle Klasse Mensch mit gängigen Attributen
# Erstelle dann eine unterklasse als Student mit Nummer, Semster Studiengang
# Zusatzaufgabe -- Erstelle einige Objekte und interiere über sie

class mensch:
    name = ''
    vorname = ''
    alter = 0

    def __init__(self, name, vorname, alter):
        self.name = name
        self.vorname = vorname
        self.alter = alter

    def printName(self):
        print('Name:', self.name)
        print('Vorname:', self.vorname)
        print('Alter:', self.alter)

# Hier werden die Attribute bestimmt und ausgegeben
aus01 = mensch('lobsiger', 'matthias', 48)
aus01.printName()

class student(mensch):
    nr = 0
    semester = 0
    studiengang = ''

    def __init__(self, nr, semester, studiengang, name, vorname, alter):
        super(student, self).__init__(name, vorname, alter)
        self.nr = nr
        self.semester = semester
        self.studiengang = studiengang

    def print_All(self):
        super(student, self).printName()
        print('Nummer: ', self.nr)
        print('Semester: ', self.semester)
        print('Studiengang', self.studiengang)

Matthias = student(52625, 4, 'Informatik', 'Lobsiger', 'Matthias', 48)
Matthias.print_All()

# ---------interieren---------wer ist ei Student ? --------------------
Peter = mensch('Peter', 'Müller', 23)
print('Ist Peter ein Student?')
if isinstance(Peter, student):
    print('JA')
else:
    print('NEIN')

print('Ist Matthias ein Student?')
if isinstance(Matthias, student):
    print('JA')
else:
    print('NEIN')


