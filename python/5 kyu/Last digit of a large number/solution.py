digitsRepetition = {0:[0],
                    1:[1],
                    2:[2,4,8,6],
                    3:[3,9,7,1],
                    4:[4,6],
                    5:[5],
                    6:[6],
                    7:[7,9,3,1],
                    8:[8,4,2,6],
                    9:[9,1]}

def last_digit(n1, n2):
    if (n2 == 0):
        return 1
    n1LastDigit = n1 % 10 # We are interested only in the last digit
    indexInTheCycle = n2 % len(digitsRepetition[n1LastDigit])
    return (digitsRepetition[n1LastDigit][indexInTheCycle-1])

def testing(value1, value2):
    if (value1 == value2) :
        print("You are wizard Harry!")
    else :
        print("50 points goes to Slytherin")

n1 = 4
n2 = 1 
result = last_digit(n1, n2)
testing (result, 4)

n1 = 4
n2 = 2 
result = last_digit(n1, n2)
testing (result, 6)

n1 = 9
n2 = 7 
result = last_digit(n1, n2)
testing (result, 9)

n1 = 10
n2 = 10**10 
result = last_digit(n1, n2)
testing (result, 0)

n1 = 2**200
n2 = 2**300 
result = last_digit(n1, n2)
testing (result, 6)

n1 = 3715290469715693021198967285016729344580685479654510946723
n2 = 68819615221552997273737174557165657483427362207517952651 
result = last_digit(n1, n2)
testing (result, 7)

