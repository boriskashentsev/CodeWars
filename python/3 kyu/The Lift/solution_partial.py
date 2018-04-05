class Lift(object):
    direction = 0
    capacity = 0
    people = []
    floor = 0
    floorsToVisit = []
    listOfVisitedFloors = []

    @classmethod
    def __init__(cls, capacity):
        cls.direction = -1 # "1" for up and "-1" for down. it is assigned -1 at the beginning because we treat as if Lift just arrived from the top and ready to start it's movement up
        cls.capacity = capacity
        cls.people = []
        cls.floor = 0
        cls.floorsToVisit = []
        cls.listOfVisitedFloors = [0]

    # function that seeks floors that Lift needs to visit.
    # we assume that function is called right before Lift is switching its direction
    @classmethod
    def FindFloorsToVisit(cls, queues):
        cls.direction = -cls.direction
        cls.floorsToVisit = list(cls.people)
        floorsPossibleToVisit = []
        if (cls.direction > 0):
            floorsPossibleToVisit = range(cls.floor, len(queues))
        else:
            floorsPossibleToVisit = range(cls.floor, -1, -1)
        for floor in floorsPossibleToVisit:
            peopleOnIthFloor = queues[floor]
            if (cls.direction > 0): # lift goes up
                if (len([person for person in peopleOnIthFloor if person > floor]) > 0): # there are people going up from the current floor
                    cls.floorsToVisit.append(floor)
            if (cls.direction < 0): # lift goes down
                if (len([person for person in peopleOnIthFloor if person < floor]) > 0): # there are people going down from the current floor
                    cls.floorsToVisit.append(floor)
        cls.floorsToVisit = list(set(cls.floorsToVisit))
        cls.floorsToVisit.sort()
        if (cls.direction < 0):
            cls.floorsToVisit.reverse()

        # At this point we have a list of floors that asked for the lift that are going in the same direction as the lift.
        # we are missing floors that are past the maximum (minimum when going down) floor, that are going the opposite direction.
        if (cls.direction > 0) :
            floorsPossibleToVisit = range(len(queues)-1, max(cls.floorsToVisit or [cls.floor]),-1)
        else :
            floorsPossibleToVisit = range(0,min(cls.floorsToVisit or [cls.floor]))
        
        for floor in floorsPossibleToVisit:
            peopleOnIthFloor = queues[floor]
            if (cls.direction > 0):
                if (len([person for person in peopleOnIthFloor if person < floor]) > 0):
                    cls.floorsToVisit.append (floor)
                    break
            else:
                if (len([person for person in peopleOnIthFloor if person > floor]) > 0):
                    cls.floorsToVisit.append (floor)
                    break

    @classmethod
    def AddFloorToVisit(cls, newFloor):
        cls.floorsToVisit.append(newFloor)
        cls.floorsToVisit = list(set(cls.floorsToVisit))
        cls.floorsToVisit.sort()
        if (cls.direction < 0):
            cls.floorsToVisit.reverse()

    # this method will move lift through the list of floors in one direction and collect people
    @classmethod
    def MoveThroughAllFloors(cls ,queues):

        while (len(cls.floorsToVisit) > 0):
            cls.MoveToTheNextNeededFloor(queues)

        # Let's collect people from the last floor that lift stopped at
        peopleOnFloor = queues[cls.floor]

        #print ("Collecting: ",peopleOnFloor)
        while len(peopleOnFloor) > 0:
            if cls.capacity > len(cls.people):
                #print (cls.people)
                cls.people.append(peopleOnFloor[0])
                peopleOnFloor.pop(0)
            else:
                break
        
        #print (cls.people)
        #print (self.)
        #print (queues)

    @classmethod
    def MoveToTheNextNeededFloor(cls, queues):
        visitingFloor = cls.floorsToVisit.pop(0)
        cls.floor = visitingFloor
        if (cls.listOfVisitedFloors[len(cls.listOfVisitedFloors)-1] != visitingFloor):
            cls.listOfVisitedFloors.append(visitingFloor)
        # First, let people exit

        indexOfLeavingPeople = [i for i,person in enumerate(cls.people) if person == visitingFloor]
        cls.removeElementsFromList(cls.people, indexOfLeavingPeople)

        # Now, let new people enter
        indexOfEnteredPeople = []
        for i,personNeedsFloor in enumerate(queues[visitingFloor]):
            if cls.capacity > len(cls.people):
                if cls.direction > 0:
                    if personNeedsFloor > visitingFloor:
                        cls.people.append(personNeedsFloor)
                        cls.AddFloorToVisit(personNeedsFloor)
                        indexOfEnteredPeople.append(i)
                        #print (self.people)
                else:
                    if personNeedsFloor < visitingFloor:
                        cls.people.append(personNeedsFloor)
                        cls.AddFloorToVisit(personNeedsFloor)
                        indexOfEnteredPeople.append(i)
            else:
                break

        cls.removeElementsFromList(queues[visitingFloor], indexOfEnteredPeople)
    
    @classmethod
    def removeElementsFromList(cls, listWithElements, indices):
        #print (listWithElements, indices)
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
        self.lift.FindFloorsToVisit(newQueues)
        print (newQueues)
        while len(self.lift.floorsToVisit) > 0:
            self.lift.MoveThroughAllFloors(newQueues)
            self.lift.FindFloorsToVisit(newQueues)
        
        result = self.lift.listOfVisitedFloors
        if (len(result) == 0):
            result.insert(0,0)
        if (result[len(result)-1] != 0):
            result.append(0)
        
        print result
        return result

def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

# Floors:    G     1      2        3     4      5      6         Answers:
tests = [#[ ( (),   (),    (5,5,5), (),   (),    (),    () ),     [0, 2, 5, 0]          ],
         #[ ( (),   (),    (1,1),   (),   (),    (),    () ),     [0, 2, 1, 0]          ],
         #[ ( (),   (3,),  (4,),    (),   (5,),  (),    () ),     [0, 1, 2, 3, 4, 5, 0] ],
         #[ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ],
         #[ ( (5,),   (),  (),      (),    (),    (),    () ),     [0, 5, 0] ],
         [ ((2,), (6,), (3, 7, 6, 8, 6), (8, 5, 8, 8), (), (8, 0), (), (), (5,)), [0, 1, 2, 3, 5, 6, 8, 5, 0, 2, 3, 5, 6, 7, 2, 3, 5, 6, 8, 3, 5, 8, 3, 8, 0] ]
         ]
  
for queues, answer in tests:
    lift = Dinglemouse(queues, 2)
    testing(lift.theLift(), answer)
    
    