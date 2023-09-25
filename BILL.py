def main():
    name = input()
    cost = int(input())
    ves = int(input())
    money = int(input())
    itg = ves * cost
    bill(name, cost, ves, money, itg)

    
def bill(name, cost, ves, money, itg):

    nthg = ' '

    tt = '                           '
    tsp = len(tt) - len(name) + 2

    cs = '                              '
    csp = len(cs) - (len(str(cost)) + len(str(ves)) + len('кг * руб/кг') + 0)

    inp = '                          '
    inpp = len(inp) - ((len(str(money)) + 2))

    itgs = '                     '
    itgsp = len(itgs) - (len(str(itg)) - 5)

    mbck = '                             '
    mbcks = len(mbck) - (len(str(money - itg)) + 3)
    
    print('================Чек================')
    print(f'Товар:{nthg * tsp}{name}')
    print(f'Цена:{nthg * csp}{ves}кг * {cost}руб/кг')
    print(f'Итого:{nthg * itgsp}{itg}руб')
    print(f'Внесено:{nthg * inpp}{money}руб')
    print(f'Сдача:{nthg * mbcks}{money - itg}руб')
    print('===================================')

    
if __name__ == main():
    main()