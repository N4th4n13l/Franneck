# ZIP praktische Zusammenführung von Daten | https://www.youtube.com/watch?v=5cdQdSl41M8&list=PLt_1e8h-E5Lb3shyy92ry-HcW-kKCXMXy&index=12
# Video 12 aus der Reihe

smaller = [1, 2, 3, 6]
name = ['Jan', 'Horst', 'Gabriel', 'Python']

for val01, val02 in zip(smaller, name):
    print(val01, val02)

neue_Liste = list(zip(smaller, name))
print(neue_Liste)

for val in neue_Liste:
    print(val[0], val[1])


