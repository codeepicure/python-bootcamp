from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.


print(logo)

user_bids = {}



no_more_users = False

while not no_more_users:    
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))
  
  user_bids[name]  = bid
  has_more_users = input("Are there other users? 'yes/no' ")
  no_more_users = True if has_more_users != 'yes' else False;clear()


winner = ""
win_bid = 0

for user in user_bids:
  if(user_bids[user] > win_bid):
    win_bid = user_bids[user]
    winner = user

print(f"The winner of the auction is {winner} with a winning bid of {win_bid}")