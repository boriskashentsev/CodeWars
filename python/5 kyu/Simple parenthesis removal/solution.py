def signCombination(arrayOfSigns, curSign):
    if reduce (lambda x, y: x == y, arrayOfSigns, curSign) :
        return '+'
    return '-'

def solve(s):
    result = []
    indx = 0
    signStack = [] # true for + and false for -. That way is easier to count the sign combination
    curSign = True
    arr = list(s)
    while indx < len(arr) :
        if arr[indx] in ['-', '+'] :
            curSign = True if arr[indx] == '+' else False
        elif arr[indx] == ')' :
            signStack.pop()
            curSign = True
        elif arr[indx] == '(' :
            signStack.append(curSign)
            curSign = True
        else :
            sign = signCombination(signStack, curSign)
            if len(result) > 0 or len(result) == 0 and sign == '-':
                result.append(sign)
            result.append(arr[indx])
        indx += 1
    return reduce(lambda x, y: x+y, result, '')

def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

tests = [[ "a-(b)",                                         "a-b" ],
         [ "a-(-b)",     "a+b" ]
         ]
  
for indx, [task, answer] in enumerate(tests):
    print ("Test #%d :" % indx)
    testing(solve(task), answer)