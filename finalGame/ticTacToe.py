class ticTacToe:

  def game (player1, player2):
    player1=player1
    player2=player2
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