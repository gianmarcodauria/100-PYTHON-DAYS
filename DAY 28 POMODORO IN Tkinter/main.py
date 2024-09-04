
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
fg=GREEN
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work_sec = WORK_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60
after_cancel_timer = " "

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(after_cancel_timer)  # cancel the normal after BUT it needs a name variable
    canvas.itemconfig(timer_canva, text="00:00")
    timer_text.config(text="Timer  ⏱️", fg=GREEN)
    check_mark.config(text=" ")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print(reps)
    if reps % 8 == 0:  # no remainder? long break then
        countdown(long_break_sec)
        timer_text.config(text="Break  ☕", fg=RED)
    elif reps % 2 == 0:  # is it even? short break then
        countdown(short_break_sec)
        timer_text.config(text="Break  ☕", fg=PINK)
    else:
        countdown(work_sec)
        timer_text.config(text="Work 🧑🏻‍💻", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    # math.floor returns the largest whole number that is less than or equal to x
    # if x = 4.8, it returns 4
    count_min = math.floor(count / 60) # for the number of minutes
    count_sec = count % 60  # in order to get the seconds as remainders
    if count_sec < 10:  # python's dynamic typing here, that's pretty unique; from an integer to a string
                       # < 10 because that is when it's going to be one digit(one single 0), and
        count_sec = f"0{count_sec}"
                        # that is when we manually add a 0 digit using an fstring after the first 0
    # to change a text for a title label we would just:
    # title_label.config(text=) BUT THAT'S NOT HOW IT WORKS FOR A CANVAS!
    # for a canvas, it needs a particular item (variable which contains the created text here)
    canvas.itemconfig(timer_canva, text=f"{count_min}:{count_sec}")
    if count > 0:
        global after_cancel_timer
        after_cancel_timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = " "
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("YOU LIKE POMODORO?")
window.config(padx=100, pady=50, bg=YELLOW)
# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# highlight thickness removes the square left behind by the bg
tomato_img = PhotoImage(file="tomato.png")  # canvas_image expects a variable with the img and not the image itself
canvas.create_image(100, 112, image=tomato_img)   # half of the w and h in order to center it
timer_canva = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Labels
timer_text = Label(text="Timer  ⏱️", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45))
timer_text.grid(column=1, row=0)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25))
check_mark.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", font=(FONT_NAME, 18), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 18), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


# the very existence of mainloop make it harder to other simple loops to simply work the way they should,
# so, keep an eye on this one
window.mainloop()
# in tkinter, we use the .after() method, instead of time.sleep() - see up above ^
