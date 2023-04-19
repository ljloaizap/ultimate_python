import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient


email = os.environ.get('SENDGRID_EMAIL')

message = Mail(
    from_email=email,
    to_emails=email,
    subject='Test email with Sendgrid',
    html_content='<b>Ultimate Python</b> course'
)

try:
    api_key = os.environ.get('SENDGRID_API_KEY')
    sg = SendGridAPIClient(api_key)
    response = sg.send(message)
    print(
        response.status_code,
        response.body,
        response.headers
    )
except Exception as ex:
    print(ex)
