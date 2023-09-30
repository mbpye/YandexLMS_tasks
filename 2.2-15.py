# Ввод защитных чисел Зерона
first_defense = input()
second_defense = input()

# Собираем список всех цифр из обоих защитных чисел
all_digits = list(map(int, first_defense + second_defense))

# Находим максимальную, минимальную и сумму оставшихся двух цифр
max_digit = max(all_digits)
min_digit = min(all_digits)
remaining_sum = sum(all_digits) - max_digit - min_digit

# Собираем трехзначное магическое число
magic_number = str(max_digit) + str(remaining_sum % 10) + str(min_digit)

# Выводим магическое число
print(magic_number)
