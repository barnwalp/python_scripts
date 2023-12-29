import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def send_mail(text='Email body', subject='Hello world', from_email='vyapar123@outlook.com', to_emails=None):
    assert isinstance(to_emails, list)

    username = os.environ.get('hotmail_email')
    password = os.environ.get('hotmail_password')

    msg = MIMEMultipart('random')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    # txt_part = MIMEText(text, 'plain')
    # msg.attach(txt_part)

    html_part = MIMEText(text, 'html')
    msg.attach(html_part)

    msg_str = msg.as_string()
    server = smtplib.SMTP(host='smtp.outlook.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()


if __name__ == '__main__':
    body = "<h1>This is some random text for the mail test</h1><h3>some more text</h3>"
    sub = "check this out"
    send_mail(text=body, subject=sub, to_emails=['vyapar123@outlook.com'])
