import smtplib
import datetime as dt
import random

my_email = "pythonmail366@gmail.com"
password = "nuql kpby amvt gqwm"  # Generated App Password on our provider


motivations = []


def send_motivation():
    global motivations
    message = random.choice(motivations)
    with smtplib.SMTP("smtp.gmail.com") as connection:  # insert our mail provider
        # using "with" will close off that connection automatically
        connection.starttls()   # secure our connection with the mail server
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="giallodauria@gmail.com",
                            msg=f"Subject:Un aforisma per te:\n\n{message}")
        print(message)


# ------------ list of quotations ------ #

with open("quotes.txt") as file_txt:
    for quotes in file_txt:
        motivations.append(quotes)

print(motivations)

#  ----------- datetime ----------- #

now = dt.datetime.now()
day_of_week = now.weekday()  # 0 IS MONDAY ETC
if day_of_week == 1:
    send_motivation()





