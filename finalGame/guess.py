class guess:

  def game():
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