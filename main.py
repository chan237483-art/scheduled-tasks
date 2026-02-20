import datetime,smtplib,random,pandas
import os

birthdays_list = pandas.read_csv('birthdays.csv')
print(birthdays_list)
today = datetime.datetime.now()
for i in range(len(birthdays_list)):
    if today.month == birthdays_list[i]['month']:
        if today.day == birthdays_list[i]['day']:
            num = random.randint(1,3)
            my_email = os.environ.get("MY_EMAIL")
            password = os.environ.get("MY_PASSWORD")
            with open(f"./letter_templates/letter_{num}.txt") as letter:
                content = letter.read()
                content = content.replace("[NAME]", birthdays_list[i]['name'])
            with smtplib.SMTP('smtp.gmail.com' ) as smtp:
                smtp.starttls()
                smtp.login(user=my_email, password=password)
                smtp.sendmail(from_addr=my_email,
                              to_addrs=birthdays_list[i]['email'],
                              msg=f"subject:Happy Brithday!!!\n\n{content}"
                              )
