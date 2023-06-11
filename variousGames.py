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
  
  if select == "3":
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
                  user_answer = input(question)

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

  if select == "5":
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


  if select == "7":
    print ("\n","\033[3;31m","    Story Games")
    print("~----------------------~")
    Cambion = print("1. ~Coming Soon~")
    print("\033[0m")
    
    Select2 = input ("\nWhat Story do you want to play?: ")
    
  else:
    print("Wrong input, try again.")