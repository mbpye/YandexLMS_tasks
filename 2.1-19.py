product_name = input()
product_price = int(input())
product_weight = int(input())
amount_paid = int(input())

total_cost = product_price * product_weight

change = amount_paid - total_cost

dop_str = str(product_weight) + 'кг * ' + str(product_price) + 'руб/кг'

print("================Чек================")
print(f"Товар: {product_name:>28}")
print(f"Цена: {dop_str:>29}")
print(f"Итого: {(total_cost):>25}руб")
print(f"Внесено: {(amount_paid):>23}руб")
print(f"Сдача: {(change):>25}руб")
print("===================================")
