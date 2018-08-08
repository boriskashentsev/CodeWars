import time

class train:
    def __init__(self, tr, trPos):
        self.onStation = 0
        self.length = len(tr)
        self.isExpress = True if tr[0]in 'Xx' else False
        self.position = trPos
        self.direction = -1 if tr[0].isupper() else 1
        self.letter = tr[0].upper()
    def __repr__(self):
        return "Train: %s Lenth: %d, Position: %d, Direction: %d" %(self.letter, self.length, self.position, self.direction)
    

dirOfMove = [   [ -1, -1,  0,  1,  1,  1,  0, -1],
                [  0, -1, -1, -1,  0,  1,  1,  1]]
            #   [  ^, <^,  <, <v,  v, v>,  >, ^>] 

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
    modTrack = map(lambda x: list(x), track)
    steps = {}
    if modTrack[len(modTrack)-1] == [] :
        modTrack.pop()
    for i in range(len(modTrack[0])):
        if modTrack[0][i] in "-|SX+/\\":
            start = [0, i]
            break
    curDir = 7 # curDirection -> range(8)
    curLoc = start
    curStep = 0
    while curLoc != start or curStep == 0 :
        for ind in [0, -1, -2, 1, 2] :
            newLoc = newLocation(curLoc, moveDirection((curDir + ind) % 8))
            if isInsideMap(curLoc, moveDirection((curDir + ind) % 8), [len(modTrack), len(modTrack[newLoc[0]]) if len(modTrack) > newLoc[0] else 0]):
                mapStatus = whatOnMap(modTrack, curLoc, moveDirection((curDir + ind) % 8))
                if type(mapStatus) == str and mapStatus in "-|SX+/\\" or type(mapStatus) == list: # There should be other statuses. Make changes
                    if type(modTrack[curLoc[0]][curLoc[1]]) == str :
                        modTrack[curLoc[0]][curLoc[1]] = [curStep]
                    elif type(modTrack[curLoc[0]][curLoc[1]]) == list :
                        modTrack[curLoc[0]][curLoc[1]].append(curStep)
                    else :
                        # print "Weird modified track status. Step:", curStep, "Location:", newLocation(curLoc, moveDirection(curDir))
                        exit()
                    steps[curStep] = curLoc
                    curDir = (curDir + ind) % 8
                    curLoc = newLocation(curLoc, moveDirection(curDir))
                    curStep += 1
                    break
                elif mapStatus == ' ':
                    pass
                else :
                    # print "Weird map status. Step:", curStep, "Location:", newLocation(curLoc, moveDirection((curDir + ind) % 8))
                    exit()
    return (steps, modTrack)

def printTrack(steps,track): # only printing
    for row in track:
        line = ''
        for element in row:
            if element == ' ':
                line += ' '
            else:
                char = ''
                for stepNum in element:
                    if steps[stepNum][1] != '':
                        if char == '':
                            char = steps[stepNum][1]
                            break
                if char == '':
                    line += '.'
                else :
                    line += char
        print line
    print ''

# testing return emptyTrak, otherwise boolean would suffice
def putTrains(steps, track, trains):
    emptyTrack = {k: [v, ''] for k,v in steps.items()}
    for ind,train in enumerate(trains):
        pos = train.position
        location = steps[pos]
        poss = track[location[0]][location[1]] # possible positions to check
        otherPos = pos if len(poss) == 1 else poss[0] if poss[0] != pos else poss[1]
        if emptyTrack[pos][1] == '' and emptyTrack[otherPos][1] == '':
            emptyTrack[pos][1] = train.letter
            for i in range(1,train.length):
                pos = (train.position - train.direction*i)%len(steps.keys())
                location = steps[pos]
                poss = track[location[0]][location[1]] # possible positions to check
                otherPos = pos if len(poss) == 1 else poss[0] if poss[0] != pos else poss[1]
                if emptyTrack[pos][1] == '' and emptyTrack[otherPos][1] =='' :
                    emptyTrack[pos][1] = train.letter.lower()
                else :
                    if ind > 0:
                        print "Trains intersected"
                    else:
                        print "Train intersected itself"
                    return {}
        else :
            print "Trains intersected"
            return {}
    return emptyTrack

def moveTrains(steps, track, trains):
    for train in trains: # moving trains here and then putting them to the track
        if train.onStation > 0:
            train.onStation -= 1
            # print "%s train on station" % (train.letter)
        else:
            train.position = (train.position + train.direction) % len(steps)
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
    while time <= limit:
        stepsWTrains = putTrains(steps, nTrack, trains)
        if len(stepsWTrains) == 0:
            return time
        if time in range(510,520): # for bigger test to check the moment of the intersection
            print "---> Time: %d <---" % (time)
            printTrack(stepsWTrains, nTrack)
        moveTrains(steps, track.split('\n'), trains)
        time += 1
    return -1 if time > limit else time



def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

TRACK_EX = """\
/---\\
|   |
|   S
|   |
\\-S-/
"""
testing(train_crash(TRACK_EX, "aaaaaA", 4, "Bbb", 11, 1000), 7)

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