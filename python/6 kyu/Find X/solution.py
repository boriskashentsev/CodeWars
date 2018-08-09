def find_x(n):
    return (3*n-2)*n*n

def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

tests = [[ 1,                                         1 ],
         [ 2,     16 ],
         [ 3,                             63 ]
         ]
  
for indx, [task, answer] in enumerate(tests):
    print ("Test #%d :" % indx)
    testing(find_x(task), answer)