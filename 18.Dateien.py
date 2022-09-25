# Dateien | lesen und schreiben

text = 'Ich gehe nach Hause'
text2 = 'Ich gehe erst morgen nach Hause'
data = [1, 2, 3, 4, 5]

# w = schreiben, r = lesen, a = append

with open('geschichte.txt', 'w') as f:
    f.write(text + '\n')
    f.write(text2 + '\n')

text_neu = ""

with open('geschichte.txt', 'r') as f:
    for line in f:
        print(line)
# -------------------------------------
with open('geschichte.txt', 'r') as f:
    text_neu += f.readline()
    text_neu += f.readline()
print(text_neu)
# -------------------------------------
with open('data.txt', 'a') as f:
    for val in data:
        f.write(str(val))
        print(val)
