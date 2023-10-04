number = list(map(int, input()))

max_num = max(number)
max_num_index = number.index(max_num)

number.pop(max_num_index)

se_max = max(number)

number.sort()

min_num = number[0]

if 0 in number:
    if number.count(0) == 1:
        min_non_zero = min([x for x in number if x != 0])
        first = str(min_non_zero) + '0'
    else:
        first = str(se_max) + '0'
else:
    first = str(min_num) + str(number[1])

second = str(max_num) + str(se_max)
print(first, second)

