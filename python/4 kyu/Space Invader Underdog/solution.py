def newLocation (position, moves, width):
    endLoc = position + moves
    di, dj = 0, 0
    while (endLoc < 0) or (endLoc >= width):
        if endLoc < 0:
            di += 1
            endLoc = - endLoc - 1
        else: #endLoc > width
            di += 1
            endLoc = (width - 1) - (endLoc - width)
    dj = endLoc - position
    return [di, dj]

def oneStepAtATime(aliens, height):
    newStep = list(map(lambda x: list(map(lambda y: [], x)), aliens))
    shipsFlag = False
    for i in range (len(aliens)):
        for j in range(len(aliens[0])):
            for alien in aliens[i][j]:
                [di, dj] = newLocation(j, alien, len(aliens[0]))
                if i + di >= height:
                    return False # Game Lost
                else:
                    shipsFlag = True
                    newStep[i + di][j + dj].append(alien*((-1)**(di)))
    if shipsFlag :
        return newStep
    else :
        return True # Game won

def tryToShoot(aliens, shipLocation):
    for i in reversed(range(len(aliens))):
        if aliens[i][shipLocation] != []:
            return i
    return -1

def killAlien(aliens):
    if len(aliens) == 1:
        return []
    aliens = sorted(aliens)
    if abs(aliens[0])  > abs(aliens[-1]):
        return aliens[1:len(aliens)]
    else:
        return aliens[0:len(aliens)-1]

def blast_sequence(aliens,position):
    result = []
    newAliens = list(map(lambda x: list(map(lambda y: [y] if y != 0 else [], x)), aliens))
    emptyLines = position[0]-len(aliens)
    if emptyLines > 0:
        for i in range(emptyLines):
            line = []
            for j in range(len(aliens[0])):
                line.append([])
            newAliens.append(line)
    
    timer = 0
    while True:
        newAliens = oneStepAtATime(newAliens, position[0])
        if newAliens == False:
            return None
        elif newAliens == True:
            return result
        else:
            resultOfShot = tryToShoot(newAliens, position[1])
            if resultOfShot >= 0:
                result.append(timer)
                newAliens[resultOfShot][position[1]] = killAlien(newAliens[resultOfShot][position[1]])
        timer += 1
    return [1]

def testing(value1, value2):
    if (value1 == value2):
        print "Correct!"
    else:
        print "Nope. Expected %s, received %s" % (str(value2), str(value1))

example_aliens = [
	[[3,1,2,-2,2,3,6,-3,7,1]],
	[[5,2,-2,3,1,0,4,8,3,-2,5],[1,4,-1,0,3,6,1,-3,1,2,-4]],
	[[4,1,-7,-5,1,6,3,-2,1,0,2,6,5],[2,0,3,-4,0,2,-1,5,-8,-3,-2,-5,1],[1,2,0,-6,4,7,-2,4,-4,2,-5,0,4]]
    ]
example_positions = [
    [6,4],
    [10,2],
    [15,6]
    ]
example_solutions = [
	[0,2,3,4,5,9,10,13,19,22],
	[1,4,5,6,8,9,10,12,14,15,16,18,19,20,21,26,27,30,32,36],
	[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,17,18,19,21,22,23,25,27,30,31,32,35,36,38,40,43,45,56,58]
    ]

for aliens,pos,sol in zip(example_aliens,example_positions,example_solutions):
	testing(blast_sequence(aliens,pos),sol)