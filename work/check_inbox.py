import imaplib
import email
import os


# Hotmail configuration using imap protocol
def connect():
    host = 'imap.outlook.com'
    username = os.environ.get('hotmail_email')
    password = os.environ.get('hotmail_password')

    # connecting to mail server
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    return mail


def filter_sender(mail, sender):
    mail.select('inbox')
    # all uid will be returned as byte string, result = OK
    # and data = [b'5 20 21 25 27 29 31 33 35 37]
    result, data = mail.uid('search', None, 'ALL')

    # convert strings to a list
    inbox_item_list = data[0].split()
    for value in inbox_item_list:
        # fetching the email data in bytes
        result2, email_data = mail.uid('fetch', value, '(RFC822)')
        # converting byte email to raw_email data
        raw_email = email_data[0][1].decode('utf-8', errors='ignore')
        # converting raw_email string to email message
        email_message = email.message_from_string(raw_email)
        if email_message["From"] == sender:
            print(f'Email subject: {email_message["Subject"]}')

    # method available with email message
    # print(dir(email_message))
    # print(f'Email is From: {email_message["From"]}')
    # print(f'Email is send to: {email_message["To"]}')
    # print(f'Email subject is: {email_message["Subject"]}')


sender = 'vyapar123@outlook.com'
filter_sender(connect(), sender)

# get content type of email body
# print(email_message.get_payload())
# _, search_data = mail.search(None, "UNSEEN")
# # print(search_data)

# for num in search_data[0].split():
#     _, data = mail.fetch(num, '(RFC822)')
#     # print(data)
#     _, b = data[0]
#     # print(b)
#     email_message = email.message_from_bytes(b)
#     print(email_message)
# # print(search_data)
