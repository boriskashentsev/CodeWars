import time

class train:
    def __init__(self, tr, trPos):
        self.onStation = 0
        self.length = len(tr)
        self.isExpress = True if tr[0]in 'Xx' else False
        self.position = trPos
        self.direction = -1 if tr[0].isupper() else 1
        self.letter = tr[0].upper()
        self.moved = False
    def __repr__(self):
        return "Train: %s Lenth: %d, Position: %d, Direction: %d" %(self.letter, self.length, self.position, self.direction)
    

dirOfMove = [   [ -1 ,  -1 ,  0 ,  1 ,  1 ,   1 ,  0 , -1],
                [  0 ,  -1 , -1 , -1 ,  0 ,   1 ,  1 ,  1],
                [ '|', '\\', '-', '/', '|', '\\', '-', '/']]
            #   [  ^ ,  <^ ,  < , <v ,  v ,  v> ,  > , ^>]

possibleMoves= {
    '-': [0],
    '|': [0],
    'S': [0],
    'X': [0],
    '+': [0],
    '/': [0, -1, 1],
    '\\':[0, -1, 1]
}

def moveDirection(ind) :
    return [dirOfMove[0][ind], dirOfMove[1][ind]]

def isInsideMap(curLoc, move, size):
    if curLoc[0] + move[0] >= 0 and curLoc[0] + move[0] < size[0] :
        if curLoc[1] + move[1] >= 0 and curLoc[1] + move[1] < size[1] :
            return True
    return False

def newLocation(curLoc, move) :
    return [curLoc[0] + move[0], curLoc[1] + move[1]]

def whatOnMap(track, curLoc, move) :
    return track[curLoc[0] + move[0]][curLoc[1] + move[1]]

def trackToSteps(track):
    modTrack = list(map(lambda x: list(x), track))
    steps = []
    if modTrack[len(modTrack)-1] == [] : # Making sure that there is no empty string in the end of the track
        modTrack.pop()
    for i in range(len(modTrack[0])):
        if modTrack[0][i] in "-|SX+/\\":
            start = [0, i]
            break
    curDir = 7 # curDirection -> range(8)
    curLoc = start
    curStatus = modTrack[start[0]][start[1]]
    trueCurStatus = track[start[0]][start[1]]
    curStep = 0
    while curLoc != start or curStep == 0 :
        for ind in possibleMoves[trueCurStatus] :
            newLoc = newLocation(curLoc, moveDirection((curDir + ind) % 8))
            if isInsideMap(curLoc, moveDirection((curDir + ind) % 8), [len(modTrack), len(modTrack[newLoc[0]]) if len(modTrack) > newLoc[0] else 0]):
                mapStatus = whatOnMap(modTrack, curLoc, moveDirection((curDir + ind) % 8))
                trueMapStatus = whatOnMap(track, curLoc, moveDirection((curDir + ind) % 8))
                expectedStatus = dirOfMove[2][(curDir + ind) %8] + '+'
                if trueCurStatus in '/\\' and not ((trueMapStatus in expectedStatus and ind != 0) or (trueMapStatus in '\\/XS' and ind == 0)):
                        pass
                elif type(mapStatus) == str and mapStatus in "-|SX+/\\" or type(mapStatus) == list: # There should be other statuses. Make changes
                    if type(modTrack[curLoc[0]][curLoc[1]]) == str :
                        modTrack[curLoc[0]][curLoc[1]] = [curStep]
                    elif type(modTrack[curLoc[0]][curLoc[1]]) == list :
                        modTrack[curLoc[0]][curLoc[1]].append(curStep)
                    else : # error on the map
                        pass
                    steps.append(curLoc)
                    curLoc = newLocation(curLoc, moveDirection((curDir + ind) % 8))
                    if trueMapStatus in '/\\' and trueCurStatus not in '/\\':
                        for i in [-1, 1]:
                            if dirOfMove[2][(curDir + i) % 8] == mapStatus:
                                curDir = (curDir + i) % 8
                                break
                    else :
                        curDir = (curDir + ind) % 8
                    curStep += 1
                    curStatus = mapStatus
                    trueCurStatus = track[curLoc[0]][curLoc[1]]
                    break
                elif mapStatus == ' ':
                    pass
                else : # error on the map
                    pass
    return (steps, modTrack)

# testing return emptyTrak, otherwise boolean would suffice
def putTrains(steps, track, trains):
    emptyTrack = list(map(lambda x: [x, ''], steps))
    for train in trains:
        pos = train.position
        location = steps[pos]
        poss = track[location[0]][location[1]] # possible positions to check
        otherPos = pos if len(poss) == 1 else poss[0] if poss[0] != pos else poss[1]
        if emptyTrack[pos][1] == '' and emptyTrack[otherPos][1] == '':
            emptyTrack[pos][1] = train.letter
            for i in range(1,train.length):
                pos = (train.position - train.direction*i)%len(steps)
                location = steps[pos]
                poss = track[location[0]][location[1]] # possible positions to check
                otherPos = pos if len(poss) == 1 else poss[0] if poss[0] != pos else poss[1]
                if emptyTrack[pos][1] == '' and emptyTrack[otherPos][1] =='' :
                    emptyTrack[pos][1] = train.letter.lower()
                else :
                    return []
        else :
            return []
    return emptyTrack

# Similar to putTrain but we manipulate only two elements
def moveTrainsOnTracks(steps, track, trains):
    newSteps = steps[:]
    for train in trains:
        if train.moved:
            newSteps[(train.position - train.direction * (train.length))%len(steps)][1] = ''
    for train in trains:
        if train.moved:
            pos = train.position
            location = steps[pos][0]
            poss = track[location[0]][location[1]] # possible positions to check
            otherPos = pos if len(poss) == 1 else poss[0] if poss[0] != pos else poss[1]
            if newSteps[pos][1] == '' and newSteps[otherPos][1] == '' :
                newSteps[(pos - train.direction)%len(steps)][1] = train.letter.lower()
                newSteps[pos][1] = train.letter
            else :
                return []
    return newSteps

def moveTrains(steps, track, trains):
    for train in trains: # moving trains here and then putting them to the track
        if train.onStation > 0:
            train.onStation -= 1
            train.moved = False
        else:
            train.position = (train.position + train.direction) % len(steps)
            train.moved = True
            if not train.isExpress :
                loc = steps[train.position]
                if track[loc[0]][loc[1]] == 'S':
                    train.onStation = train.length-1


def train_crash(track, a, aPos, b, bPos, limit):
    (steps, nTrack)=trackToSteps(track.split('\n')) 
    trains = []
    trains.append(train(a, aPos))
    trains.append(train(b, bPos))
    time = 0
    stepsWTrains = putTrains(steps, nTrack, trains)
    if len(stepsWTrains) == 0:
        return time
    while time <= limit:
        if time > 0:
            stepsWTrains = moveTrainsOnTracks(stepsWTrains, nTrack, trains)
        if len(stepsWTrains) == 0:
            return time
        #printTrack(stepsWTrains, nTrack)
        moveTrains(steps, track.split('\n'), trains)
        time += 1
    return -1



def testing(value1, value2):
    if (value1 == value2):
        print "Correct!"
    else:
        print "Nope. Expected %s, received %s" % (str(value2), str(value1))

TRACK_EX = """\
/---\\
|   |
|   S
|   |
\\-S-/
"""
testing(train_crash(TRACK_EX, "aaaaaA", 4, "Bbb", 11, 100), 7)

TRACK_EX = """\
   /---\\
   |   |
   |   |
/--//--/
|   |
|   |
\\---/
"""
testing(train_crash(TRACK_EX, "aaaA", 4, "bbB", 17, 100), -1)

TRACK_EX = """\
/-------\\ 
|       | 
S       | 
|       | 
\\-------+--------\\
        |        |
        S        |
        |        |
        \\--------/
# """
testing(train_crash(TRACK_EX, "Aaaaaaa", 14, "Xxxxxxxxxx", 3, 2000), 65)

TRACK_EX = """\
                                /------------\\
/-------------\\                /             |
|             |               /              S
|             |              /               |
|        /----+--------------+------\\        |   
\\       /     |              |      |        |     
 \\      |     \\              |      |        |                    
 |      |      \\-------------+------+--------+---\\
 |      |                    |      |        |   |
 \\------+--------------------+------/        /   |
        |                    |              /    | 
        \\------S-------------+-------------/     |
                             |                   |
/-------------\\              |                   |
|             |              |             /-----+----\\
|             |              |             |     |     \\
\\-------------+--------------+-----S-------+-----/      \\
              |              |             |             \\
              |              |             |             |
              |              \\-------------+-------------/
              |                            |               
              \\----------------------------/ 
"""

t0 = time.time()
testing(train_crash(TRACK_EX, "Aaaa", 147, "Bbbbbbbbbbb", 288, 1000), 516)
t1 = time.time()

print t1-t0