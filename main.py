import os
import csv
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv
my_email=os.environ.get("MY_EMAIL")
my_password=os.environ.get("MY_PASSWORD")
# 2. Check if today matches a birthday in the birthdays.csv
now=dt.datetime.now()
today=now.date()
f=["letter_templates/letter_2.txt",
   "letter_templates/letter_3.txt",
   "letter_templates/letter_1.txt"]
with open("birthdays.csv","r") as file:
    reader=csv.DictReader(file)
    for rows in reader:
        if int(rows["day"])==today.day and int(rows["month"])==today.month:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            letter=random.choice(f)
            with open(letter,"r") as wishes:
                content=wishes.read()
            content=content.replace("[NAME]",rows["name"])
# 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com",587) as connection:

                connection.starttls()
                connection.login(user=my_email,password=my_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=rows["email"],
                                    msg=f"Subject:Happy Birthday \n\n{content}")
