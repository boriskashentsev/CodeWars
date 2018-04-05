class Lift(object):
    direction = 0
    capacity = 0
    people = []
    floor = 0
    listOfVisitedFloors = []

    @classmethod
    def __init__(cls, capacity):
        cls.direction = 1 # "1" for up and "-1" for down. it is assigned -1 at the beginning because we treat as if Lift just arrived from the top and ready to start it's movement up
        cls.capacity = capacity
        cls.people = []
        cls.floor = 0
        cls.listOfVisitedFloors = [0]

    # function that seeks next floors that Lift needs to visit.
    @classmethod
    def FindFloorToVisit(self, queues):
        # First, check people in the lift and closest floor they need to visit
        nextFloor = 0
        if self.direction > 0 :
            nextFloor = min([x for x in self.people if x > self.floor] or [-1])
        else :
            nextFloor = max([x for x in self.people if x < self.floor] or [-1])

        # Second, check people on the floors and see if they are going the same direction
        floorsPossibleToVisit = []
        if (self.direction > 0):
            floorsPossibleToVisit = range(self.floor + 1, len(queues))
        else:
            floorsPossibleToVisit = range(self.floor - 1, -1, -1)
        for floor in floorsPossibleToVisit:
            peopleOnIthFloor = queues[floor]
            if (self.direction > 0): # lift goes up
                if (len([person for person in peopleOnIthFloor if person > floor]) > 0): # there are people going up from the current floor
                    if (nextFloor > 0):
                        nextFloor = min([nextFloor, floor])
                    else:
                        nextFloor = floor
                    break
            if (self.direction < 0): # lift goes down
                if (len([person for person in peopleOnIthFloor if person < floor]) > 0): # there are people going down from the current floor
                    nextFloor = max([nextFloor, floor])
                    break

        # Third, if at this point we didn't find next floor to check, let's see if there are people who asked for elevator to go opposite direction
        if nextFloor >=0 :
            return nextFloor
        else :
            if (self.direction > 0) :
                floorsPossibleToVisit = range(len(queues)-1, self.floor, -1)
            else :
                floorsPossibleToVisit = range(0, self.floor)
            
            for floor in floorsPossibleToVisit:
                peopleOnIthFloor = queues[floor]
                if (self.direction > 0):
                    if (len([person for person in peopleOnIthFloor if person < floor]) > 0):
                        return floor
                else:
                    if (len([person for person in peopleOnIthFloor if person > floor]) > 0):
                        return floor
        
        # And last, if we ended up here, Lif has to turn around and Go into the oposite direction
        return -1

    @classmethod
    def MoveLiftOneDirection(self, queues):
        nextFloor = self.FindFloorToVisit(queues)
        while nextFloor >=0 :
            self.MoveToTheNextNeededFloor(nextFloor, queues)
            nextFloor = self.FindFloorToVisit(queues)
        # We at the end of one way go, time to turn around and check the other direction
        self.direction = -self.direction
        # Now let's pick up people on the current floor and who is going the opposite the one we started the run with
        indexOfEnteredPeople = []
        for i,personNeedsFloor in enumerate(queues[self.floor]):
            if self.capacity > len(self.people):
                if self.direction > 0:
                    if personNeedsFloor > self.floor:
                        self.people.append(personNeedsFloor)
                        indexOfEnteredPeople.append(i)
                else:
                    if personNeedsFloor < self.floor:
                        self.people.append(personNeedsFloor)
                        indexOfEnteredPeople.append(i)
            else:
                break

        self.removeElementsFromList(queues[self.floor], indexOfEnteredPeople)

    @classmethod
    def MoveToTheNextNeededFloor(self, visitingFloor, queues):
        self.floor = visitingFloor
        if (self.listOfVisitedFloors[len(self.listOfVisitedFloors)-1] != visitingFloor):
            self.listOfVisitedFloors.append(visitingFloor)
        # First, let people exit

        indexOfLeavingPeople = [i for i,person in enumerate(self.people) if person == visitingFloor]
        self.removeElementsFromList(self.people, indexOfLeavingPeople)

        # Now, let new people enter
        indexOfEnteredPeople = []
        for i,personNeedsFloor in enumerate(queues[visitingFloor]):
            if self.capacity > len(self.people):
                if self.direction > 0:
                    if personNeedsFloor > visitingFloor:
                        self.people.append(personNeedsFloor)
                        indexOfEnteredPeople.append(i)
                else:
                    if personNeedsFloor < visitingFloor:
                        self.people.append(personNeedsFloor)
                        indexOfEnteredPeople.append(i)
            else:
                break

        self.removeElementsFromList(queues[visitingFloor], indexOfEnteredPeople)
    
    @classmethod
    def removeElementsFromList(cls, listWithElements, indices):
        indices.reverse()
        for index in indices:
            listWithElements.pop(index)

class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.lift = Lift(capacity)
        self.queues = queues
    
    def tupleToList(self, queues):
        result = []
        for element in queues:
            result.append(list(element))
        return result

    def theLift(self):
        result = [0]
        newQueues = self.tupleToList(self.queues)

        self.lift.MoveToTheNextNeededFloor(0,newQueues)
        nextFloor=self.lift.FindFloorToVisit(newQueues)
        while nextFloor != -1:
            self.lift.MoveLiftOneDirection(newQueues)
            nextFloor = self.lift.FindFloorToVisit(newQueues)
        
        result = self.lift.listOfVisitedFloors
        if (len(result) == 0):
            result.insert(0,0)
        if (result[len(result)-1] != 0):
            result.append(0)
        
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
         [ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ],
         [ ( (5,),   (),  (),      (),    (),    (),    () ),     [0, 5, 0] ],
         [ ((2,), (6,), (3, 7, 6, 8, 6), (8, 5, 8, 8), (), (8, 0), (), (), (5,)), [0, 1, 2, 3, 5, 6, 8, 5, 0, 2, 3, 5, 6, 7, 2, 3, 5, 6, 8, 3, 5, 8, 3, 8, 0] ]
         ]
  
for queues, answer in tests:
    lift = Dinglemouse(queues, 2)
    testing(lift.theLift(), answer)
    
    