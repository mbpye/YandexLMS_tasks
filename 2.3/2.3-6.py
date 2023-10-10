def nod(x1, x2):
    buff = [1]
    if x1 % x2 == 0:
        buff.append(x2)
    elif x2 % x1 == 0:
        buff.append(x1)  
    delta = max(x1, x2)
    alpha = min(x1, x2)
    for x in range(2, delta):
        if (delta % x == 0) and (alpha % x == 0):
            buff.append(x)
    return max(buff)


s1 = int(input())
s2 = int(input())
print(nod(s1, s2))