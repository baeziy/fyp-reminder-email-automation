from send_emails import send_email  # local python module
from send_emails import calc_days
from send_emails import get_quote



def sending_emails():

    global email_counter  # Declare email_counter as global

    for i in range(len(names)):
        send_email(
            subject=f"{calc_days()} days left!",
            name=names[i],
            receiver_email=emails[i],
            days = calc_days(),
            quote_Author= get_quote()
        )
        email_counter+=1

    return f"Total Emails Sent: {email_counter}"

email_counter = 0

names = ["Fahad", "Sarmad"]
emails = ["mustfakmalik@gmail.com", "mustafakmalik2000@gmail.com"]

print( sending_emails())