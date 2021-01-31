import smtplib

def send_email():
    with smtplib.SMTP() as smtp:
        smtp.connect()