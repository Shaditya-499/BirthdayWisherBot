import datetime as dt
import smtplib
import pandas as pd
import random

df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
month = now.month
date = now.day

my_mail = "shaditya499@gmail.com"
Password = "ibqa gvsd kehu zfvr "
with open(f"./letter_templates/letter_{random.randint(1,3)}.txt","r") as template:
    contents = template.read()

birthday_df = df[(df["month"]==month) & (df["day"]==date)]
birthday_df = birthday_df.set_index("name")
for index,row in birthday_df.iterrows():
    name = row.name
    birthdaymail = row.email
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=Password)
        contents = contents.replace("[NAME]", name)
        print(contents)
        connection.sendmail(from_addr=my_mail, to_addrs=birthdaymail,msg=f"Subject:Happy Birthday!! \n\n{contents}")