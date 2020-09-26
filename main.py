from decouple import config
import smtplib
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = config('GMAIL_ADDRESS')
EMAIL_PASS = config('GMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'This is a reminder'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS  # sending to myself
msg.set_content("Don't forget to order the movie tickets for tonight")

# adding attachments option
files_to_attach = ['bond.jpg']

for file in files_to_attach:
    with open(file, 'rb') as f:
        attachment_file = f.read()
        attachment_name = f.name
        attachment_type = imghdr.what(attachment_name)

    msg.add_attachment(attachment_file, maintype='image',
                       subtype=attachment_type,
                       filename=attachment_name)


def send_email():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
        smtp.send_message(msg)


if __name__ == "__main__":
    send_email()
