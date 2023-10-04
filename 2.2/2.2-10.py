number = int(input())

if 100 <= number <= 999:
    digit1 = number // 100  
    digit2 = (number // 10) % 10  
    digit3 = number % 10  

    sum1 = digit1 + digit2
    sum2 = digit2 + digit3

    if sum1 >= sum2:
        encrypted_number = str(sum1) + str(sum2)
    else:
        encrypted_number = str(sum2) + str(sum1)

    print( encrypted_number)
