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
