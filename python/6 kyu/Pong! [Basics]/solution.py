class Pong:
    def __init__(self, max_score):
        self.max_score = max_score
        self.scores = [0, 0]
        self.paddle_length = 7
        self.current_player = 0 # 0 and 1 for 1st and 2nd player respectively

    def play(self, ball_pos, player_pos):
        print self.scores
        solution = ""
        if (self.max_score not in self.scores):
            if ball_pos >= player_pos - int(self.paddle_length / 2) and ball_pos <= player_pos + int(self.paddle_length / 2) :
                solution = "Player " + str(self.current_player + 1) + " has hit the ball!"
                self.current_player = (self.current_player + 1) % 2
            else :
                self.current_player = (self.current_player + 1) % 2
                self.scores[self.current_player] += 1
                if (self.max_score in self.scores) :
                    solution = "Player " + str(self.current_player +1 ) + " has won the game!"
                else :
                    solution = "Player " + str((self.current_player + 1) % 2 + 1) + " has missed the ball!"
        else:
            solution = "Game Over!"
        return solution

def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

game = Pong(2)

tests = [[ [50, 53], "Player 1 has hit the ball!" ],
         [ [100, 97], "Player 2 has hit the ball!" ],
         [ [0, 4], "Player 1 has missed the ball!" ],
         [ [25, 25], "Player 2 has hit the ball!" ],
         [ [75, 25], "Player 2 has won the game!" ],
         [ [50, 50], "Game Over!"]
         ]
  
for indx, [task, answer] in enumerate(tests):
    print ("Step #%d :" % indx)
    testing(game.play(task[0], task[1]), answer)