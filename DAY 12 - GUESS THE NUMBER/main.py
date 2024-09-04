#Number Guessing Game Objectives:

# Include an ASCII art logo.
import random
import art
import clear
print(art.logo)
# Allow the player to submit a guess for a number between 1 and 100.
print(f"Welcome to the Number Guessing Game!\n")
difficulty = input(f"I'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()

#Let's define the easy mode#
############################

if difficulty == "easy":
  attempts = 11
  print(f"You have 10 attempts remaining to guess the number.\n")
  num = 0
  user_num = 0
  num = random.randint(1, 100)
  in_game = True
  while in_game:
    if attempts == 0:
      print(f"You've run out of guesses, you lose.")
      in_game = False
    attempts -= 1
    if attempts >= 1:
      user_num = int(input(f"Make a guess: "))
      if num > user_num:
        print(f"Too low.\nYou have {attempts - 1} attempts remaining to guess the number.\n")
      elif num < user_num:
        print(f"Too high.\nYou have {attempts - 1} attempts remaining to guess the number.\n")
      elif num == user_num:
        print(f"You got it! The answer was {num}.")
        in_game = False

#Let's define the hard mode#
############################
elif difficulty == "hard":
  attempts = 6
  print(f"You have 5 attempts remaining to guess the number.\n")
  num = 0
  user_num = 0
  num = random.randint(1, 100)
  in_game = True
  while in_game:
    if attempts == 0:
      print(f"You've run out of guesses, you lose.")
      in_game = False
    attempts -= 1
    if attempts >= 1:
      user_num = int(input(f"Make a guess: "))
      if num > user_num:
        print(f"Too low.\nYou have {attempts - 1} attempts remaining to guess the number.\n")
      elif num < user_num:
        print(f"Too high.\nYou have {attempts - 1} attempts remaining to guess the number.\n")
      elif num == user_num:
        print(f"You got it! The answer was {num}.")
        in_game = False


