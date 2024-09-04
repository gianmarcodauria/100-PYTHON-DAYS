import random
import art
import game_data
from replit import clear

print(art.logo)
first_new_data = game_data.data
a = random.randint(0, 49)
print(f"Compare: {first_new_data[a]['name']}, a {first_new_data[a]['description']}, from {first_new_data[a]['country']}")
print(art.vs)
sec_new_data = game_data.data
b = random.randint(0,49)
print(f"Against: {sec_new_data[b]['name']}, a {sec_new_data[b]['description']}, from {sec_new_data[b]['country']}")
choice = input("Who has more followers? Type 'A' or 'B': "" ").lower()


#Let's create a function to compare the followers of the two options after the first choice input: it will start a loop until one of the options loses.
#eache time the user guesses correctly, the score will increase by 1 and we roll again the options and we ask the user to guess again.
##By the end, the while loop shall break when the player make a bad choice##
def compare(firstdata, secdata, choice, a, b):
  score = 0
  game = True
  while game == True:
    if choice == "a":
      if firstdata[a]['follower_count'] > secdata[b]['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
        a = random.randint(0, 49)
        b = random.randint(0,49)
      elif firstdata[a]['follower_count'] < secdata[b]['follower_count']:
        print(f"Sorry, that's wrong. Final score: {score}")
        game = False
        break
    elif choice == "b":
      if secdata[b]['follower_count'] > firstdata[a]['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
        b = random.randint(0,49)
        a = random.randint(0, 49)
      elif secdata[b]['follower_count'] < firstdata[a]['follower_count']:
        print(f"Sorry, that's wrong. Final score: {score}")
        game = False
        break
    clear()
    print(art.logo)
    print(f"Compare: {firstdata[a]['name']}, a {firstdata[a]['description']}, from {firstdata[a]['country']}")
    print(art.vs)
    print(f"Against: {secdata[b]['name']}, a {secdata[b]['description']}, from {secdata[b]['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': "" ").lower()

compare(first_new_data, sec_new_data, choice, a, b)