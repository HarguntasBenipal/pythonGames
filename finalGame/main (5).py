from rockPaperScissors import rockPaperScissors
from ticTacToe import ticTacToe
from calculator import calculator
from guess import guess

print("\033[34m")
player1 = input ("\nName of User/Player 1: ") 
print("\033[0m")
print("\033[31m")
player2 = input ("Name of User/Player 2: ")
print("\033[0m")

while True:
  print("\n         Menu")
  print("~----------------------~")
  print("\n1. ~RockPapperScissors~")
  print("2. ~TikTacToe~")
  print("3. ~Calculator~")
  print("4. ~GuessTheNumber")

  select = input("What do you want to do?: ")

  if select == "1":
    rockPaperScissors.game()

  elif select == "2":
    ticTacToe.game(player1, player2)
    
  elif select == "3":
    calculator.game()

  elif select == "4":
    guess.game()
    
  else:
    print("Wrong input, try again.")
