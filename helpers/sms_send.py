import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

def send_email(send_email, code):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(from_addr=EMAIL, to_addrs=send_email, msg=f'Your Confirmation Code is {code}')
        print('Email sent!')
    except Exception as e:
        print(e)