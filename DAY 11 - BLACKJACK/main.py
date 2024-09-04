############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Code #####################
import random
from art import logo
from replit import clear
print(logo)

def sum_cards(cards):
  sum = 0
  for card in cards:
    sum += card
    if (cards[0] == 11 and cards[1] == 10) or (cards[0] == 10 and cards[1] == 11):
      return 0
    elif sum > 20 and card == 11:
      sum -= 10
  return sum

def deal_card(player_card, pc_card):
  player_card.append(random.choice(cards))
  player_card.append(random.choice(cards))
  pc_card.append(random.choice(cards))
  pc_card.append(random.choice(cards))

def deal_card_player(player_card):
  player_card.append(random.choice(cards))

user_cards = []
computer_cards = []
sum_user = 0
sum_pc = 0
deal_card(user_cards, computer_cards)
sum_user = sum_cards(user_cards)
sum_pc = sum_cards(computer_cards)
print(f"Your cards: {user_cards}, total is: {sum_user}.")
print(f"PC first card: {computer_cards[0]}")

loop = True
while loop:
  if sum_user == 0:
    print("You win with a Blackjack!")
    loop = False
  elif sum_pc == 0:
    print("PC win with a Blackjack!")
    loop = False
  elif sum_user > 21:
    print(f"Your cards: {user_cards}, total is: {sum_user}.")
    print(f"PC cards: {computer_cards}")
    print("You lose!")
    loop = False
  elif sum_pc > 21:
    print(f"Your cards: {user_cards}, total is: {sum_user}.")
    print(f"PC cards: {computer_cards}")
    print("PC lose!")
    loop = False
  else:
    ask = input("Do you want to draw another card? Type 'y' or 'n': ")
    if ask == "y":
      deal_card_player(user_cards)
      if sum_cards(computer_cards) < 18:
        deal_card_player(computer_cards)
      sum_user = sum_cards(user_cards)
      sum_pc = sum_cards(computer_cards)
      print(f"Your cards: {user_cards}, total is: {sum_user}.")
      print(f"PC cards: {computer_cards}")
    elif ask == "n":
      print(f"Your cards: {user_cards}, total is: {sum_user}.")
      print(f"PC cards: {computer_cards}")
      if sum_user > sum_pc:
        print("You win!")
        loop = False
      elif sum_user < sum_pc:
        print("You lose!")
        loop = False
      elif su_user == sum_pc:
        print("Draw!")
        loop = False

question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if question == "y":
  clear()
else:
  print("Goodbye!")

#-------------------------------------------#


