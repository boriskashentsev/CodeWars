def differences(array):
    result = []
    for i in range(1,len(array)):
        result.append(array[i]-array[i-1])
    return result

def find_pattern(sequence):
    diffs = differences(sequence)
    for length in range(1,len(diffs)):
        if (len(diffs) % length == 0):
            nOfParts = int(len(diffs) / length)
            flag = True
            for i in range(1, nOfParts):
                if diffs[0:length] != diffs[length*i:length*(i+1)]:
                    flag = False
                    break
            if flag:
                return diffs[0:length]
    return diffs

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