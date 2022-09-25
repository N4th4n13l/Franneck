# For Schleiffen | https://www.youtube.com/watch?v=5cdQdSl41M8&list=PLt_1e8h-E5Lb3shyy92ry-HcW-kKCXMXy&index=12

# für jeden Durchgang bekommt die Variable einen neuen Wert
# 0,1,2,3,4,5 etc.

for _ in range(2): # anstelle einer Variable kann auch ein _ gemacht werden !!!!!
    zahl = int(input('Gib eine Zahl ein!\n'))

    if zahl < 10:
        print('Fall 01')
    elif zahl >= 10 and zahl < 20:
        print('Fall 02')

    else:
        print('Fall 03')
# oder ich kann for auch nutze um aus Listen zu lesen - also hier um 3 Items zu counten
# for in und :  - das ist alles, was es braucht, um diverse Sachen zu machen !!!!!!!!!!!!!!!!!!!!!!
einkaufs_liste = ['Apfel', 'Orange', 'Birne']
for item in einkaufs_liste:
    print(item)

