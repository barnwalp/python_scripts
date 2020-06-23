import os
from openpyxl import load_workbook
from exchangelib import Account, Message, Credentials, HTMLBody
from exchangelib import Configuration, DELEGATE

# Getting the sensitive information from environment variables
outlook_user = os.environ.get('OUTLOOK_USER')
outlook_password = os.environ.get('OUTLOOK_PASS')
outlook_server = os.environ.get('OUTLOOK_SERVER')
outlook_email = os.environ.get('OUTLOOK_EMAIL')

# Using necessary credential and config to connect exchange server
credentials = Credentials(username=outlook_user, password=outlook_password)
config = Configuration(server=outlook_server,
                       credentials=credentials)
account = Account(primary_smtp_address=outlook_email,
                  config=config, autodiscover=False,
                  access_type=DELEGATE)

wb = load_workbook(filename="eRACTS Complaint.xlsx")
ws = wb["mail"]

# contains content in HTML format
html = """
<html><body><h3>Pl find the current list of eRACTS complaint which have not yet been resolved, pl go through each case and provide current status of complaint and target date of rectification:</h3>
"""

for whole_row in ws.iter_rows(min_row=1, max_row=1):
    html += "<table border=1><tr>"
    for row in whole_row:
        html += f'<th>{row.value}</th>'
    html += "</tr>"

for whole_row in ws.iter_rows(min_row=2):
    html += "<tr>"
    for row in whole_row:
        if row.value is not None:
            html += f'<td>{row.value}</td>'
        else:
            html += f'<td>{" "}</td>'
    html += "</tr>"

html += """
</table>
<p>
<br>
With Regards<br>
Pankaj Barnwal<br>
</p>
</body>
</html>
"""
# print(html)

msg = Message(
    account=account,
    subject="eRACTS complaint status - 230620 - Sambalpur DO",
    body=HTMLBody(html),
    to_recipients=['barnwalp@indianoil.in']
)

msg.send_and_save()

"""
with open("Simple.html", "w", encoding="utf-8") as filehtml:
    filehtml.write(html)

os.system("Simple.html")
"""
