import random

class montyHall:
     def __init__(self, switch = False, ai=False):
        self.doors = [0, 0, 0]
        self.choice = 0
        self.generateGame()
        self.switch = switch
        self.ai = ai

     def generateGame(self):
        possibilities = [0,1,2]
        gold = random.randint(0, 2)
        possibilities.remove(gold)
        
        # create the game
        self.doors[possibilities[0]] = -1
        self.doors[possibilities[1]] = -1
        self.doors[gold] = 1

     def unveilDoor(self):
          while True:
            door = random.randint(0, 2)
            if door == self.choice-1:
                continue
            if self.doors[door] == -1:
                print ("There is a goat behind door: ", door + 1)
                break
          if not self.ai:
               change = input("Would you like to change your choice (Y) or (N): ")
          tempDoors = self.doors.copy()
          tempDoors.remove(self.doors[self.choice-1])
          tempDoors.pop(self.doors[door])

         
          if self.ai and self.switch:
               self.choice = tempDoors[0] + 1
               print("You Switched")
          elif self.ai and not self.switch:
               print("You didn't switch")
          elif change == "Y":
               self.choice = tempDoors[0] + 1
               print("You Switched")
          else:
               print("You didnt switch")

          return

     def playGame(self, choice):

          if choice > 0:
               self.choice = choice
          else:
               self.choice = int(input("Pick a Door (1) (2) (3): "))
          self.unveilDoor()

          print("Unveiling Your Door!!!!")

          if self.doors[self.choice-1] == -1:
               print("You got a goat.")
               return -1
          else:
               print("You got gold.")
               return 1
        

class AI:
     def __init__(self, games, switch):
          self.games = games
          self.wins = 0
          self.losses = 0
          self.switch = switch

     def runAi(self):
          for i in range(self.games):
               game = montyHall(True, True)
               if (game.playGame(random.randint(1,3)) == 1):
                    self.wins+=1
               else:
                    self.losses+=1

          if self.switch:
               print("With Switching Each time: ")
          else:
               print("With Not-Switching each time: ")    

          print("Loss: ", self.losses)
          print("Wins: ", self.wins)
          input('')


while True:
     games = input("How many games to run Monty Hall Sim on: ")
     switch = input("Would you like to (S)witch each time or (ST)ay: ")

     if (switch == "ST"):
          switch = False
     elif (switch == 'S'):
          switch = True
     else:
          continue

     ai = AI(int(games), switch)
     ai.runAi()

     choice = input ("Press any key to play again or (Q) to quit: ")

     if choice == 'Q':
          break