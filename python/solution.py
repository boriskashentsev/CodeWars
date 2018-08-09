def find_pattern(sequence):
    return [1]

def testing(value1, value2):
    if (value1 == value2):
        print "Correct!"
    else:
        print "Nope. Expected %s, received %s" % (str(value2), str(value1))

tests = [[ [1, 2, 3, 4, 5],                                         [1] ],
         [ [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],     [1, 1, 1, 1, -1, -1, -1, -1] ],
         [ [1, 5, 2, 3, 1, 5, 2, 3, 1],                             [4, -3, 1, -2] ],
         [ [1, 5, 4, 8, 7, 11, 10, 14, 13],                         [4, -1] ],
         [ [0, 1],                                                  [1] ],
         ]
  
for indx, [task, answer] in enumerate(tests):
    print ("Test #%d :" % indx)
    testing(find_pattern(task), answer)