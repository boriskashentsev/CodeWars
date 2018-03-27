class Dinglemouse(object):

    def __init__(self, queues, capacity):
        pass
        
    def theLift(self):
        return []

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
    
    