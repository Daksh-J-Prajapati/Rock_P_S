user_input = str(input("Type 'start' to begin the program: ")). strip()
if user_input == "start":
   print("Game started! ")


   import time
   print("Rock Paper Scissors")
   time.sleep (5)
   print(" Welcome, today we are going to initialize the game called Rock Paper Scissors ")
   time.sleep (5)


   #-------------------------------------------------------------------------------------------------


   import random


   # Function to handle restarting the game
   def restart_game():
       restart = input("Wanna try again? (Yes/No): ").strip().lower()
       if restart == "yes":
           import os
           import sys
           os.execv(sys.executable, ['python'] + sys.argv)  # Restart the program
       else:
           print("Thanks for playing! Goodbye!")


   # Random choice for the computer (1 = Rock, 2 = Paper, 3 = Scissors)
   element = random.randint(1, 3)


   # Get user's choice
   elementyou = input("Please choose which element you want to pick for this round.\n - Rock \n - Paper \n - Scissors: ").strip().capitalize()


   # Validate user's input
   if elementyou not in ["Rock", "Paper", "Scissors"]:
       print("Invalid input. Please choose Rock, Paper, or Scissors.")
   else:
       # Display computer's choice
       if element == 1:
           print("Computer chose Rock.")
       elif element == 2:
           print("Computer chose Paper.")
       else:
           print("Computer chose Scissors.")


       # Determine the outcome
       if elementyou == "Rock" and element == 3:
           print("You win!")
       elif elementyou == "Paper" and element == 1:
           print("You win!")
       elif elementyou == "Scissors" and element == 2:
           print("You win!")
       elif elementyou == "Rock" and element == 2:
           print("You lose!")
           restart_game()  # Restart the game
       elif elementyou == "Paper" and element == 3:
           print("You lose!")
           restart_game()
       elif elementyou == "Scissors" and element == 1:
           print("You lose!")
           restart_game()
       else:
           print("It's a tie!")
           restart_game()  # Restart the game


else:
   print("Invalid input: Please type 'start' to initialize the game.")
      




