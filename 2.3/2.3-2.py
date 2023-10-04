s = input()
s1 = input()
s2 = input()
delta = s + s1 + s2
x = 0

while 'зайка' in delta:
    x += 1
    delta=delta.replace('зайка','',1)
print(x)