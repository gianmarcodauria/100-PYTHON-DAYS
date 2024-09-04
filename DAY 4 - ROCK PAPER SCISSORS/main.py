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

#Write your code below this line 👇

import random

my_num = (int(input("What do you choose? \n \n Type 0 for Rock, 1 for Paper or 2 for Scissors.\n \n")))
casual_num = random.randint(0, 2)
if my_num == 0:
    print(rock)
    if casual_num == 0:
        print(f" \nComputer chose: {rock} \n")
        print(" \n Draw")
    elif casual_num == 1:
        print(f" \nComputer chose: {paper} \n")
        print(" \n You Lose")
    elif casual_num == 2:
        print(f" \nComputer chose: {scissors} \n")
        print(" \nYou Win")
elif my_num == 1:
    print(paper)
    if casual_num == 1:
        print(f" \nComputer chose: {paper} \n")
        print(" \nDraw")
    elif casual_num == 0:
        print(f" \nComputer chose: {rock} \n")
        print(" \nYou win")
    elif casual_num == 2:
        print(f" \nComputer chose: {scissors} \n")
        print(" \nYou lose")
elif my_num == 2:
    print(scissors)
    if casual_num == 2:
        print(f" \n Computer chose: {scissors} \n")
        print(" \nDraw")
    elif casual_num == 0:
        print(f" \nComputer chose: {rock} \n")
        print(" \nYou lose")
    elif casual_num == 1:
        print(f" \nComputer chose: {paper} \n")
        print(" \nYou win")
