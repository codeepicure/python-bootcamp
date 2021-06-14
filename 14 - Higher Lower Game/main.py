from art import logo
from art import vs
from game_data import data
from replit import clear
import random

game_is_in_play = True
user_score = 0

# print the logo
def print_logo():
  print(logo)

# get 2 random numbers that are not equal to each other
def get_two_items():
  item1 = 0
  item2 = 0;
  data_len = len(data)

  while item1 == item2:
    item1 = random.randint(0,data_len)
    item2 = random.randint(0,data_len)

  return item1, item2


# get the 2 questions and present them
def print_question(q1, q2):
  print(f"Compare A: {data[q1]['name']}, a {data[q1]['description']} from {data[q1]['country']}")
  print(vs)
  print(f"Compare B: {data[q2]['name']}, a {data[q2]['description']} from {data[q2]['country']}")




def play_game():
  global user_score
  print("Game in play")
  q1, q2 = get_two_items()
  user_answer = 0
  actual_answer = 0
  print_question(q1, q2)
  answer = input("Who has more followers? A or B: ")
  if(answer == 'A'):
    user_answer = q1
  else:
    user_answer = q2

  if(data[q1]['follower_count'] > data[q2]['follower_count']):
    actual_answer = q1
  else:
    actual_answer = q2
  
  if(user_answer == actual_answer):
    user_score += 1
    clear()
    print(f"You score is currently {user_score}.")
    play_game()
  else:
    print(f"Sorry, that's wrong. Final score: {user_score}.")
    return
  

while game_is_in_play:
  clear()
  print_logo()
  play_game()
  play_again = input("Would you like to play again? Type 'yes' or 'no': ")
  if(play_again.lower() != 'yes'):
    game_is_in_play = False
  user_score = 0
