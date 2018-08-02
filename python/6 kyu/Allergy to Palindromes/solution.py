def count_pal(n):  # amount of digits
    solution = [0, 0]
    for i in range(1,n+1):
        # value of possible unique numbers that we can have
        value = int(i / 2) if i % 2 == 0 else int(i / 2) + 1
        # calculate the number of palendrom numbers for current number of digits
        curDigits = 10 ** (value -1) * 9 # 9 because the first numbers can not be zero
        if i == n :
            solution[0] = curDigits
        solution[1] += curDigits
    return solution

def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

tests = [[ 1,  [9, 9] ],
         [ 2,  [9, 18] ],
         [ 5,  [900, 1098] ],
         [ 10, [90000, 199998] ],
         [ 70, [90000000000000000000000000000000000, 199999999999999999999999999999999998] ]
         ]
  
for indx, [task, answer] in enumerate(tests):
    print ("Test #%d :" % indx)
    testing(count_pal(task), answer)