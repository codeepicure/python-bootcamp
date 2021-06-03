import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
computer_choice = random.randint(0,len(choices)-1)
computer_image = choices[computer_choice]

user_choice = input("Choose one of the following:\n1. Rock\n2. Paper\n3. Scissors\n")
user_choice_int = int(user_choice)-1

print(f"You chose:\n{choices[user_choice_int]}")
print(f"Computer chose:\n{computer_image}")

if(computer_choice == user_choice_int):
  print("Draw, play again!")
elif((computer_choice == 0 and user_choice_int == 2) or (computer_choice == 2 and user_choice == 1) or (computer_choice == 1 and user_choice == 0)):
  print("Computer wins!")
else:
  print("You win!")
