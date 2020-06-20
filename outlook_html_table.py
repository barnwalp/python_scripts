from openpyxl import load_workbook
from exchangelib import Account, Message, HTMLBody, Credentials
from exchangelib import Configuration, DELEGATE
import os

# Getting the sensitive information from enviornment variables
outlook_user = os.environ.get('OUTLOOK_USER')
outlook_password = os.environ.get('OUTLOOK_PASS')
outlook_server = os.environ.get('OUTLOOK_SERVER')
outlook_email = os.environ.get('OUTLOOK_EMAIL')

# Using the necessary credential and configuration to connect to
# the exchange server
credentials = Credentials(username=outlook_user, password=outlook_password)
config = Configuration(server=outlook_server,
                       credentials=credentials)
account = Account(primary_smtp_address=outlook_email,
                  config=config, autodiscover=False,
                  access_type=DELEGATE)

# Getting the excel worsheet for fetching the data
wb = load_workbook(filename="eRACTS Complaint.xlsx")
ws = wb["mail"]

mail_body = HTMLBody(
    """
    <html>
        <body>
            <h3>
                Pl find the current list of eRACTS complaint which have not
                yet been resolved, pl go through each case and provide current
                status of complaint and target date of rectification:
            </h3>
            <table>
                <tr>
                    <th><%= ws['A1'].value %></th>
                    <th><%= ws['B1'].value %></th>
                    <th><%= ws['C1'].value %></th>
                </tr>
                <tr>
                    <td><%= ws['A2'].value %></td>
                    <td><%= ws['B2'].value %></td>
                    <td><%= ws['C2'].value %></td>
                </tr>
        </body>
    </html>
    """
)

msg = Message(
    account=account,
    subject="eRACTS complaint status - 190620 - Sambalpur DO",
    body = mail_body,
    to_recipients=['barnwalp@indianoil.in']
)
msg.send_and_save()
