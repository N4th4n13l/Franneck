# while Schleiffen | https://www.youtube.com/watch?v=5cdQdSl41M8&list=PLt_1e8h-E5Lb3shyy92ry-HcW-kKCXMXy&index=12
# while bis break ********************
zahl = 0.0
ergebnis = 25
weiterspielen = True
zufallszahl = 14

while weiterspielen:  # Etwas so lange machen bis anderer Befehl
    zahl = int(input('Gib eine Zahl ein!\n'))

    if zahl < 10:
        print('Fall 01')
    elif zahl >= 10 and zahl < 20:
        print('Fall 02')

    else:
        print('Fall 03')

    weiterspielen = int(input('Weiterspielen? (0 oder 1 ein)!\n'))  # gleich True or False

    if zahl < 10:
        print('Fall 01')
    elif zahl >= 10 and zahl < 20:
        if zahl == zufallszahl:
            print('Ende und out')      # oder durch ein Ereigniss
            break                      # bricht while Schleiffe ab wenn etwas bestimmtes eintrifft

    else:
        print('Fall 03')
    weiterspielen = int(input('Weiterspielen? (0 oder 1 ein)!\n'))  # gleich True or False

    # ----------------------------------------------------------------------------

    # while Loops
    count = 0
    while count < 10:
        print('Etwas ist wahr')
        count = count + 1
    print('After the loop')
    # -------------------------------------------------------------------------------