'''
INFORMATION:
    • This program helps us send birthday emails to our friends and relatives.
    • It uses python in-built module "smtplib" that is used to deal with emails.

'''

# Code For Automated Birthday Wisher
import smtplib, random, json
import datetime as dt
import pandas as pd

# FUNCTION TO MAKE A CONNECTION AND SEND THE EMAIL:-  ------------------------------------------------
# Sender's mail and password
MY_MAIL = ""       # [ Enter Your Email ]
MY_PASSWORD = ""   # [ Enter Your Password ]

def wishBirthday():
    # [ Enter SMTP Associated To Your Email ]
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        # Securing the connection by applying a tls (Transport Layer Security)
        connection.starttls()
        # Login in to the sender's mail account
        connection.login(user=MY_MAIL, password=MY_PASSWORD)
        # Send the mail
        connection.sendmail(
            from_addr=MY_MAIL, 
            to_addrs=bd_email, 
            msg=f"Subject:Happy Birthday!\n\nDear {bd_name}\n\n{bd_wish}"
        )


# CHECKING FOR ANY BIRTHDAYS TODAY:-  ---------------------------------------------------------------
now = dt.datetime.now()
month = now.month
day = now.day
all_bd = pd.read_csv("Database/File_BirthdayDates.csv")
all_bd = all_bd.to_dict("records")
for bd in all_bd:
    bd_name = bd['name']
    bd_email = bd['email']
    bd_month = int(bd['month'])
    bd_day = int(bd['day'])
    # Selecting a random birthday wish
    with open("Database/File_BirthdayWishes.json") as wishes:
        all_wishes = json.load(wishes)
        bd_wish = all_wishes[f"wish_{random.randint(1, len(all_wishes))}"]
    # Checking if today matches with any birthdays or not
    if bd_month == month and bd_day == day:
        wishBirthday()
