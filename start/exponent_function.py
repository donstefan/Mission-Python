def raise_to_power(number, power_number):
    result = 1
    for index in range(power_number):
        result = result * number
    return result

print(raise_to_power(3, 3))