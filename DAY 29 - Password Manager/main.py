from tkinter import *  # all classes
from tkinter import messagebox
import random
import pyperclip

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

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_entry.get()
    email = mail_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops!", message="Please fill the blank fields.")
    else:
    # messagebox return a boolean value:
        is_ok = messagebox.askokcancel(title=website, message=f"Website: {website} \n" 
                                                              f"Email: {email} \n"
                                                              f"Password: {password}\n Is it okay to save?")
        if is_ok:
            data = (f"{website} | {email} | {password}\n")
            data_text = open("data.txt", "a")
            data_text.write(data)
            data_text.close()
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

web_entry = Entry(width=36)
web_entry.grid(column=1, row=1, columnspan=2)
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






window.mainloop()