directions = [  [[0,0],[1,0],[2,0],[3,0]], # v
                [[0,1],[1,1],[2,1],[3,1]], #  v
                [[0,2],[1,2],[2,2],[3,2]], #   v
                [[0,3],[1,3],[2,3],[3,3]], #    v
                [[0,3],[0,2],[0,1],[0,0]], #    <
                [[1,3],[1,2],[1,1],[1,0]], #    <
                [[2,3],[2,2],[2,1],[2,0]], #    <
                [[3,3],[3,2],[3,1],[3,0]], #    <
                [[3,3],[2,3],[1,3],[0,3]], #    ^
                [[3,2],[2,2],[1,2],[0,2]], #   ^
                [[3,1],[2,1],[1,1],[0,1]], #  ^
                [[3,0],[2,0],[1,0],[0,0]], # ^
                [[3,0],[3,1],[3,2],[3,3]], # >
                [[2,0],[2,1],[2,2],[2,3]], # >
                [[1,0],[1,1],[1,2],[1,3]], # >
                [[0,0],[0,1],[0,2],[0,3]]] # >

def checkClues(array, clues):
    for i in range (len(clues)):
        if clues[i] > 0:
            curHeight = 0
            curClue = clues[i]
            for loc in directions[i]:
                if len (array[loc[0]][loc[1]]) != 1:
                    return False
                if array[loc[0]][loc[1]] > curHeight:
                    curClue -= 1
                    curHeight = array[loc[0]][loc[1]]
            if curClue != 0:
                return False
    return True

def placeNumber(array, number, x, y):
    beforePlacing = []
    for i in range(4):
        beforePlacing.append(list(array[x][i]))
        if number in array[x][i] and i != y:
            array[x][i].remove(number)   
        beforePlacing.append(list(array[i][y]))         
        if number in array[i][y] and i != x:
            array[i][y].remove(number)
    array[x][y] = [number]
    return beforePlacing

def removeNumber(array, x, y, prevValues):
    ind = 0
    for i in range(4):
        array[x][i] = prevValues[ind]
        ind += 1
        array[i][y] = prevValues[ind]
        ind += 1

# square in 0 ... 15
def bruteForce (array, square, clues):
    loc = [int(square / 4), square % 4]
    if square == 15 :
        if len(array[loc[0]][loc[1]]) == 1 :
            if checkClues(array, clues) :
                return array
        return []
    else :
        for element in array[loc[0]][loc[1]]:
            beforePlacing = placeNumber(array, element, loc[0], loc[1])
            solutionArray = bruteForce(array, square + 1, clues)
            if len(solutionArray) > 0:
                return solutionArray
            removeNumber(array, loc[0], loc[1], beforePlacing)
        return []


def placeEasyNumber(array, lookingFor, direction, location):
    anotherDirection = -1
    if direction in range(4) or direction in range(8,12) :
        anotherDirection = len(directions) - 1 - location[0]
    else :
        anotherDirection = location[1]
    for loc in directions[anotherDirection]:
        if lookingFor in array[loc[0]][loc[1]] :
            array[loc[0]][loc[1]].remove(lookingFor)
    for j in range(1,len(directions[direction])):
        loc = directions[direction][j]
        if lookingFor in array[loc[0]][loc[1]] :
            array[loc[0]][loc[1]].remove(lookingFor)
    array[location[0]][location[1]] = [lookingFor]

def easyNumbers(array, clues):
    easyFours = map(lambda x: True if x == 4 else False, clues)
    easyOnes = map(lambda x: True if x == 1 else False, clues)
    for i in range(len(easyOnes)) :
        if easyFours[i] :
            for num,j in enumerate(directions[i]) :
                placeEasyNumber(array, num + 1, i, j)
        elif easyOnes[i] :
            placeEasyNumber(array, 4, i, directions[i][0])

def solve_puzzle (clues):
    element = []
    for i in range (4) :
        element.append(i + 1)
    result = []
    for i in range (4) :
        line = []
        for i in range (4) :
            line.append(list(element))
        result.append(list(line))
    cluesList = list(clues)

    easyNumbers(result, cluesList)

    result = bruteForce(result, 0, cluesList)
    resultTuple = ()
    for line in result:
        lineTuple = ()
        for element in line:
            lineTuple = lineTuple + (element[0],)
        resultTuple = resultTuple + (lineTuple,)

    return resultTuple

def testing(value1, value2):
    if (value1 == value2):
        print "Correct!"
    else:
        print "Nope. Expected %s, received %s" % (str(value2), str(value1))

tests = [#[ ( 2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3 ), 
        # ( ( 1, 3, 4, 2 ),       
        # ( 4, 2, 1, 3 ),       
        # ( 3, 4, 2, 1 ),
        # ( 2, 1, 3, 4 )
        # ) ],
        [ ( 0, 0, 1, 2, 0, 2, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0 ),
        ( ( 2, 1, 4, 3 ), 
        ( 3, 4, 1, 2 ), 
        ( 4, 2, 3, 1 ), 
        ( 1, 3, 2, 4 ) ) ]
        ]
  
for indx, [task, answer] in enumerate(tests):
    print ("Test #%d :" % indx)
    testing(solve_puzzle(task), answer)