import smtplib
import datetime as dt
import random

# Email address and password for the account from which the email will be sent
MAIL = ""
PASSWORD = ""

# Get the email address of the recipient from the user
user_email = input("Enter the email address you want to send to: ")

# Get the subject of the email from the user
user_subject = input("Enter your email subject here: ")

# Get the message to be sent from the user
user_message = input("Enter what you want to send: ")

# Get the current day of the week
now = dt.datetime.now()
weekday = now.weekday()

# If it is Wednesday, send an email with a random quote and the user's message
if weekday == 3:
    # Read the quotes from the quotes.txt file
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    try:
        # Connect to the email server and send the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MAIL, PASSWORD)
            connection.sendmail(
                from_addr=MAIL,
                to_addrs=f"{user_email}",
                msg=f"Subject: {user_subject}\n\n{user_message}\n\n{quote}",
            )

    except EOFError:
        # Print an error message if the connection to the email server could not be established
        print("Couldn't connect to smtp, please check your login details")
