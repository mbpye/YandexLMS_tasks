# Ввод данных
Weight, cost, costT, costT1 = int(input()), int(input()), int(input()), int(input())

weight1 = int((cost - costT1) * Weight / (costT - costT1))
weight2 = Weight - weight1

print(weight1, weight2)

