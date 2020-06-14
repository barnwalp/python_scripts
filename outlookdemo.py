from exchangelib import Credentials, Account
from exchangelib import DELEGATE, Configuration
import os

# getting the sensitive information from enviornment variables
# stored in the .bash_profile
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

for item in account.inbox.all().order_by('-datetime_received')[:10]:
    print(item.subject, item.sender, item.datetime_received)
