class calculator:

  def game():
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