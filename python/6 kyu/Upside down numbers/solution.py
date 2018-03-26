import math

def rotatedNumber (n):
    if n == 0 :
        return 0
    number = n
    result = 0
    options = {0: 0, 1: 1, 2: -1, 3: -1, 4: -1, 5: -1, 6: 9, 7: -1, 8: 8, 9: 6}

    while number > 0 :
        part = number % 10
        if options[part] >= 0 :
            result = result * 10 + options[part]
        else :
            return -1
        number = math.floor(number / 10)
    return result

def solve(a, b):
    result = 0
    for i in range(a,b) :
        if i == rotatedNumber(i) :
            result += 1
    return result
