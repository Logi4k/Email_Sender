import smtplib


mail = ""
password = ""


# Ask user fo email they want to send email to
user_email = input("Enter the email address you want to send to: ")

# Ask user for subject details
user_subject = input("Enter your email subject here: ")

# Ask for what the user wants to send
user_message = input("Enter what you want to send: ")


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=mail, password=password)
    connection.sendmail(
        from_addr=mail,
        to_addrs=f"{user_email}",
        msg=f"Subject:{user_subject}\n\n{user_message}",
    )
