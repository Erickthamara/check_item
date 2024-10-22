from twilio.rest import Client
import os
from dotenv import load_dotenv
import requests
import vonage

load_dotenv()

def sendSms():
    client = vonage.Client(key="f724673a", secret=os.getenv('V_SECRET'))
    sms = vonage.Sms(client)
    responseData = sms.send_message(
    {
        "from": "Check Items",
        "to": os.getenv('RECEIVER_PHONE'),
        "text": f"ITEM BACK IN STOCK. Purchase it by clicking {os.getenv('TARGET_URL')} ",
    }
    )


if __name__=="__main__":
    sendSms()



