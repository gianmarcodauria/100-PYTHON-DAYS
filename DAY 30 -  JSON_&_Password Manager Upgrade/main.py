from tkinter import *  # all classes
from tkinter import messagebox
import random
import pyperclip
import json

# messagebox is not in tkinter classes;
# by effect, it is only a module

import math


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 9)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    # List comprehension's FOR LOOPS:
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    # random choice as many times as randomInt in range(nr__) es: x, 4 times
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_entry.insert(0, password)
    pyperclip.copy(password)  # a python project for faster copy/paste - already in the clipboard
    # as soon as you generate the password using the button

# --------------------------- FIND PASSWORD -------------------------------- #

def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"{website}\n"
                                                       f"your email is: {email}\n"
                                                       f"and the password is: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website}")
            #  data is the dict - website is the i/key we're checking
            #










# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_entry.get()
    email = mail_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops!", message="Please fill the blank fields.")
    else:
        try:  # TRY THE PIECE THAT WILL PROBABLY RETURN AN ERROR
            with open("data.json", "r") as data_file:
                data_load = json.load(data_file)  # converts data into a python dict
        except FileNotFoundError: # Reading new data  # EXCEPT IS USED WHEN YOU KNOW WHERE IT'S
            # GOING TO HAVE A BUG(KIND ETC) AND MAKE IT DO SOMETHING FOR IT
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else: # ELSE WHEN IT IN THE "NORMAL" STATE, WHERE IT IS WORKING AS PROMISED
            # HERE WE GIVE THE RIGHT ORDERS FOR THE NORMAL STATE
            data_load.update(new_data)
            # Saving updated new data
            with open("data.json", "w") as data_file:
                json.dump(data_load, data_file, indent=4)
        finally:  # ONCE EVERYTHING HAPPENED THE RIGHT WAY,
            # WE CLEAN THE CODE
            web_entry.delete(0, END)
            #mail_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------- ------------ UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(width=400, height=300)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
web_site_label = Label(text="Website:")
web_site_label.grid(column=0, row=1)

mail_user_label = Label(text="Email/Username:")
mail_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries

web_entry = Entry(width=20)
web_entry.grid(column=1, row=1,)
web_entry.focus()


mail_entry = Entry(width=36)
mail_entry.grid(column=1, row=2, columnspan=2)
mail_entry.insert(0, "gdauria@gmail.com")


pass_entry = Entry(width=20)
pass_entry.grid(column=1, row=3)


# Buttons

gen_pass = Button(text="Generate Password", width=12, command=password_generator)
gen_pass.grid(column=2, row=3)

add = Button(text="Add", width=34, command=save)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", width=10, command=find_password)
search.grid(column=2, row=1,)





window.mainloop()