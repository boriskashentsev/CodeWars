class Calculator():
    def simpleCalculation(self, left, right, sign):
        result = 0
        if sign == '+':
            result = left + right
        elif sign == '-':
            result = left - right
        elif sign == '*':
            result = left * right
        elif sign == '/':
            result = left / right 
        else :
            print "What were you expecting here?"
        return result
        
    def evaluate(self, string):
        signsOrder = {"-": 0, "+": 0, "*": 1, "/": 1}
        sep = string.split() # string separated 
        print sep
        ind = 0
        diff = []
        signs = [] # stack of signs
        # convert to different array style in case there will be more operations and brackets in the future
        while ind < len(sep): 
            if sep[ind].replace('.','',1).isdigit() :
                diff.append(float(sep[ind]))
            else:
                if (len(signs) > 0):
                    prSign = signs.pop()
                    if (signsOrder[prSign] < signsOrder[sep[ind]]):
                        signs.append(prSign)
                        signs.append(sep[ind])
                    else :
                        while (signsOrder[prSign] >= signsOrder[sep[ind]]) :
                            diff.append(prSign)
                            if len(signs) > 0 : 
                                prSign = signs.pop()
                            else:
                                break
                        if (signsOrder[prSign] < signsOrder[sep[ind]]):
                            signs.append(prSign)
                        signs.append(sep[ind])
                else : 
                    signs.append(sep[ind])
            ind += 1
        while (len(signs) > 0):
            diff.append(signs.pop())

        solution = []
        i = 0
        while i < len(diff) :
            if (diff[i] not in signsOrder.keys()):
               solution.append(diff[i])
            else:
                right = solution.pop()
                left = solution.pop()
                solution.append(self.simpleCalculation(left, right, diff[i]))
            i += 1 
        
        return int(solution[0]) if int(solution[0]) == solution[0] else solution[0]

def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

tests = [[ "2 / 2 + 3 * 4 * 1", 13 ],
         [ "2 / 2 + 3 * 4 - 6", 7 ],
         [ "3 + 4",             7 ],
         ]
  
for indx, [task, answer] in enumerate(tests):
    print ("Test #%d :" % indx)
    testing(Calculator().evaluate(task), answer)

    map(lambda x: float(x) if x.replace('.','',1).isdigit() else x , "12.243 342 + 4234 / 34.43".split())