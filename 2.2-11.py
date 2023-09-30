number = int(input())

if 100 <= number <= 999:
    digit1 = number // 100  # Сотни
    digit2 = (number // 10) % 10  # Десятки
    digit3 = number % 10  # Единицы

    min_digit = min(digit1, digit2, digit3)
    max_digit = max(digit1, digit2, digit3)

    remaining_digit = digit1 + digit2 + digit3 - min_digit - max_digit

    if min_digit + max_digit == remaining_digit * 2:
        print("YES")
    else:
        print("NO")
else:
    print()
