from math import sqrt

def isPrime(n):
    for i in range (2,int(sqrt(n))+2) :
        if n % i == 0 :
            return False
    return True

def consistsOfPrimes(n):
    number = n
    result = -1
    counter = 0
    while number > 0 :
        if (number % 10) in [2,3,5,7]:
            result = counter
        number = int(number / 10)
        counter += 1
    if result >= 0 :
        return int(10**result)
    else :
        return result

def solve(n):
    result = 1
    while n > 0 :
        result += 1
        addition = consistsOfPrimes(result)
        if addition < 0:
            isPrimeBool = isPrime(result)
            if not isPrimeBool:
                n -= 1
        else :
            result += addition - 1
    return result
