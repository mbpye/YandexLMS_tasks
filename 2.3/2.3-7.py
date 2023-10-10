def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

number1 = int(input())
number2 = int(input())

gcd_result = gcd(number1, number2)

lcm_result = (number1 * number2) // gcd_result

print(lcm_result)