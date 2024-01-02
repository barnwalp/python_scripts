import os;
import logging;
import pretty_errors;
from dotenv import load_dotenv
from exchangelib import Account, Message, Credentials, Configuration, DELEGATE, FaultTolerance
from exchangelib.util import PrettyXmlHandler;


def send_mail(content):
    # Load environment variables from the .env file
    load_dotenv()

    # Access environment variables
    outlook_user = os.getenv('OUTLOOK_USER')
    outlook_password = os.getenv('OUTLOOK_PASS')
    outlook_server = os.getenv('OUTLOOK_SERVER')
    outlook_email = os.getenv('OUTLOOK_EMAIL')

    print(f"outlook data: {outlook_user, outlook_password, outlook_server, outlook_email}")
    print("ioc\\00504802");

    logging.basicConfig(level=logging.DEBUG, handlers=[PrettyXmlHandler()])

    credentials = Credentials(
        username="ioc\\00504802",
        password="Umami@01"
        )

    config = Configuration(
        # server="mail.indianoil.in/EWS/Exchange.asmx",
        server="mail.indianoil.in",
        # retry_policy=FaultTolerance(max_wait=3600),
        credentials=credentials,
        )

    account = Account(
        primary_smtp_address="barnwalp@indianoil.in",
        config=config,
        autodiscover=False,
        access_type=DELEGATE
        )

    msg = Message(
        account=account,
        subject="Test Mail",
        # body=HTMLBody(content),
        body=content,
        to_recipients=["barnwalp@indianoil.in"],
        cc_recipients=["barnwalp@indianoil.in"]
        )
    msg.send_and_save()

if __name__ == "__main__":
    content = 'This is a test mail'
    send_mail(content);
