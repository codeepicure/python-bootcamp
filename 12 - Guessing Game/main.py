from arty import logo
import random
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print(logo)
playing_game = True
easy_game = 10
hard_game = 5
game_type = easy_game
user_guess = 0
try_again = "no"

while playing_game:
  print("Welcome to the Guessing Game")
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if(difficulty.lower() == 'easy'):
    game_type = easy_game
  elif(difficulty.lower() == 'hard'):
    game_type = hard_game
  else:
    print("No game type given, defaulting to hard")
    game_type = hard_game

  random_number = random.randint(1,100)
  attempts = game_type-1

  for i in range(0,game_type):
    user_guess = int(input("What's your guess? "))
    if(user_guess<random_number):
      print(f"You have {attempts} attempts remaining. You have to guess higher")
      attempts-=1
    elif(user_guess > random_number):
      print(f"You have {attempts} attempts remaining. You have to guess lower")
      attempts-=1
    else:
      break

  if(user_guess == random_number):
    print("You won! Congratulations")
  else:
    print("You ran out of luck!")
    
  try_again = input("Would you like to try again? Type 'yes' or 'no': ")
  if(try_again.lower() == 'no'):
    playing_game = False

  