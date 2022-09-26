# Objekte |
# Was sind Objekte und was bedeutet das?
# items ist ein Objekt und kann mit items. (siehe Liste die erscheint) vervollständigt werden
items = [1, 2]
items.append(3)
items.pop(-1)
print(id(items)) # wo ist das Object gespeichert?

# --------------------------------------------------
# das ist auch ein Objekt

class Dog:
    def bark(self): # in einer Klasse definieren wir eine Funktion mit self - Objektorientierte Programmierung
        print('wuff wuff')


roger = Dog()
print(type(roger)) # = <class '__main__.Dog'> roger bezieht sich auf die Klasse Dog

# ------------------ mit inet Constructor -----------------------------
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print('Woof')


roger = Dog('Roger', 8)
print(roger.name)
print(roger.age)
(roger.bark())  # wir geben nur die Funktion aus - print ist ja schon in der Funkion bark entalten

# ----------------------------------------- JETZT KOMMT ES ------------------------------------

class Animal:
    def walk(self):
        print('Walking')

class Dog(Animal):   # !!!! @@ Wenn wir uns hier auf die Klasse Animal beziehen
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print('Woof')


roger = Dog('Roger', 8)
print(roger.name)
print(roger.age)
roger.bark()  # wir geben nur die Funktion aus - print ist ja schon in der Funktion bark oben enthalten
roger.walk() # @@ Können wir uns hier auch auf die Klasse Animal beziehen