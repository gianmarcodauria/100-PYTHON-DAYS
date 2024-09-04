#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like?"))
nr_numbers = int(input(f"How many numbers would you like?"))

password_letters = ""
password_symbols = ""
password_numbers = ""

for char in range (1, nr_letters + 1):
  chosen_letters = random.choice(letters)
  password_letters += chosen_letters
for char in range (1, nr_symbols + 1):
  chosen_symbols = random.choice(symbols)
  password_symbols += chosen_symbols
for char in range (1, nr_numbers + 1):
  chosen_numbers = random.choice(numbers)
  password_numbers += chosen_numbers

order = random.randint(0,2)
if order == 0:
  print(f"Your password is: {password_letters}{password_symbols}{password_numbers}")
elif order == 1:
  print(f"Your password is: {password_numbers}{password_letters}{password_symbols}")
else:
  print(f"Your password is: {password_symbols}{password_numbers}{password_letters}")

#Or... use random.shuffle() to shuffle the list
