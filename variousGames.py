while True:
  print("\033[34m")
  player1 = input ("\nName of User/Player 1: ") 
  print("\033[0m")
  print("\033[31m")
  player2 = input ("Name of User/Player 2: ")
  print("\033[0m")
  
  print("\033[34m")
  print ("\n         Menu")
  print("~----------------------~")
  print("\033[0;0m", " Action will not work", "\n   if not spelt right.", "\n  Some stuff may need a", "\nrestart to use other stuff", "\033[34m")
  RockPaperScissors = print("\n1. ~RockPapperScissors~")
  TikTakToe = print("2. ~TikTakToe~")
  HangMan = print("3. ~HangMan~")
  Calculator = print("4. ~Calculator~")
  BlackJack = print("5. ~BlackJack~")
  GuessNum = print ("6. ~GuessTheNumber")
  StoryG = print ("7. ~Story Games~")
  print("\033[0m")
  
  select = input("\nWhat do you want to do?: ")

  if select == "1":
    
    option = input("\n1.Player vs Player\n2.Player vs Computer\nWhat do you want to do?: ")
    
    if option == "1":
      print("\nE P I C    🪨  📄 ✂️    B A T T L E ")
      print()
      print("Select your move (R, P or S)")
      #print()
      player1Move = input("Player 1 > ")
      #print()
      player2Move = input("Player 2 > ")
      #print()
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
      
  elif select == "2":

    import random

    def randomize_first_player(player1, player2):
      players = [player1, player2]
      random.shuffle(players)
      return players[0]

    # Randomize who goes first
    first_player = randomize_first_player(player1, player2)
    second_player = randomize_first_player(player1, player2)

    # Print the result
    print("\nFirst player:", first_player or second_player)

    print("")
    # Tic-Tac-Toe

    # Create the board
    board = [' ' for _ in range(9)]

    # Function to display the board
    def display_board():
        print("-------------")
        print("|", board[0], "|", board[1], "|", board[2], "|")
        print("-------------")
        print("|", board[3], "|", board[4], "|", board[5], "|")
        print("-------------")
        print("|", board[6], "|", board[7], "|", board[8], "|")
        print("-------------")

    # Function to check if a player has won
    def check_win(player):
        # Check rows
        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] == player:
                return True
        # Check columns
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] == player:
                return True
        # Check diagonals
        if board[0] == board[4] == board[8] == player:
            return True
        if board[2] == board[4] == board[6] == player:
            return True
        return False

    # Function to check if the board is full
    def check_draw():
        return ' ' not in board

    # Main game loop
    def play_game():
        current_player = 'X'
        while True:
            display_board()
            position = int(input("Enter a position (1-9): ")) - 1

            if board[position] == ' ':
                board[position] = current_player

                if check_win(current_player):
                    display_board()
                    print(current_player, "wins!")
                    break

                if check_draw():
                    display_board()
                    print("It's a draw!")
                    break

                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move. Try again.")

    # Start the game
    play_game()
  
  elif select == "3":
    import random

    def hangman():
        word_list = ['python', 'hangman', 'computer', 'programming', 'openai', 'algorithm', 'dessert', 'desert', 'airplane',	'boat',	'baby', 'ears',	'scissors',	'cough', 'cold',	'phone',	'laugh', 'blink',	'hairbrush',	'sneeze', 'spin',	'hammer',	'book', 'phone',	'toothbrush',	'jump', 'clap', 'slap', 'watermelon', 'sonic', 'archer',	'ghost',	'balance', 'shoelaces',	'sick',	'balloon', 'banana', 'monster',	'hiccup', 'stomp',	'hungry', 'slip',	'karate', 'ladder', 'scare',	'fishing',	'dizzy', 'read',	'hot', 'birthday',	'president',	'apartment', 'cradle',	'coffee',	'trampoline', 'waterfall',	'window',	'proud' ,'stuck',	'flashlight',	'marry', 'overwhelm',	'judge'	,'shadow' ,'halo'	,'measure'	,'clown' ,'chomp'	,'slither']
        chosen_word = random.choice(word_list).lower()
        guessed_letters = []
        attempts = 6

        while True:
            print_hangman(attempts)
            print_word(chosen_word, guessed_letters)

            if attempts == 0:
                print("You lose! The word was:", chosen_word)
                break

            if all(letter in guessed_letters for letter in chosen_word):
                print("Congratulations! You guessed the word:", chosen_word)
                break

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input! Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue

            guessed_letters.append(guess)

            if guess not in chosen_word:
                attempts -= 1
                print("Incorrect guess!")

    def print_hangman(attempts):
        stages = [
            '''
               --------
              |      |
              |      O
              |     \\|/
              |      |
              |     / \\
              -
            ''',
            '''
               --------
              |      |
              |      O
              |     \\|/
              |      |
              |     /
              -
            ''',
            '''
              --------
              |      |
              |      O
              |     \\|/
              |      |
              |
              -
            ''',
            '''
              --------
              |      |
              |      O
              |     \\|
              |      |
              |
              -
            ''',
            '''
              --------
              |      |
              |      O
              |      |
              |      |
              |
              -
            ''',
            '''
              --------
              |      |
              |      O
              |
              |
              |
              -
            ''',
            '''
              --------
              |      |
              |
              |
              |
              |
              -
            '''
        ]

        print(stages[6 - attempts])

    def print_word(word, guessed_letters):
        masked_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(masked_word)

    hangman()
 
  elif select == "4":
    def add(x, y):
      return x + y

    def substract(x, y):
        return x - y

    def multiply(x, y):
       return x * y

    def divide(x, y):
        if y != 0:
          return x/y

        else:
          return "Error, number can't be divisible by 0"

    while True:
        numchoice = int(input("\033[31m" + """
      \033[0m1. """ + "\033[31m" + """Add
      \033[0m2. """ + "\033[31m" + """Sub
      \033[0m3. """ + "\033[31m" + """Multiply
      \033[0m4. """ + "\033[31m" + """Divide
      \033[0m5. """ + "\033[31m" + """Math Quiz
      \033[0m6. """ + "\033[31m" + """Exit


      Answer: (use numbers between 1-6)
      """ + "\033[0m"))



        if numchoice == 1:
          num1 = float(input("What is the first number? > "))
          num2 = float(input("WHat is the next number you want added? > "))
          print("\n Results:", add(num1, num2), "\n")


        elif numchoice == 2:
          num1 = float(input("What is the first number? > "))
          num2 = float(input("WHat is the next number you want added? > "))
          print("\n Results:", substract(num1, num2), "\n")


        elif numchoice == 3:
          num1 = float(input("What is the first number? > "))
          num2 = float(input("WHat is the next number you want added? > "))
          print("\n Results:", multiply(num1, num2), "\n")


        elif numchoice == 4:
          num1 = float(input("What is the first number? > "))
          num2 = float(input("WHat is the next number you want added? > "))
          print("\n Results:", divide(num1, num2), "\n")

        elif numchoice == 5:
          import random

          def generate_question():
              """Generates a random math question."""
    # Choose a random operation
              operation = random.choice(['+', '-', '*', '/'])
    
    # Generate two random numbers
              if operation == '/':
        # For division, ensure the numbers have a whole number quotient
                  divisor = random.randint(1, 10)
                  dividend = random.randint(1, 10) * divisor
              else:
                  divisor = random.randint(1, 10)
                  dividend = random.randint(1, 10)
    
    # Generate the question string
              question = f"What is {dividend} {operation} {divisor}? "
    
    # Compute the correct answer
              if operation == '+':
                  answer = dividend + divisor
              elif operation == '-':
                  answer = dividend - divisor
              elif operation == '*':
                  answer = dividend * divisor
              else:
                  answer = dividend // divisor
    
              return question, answer


          def check_answer(question, user_answer, correct_answer):
              """Checks if the user's answer is correct."""
              if type(user_answer)==str:
                print("Please re-enter")
              elif user_answer == correct_answer:
                  print("Correct!")
                  return True
              else:
                print(f"Wrong! The correct answer is {correct_answer}.")
                return False


          def math_quiz(num_questions):
              """Runs a math quiz with the specified number of questions."""
              score = 0
    
              for _ in range(num_questions):
                  question, answer = generate_question()
                  user_answer = int(input(question))

                  if type(user_answer)==str:
                      print("Please re-enter")
                  elif check_answer(question, int(user_answer), answer):
                      score += 1
    
              print(f"\nQuiz completed! Your score is {score}/{num_questions}.")


# Run the math quiz with 5 questions
          math_quiz(5)

        elif numchoice == 6:
          print("Exiting...")
          break
        else:
          print("\nRestart")

          tryagain = input("Would you like to try again? (Yes/No) > ")
          if tryagain != "Yes":
           print("\nCya")
          break

    else:
      print("Alright\n")

  elif select == "5":
    import random

# Create a deck of cards
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Assign values to the cards
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Define the classes for the game
    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank
            self.value = card_values[rank]

        def __str__(self):
            return f"{self.rank} of {self.suit}"


    class Deck:
        def __init__(self):
            self.cards = []
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit, rank))
            random.shuffle(self.cards)

        def deal_card(self):
            return self.cards.pop()


    class Hand:
        def __init__(self):
            self.cards = []
            self.value = 0
            self.aces = 0

        def add_card(self, card):
            self.cards.append(card)
            self.value += card.value
            if card.rank == 'A':
                self.aces += 1

        def adjust_for_ace(self):
            while self.value > 21 and self.aces:
                self.value -= 10
                self.aces -= 1


    class Chips:
        def __init__(self):
            self.total = 100
            self.bet = 0

        def win_bet(self):
            self.total += self.bet

        def lose_bet(self):
            self.total -= self.bet


# Functions for gameplay
    def take_bet(chips):
        while True:
            try:
                chips.bet = int(input("How many chips would you like to bet? "))
                if chips.bet > chips.total:
                    print("Sorry, you don't have enough chips. You have", chips.total, "chips.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")


    def hit(deck, hand):
        hand.add_card(deck.deal_card())
        hand.adjust_for_ace()


    def hit_or_stand(deck, hand):
        global playing
        while True:
            action = input("Do you want to Hit or Stand? Enter 'h' or 's': ").lower()
            if action == 'h':
                hit(deck, hand)
            elif action == 's':
                print("Player stands. Dealer's turn.")
                playing = False
            else:
                print("Invalid input. Please enter 'h' or 's'.")
                continue
            break


    def show_some(player, dealer):
        print("\nPlayer's cards:")
        for card in player.cards:
            print(card)
        print("\nDealer's cards:")
        print("<hidden card>")
        for card in dealer.cards[1:]:
            print(card)


    def show_all(player, dealer):
        print("\nPlayer's cards:")
        for card in player.cards:
            print(card)
        print("\nDealer's cards:")
        for card in dealer.cards:
            print(card)

    def player_busts(player, dealer, chips):
        print("Player busts!")
        chips.lose_bet()

    def player_wins(player, dealer, chips):
        print("Player wins!")
        chips.win_bet()

    def dealer_busts(player, dealer, chips):
        print("Dealer busts!")
        chips.win_bet()

    def dealer_wins(player, dealer, chips):
        print("Dealer wins!")
        chips.lose_bet()

    def push(player, dealer):
        print("It's a tie! Push.")


# Main game logic
    while True:
        print("\nWelcome to Blackjack! Get as close to 21 as you can without going over.")
        print("Dealer hits until she reaches 17. Aces count as 1 or 11.")

    # Create deck and deal initial hands
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

    # Set up player's chips
        player_chips = Chips()

    # Prompt the player for their bet
        take_bet(player_chips)

    # Show initial cards (one dealer card is hidden)
        show_some(player_hand, dealer_hand)

        playing = True
        while playing:
        # Prompt for player to Hit or Stand
            hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, player busts and breaks out of the loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

    # If player hasn't busted, play dealer's hand until dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

        # Show all cards
            show_all(player_hand, dealer_hand)

        # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

    # Inform the player of their chips total
        print("\nPlayer's total chips:", player_chips.total)

    # Ask to play again
        play_again = input("Do you want to play again? Enter 'y' or 'n': ").lower()
        if play_again != 'y':
            break

  elif select == "6":
    import random

    def guess_the_number():
        print("Welcome to Guess the Number!")
        print("I'm thinking of a number between 1 and 100.")
        print("You have 10 attempts to guess the number.")
    
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
    
        while attempts < max_attempts:
            guess = int(input("Take a guess: "))
            attempts += 1
        
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number in", attempts, "attempts.")
                return
    
        print("Sorry, you ran out of attempts. The number was", secret_number)

    guess_the_number()


  elif select == "7":
    print ("\n","\033[3;31m","     Story Games")
    print(" ~----------------------~")
    print("Note: Story games won't save", "\nprogress so stay on window or") 
    print("  tab to keep your progress")
    print("  And do NOT turn off your")
    print("      device/desktop")
    Cambion = print("\n1. ~Cambion~")
    print("\033[0m")
    
    Select2 = input ("\nWhat Story do you want to play?: ")
    if Select2 == "1":
      print("")
      print("")
      print("")
      print("")
      print("")
      print("\033[3;31m", "                     Hello", "\033[0m")
      print("            --------------------------")
      print("            This is the World speaking.")
      print("              I'll be both your Hint")
      print("               Narrator, and advisor")
      print("")
      print("")
      print("")
      print("")
      print("")

      print("This is a" , "\033[1;38m",  "STORY" , "\033[0m", "that allows you to choose your own", "\033[1;31m", "PATH", "\033[0m")
      print("\nYour desisions", "\033[1;31m", "AFFECT", "\033[0m", "your story and outcome")
      Name = input ("What is your Hero's name?: ")
      print("\n",Name, "Ah interesting, that's a very weird name. You may not be from around here, anyways adventurer your goal is to take down the", "\033[31m", "DEMIGOD", "\033[0m")

      while True:
        Race = input ("\nWill you become a [Human] or [Demon]?: ")
        if Race == "Human":
          print("\nGoing on the path of", "\033[1;34m","RIGHTEOUSNESS", "\033[0m","I see, Alright")
          print("\nAlright Hero, Lets Start The Story")
    
        elif Race == "Demon":
          print("\nOn the path of Evil I see, Alright")
        else:
          print("You spelt it Wrong, try again")
        if Race == "Demon" or Race == "Human":
          break


    
      print("")
      print("")
      print("")
      print("\033[3;31m", "   Chapter 1", "\033[0m")
      print("  -------------")
      print("  A", "\033[1;36m", "New", "\033[0m", "World",)
      print("")
      print("")
      print("")
      print("\nThis story starts in your room you wake up out of bed")

      while True:
        Explore = input ("Do you want to go explore the world and maybe Fight monsters? Yes/No?: ")
  
        if Explore == "Yes":
          print("\nAlright lets go")
    
        elif Explore == "No": print("\nYou were lazy and went back to sleep, your house collapsed and you died. This happened because you did not know your house was falling apart.", "\nTry a different route")

        else:
          print("You spelt it wrong, try again")
        if Explore == "Yes":
          break
    
      if Explore == "Yes":
        print("\nYou find out you're living in the middle of no where. You were wondering outside through an open field of grass for awhile and found a monster, above it shows Level1")

      while True:
        FightC1 = input("\nHow do you want to attack? [Head on], [Sneak], [Tactically] or [Leave it]? Spell correctly: ")
  
        if FightC1 == "Head on":
          print("\nYou died, next time try something more safer")
    
        elif FightC1 == "Leave it":
          print("\033[1;31m", "You Died", "\033[0m",)
          print("The monster took the chance to attack while you were not looking. Try agina")
  
        if FightC1 == "Sneak":
          print("\nYou sneaked up on the monster but he notices you. You attack as fast as you can in a panick and died.", "\nTry agin")
    
        elif FightC1 == "Tactically":
          print("\nYou charged at it and dodge it's attacks and delived the finishing blow.")
        else:
          print("You spelt it wrong, try again.")
        if FightC1 == "Tactically":
          break

      if FightC1 == "Tactically":
        print("\033[34m", "\n  ! Notice:   ", "\033[0m") 
        print(" ------------")
        print("\033[33m", " LEVEL",  "\033[0m", "UP!")
        print("\033[1;34m", "\nYou've gained 1 IQ trait", "\033[0m")
  
      while True:
        CR = input("\nWould you like to [Continue] or [Head back]?: ")
        if CR == "Continue":
            print("\nYou continue to wonder around and come across 2 paths.")

        elif CR == "Head back": 
          print("You head back to your home but it had collapsed")
          print("\nYou head back and continue exploring and found 2 paths knowing that, this may be the only way to possibly finding cilvilization")
        else:
          print("You spelt it wrong, try again.")
        if CR == "Continue" or CR == "Head back":
          break

      while True:
        path = input ("\npath [1] leads to another meadow, path [2] leads into a forest. Which will you take?: ")
        if path == "1":
              print("You continue on through the meadow. But there was nothing to explore so you head back to the paths.")
      
        elif path == "2":
          print("You walk through the muddy path forest")
    
        else:
          print("You Spelt Wrong, try again.")
        if path == "2":
          break
    
      while True:  
        muddypath = input("\nYou wonder through the muddy path, and half-way through you find out it's quicksand, will you [Fight] or [Yell for help]?: ")
        if muddypath == "Fight": 
          print("\033[1;31m", "\nYOU DIED", "\033[0m")
          print("\nYou tried to fight through the quicksand but ended up dying like a fool")
  
        elif muddypath == "Yell for help":
          print("\nYou yell for help, about 5 strangers in armour with a", "\033[1;34m", "blue embroided cloth", "\033[0m", "around them come to the rescue")
          print("The strangers cloths all had different", "\033[1;34m", "animals", "\033[0m", "as if those were", "\033[1;34m", "acient hieroglyphics", "\033[0m")
        else:
          print("You spelt it wrong, try again.")
        if muddypath == "Yell for help":
          break

      print("\nCommander Knight and his team saves you")
      print("Commander Knight: Hey, what are you doing wondering around here??")

      while True:
        knightans1 = input("\nYou think about what the knight is saying, will you [Truth] or [Insult]? ")
        if knightans1 == "Truth":
          print("\nYou tell the guard you that are training and looking for monsters to kill")
          print("Commander Knight: So it's a newbie, alright. Head on your way, no need to thank us.")
        elif knightans1 == "Insult":
          print("\nYou feel offended by the way the commander knight is talking to you and cuss him out.")
          print("\033[1;31m", "YOU DIED", "\033[0m")
          print("The commander knight got annoyed of your attitude even after he saved you, so he ends out slicing off your head")
        else:
          print("You spelt it wrong try again.")
        if knightans1 == "Truth":
          break

      print("")
      print("")
      print("")
      print("\033[3;31m", "             Chapter 2", "\033[0m")
      print(" ------------------------------------")
      print("  The", "\033[3;36m", "Ghosts", "\033[0m", "of", "\033[9;31m", "Ever Moon Kingdom", "\033[0m")
      print("")
      print("")
      print("")

      while True:
        ask = input ("\nDo you want to ask which way is the kingdom before they leave? Yes/No: ")

        if ask == "No":
          print("\nYou let them walk away and continue your way through the forest")
          print ("Eventually you get lost but found a brick wall that looks about 20 feet tall")
          print("You follow the brick wall all the way to one of the entrances")

        elif ask == "Yes":
          print ("\nCommander Knight: Oh Hey, it's newbie guys, what is it?")
          print("\nHey knights, which way is the kingdom?")
          print ("\nCommander Knight: It's past the forest and down the river stream")
          print("You thank the Commander and rushed over to the kingdom")
          print ("Eventually you found the river stream and followed until you found a brick wall that looks about 20 feet tall")

        else:
          print("You spelt it wrong, try again.")
        if ask == "Yes" or ask == "No":
          break

      print("\nA Knight yells:")
      print("Who goes there!?")


      while True:
        ansquestion1 = input("\nWill you tell the guard that you met the commander knight and want to get into the kingdom, or pretend like a vistor? Knight/Vistor: ")
  
        if ansquestion1 == "Knight":
          print("\nSupervisor Guard: Alright! Open the gate!")
          print("\nThe gate opens and you venture into the captial city")
  
        elif ansquestion1 == "Vistor":
          print("\nYou yell back that you are a visting adventurer, the supervisor guard comes closer and asks for an id or any proof of idenification")
          print("\nYou forgot that you left everything at your house, so you tell the guard you don't have any")
          print("\nGuard: What the hell are you doing wondering around as an adventurer without an idenification? Get the hell out of here")

        else:
          print("You spelt it wrong, try it again")

        if ansquestion1 == "Knight":
          break

      print("\nYou ask what kingdom you are in")
      print("Supervisor Guard: You are in The Ever Moon Kingdom")
      print("\nCommander Royal Guard is walking by")
      print("\nSupervisor Guard: Commander Sir!")
      print("Commander Royal Guard: Who's this?")
      print("Supervisor Guard: Someone who cliams to know you, Sir!")

      while True:
        KnightQ = input("\nCommander Royal Guard: He claims to know the commander knight!? Preposterous! What does the Commander Knight looks like? Would you like to answer [Blue enbroided cloth] or [Acient hieroglyphics] on the cloth?: ")

        if KnightQ == "Blue enbroided cloth":
          KnightQ = input("\nCommander Royal Guard: Wait, what? What did the embodiments look like!? [Ancient hieroglyphics]: ")
          if KnightQ == "Ancient hieroglyphics":
            print("There's no way, we must take you to his majesty, Immediately!")

        elif KnightQ == "Ancient hieroglyphics":
          KnightQ = input("\nCommander Royal Guard: Wait, what? What did the embodiments look like!? [Blue enbroided cloth]: ")
          if KnightQ == "Blue enbroided cloth":
            print("There's no way, we must take you to his majesty, Immediately!")
    
        else:
          print("You spelt it wrong, try again")

        if KnightQ == "Blue enbroided cloth" or KnightQ == "Ancient hieroglyphics":
          break

      print("\nCommander Royal Guard: Hey! we need a ride to the castle!")
      print("Coachman : Y-Yes Sir!")
      print("You and the Royal Commander guard rush to the kingdom, after an hour you finally reach")
      print("\nCommander Royal Guard: Hey guard, let this guy in, we need an audiance with the king")
      print("Guard: Y-Yes sir! Will do , give me couple of minutes")

      while True:
        QForest = input("So, what is your name?: ")
        if QForest == (Name):
          QForest = input("I see, so where did you ses these Knights? [Forest]: ")
          if QForest == "Forest":
            print("I see, well your gonna meet the king so you will neeed to explain what you saw")
        else:
          print("You spelt is wrong, try again")
        if QForest == "Forest":
          break






      print("\nAbout 30 minutes passed")
      print("Guard: The king is ready to meet with you")
      print("\nYou head through the throne room")
      print("King: You their! State your purpose")
      print("Ayumu: I'm Count Ayumu von Tuatha Dé")
      print("King: I see your the prodigy that everyone is talking about within our ranks, well why have you come?")
      print("Ayumu: This boy has seen something that I can't even fathom to speak, he saw some knights in the middle of no where")

      while True:
        KingQ = input("King: Speak boy, what did you see? [Tell what you told Ayumu] or where you saw them [Forest]:")
        if KingQ == "Tell what you told Ayumu":
          KingQ = input("King: You what!? Where did you see them!? [Forest]: ")
          if KingQ == "Forest":
            print("King: It can't be, the Hero's from 100 years ago")
        elif KingQ == "Forest":
          KingQ = input ("King: Odd, what did these knights look like? [Tell what you told Ayumu]: ")
          if KingQ == "Tell what you told Ayumu":
            print("King: It can't be, the Hero's from 100 years ago")
        else:
          print("You spelt it wrong, try again.")
        if KingQ == "Tell what you told Ayumu" or KingQ == "Forest":
          break

      print("\nKing: Come with me boy, you to Ayumu to my quarters, there's something I must tell you both")
      
      print("\n")
      print("")
      print("")
      print("\033[3;31m", "        Chapter 3", "\033[0m")
      print(" --------------------------")
      print("\033[3;34m", "Hero's", "\033[0m", "from 100 years ago")
      print("")
      print("")
      print("")
      print("\nKing: Welcome to my quarters, have a seat")
      print("You ask whats going on")
      print("\nAyumu: What you saw in the forest was the knights from 100 years ago during the Calamity period")

      while True:
        NumberOfKnight = input("\nKing: He's right, but I must ask, how many Knights did you see? [3], [8], or [5]?: ")
        if NumberOfKnight == "3":
          print("King: Impossible, there wasn't 3, try remembering")

        elif NumberOfKnight == "8":
          print("King: Liar, the wasn't that many, try rememebering")

        if NumberOfKnight == "5":
          print("King: I don't belive it, even now they are still together")
  
        else:
          print("\nTry again [Hint: Look back on the story how many knights were there to help you]")
        if NumberOfKnight == "5":
          break

      print("\nKing: Those 5 Hero's were what gave us peace and freedom. Their names were...")
      print("\033[3;32m", "\nKenji Gushiken: He is the Hero of brute Strength, anyone he fights, he use’s his fists or iron gauntlets with engraved magic that can increase his attacks ten folds, including his hammer.", "\033[0m")

      print("\033[3;37m", "\nYōsei Genji: She is a fairy that has supernatural healing powers. It is a light spell that can fend off demons and put monsters under he control.", "\033[0m")

      print("\033[3;35m", "\nKiera Kanamori: Kiera is crafter and a smith. She provides tools to the team and create magical weapon’s. Her reason for being within the 5 hero’s are her incredible aiming skills. She can hit anything from 5 miles and up which also makes her there intellegence and sniper.", "\033[0m")

      print("\033[3;33m", "\nBertrand Licht: Bertrand is a damage taker, he can put up shields that can block S level magic. He can turn his shield into a bright light that can stun anyone and anything or a light sword that can cut through anything.", "\033[0m")

      print("\033[3;31m", "\nHomura Akuma: He is one of the last Akuma within his bloodline. His father was once a king but a Demon had destroyed everything, yet somehow he’s alive. He blames himself but eventually started fight for revenge and honor. fights with a holy chain whip which can light on fire. His chain whip can infinitely extend to his desire.", "\033[0m")

      print("King: These people were legends but finding them in the forest is unbelievable")

      while True:
        Quest = input("\nKing: Will you tell us where they might be? Yes/No: ")
        if Quest == "Yes":
          print("Great my army will leave tommorow at first light")

        elif Quest == "No":
          print ("That's too bad, well we will help set you off on your journey if you plan on leaving, but for telling us this, please stay within our hospiltality")
  
        else:
          print("You spelt it wrong, try again")
        if Quest == "Yes" or Quest == "No":
          break

      print("World: It's been sometime since we spoke")
      print("I came to remind...")
      print("\nThis is a" , "\033[1;38m",  "STORY" , "\033[0m", "that allows you to choose your own", "\033[1;31m", "PATH", "\033[0m")
      print("\nYour desisions", "\033[1;31m", "AFFECT", "\033[0m", "your story and outcome")
      print("So, since you have been at this for awhile, I think you deserve a checkpoint, but don't forget what your goal is...")
      print("\nI will be setting a checkpoint right now. If you leave the game you have to restart, but with this checkpoint, if anything were to happen like you", "\033[1;31m", "Dying", "\033[0m", "along the way, you will come back here from now on")
      print("You have been relying on the quick death to much so be careful.")

      print("")
      print("")
      print("")
      print("\033[3;31m", "        Chapter 4", "\033[0m")
      print(" --------------------------")
      print("      The", "\033[4;31m", "Restart", "\033[0m")
      print("")
      print("")
      print("")


      print("A maid leads you to a room to rest in.")
      print("Maid: Here is your room, if YoU n337-")
      print("World: Your check point have been set", "\033[3;31m", "Good Luck", "\033[0m")
      print("Maid: S~? Sr~!? Sir!? Are you okay, you just fainted")
      print("Maid: You gave me a scare, I was saying if you need anything, will be in the next room")

      while True:  
        Sleep = input("\nWould you like to go to sleep or stay awake? [Sleep] or [Stay awake]: ")
        if Sleep == "Sleep":
          print("\nAfter 2 hours of sleep you wake up to a loud scraping sound that is coming closer and closer")
          Escape = input("\nWould you like to go back to [Sleep] or [Investigate]?: ")
          if Escape == "Sleep":
            print("\nYou wake up back when the maid had left your room")
          elif Escape == "Investigate":
            print("\nYou open the door to see what was going on but you were to drowsy and scared to react and", "\033[1;31m", "Died", "\033[0m")
            print("\nYou wake up back when the maid had left your room")
  
        elif Sleep == "Stay awake":
          print("\nYou stay awake for 2 hours but start to fall asleep and started hearing and loud scraping sound getting closer and closer")
  
        else:
          print("You spelt it wrong, try again")
        if Sleep == "Stay awake":
          break

      print("\nYou go to investigate and dodge a spear that flew towards you")

      while True:
        RunAway = input ("\nDo you want to [Run] through the door or [Jump] out the window?: ")
        if RunAway == "Run":
          print("\nYou run through the door and turn right but it was too dark to see and reached a dead end. you turn around and", "\033[1;31m", "Died", "\033[0m", "by the killer")
        elif RunAway == "Jump":
          print("\nYou run to the window and jump, soon you relize there is no ledge and it's so foggy that you can't see anything to break your fall, your only option was to try and grab the walll")
          fall = input ("\nDo you want to [Fall] or grab the [Wall]?: ")
          if fall == "Fall":
            print("\nYou took the leap of faith opyion and continue to fall, the fog had cleared up and you saw a brick ground.")
          elif fall == "Wall":
            print ("\nYou scrape your nail and lost balence and splatted on the ground")

        else:
          print("\nYou spelt it wrong.")

        if fall == "Fall":
          break

      print("\nAs you were falling, you had stopped with a jolt and relized someone caught you before you touched the ground you looked up saw it was Ayumu who caught you")

      print("\nAyumu: Are you okay", Name, "?")
      print("\nAyumu: Why were you falling from that high up?")
      while True:
        SleepEX = input ("\nTell Ayumu what had [Happened] or keep it a [Secret]?: ")
        if SleepEX == "Happened":
          print("\nAyumu: That's madness, well you can sleep here if you want in my quarters and make sure nothing like that happenes again")
        elif SleepEX == "Secret":
          print("\nAyumu: I can't help you if you don't tell me whats going on")
        else:
          print("You spelt it wrong.")
        if SleepEX == "Happened":
          break

      print("In your sleep you having the best dream but a dark evil smoke consumes it and someone approaches you within your dream.")
      print("\033[31m", "\n???:", "Hello young one, you don't know me but I know you")
      print("\nWhen you set on your adventure to the forest, I will be waiting for you in a ancient labyrinth, until then I will be burning this crest into your chest. Lastly remember this...You can't tell anyone of this otherwise you will be", "ELIMINATED", "\033[0m")
      print("\nYou wake up with ajolt and remember that strange dream you had")
      print("You check if the crest was burned into your chest, you examine it and fint out you have become stronger")
      print("\033[34m", "\n           ! Notice:   ", "\033[0m")
      print("        ----------------")
      print("          You Obtained")
      print("\n","\033[3;97m","Crest of the","\033[3;31m","D","\033[3;35m", "E","\033[3;31m", "M","\033[3;35m", "O","\033[3;31m", "N","\033[3;35m", "S", "\033[0m")
      print("\033[34m", "\n         ! Notice:   ", "\033[0m")
      print("      ----------------")
      print("You have leveled up to 50")
      print("\033[34m", "\n         ! Notice:   ", "\033[0m")
      print("      ----------------")
      print("   All states increased by","\n         25 points")
      print("\033[34m", "\n         ! Notice:   ", "\033[0m")
      print("      ----------------")
      print("All states has been muliplied", "\n           by 500")
      print("\033[34m", "\n         ! Notice:   ", "\033[0m")
      print("      ----------------")
      print("    New skills acquired")
      print("\033[34m", "\n         ! Notice:   ", "\033[0m")
      print("      ----------------")
      print("\033[32m","      HP: 26,000", "\033[31m", "\n       Strength: 12,500","\033[36m" "\n       Speed: 12,500", "\033[94m", "\n       Defence: 12,500", "\033[0m","\n       Intelligence: 12,500", "\033[92m","\n       Luck: 82%","\033[0m")
      print("Ayumu:", Name, "You okay? You scared me")
      while True:
        DreamW = input ("\nDo you want the [Tell] Ayume about the dream or keep it a [Secret]?: ")
        if DreamW == "Tell":
          print("\nAs you tell Ayumu about the dream, time froze and the same evil smoke surrounded you")
          print("???: I told you now to say anything... NOW", "\033[31m", "DIE", "\033[0m")
        elif DreamW == "Secret":
          print("Ayumu: I see well, I hope you can tell me in the future but right now we need to head into the forest where you found those knights")
        else:
          print("You spelt it wrong.")
        if DreamW == "Secret":
          break
      print("\nYou packed your stuff and headed outside where the calvary was waitting to storm the forest")
      print("\nAyumu: Hey", Name, ",Am gonna be coming as well since the king decided to stay at the castle")
      print("\nAyumu: Alright men! March towards forest")
      print("\nYou, Ayumu and the calvary were marching towards the forest and eventually you got lost")
      while True:
        Path2 = input ("[Contimue] on the Same path or take a [Different] route?: ")
        if Path2 == "Continue":
          print("You mention this was the area you saw the knights")
        elif Path2 == "Different":
          print("I don't see anyone here plus the forest gets denser from here, lets head back")
        else:
          print("You spelt it wrong.")
        if Path2 == "Continue":
          break
      print("\nKnight1: Hey did you see that, I thought I saw aghost")
      print("Knight2: You alright, I think you drank too much")
      print("Knight1: Maybe")
      print("Ayumu: What did you say! Where!?")
      print("Knight1: Over there, sir!")
      print("Ayumu: Let's go", Name)
      print("\nYou head deeper into the forest and the air pressure becomes heavier")
      print("Ayumu: The Horses stopped for some reason, we should walk from here")
      print("\nAs you walk furthur into the forest you come across a beast")
      while True:
        FightBst = input ("\nAyumu: That looks like a SSSR-Ranked beast! Do you want to [Fight] it or [Sneak] around it?: ")
        if FightBst == "Fight":
            print("You slay the beast in one shot")
            print("Ayumu: Who are you, how are you so strong!?")
        elif FightBst == "Sneak":
          print("\nAyumu struggles but kills it but another one showed up")
          FightBeast2 = input ("[Attack] or [Help] Ayumu?: ")
          if FightBeast2 == "Attack":
            print("You slay the beast in one shot")
          elif FightBeast2 == "Help":
            print("You try to help Ayumu but died to the beast and you get ambused and", "\033[31m", "DIED", "\033[0m")
        else:
          print("You spelt it wrong.")

        if FightBst == "Fight" or FightBeast2 == "Attack":
          break

      print("\nAfter defeating a horde of beasts, you finally rest a little to collect your bearings before you continue your journey to find the Hero's")
      print("\nAs you journey furthure into the forest your start to see red gooey stuff like slime, lave and malice all mixed together")
      print("\nAyumu: Hey look, I see a a the Hero's near a gate")
      print("You and Ayumu run towards the Hero's")
      print("\nAyumu: No way! It's the Hero's from 100 years ago but why are they red? *Gasp*")
      print("Ayumu: *Ayumu pushes you out the way* Watch Out!!")
      print("\nKnight: The commandor knight has been slain")
      print("You turn around and the Hero charged at you and you...")
      print("\033[31m", "DIED", "\033[0m")
      print("")
      print("\n","\033[31m", "???: Welcome to purgatory. You are quite promising fighter even after I gave you that, I shall restore you just this once but make it count, I'm dying to meet you in person")
      while True:
        purgatory = input("???: So what will it be? [Restart] or [Stay] here with me?: ")
        if purgatory == "Restart":
          print("???: Very well lets see what your capable off after seeing", "\033[31m", "Eeverything", "\033[0m")
        elif purgatory == "Stay":
              print("I see well, since I want to meet you really badly still, why don't you fight my right hand man, if he wins, you restart, if you win...you can stay")
              purgatory2 = input ("[Deal] or [No] deal?: ")
              if purgatory2 == "Deal":
                print("???: Very well", "\033[31m", "FIGHT", "\033[0m")
                print("After fighting for what felt like years you lost")
                print("???: I'm impressed but you lost, so happy seeing again in the land of the living")
              elif purgatory2 == "No":
                print("You don't have a choice")
                print("After fighting for what felt like years you lost")
                print("???: I'm impressed but you lost, so happy seeing again in the land of the living")
        else:
          print("You spelt it wrong.")
        if purgatory == "Restart" or purgatory2 == "Deal" or purgatory2 == "No":
          break


      print("")
      print("\n")
      print("")
      print("")
      print("")
      print("")
      print("\033[3;31m", "                     Hello", "\033[0m")
      print("            --------------------------")
      print("            This is the World speaking.")
      print("              I'll be both your Hint")
      print("               Narrator, and advisor")
      print("")
      print("")
      print("")
      print("")
      print("")

      while True:
        Explore = input ("\nDo you want to go explore the world and maybe Fight monsters? Yes/No?: ")
  
        if Explore == "Yes":
          print("\nAlright lets go")
    
        elif Explore == "No": print("\nYou were lazy and went back to sleep, your house collapsed and you died. This happened because you did not know your house was falling apart.", "\nTry a different route")

        else:
          print("You spelt it wrong, try again")
        if Explore == "Yes":
          break

      while True:  
        muddypath = input("\nYou wonder through the muddy path, and half-way through you find out it's quicksand, will you [Fight] or [Yell for help]?: ")
        if muddypath == "Fight": 
          print("\033[1;31m", "\nYOU DIED", "\033[0m")
          print("\nYou tried to fight through the quicksand but ended up dying like a fool")
  
        elif muddypath == "Yell for help":
          print("\nYou yell for help, about 5 strangers in armour with a", "\033[1;34m", "blue embroided cloth", "\033[0m", "around them come to the rescue")
          print("The strangers cloths all had different", "\033[1;34m", "animals", "\033[0m", "as if those were", "\033[1;34m", "acient hieroglyphics", "\033[0m")
        else:
          print("You spelt it wrong, try again.")
        if muddypath == "Yell for help":
          break

      while True:
        ansquestion1 = input("\nWill you tell the guard that you met the commander knight and want to get into the kingdom, or pretend like a vistor? Knight/Vistor: ")
  
        if ansquestion1 == "Knight":
          print("\nSupervisor Guard: Alright! Open the gate!")
          print("\nThe gate opens and you venture into the captial city")
  
        elif ansquestion1 == "Vistor":
          print("\nYou yell back that you are a visting adventurer, the supervisor guard comes closer and asks for an id or any proof of idenification")
          print("\nYou forgot that you left everything at your house, so you tell the guard you don't have any")
          print("\nGuard: What the hell are you doing wondering around as an adventurer without an idenification? Get the hell out of here")

        else:
          print("You spelt it wrong, try it again")

        if ansquestion1 == "Knight":
          break

      while True:
        RunAway = input ("\nDo you want to [Run] through the door or [Jump] out the window?: ")
        if RunAway == "Run":
          print("\nYou run through the door and turn right but it was too dark to see and reached a dead end. you turn around and", "\033[1;31m", "Died", "\033[0m", "by the killer")
        elif RunAway == "Jump":
          print("\nYou run to the window and jump, soon you relize there is no ledge and it's so foggy that you can't see anything to break your fall, your only option was to try and grab the walll")
        fall = input ("\nDo you want to [Fall] or grab the [Wall]?: ")
        if fall == "Fall":
            print("\nYou took the leap of faith opyion and continue to fall, the fog had cleared up and you saw a brick ground.")
        elif fall == "Wall":
          print ("\nYou scrape your nail and lost balence and splatted on the ground")

        else:
          print("\nYou spelt it wrong.")

        if fall == "Fall":
          break

      print("\nAs you were falling, you had stopped with a jolt and relized someone caught you before you touched the ground you looked up saw it was Ayumu who caught you")

      print("\nAyumu: Are you okay", Name, "?")
      print("\nAyumu: Why were you falling from that high up?")

      print("\033[34m", "\n           ! Notice:   ", "\033[0m")
      print("        ----------------")
      print("          You Obtained")
      print("\n","\033[3;97m","Crest of the","\033[3;31m","D","\033[3;35m", "E","\033[3;31m", "M","\033[3;35m", "O","\033[3;31m", "N","\033[3;35m", "S", "\033[0m")
      print("\033[34m", "\n         ! Notice:   ", "\033[0m")
      print("      ----------------")
      print("You have leveled up to 50")
      print("\033[34m", "\n         ! Notice:   ", "\033[0m")
      print("      ----------------")
      print("   All states increased by","\n         25 points")
      print("\033[34m", "\n         ! Notice:   ", "\033[0m")
      print("      ----------------")
      print("All states has been muliplied", "\n           by 500")
      print("\033[34m", "\n         ! Notice:   ", "\033[0m")
      print("      ----------------")
      print("    New skills acquired")
      print("\033[34m", "\n         ! Notice:   ", "\033[0m")
      print("      ----------------")
      print("\033[32m","      HP: 26,000", "\033[31m", "\n       Strength: 12,500","\033[36m" "\n       Speed: 12,500", "\033[94m", "\n       Defence: 12,500", "\033[0m","\n       Intelligence: 12,500", "\033[92m","\n       Luck: 82%","\033[0m")

      while True:
        Path2 = input ("\n[Contimue] on the Same path or take a [Different] route?: ")
        if Path2 == "Continue":
          print("You mention this was the area you saw the knights")
        elif Path2 == "Different":
          print("I don't see anyone here plus the forest gets denser from here, lets head back")
        else:
          print("You spelt it wrong.")
        if Path2 == "Continue":
          break

      while True:
        FightBeast = input ("\nAyumu: That looks like a SSSR-Ranked beast! Do you want to [Fight] it or [Sneak] around it?: ")
        if FightBst == "Fight":
            print("You slay the beast in one shot")
            print("Ayumu: Who are you, how are you so strong!?")
        elif FightBst == "Sneak":
          print("\nAyumu struggles but kills it but another one showed up")
          FightBeast2 = input ("[Attack] or [Help] Ayumu?: ")
          if FightBeast2 == "Attack":
            print("You slay the beast in one shot")
          elif FightBeast2 == "Help":
            print("You try to help Ayumu but died to the beast and you get ambushed and", "\033[31m", "DIED", "\033[0m")
        else:
          print("You spelt it wrong.")

        if FightBst == "Fight" or FightBeast2 == "Attack":
          break

      print("\033[31m")
      print("???: Welcome back to where you once were now show me what you have learned", "\033[0m")

      print("\nAfter defeating a horde of beasts, you finally rest a little to collect your bearings before you continue your journey to find the Hero's")
      print("\nAs you journey furthure into the forest your start to see red gooey stuff like slime, lave and malice all mixed together")
      print("\nAyumu: Hey look, I see a a the Hero's near a gate")
      while True:
        StopA = input ("\n[Stop] Ayumu from running towards the Hero's or use him as [Bait]?: ")
        if StopA == "Stop":
          print("Ayumu: Why? Now that I look carfully, they seem to be covered in that red gooey thing")
        elif StopA == "Bait":
          print("Ayumu: Why are you standing there come on...Now that I look carfully, they seem to be covered in that red gooey thing")
        else :
          print("You spelt it wrong.")
        if StopA == "Stop" or StopA == "Bait":
          break

      print("\nAyumu: 4 of the Hero's are opening the gate and heading inside while the fifth one, Bertrand Licht is charging at us...Charging at us? Charging at us, run!!")
      print("Ayumu: You remember the king told us that he's a total damage taker so he might take a while to stop you go on ahead while me and my men will hold him off")

      while True:
        Fight5H = input ("\n[Help] Ayumu or [Chase] after the other four?: ")
        if Fight5H == "Help":
          print("Ayumu: Thanks now lets beat him")
          print("Ayumu: He's coming!")
          Fight5HA = input("[Charge], [Dodge], or [Attack]?: ")
          if Fight5HA == "Charge":
            print("You immobilized him but you took some heavy damage \nYour HP 5,000/12,500")
            print("He stuns everyone around you including you and kills every one including you")
          elif Fight5HA == "Dodge":
            print("He stuns everyone around you including you and kills everyone")
            print("You continue to attack him and you exhaust yourself and Bertrand took the chance to kill you")
          elif Fight5HA == "Attack":
            print("Your attack was ineffective")
            print("He stuns everyone around you including you and kills every one including you")
        elif Fight5H == "Chase":
          print("Ayumu: I promise I will catchup to you, now go")

        else:
          print("You spelt it wrong")
        if Fight5H == "Chase":
          break

      print("")
      print("\nAs you continue to head further into the strange place you soon mEeT...")

      print("\033[31m", "\n???: Hello there, welcome to my labyrinth now...", "\033[4;31m", "FIND ME", "\033[0m")

      print("")
      print("")
      print("")
      print("\033[3;31m", "        Chapter 5", "\033[0m")
      print(" --------------------------")
      print("      The", "\033[4;31m", "Labyrinth", "\033[0m")
      print("")
      print("")
      print("")

      print("???: Hello, do you remember me?")
      print("World: I'm the world and I will try my best to guide you")
      while True:
        ReadyM = input ("World: Are you [Ready]?: ")
        if ReadyM == "Ready":
          print("World: Let's go...")
        else:
          print("I don't seem to understand, try spelling it correctly.")
        if ReadyM == "Ready":
          break

      # Define the maze as a 2D list
      maze = [
          ['#', '#', '#', '#', '#', '#', '#', '#', 'X', '#'],
          ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
          ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
      ]

      # Find the starting position of the player
      def find_start_position(maze):
          for i in range(len(maze)):
              for j in range(len(maze[i])):
                  if maze[i][j] == ' ':
                      return i, j

      # Move the player within the maze
      def move_player(maze, direction, position):
          x, y = position

          if direction == 'up':
              new_x, new_y = x - 1, y
          elif direction == 'down':
              new_x, new_y = x + 1, y
          elif direction == 'left':
              new_x, new_y = x, y - 1
          elif direction == 'right':
              new_x, new_y = x, y + 1
          else:
              return False

          if maze[new_x][new_y] == ' ':
              maze[new_x][new_y] = 'P'
              maze[x][y] = ' '
              return new_x, new_y
          elif maze[new_x][new_y] == '#':
              return False

      # Main game loop
      def play_game(maze):
          position = find_start_position(maze)

          while True:
              # Display the maze
              for row in maze:
                  print(' '.join(row))

              # Get the player's move
              direction = input('Enter your move "Hint: Type "right" to begin the maze" (up/down/left/right): ')

              # Move the player
              new_position = move_player(maze, direction, position)

              if new_position:
                  position = new_position
              else:
                  print('Invalid move. Try again.')

              # Check if the player reached the goal
              if position == (1, 8):
                  print('\nWorld: That is only the first one...let us continue further')
                  break

      # Start the game
      play_game(maze)

      # Define the maze as a 2D list
      maze = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
          ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
          ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#'],
          ['#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
          ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
          ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
          ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'X', '#'],
      ]

      # Find the starting position of the player
      def find_start_position(maze):
          for i in range(len(maze)):
              for j in range(len(maze[i])):
                  if maze[i][j] == ' ':
                      return i, j

      # Move the player within the maze
      def move_player(maze, direction, position):
          x, y = position

          if direction == 'up':
              new_x, new_y = x - 1, y
          elif direction == 'down':
              new_x, new_y = x + 1, y
          elif direction == 'left':
              new_x, new_y = x, y - 1
          elif direction == 'right':
              new_x, new_y = x, y + 1
          else:
              return False

          if maze[new_x][new_y] == ' ':
              maze[new_x][new_y] = 'P'
              maze[x][y] = ' '
              return new_x, new_y
          elif maze[new_x][new_y] == '#':
              return False

      # Main game loop
      def play_game(maze):
          position = find_start_position(maze)

          while True:
              # Display the maze
              for row in maze:
                  print(' '.join(row))

              # Get the player's move
              direction = input('Enter your move "Hint: Type "right" to begin the maze" (up/left/down/right): ')

              # Move the player
              new_position = move_player(maze, direction, position)

              if new_position:
                  position = new_position
              else:
                  print('Invalid move. Try again.')

              # Check if the player reached the goal
              if position == (15, 28):
                  print('World: You escaped, well done! But we are not done yet...Continur further')
                  break

      # Start the game
      play_game(maze)



      # Define the maze as a 2D list
      maze = [
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
          ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
          ['#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', 'X'],
          ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#'],
          ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
      ]

      # Find the starting position of the player
      def find_start_position(maze):
          for i in range(len(maze)):
              for j in range(len(maze[i])):
                  if maze[i][j] == ' ':
                      return i, j

      # Move the player within the maze
      def move_player(maze, direction, position):
          x, y = position

          if direction == 'up':
              new_x, new_y = x - 1, y
          elif direction == 'down':
              new_x, new_y = x + 1, y
          elif direction == 'left':
              new_x, new_y = x, y - 1
          elif direction == 'right':
              new_x, new_y = x, y + 1
          else:
              return False

          if maze[new_x][new_y] == ' ':
              maze[new_x][new_y] = 'P'
              maze[x][y] = ' '
              return new_x, new_y
          elif maze[new_x][new_y] == '#':
              return False

      # Main game loop
      def play_game(maze):
          position = find_start_position(maze)

          while True:
              # Display the maze
              for row in maze:
                  print(' '.join(row))

              # Get the player's move
              direction = input('Enter your move "Hint: Type "right" to begin the maze" (up/left/down/right): ')

              # Move the player
              new_position = move_player(maze, direction, position)

              if new_position:
                  position = new_position
              else:
                  print('Invalid move. Try again.')

              # Check if the player reached the goal
              if position == (11, 27):
                  print('World: You escaped, well done!')
                  break

      # Start the game
      play_game(maze)

      print("\nAs you continue to head head further in the labryinth, you find a chasm filled with malice")

      print("\033[31m")
      # Define the maze as a 2D list
      maze = [
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '-', 'X', '-', '|', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', ' ', ' ', ' ', '-', '-', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
  
      ]

      # Find the starting position of the player
      def find_start_position(maze):
          for i in range(len(maze)):
              for j in range(len(maze[i])):
                  if maze[i][j] == ' ':
                      return i, j

      # Move the player within the maze
      def move_player(maze, direction, position):
          x, y = position

          if direction == 'up':
              new_x, new_y = x - 1, y
          elif direction == 'down':
              new_x, new_y = x + 1, y
          elif direction == 'left':
              new_x, new_y = x, y - 1
          elif direction == 'right':
              new_x, new_y = x, y + 1
          else:
              return False
      
          if maze[new_x][new_y] == ' ':
              maze[new_x][new_y] = 'P'
              maze[x][y] = ' '
              return new_x, new_y
          elif maze[new_x][new_y] == '#':
              return False

      # Main game loop
      def play_game(maze):
          position = find_start_position(maze)
      
          while True:
              # Display the maze
              for row in maze:
                  print(' '.join(row))
      
              # Get the player's move
              direction = input('Enter your move "Hint: Type "right" to begin the maze" (up/left/down/right): ')
      
              # Move the player
              new_position = move_player(maze, direction, position)
      
              if new_position:
                  position = new_position
              else:
                  print('Invalid move. Try again.')
      
              # Check if the player reached the goal
              if position == (9, 10):
                  print("\033[0m")
                  print('World: Here we are. You on your own from here on out...Good Luck')
                  break
      
      # Start the game
      play_game(maze)
      
      while True:
        ChasmFall = input ("[Ready] to jump in?: ")
        if ChasmFall == "Ready":
          print("You take a leap of faith into the", "\033[31m", "Chasm", "\033[0m")
        else:
          print("You spelt it wrong")
        if ChasmFall == "Ready":
          break
      
      print("")
      print("")
      print("")
      print("\033[3;31m", "        Chapter 6", "\033[0m")
      print(" --------------------------")
      print("        The", "\033[7;31m", "Chasm", "\033[0m")
      print("")
      print("")
      print("")
      print("Don't scroll during animations...")
      import time
      
      # Define the frames of the falling animation
      frames = [
          "             |  ",
          "           |     ",
          "           |     ",
          "             |",
          "             |",
          "             ",
          "           \\ /",
          "           \\|/|",
          "            O |",
          "             ",
          "             |",
          "             |  ",
          "           |     ",
          "           |     ",
          "             |",
          "             |",
          "             ",
          "           \\ /",
          "           \\|/|",
          "            O |",
          "             ",
          "             |",
          "             |  ",
          "           |     ",
          "           |     ",
          "             |",
          "             |",
          "             ",
          "           \\ /",
          "           \\|/|",
          "            O |",
          "                 ",
      ]
      
      # Loop through the frames and print the animation
      for frame in frames:
          print(frame)
          time.sleep(0.5)  # Adjust the sleep time to control the speed of the animation
      
      import time
      
      # Define the frames of the explosion animation
      frames = [
          "   _.-^^---....,,--__       ",
          " _--                  --_   ",
          "<                        >)",
          " |                         |",
          "  \\._                   _./ ",
          "     ```--. . , ; .--'''    ",
          "           | |   |          ",
          "        .-=||  | |=-.       ",
          "________`-=#$%&%$#=-'_______",
      ]
      
      # Loop through the frames and print the animation
      for frame in frames:
          print(frame)
          time.sleep(0.5)  # Adjust the sleep time to control the speed of the animation
      
      print("You fell afce flt. You have reached the bottom of the bottomless", "\033[1;31m", "chasm", "\033[0m")
      print("\033[31m", "???: You have arrived, you are almost there, find my chamber", "\033[0m")

      print("\033[31m")
      # Define the maze as a 2D list
      maze = [
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
          ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', '#'],
          ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
          ['#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
          ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
          ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#'],
          ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
          ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
      ]
      
      # Find the starting position of the player
      def find_start_position(maze):
          for i in range(len(maze)):
              for j in range(len(maze[i])):
                  if maze[i][j] == ' ':
                      return i, j
      
      # Move the player within the maze
      def move_player(maze, direction, position):
          x, y = position
      
          if direction == 'up':
              new_x, new_y = x - 1, y
          elif direction == 'down':
              new_x, new_y = x + 1, y
          elif direction == 'left':
              new_x, new_y = x, y - 1
          elif direction == 'right':
              new_x, new_y = x, y + 1
          else:
              return False
      
          if maze[new_x][new_y] == ' ':
              maze[new_x][new_y] = 'P'
              maze[x][y] = ' '
              return new_x, new_y
          elif maze[new_x][new_y] == '#':
              return False
      
      # Main game loop
      def play_game(maze):
          position = find_start_position(maze)
      
          while True:
              # Display the maze
              for row in maze:
                  print(' '.join(row))
      
              # Get the player's move
              direction = input('Enter your move "Hint: Type "right" to begin the maze" (up/left/down/right): ')
      
              # Move the player
              new_position = move_player(maze, direction, position)
      
              if new_position:
                  position = new_position
              else:
                  print('Invalid move. Try again.')
      
              # Check if the player reached the goal
              if position == (11, 28):
                  print('\nThere is a sudden eerie silence')
                  break
      
      # Start the game
      play_game(maze)

      print("\033[m")
      
      print("\033[31m", "???: You made it, but first...", "\033[1;31m", "Entertain Me", "\033[0m")
      print("\033[31m", "???: You must fight the", "\033[1;31", "Hero's of Ever Moon Kingdom", "\033[0m")
      
      import time
      
      # Define the frames of the explosion animation
      frames = [
          "",
          "\033[3;31m", "       Chapter 7", "\033[0m",
          "-------------------------",
          "\033[1;31m", "         Hero's", "\033[0m",
          "",
      ]
      
      # Loop through the frames and print the animation
      for frame in frames:
          print(frame)
          time.sleep(0.5)  # Adjust the sleep time to control the speed of the animation
      
      print("\033[31m", "???: The first person you will fight is Yōsei Genji")
      print("\n???: Ready?", "\033[1;31m", "FIGHT", "\033[0m")
      
      
      
      
      
      
      
      print("\nRound 1")
      import random
      
      # Define the player and enemy stats
      player = {
          "name": Name,
          "max_health": 26000,
          "health": 25000,
          "attack": 12500,
          "defense": 12500
      }
      
      enemy = {
          "name": "Yōsei Genji",
          "health": 26500,
          "attack": 6000,
          "defense": 15000
      }
      
      # Game loop
      while True:
          # Print player and enemy stats
          print(f"{player['name']} Health: {player['health']}")
          print(f"{enemy['name']} Health: {enemy['health']}")
          print("-----------------------------")
      
          # Player's turn
          print("Player's turn:")
          choice = input("\nChoose an action (Attack/Block/Restart): ").lower()
      
          if choice == "attack":
              player_attack = random.randint(1, player["attack"])
              enemy_defense = random.randint(1, enemy["defense"])
              damage_dealt = player_attack - enemy_defense
              if damage_dealt > 0:
                  enemy["health"] -= damage_dealt
                  print(f"\nYou dealt {damage_dealt} damage to the {enemy['name']}!")
              else:
                  print("\nYour attack missed!")
          elif choice == "block":
              player_defense = random.randint(1, player["defense"])
              print(f"\nYou blocked the {enemy['name']}'s attack!")
          elif choice == "restart":
              # Reset player and enemy health
              player["health"] = player["max_health"]
              enemy["health"] = 265000
              print("\nGame restarted.")
              continue
          else:
              print("\nInvalid choice. Try again.")
              continue
      
          # Check if the enemy is defeated
          if enemy["health"] <= 0:
              print(f"\nYou defeated the {enemy['name']}!")
              break
      
          # Enemy's turn
          print("\nEnemy's turn:")
          enemy_attack = random.randint(1, enemy["attack"])
          player_defense = random.randint(1, player["defense"])
          damage_taken = enemy_attack - player_defense
          if damage_taken > 0:
              player["health"] -= damage_taken
              print(f"\nThe {enemy['name']} dealt {damage_taken} damage to you!")
          else:
              print(f"\nThe {enemy['name']}'s attack missed!")
      
          # Check if the player is defeated
          if player["health"] <= 0:
              print("\nYou were defeated!")
              choice = input("\nDo you want to restart? (Yes): ").lower()
              if choice == "yes":
                  # Reset player and enemy health
                  player["health"] = player["max_health"]
                  enemy["health"] = 265000
                  print("\nGame restarted.")
                  continue
              else:
                  print("You spelt ir wrong")
          
      
      # Game over
      print("\033[34m", "\n  ! Notice:   ", "\033[0m") 
      print(" ------------")
      print("\033[33m", " LEVEL",  "\033[0m", "UP!") 

      
      print("\033[31m", "???: Well done, Next!", "\033[0m")     
      
      
      
      
      
      
      
      print("\nRound 2")
      import random
      
      # Define the player and enemy stats
      player = {
          "name": Name,
          "max_health": 27000,
          "health": 26000,
          "attack": 13000,
          "defense": 13000
      }
      
      enemy = {
          "name": "Kenji Gushiken",
          "health": 30000,
          "attack": 8000,
          "defense": 5000
      }
      
      # Game loop
      while True:
          # Print player and enemy stats
          print(f"{player['name']} Health: {player['health']}")
          print(f"{enemy['name']} Health: {enemy['health']}")
          print("-----------------------------")
      
          # Player's turn
          print("Player's turn:")
          choice = input("\nChoose an action (Attack/Block/Restart): ").lower()
      
          if choice == "attack":
              player_attack = random.randint(1, player["attack"])
              enemy_defense = random.randint(1, enemy["defense"])
              damage_dealt = player_attack - enemy_defense
              if damage_dealt > 0:
                  enemy["health"] -= damage_dealt
                  print(f"\nYou dealt {damage_dealt} damage to the {enemy['name']}!")
              else:
                  print("\nYour attack missed!")
          elif choice == "block":
              player_defense = random.randint(1, player["defense"])
              print(f"\nYou blocked the {enemy['name']}'s attack!")
          elif choice == "restart":
              # Reset player and enemy health
              player["health"] = player["max_health"]
              enemy["health"] = 30000
              print("\nGame restarted.")
              continue
          else:
              print("\nInvalid choice. Try again.")
              continue
      
          # Check if the enemy is defeated
          if enemy["health"] <= 0:
              print(f"\nYou defeated the {enemy['name']}!")
              break
      
          # Enemy's turn
          print("\nEnemy's turn:")
          enemy_attack = random.randint(1, enemy["attack"])
          player_defense = random.randint(1, player["defense"])
          damage_taken = enemy_attack - player_defense
          if damage_taken > 0:
              player["health"] -= damage_taken
              print(f"\nThe {enemy['name']} dealt {damage_taken} damage to you!")
          else:
              print(f"\nThe {enemy['name']}'s attack missed!")
      
          # Check if the player is defeated
          if player["health"] <= 0:
              print("\nYou were defeated!")
              choice = input("\nDo you want to restart? (Yes): ").lower()
              if choice == "yes":
                  # Reset player and enemy health
                  player["health"] = player["max_health"]
                  enemy["health"] = 30000
                  print("\nGame restarted.")
                  continue
              else:
                  print("You spelt ir wrong")
      
      # Game over
      print("\033[34m", "\n  ! Notice:   ", "\033[0m") 
      print(" ------------")
      print("\033[33m", " LEVEL",  "\033[0m", "UP!") 
      
      print("\033[31m", "???: Your pretty strong, Next!", "\033[0m")
      
      
      
      
      
      
      
      print("\nRound 3")
      import random
      
      # Define the player and enemy stats
      player = {
          "name": Name,
          "max_health": 28000,
          "health": 27000,
          "attack": 13500,
          "defense": 13500
      }
      
      enemy = {
          "name": "Kiera Kanamori",
          "health": 36000,
          "attack": 10000,
          "defense": 9000
      }
      
      # Game loop
      while True:
          # Print player and enemy stats
          print(f"{player['name']} Health: {player['health']}")
          print(f"{enemy['name']} Health: {enemy['health']}")
          print("-----------------------------")
      
          # Player's turn
          print("Player's turn:")
          choice = input("\nChoose an action (Attack/Block/Restart): ").lower()
      
          if choice == "attack":
              player_attack = random.randint(1, player["attack"])
              enemy_defense = random.randint(1, enemy["defense"])
              damage_dealt = player_attack - enemy_defense
              if damage_dealt > 0:
                  enemy["health"] -= damage_dealt
                  print(f"\nYou dealt {damage_dealt} damage to the {enemy['name']}!")
              else:
                  print("\nYour attack missed!")
          elif choice == "block":
              player_defense = random.randint(1, player["defense"])
              print(f"\nYou blocked the {enemy['name']}'s attack!")
          elif choice == "restart":
              # Reset player and enemy health
              player["health"] = player["max_health"]
              enemy["health"] = 36000
              print("\nGame restarted.")
              continue
          else:
              print("\nInvalid choice. Try again.")
              continue
      
          # Check if the enemy is defeated
          if enemy["health"] <= 0:
              print(f"\nYou defeated the {enemy['name']}!")
              break
      
          # Enemy's turn
          print("\nEnemy's turn:")
          enemy_attack = random.randint(1, enemy["attack"])
          player_defense = random.randint(1, player["defense"])
          damage_taken = enemy_attack - player_defense
          if damage_taken > 0:
              player["health"] -= damage_taken
              print(f"\nThe {enemy['name']} dealt {damage_taken} damage to you!")
          else:
              print(f"\nThe {enemy['name']}'s attack missed!")
      
          # Check if the player is defeated
          if player["health"] <= 0:
              print("\nYou were defeated!")
              choice = input("\nDo you want to restart? (Yes): ").lower()
              if choice == "yes":
                  # Reset player and enemy health
                  player["health"] = player["max_health"]
                  enemy["health"] = 36000
                  print("\nGame restarted.")
                  continue
              else:
                  print("You spelt ir wrong")
      
      # Game over
      print("\033[34m", "\n  ! Notice:   ", "\033[0m") 
      print(" ------------")
      print("\033[33m", " LEVEL",  "\033[0m", "UP!") 
      
      print("\033[31m", "???: Interesting...Next!", "\033[0m")
      
      
      
      
      
      
      print("\nRound 4")
      import random
      
      # Define the player and enemy stats
      player = {
          "name": Name,
          "max_health": 29000,
          "health": 28000,
          "attack": 14000,
          "defense": 14000
      }
      
      enemy = {
          "name": "Homura Akuma",
          "health": 70000,
          "attack": 13000,
          "defense":9500
      }
      
      # Game loop
      while True:
          # Print player and enemy stats
          print(f"{player['name']} Health: {player['health']}")
          print(f"{enemy['name']} Health: {enemy['health']}")
          print("-----------------------------")
      
          # Player's turn
          print("Player's turn:")
          choice = input("\nChoose an action (Attack/Block/Restart): ").lower()
      
          if choice == "attack":
              player_attack = random.randint(1, player["attack"])
              enemy_defense = random.randint(1, enemy["defense"])
              damage_dealt = player_attack - enemy_defense
              if damage_dealt > 0:
                  enemy["health"] -= damage_dealt
                  print(f"\nYou dealt {damage_dealt} damage to the {enemy['name']}!")
              else:
                  print("\nYour attack missed!")
          elif choice == "block":
              player_defense = random.randint(1, player["defense"])
              print(f"\nYou blocked the {enemy['name']}'s attack!")
          elif choice == "restart":
              # Reset player and enemy health
              player["health"] = player["max_health"]
              enemy["health"] = 78000
              print("\nGame restarted.")
              continue
          else:
              print("\nInvalid choice. Try again.")
              continue
      
          # Check if the enemy is defeated
          if enemy["health"] <= 0:
              print(f"\nYou defeated the {enemy['name']}!")
              break
      
          # Enemy's turn
          print("Enemy's turn:")
          enemy_attack = random.randint(1, enemy["attack"])
          player_defense = random.randint(1, player["defense"])
          damage_taken = enemy_attack - player_defense
          if damage_taken > 0:
              player["health"] -= damage_taken
              print(f"The {enemy['name']} dealt {damage_taken} damage to you!")
          else:
              print(f"The {enemy['name']}'s attack missed!")
      
          # Check if the player is defeated
          if player["health"] <= 0:
              print("You were defeated!")
              choice = input("\nDo you want to restart? (Yes): ").lower()
              if choice == "yes":
                  # Reset player and enemy health
                  player["health"] = player["max_health"]
                  enemy["health"] = 78000
                  print("\nGame restarted.")
                  continue
              else:
                  print("You spelt ir wrong")
      
      # Game over
      print("\033[34m", "\n  ! Notice:   ", "\033[0m") 
      print(" ------------")
      print("\033[33m", " LEVEL",  "\033[0m", "UP!") 
      
      print("\033[31m", "???: You beat my strongest pawwn!? You are quite fascinating", "\033[0m")
      print("\033[31m", "???: Your are quite strong...Now, Fight me", "\033[0m")
      
      
      
      
      import random
      
      # Define the player and enemy stats
      player = {
          "name": Name,
          "health": 30000,
          "attack": 15500,
          "defense": 15500
      }
      
      enemy = {
          "name": "???",
          "health": 99999,
          "attack": 99999,
          "defense": 99999
      }
      
      # Game loop
      while True:
          # Print player and enemy stats
          print(f"{player['name']} Health: {player['health']}")
          print(f"{enemy['name']} Health: {enemy['health']}")
          print("-----------------------------")
      
          # Player's turn
          print("Player's turn:")
          choice = input("Choose an action (Attack/Block): ").lower()
      
          if choice == "attack":
              player_attack = random.randint(1, player["attack"])
              enemy_defense = random.randint(1, enemy["defense"])
              damage_dealt = player_attack - enemy_defense
              if damage_dealt > 0:
                  enemy["health"] -= damage_dealt
                  print(f"You dealt {damage_dealt} damage to the {enemy['name']}!")
              else:
                  print("Your attack missed!")
          elif choice == "block":
              player_defense = random.randint(1, player["defense"])
              print(f"You blocked the {enemy['name']}'s attack!")
          else:
              print("Invalid choice. Try again.")
              continue
      
          # Check if the enemy is defeated
          if enemy["health"] <= 0:
              print(f"You defeated the {enemy['name']}!")
              break
      
          # Enemy's turn
          print("Enemy's turn:")
          enemy_attack = random.randint(1, enemy["attack"])
          player_defense = random.randint(1, player["defense"])
          damage_taken = enemy_attack - player_defense
          if damage_taken > 0:
              player["health"] -= damage_taken
              print(f"The {enemy['name']} dealt {damage_taken} damage to you!")
          else:
              print(f"The {enemy['name']}'s attack missed!")
      
          # Check if the player is defeated
          if player["health"] <= 0:
              print("You were defeated!")
              break
      
      
      # Define the frames of the explosion animation
      frames = [
          "\033[31m", "???: Hahah!..",
          " \033[31m", "???: Hahahahhahaa!..",
          "Moros: My name is Moro's, the Demigod of destruction",
      ]
      
      # Loop through the frames and print the animation
      for frame in frames:
          print(frame)
          time.sleep(0.5)
      # Adjust the sleep time to control the speed of the animation
      print("I knew you couldn't defeat me", "\033[0m")
      
      print("The roof breaks open...")
      print("Ayumu: Sorry I took so long. Get back up on your feet! We'er not out of this yet, let's finish him off")
      
      
      
      
      
      
      
      
      print("\033[31m")
      import random
      
      # Define player and enemy stats
      players = [
          {
              "name": Name,
              "max_health": 31000,
              "health": 30000,
              "attack": 15500,
              "defense": 15500
          },
          {
              "name": "Ayumu",
              "max_health": 18000,
              "health": 17000,
              "attack": 12500,
              "defense": 10000
          }
      ]
      
      enemy = {
          "name": "Moro",
          "health": 150000,
          "attack": 15000,
          "defense": 10000
      }
      
      # Game loop
      while True:
          # Print player and enemy stats
          for player in players:
              print(f"{player['name']} Health: {player['health']}")
          print(f"{enemy['name']} Health: {enemy['health']}")
          print("-----------------------------")
      
          # Players' turn
          for player in players:
              print(f"{player['name']}'s turn:")
              choice = input("Choose an action (Attack/Block/Restart): ").lower()
      
              if choice == "attack":
                  player_attack = random.randint(1, player["attack"])
                  enemy_defense = random.randint(1, enemy["defense"])
                  damage_dealt = player_attack - enemy_defense
                  if damage_dealt > 0:
                      enemy["health"] -= damage_dealt
                      print(f"{player['name']} dealt {damage_dealt} damage to the {enemy['name']}!")
                  else:
                      print("The attack missed!")
              elif choice == "block":
                  player_defense = random.randint(1, player["defense"])
                  print(f"{player['name']} blocked the {enemy['name']}'s attack!")
              elif choice == "restart":
                  # Reset player and enemy health
                  for player in players:
                      player["health"] = player["max_health"]
                  enemy["health"] = 200
                  print("Game restarted.")
                  continue
              else:
                  print("Invalid choice. Try again.")
                  continue
      
              # Check if the enemy is defeated
              if enemy["health"] <= 0:
                  print(f"You defeated the {enemy['name']}!")
                  break
      
          # Enemy's turn
          if enemy["health"] > 0:
              print("Enemy's turn:")
              enemy_attack = random.randint(1, enemy["attack"])
              player_defense = sum(random.randint(1, player["defense"]) for player in players)
              damage_taken = enemy_attack - player_defense
              if damage_taken > 0:
                  for player in players:
                      player["health"] -= damage_taken
                  print(f"The {enemy['name']} dealt {damage_taken} damage to the players!")
              else:
                  print(f"The {enemy['name']}'s attack missed!")
      
          # Check if all players are defeated
          if all(player["health"] <= 0 for player in players):
              print("All players were defeated!")
              choice = input("Do you want to restart? (Yes/No): ").lower()
              if choice == "yes":
                  # Reset player and enemy health
                  for player in players:
                      player["health"] = player["max_health"]
                  enemy["health"] = 200
                  print("Game restarted.")
                  continue
              else:
                  break
      
          # Check if the enemy is defeated
          if enemy["health"] <= 0:
              print(f"You defeated the {enemy['name']}!")
              break
            
      print("\nAyumu: We finally freed the kingdom and the world from his clutches")
      print("You ask how was Ayumu was alive when his health declined during the battle")
      print("Ayumu: I made a deal with the devil and now I will stay alive but it creates a very high toll so this is the end for me.")
      print("*Ayumu takes a seat by a tree and drifts away to sleep. Forever*")
      print("")
      print("")
      print("\033[0m")
      print("You take a walk outside and you see everything slowly dissapearing and tunring into the beutiful lushful forest it once was")
      print("")
      print("World: You did well", Name,)
      print("World: Don't you think it time for you to rest and recover properly. Lemme see what I can do")

      
      while True:
        RestEND = input ("World: Would you like to [Rest] after you long battle and journey or go on [Another]?: ")
        if RestEND == "Rest":
          print("I see, you did work your butt off, I think you deserve it. drift away in your slumber and you will be call upon once again when calamity strikes again")
        elif RestEND == "Another":
          print("World: You're quite adventoures, let's see what other things you can do")
        else:
          print("/nWorld: I don't understand, maybe you spelt it wrong?")
        if RestEND == "Rest" or RestEND == "Another":
          break
      
      
      
      import time
      
      # Define the frames of the explosion animation
      frames = [
          " ~~-------------------------~~",
          "|                             |",
          "|                             |",
          "|                             |",
          "|                             |",
          "|        ~  The End  ~        |",
          "|          _________          |",
          "|           ||   ||           |",
          " ~~-------------------------~~",
      ]
      
      # Loop through the frames and print the animation
      for frame in frames:
          print(frame)
          time.sleep(0.5)  # Adjust the sleep time to control the speed of the animation
          
  else:
    print("Wrong input, try again.")