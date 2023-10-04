places = [input() for _ in range(3)]
places.sort()
found = False

for place in places:
    if 'зайка' in place:
        print(place, len(place))
        found = True
        break

if not found:
    print("Зайка не найдена")
