def find_pattern(sequence):
    return [1]

def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

tests = [[ [1, 2, 3, 4, 5],                                         [1] ],
         [ [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1],     [1, 1, 1, 1, -1, -1, -1, -1] ],
         [ [1, 5, 2, 3, 1, 5, 2, 3, 1],                             [4, -3, 1, -2] ],
         [ [1, 5, 4, 8, 7, 11, 10, 14, 13],                         [4, -1] ],
         [ [0, 1],                                                  [1] ],
         ]
  
for pattern, answer in tests:
    testing(find_pattern(pattern), answer)