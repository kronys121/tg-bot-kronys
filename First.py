def power(number, pow):
    print('параметры', number,pow)
    power_result = number ** pow
    return power_result

list = [1, 3, 5, 6, 7]

for element in list:
    result = power(number = element, pow = 3)

    print(result)