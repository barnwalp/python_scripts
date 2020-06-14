from exchangelib import Credentials, Account
from exchangelib import DELEGATE, Configuration

credentials = Credentials(username='ioc\\00504802', password='*********')
config = Configuration(server='mail.indianoil.in',
                       credentials=credentials)
account = Account(primary_smtp_address='barnwalp@indianoil.in',
                  config=config, autodiscover=False,
                  access_type=DELEGATE)

for item in account.inbox.all().order_by('-datetime_received')[:10]:
    print(item.subject, item.sender, item.datetime_received)
