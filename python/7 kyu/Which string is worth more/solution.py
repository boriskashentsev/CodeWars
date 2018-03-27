def highest_value(a, b):
    # Write your solution
    sum1 = 0
    sum2 = 0
    for letter in a:
        sum1 += ord(letter)
    for letter in b:
        sum2 += ord(letter)
    if sum1 >= sum2 :
        return a
    else :
        return b
