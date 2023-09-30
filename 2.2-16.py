# Ввод средних скоростей трех претендентов
petia_speed = int(input())
vasia_speed = int(input())
tolya_speed = int(input())

# Создаем словарь, в котором ключи - имена претендентов, а значения - их средние скорости
speeds = {'Петя': petia_speed, 'Вася': vasia_speed, 'Толя': tolya_speed}

# Сортируем претендентов по скорости в убывающем порядке
sorted_speeds = sorted(speeds.items(), key=lambda x: x[1], reverse=True)

# Создаем пьедестал
pedestal = [' ' * 8] * 3

for i, (name, speed) in enumerate(sorted_speeds):
    # Заполняем соответствующий уровень пьедестала
    pedestal[i] = f"{name:^8}"

# Выводим пьедестал
print('\n'.join(pedestal))
