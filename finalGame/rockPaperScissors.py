class rockPaperScissors:

  def game ():   
    option = input("\n1.Player vs Player\n2.Player vs Computer\nWhat do you want to do?: ")
    
    if option == "1":
      print("\nE P I C    🪨  📄 ✂️    B A T T L E ")
      print()
      print("Select your move (R, P or S)")
      player1Move = input("Player 1 > ")
      player2Move = input("Player 2 > ")
      
      if player1Move=="R":
        if player2Move=="R":
          print("You both picked Rock, draw!")
        elif player2Move=="S":
          print("Player1 smashed Player2's Scissors into dust with their Rock!")
        elif player2Move=="P":
          print("Player1's Rock is smothered by Player2's Paper!")
        else:
          print("Invalid Move Player 2!")

      elif player1Move=="P":
        if player2Move=="R":
          print("Player2's Rock is smothered by Player1's Paper!")
        elif player2Move=="S":
          print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
        elif player2Move=="P":
          print("Two bits of paper flap at each other. Dissapointing. Draw.")
        else:
          print("Invalid Move Player 2!")
          
      elif player1Move=="S":
        if player2Move=="R":
          print("Player 2's Rock makes metal-dust out of Player1's Scissors")
        elif player2Move=="S":
          print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
        elif player2Move=="P":
          print("Player1's Scissors make confetti out of Player2's paper!")
        else:
          print("Invalid Move Player 2!")
      else:
        print("Invalid Move Player 1!")
    elif option == "2":
      import random
      
      again = 1
      while again==1:
        userEnter = (input("Rock, Paper, Scissors, Shoot: "))
        num1 = "rock" 
        num2 = "paper" 
        num3 = "scissors" 
        ranNum = random.randint(1,3)
        
        if ranNum == 1:
          print("Computer got: "+num1)
          if userEnter == "Rock":
            print("Tied")
          elif userEnter == "Paper":
            print("User Won")
          elif userEnter == "Scissors":
            print("User lost")
          
        elif ranNum == 2:
          print("Computer got: "+num2)
          if userEnter == "Rock":
            print("User Lost")
          elif userEnter == "Paper":
            print("Tied")
          elif userEnter == "Scissors":
            print("User Won")
    
        elif ranNum == 3:
          print("Computer got: "+num3)
          if userEnter == "Rock":
            print("User Won")
          elif userEnter == "Paper":
            print("User Lost")
          elif userEnter == "Scissors":
            print("Tied")
          
        again = int(input("Would you like to play again (1 for yes, 2 for no: "))

        print("Thank you!")