from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
from sendemail import send_email

# Load environment variables from .env file
load_dotenv()


# Access the variables
url = os.getenv("TARGET_URL")
response=requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# Target the specidic class
target_text=soup.find(class_="product-usps-text").text


if target_text =="Currently Out Of Stock":
    pass
    # print("Not in stock")
else:
    receiver_emails=os.getenv("RECEIVER_EMAIL")
    send_email("Item back in stock",f"The item is back in stock.Kindly checkout {url}",receiver_emails)
    # print('In stock')


