import os
import smtplib
import imghdr
from email.message import EmailMessage


def mail():
    EMAIL_ADDRESS = 'mail@mail.com'
    EMAIL_PASSWORD = '************'

    contacts = ['mail@mail.com', 'mail@mail.com']

    msg = EmailMessage()
    msg['Subject'] = 'Accident Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'mail@mail.com'

    msg.set_content('This is a plain text email')

    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:red;">!accident</h1>
        </body>
    </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)



