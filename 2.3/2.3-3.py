start = int(input())
end = int(input())

buff = [start]

while start != end:
    if start < end:
        start += 1
        buff.append(start)
    elif start > end:
        start -= 1
        buff.append(start)

s = ''

for x in range(len(buff)):
    s += str(buff[x]) + ' ' 

print(s)