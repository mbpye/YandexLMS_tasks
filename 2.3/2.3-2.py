x = 0
while (t := input()) != 'Приехали!':
    while 'зайка' in t:
        x += 1
        t = t.replace('зайка', '', 1)
print(x)