dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dd = ['v','<','^','>']


def findInitialLocation(maze):
    for indx, row in enumerate(maze):
        if (">" in row) or ("<" in row) or ("v" in row) or ("^" in row) :
            return [indx, -1*row.find(">")*row.find("<")*row.find("v")*row.find("^")]

def findNextMoves(stepMaze, directionMaze, locations):
    loc2Check = []
    for location in locations:
        direction = directionMaze[location[0]][location[1]]
        step = stepMaze[location[0]][location[1]]
        for i in range(4):
            nLoc = [location[0]+dy[i], location[1]+dx[i]] # newLocation
            status = stepMaze[nLoc[0]][nLoc[1]]
            ## 2CHECK: if value can be small
            if status == ' ' :
                steps = 2  # number of steps in takes to get to the new location and turn the correct way
                if direction == dd[i] :
                    steps = 1 # direction is equal to the 
                stepMaze[nLoc[0]][nLoc[1]] = step+steps
                directionMaze[nLoc[0]][nLoc[1]] = dd[i]
                loc2Check.append(nLoc) # list of new locations where we can get
    return loc2Check


def mazeToStepMaze(maze, location):
    newMaze = list(map(lambda x: list(x), maze))
    newMaze[location[0]][location[1]] = 0
    return newMaze

def isOnTheEdge(locations,stepMaze):
    edgeLocation = []
    rows = len(stepMaze)
    cols = len(stepMaze[0])
    minSteps = -1
    for location in locations:
        if (location[0] == 0 or location[0] == rows-1) or (location[1] == 0 or location[1] == cols-1) : # on edge
            # print "whoop", location
            if (minSteps < 0) or (minSteps > stepMaze[location[0]][location[1]]) :
                edgeLocation = location
                minSteps = stepMaze[location[0]][location[1]]
    return edgeLocation

def traceBack(stepMaze, directionMaze, location):
    steps = []
    while stepMaze[location[0]][location[1]] != 0 :
        status = stepMaze[location[0]][location[1]]
        for i in range(4):
            nLoc = [location[0]+dy[i], location[1]+dx[i]] # newLocation
            if nLoc[0] in range(len(stepMaze)) and nLoc[1] in range(len(stepMaze[0])):
                nStatus = stepMaze[nLoc[0]][nLoc[1]]
                if type(nStatus)is int and status - nStatus in [1,2] :
                    steps.append('F')
                    if status - nStatus == 2:
                        direction = directionMaze[location[0]][location[1]]
                        directionIndex = dd.index(direction)
                        nDirection = directionMaze[nLoc[0]][nLoc[1]]
                        nDirectionIndex = dd.index(nDirection)
                        diff = nDirectionIndex - directionIndex + 4 if nDirectionIndex - directionIndex not in [0, 1, 2, 3] else nDirectionIndex - directionIndex
                        if diff == 3 :
                            steps.append('R')
                        elif diff == 1 :
                            steps.append('L')
                        elif diff == 2 :
                            steps.append('B')
                    location = nLoc
                    break
    return steps[::-1]

def escape(maze):
    locations = [findInitialLocation(maze)] #initial location should be wrapped in array
    stepMaze = mazeToStepMaze(maze, locations[0])
    directionMaze = list(map(lambda x: list(x), maze))
    solution = []
    while locations != []:
        locations = findNextMoves(stepMaze, directionMaze, locations)
        if locations != [] :
            locOfEdge = isOnTheEdge(locations, stepMaze)
            if locOfEdge != [] :
                solution = traceBack(stepMaze, directionMaze, locOfEdge)
                locations = []
        else :
            return []
    return solution

def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

tests = [[ [
  '# #',
  ' > ',
  '# #'
],                                         ['F'] ],
         [ [
  '###########',
  '#>       ##',
  '####### ###'
],     ['F', 'F', 'F', 'F', 'F', 'F', 'R', 'F'] ],
[[
  '##########',
  '#        #',
  '#  ##### #',
  '#  #   # #',
  '#  #^# # #',
  '#  ### # #',
  '#      # #',
  '######## #'
],      ['F', 'R', 'F', 'F', 'R', 'F', 'F', 'F', 'R', 'F', 'F', 'F', 'F', 'R', 'F', 'F', 'F', 'F', 'F', 'R', 'F', 'F', 'F', 'F', 'F', 'F', 'R','F', 'F', 'F', 'F', 'F', 'F']]
         ]


for indx, [pattern, answer] in enumerate(tests):
    print ("Test #%d :" % indx)
    testing(escape(pattern), answer)