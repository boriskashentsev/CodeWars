class Lift(object):
    def __init__(self, capacity):
        self.direction = -1 # "1" for up and "-1" for down. it is assigned -1 at the beginning because we treat as if Lift just arrived from the top and ready to start it's movement up
        self.capacity = capacity
        self.people = []
        self.floor = 0
        self.destination = -1
        self.floorsToVisit = []

    # function that seeks floors that Lift needs to visit.
    # we assume that function is called right before Lift is switching its direction
    def findFloorsToVisit(self, queues):
        self.direction = -self.direction
        self.floorsToVisit = self.people
        floorsPossibleToVisit = []
        if (self.direction > 0):
            floorsPossibleToVisit = range(self.floor, len(queues))
        else:
            floorsPossibleToVisit = range(self.floor, -1, -1)
        for floor in floorsPossibleToVisit:
            peopleOnIthFloor = queues[floor]
            if (self.direction > 0): # lift goes up
                if (len([person for person in peopleOnIthFloor if person > floor]) > 0): # there are people going up from the current floor
                    self.floorsToVisit.append(floor)
            if (self.direction < 0): # lift goes down
                if (len([person for person in peopleOnIthFloor if person < floor]) > 0): # there are people going down from the current floor
                    self.floorsToVisit.append(floor)
        self.floorsToVisit = list(set(self.floorsToVisit))
        self.floorsToVisit.sort()
        if (self.direction < 0):
            self.floorsToVisit.reverse()

        # At this point we have a list of floors that asked for the lift that are going in the same direction as the lift.
        # we are missing floors that are past the maximum (minimum when going down) floor, that are going the opposite direction.
        if (self.direction > 0) :
            floorsPossibleToVisit = range(len(queues)-1, self.floor,-1)
        else :
            floorsPossibleToVisit = range(0,self.floor)
        
        for floor in floorsPossibleToVisit:
            peopleOnIthFloor = queues[floor]
            if (self.direction > 0):
                if (len([person for person in peopleOnIthFloor if person < floor]) > 0):
                    self.floorsToVisit.append (floor)
                    break
            else:
                if (len([person for person in peopleOnIthFloor if person > floor]) > 0):
                    self.floorsToVisit.append (floor)
                    break

        print(self.floorsToVisit)


        

class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.lift = Lift(capacity)
        self.queues = queues
        
    def theLift(self):
        result = [0]
        self.lift.findFloorsToVisit(queues)
        return result

def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

# Floors:    G     1      2        3     4      5      6         Answers:
tests = [[ ( (),   (),    (5,5,5), (),   (),    (),    () ),     [0, 2, 5, 0]          ],
         [ ( (),   (),    (1,1),   (),   (),    (),    () ),     [0, 2, 1, 0]          ],
         [ ( (),   (3,),  (4,),    (),   (5,),  (),    () ),     [0, 1, 2, 3, 4, 5, 0] ],
         [ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ]]
  
for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    testing(lift.theLift(), answer)
    
    