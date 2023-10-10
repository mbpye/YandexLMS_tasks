n = int(input())
max_sum = 0
max_base = 0


for base in range(2, 11):
    num = n
    sum_digits = 0
    while num > 0:
        sum_digits += num % base
        num //= base
    if sum_digits > max_sum:
        max_sum = sum_digits
        max_base = base

print(max_base)