import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from datetime import date
import requests

from dotenv import load_dotenv 
PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load the environment variables

current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

# Send email
def send_email(subject, receiver_email, name, days, quote_Author):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("VitalCareX.", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Assalam-O-Alaikum {name}!,
        I hope you are well.
        I just wanted to drop you a quick note to remind you that only {days} are left for our FYP report submission.
        Here's a quote to boost your motivation:-
        {quote_Author[0]}
        {quote_Author[1]}
        
        Mustafa Kamal
        """
    )

    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p> Assalam-O-Alaikum {name}!,</p>
        <p>I hope you are well.</p>
        <p>I just wanted to drop you a quick note to remind you that only <strong>{days}</strong> are left for our <strong>FYP FYP report submission.</strong></p>
        <p>Here's a quote to boost your motivation:-</p>
        <p><strong><em>{quote_Author[0]}<em></strong></p>
        <p><em>-{quote_Author[1]}<em></p>
        <br>
        <p>Mustafa Kamal</p>
      </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Calculate days left
def calc_days():
    today = date.today()
    presentation_date = date(2023, 11, 1)
    days = presentation_date - today
    return days.days

# Get quote and author from Ninja API
def get_quote():
    category = 'inspirational'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': '8i0KwvL2H9pglrKGBrzl+w==X6GMBXDkdHC0Mcj8'})
    if response.status_code == requests.codes.ok:
        data = response.json()
        return data[0]["quote"], data[0]["author"]

    
if __name__ == "__main__":
    send_email(
        subject=f"{calc_days()} days left!",
        name="Mustafa Kamal",
        receiver_email="mustfakmalik@gmail.com",
        days = calc_days(),
        quote_Author= get_quote()
    )