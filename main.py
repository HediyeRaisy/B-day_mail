import datetime as dt
import pandas
import smtplib
import random

my_email = "YOUR_GMAIL"
password = "THE_PASSWORD_OF_YOUR_EMAIL"
now = dt.datetime.today()
data = pandas.read_csv("birthdays.csv")
data = data.to_dict('records')
for i in range(0,len(data)):
    if data[i]['month'] == now.month and data[i]['day'] == now.day :
        print("month checked")
        num = random.randint(1,3)
        with open(f"./letter_templates/letter_{num}.txt" , mode="r") as file:
            letter = file.read()

        letter = letter.replace("[NAME]", data[i]["name"])
        print(letter)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=f"{data[i]['email']}",
                                msg=f"Subject:Happy Birthday! :)\n\n{letter}")

