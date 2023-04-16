from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
import os


def send_email():

    # Message object
    message = MIMEMultipart()
    message["from"] = "Liliana J Loaiza P"
    message["to"] = "ljloaizap@gmail.com"
    message["subject"] = "This is a python test"

    # Content
    body_content = """
        Message body. Email with attached image. New cred2.
    """
    body = MIMEText(body_content)
    message.attach(body)

    # Image
    img_path = Path("native_modules_9/seeds.jpg")
    mime_image = MIMEImage(img_path.read_bytes())
    message.attach(mime_image)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        try:
            smtp.ehlo()  # This is to identify ourselves
            smtp.starttls()  # Send encrypted emails

            smtp.login(
                user=os.getenv('django_app_email_dir'),
                password=os.getenv('django_app_email_pwd')
            )
            smtp.send_message(message)
            print("Email has been sent.")
        except Exception as ex:
            print(f"Error when trying to send an email: {ex}")


def main():
    send_email()


main()
