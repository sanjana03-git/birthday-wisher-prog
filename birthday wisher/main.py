# import smtplib
# import datetime as dt
# import random

# MY_EMAIL = ""
# MY_PASSWORD = ""

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 1:
#     with open("birthday wisher/quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)

#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL, 
#             to_addrs=MY_EMAIL,
#             msg=f"Subject:Monday Motivation\n\n{quote}"
#         )





















# import smtplib

# my_email = ""
# password = ""

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="", 
#         msg="Subject:Hello\n\n This is the body of my email"
#         )


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# print(year)

