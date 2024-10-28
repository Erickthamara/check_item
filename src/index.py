from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
# from utils.sendemail import send_email
# from utils.sendsms import sendSms
import psycopg2
import datetime


# Load environment variables from .env file
load_dotenv()


# Access the variables
# url = os.getenv("TARGET_URL")
# url='https://www.amazon.com/PlayStation%C2%AE5-console-slim-PlayStation-5/dp/B0CL61F39H/ref=sr_1_2?crid=4GO4GVIHXGNI&dib=eyJ2IjoiMSJ9.aROW79MsRByTUgxUhXuZ77gJZIwBrECSdQvgP5OEfQkN_OfMh7PCJr1TbT040s2v.-XZaszxfRsMoXbBOmfM-gLvnBAPPg1Cd8xTCcYIW3jA&dib_tag=se&keywords=sony%2Bplay%2Bstation%2B5%2Bamazon%27s%2Bchoice&qid=1729619250&rnid=2941120011&s=videogames&sprefix=sonyplay%2Bstation%2B5%2Bamazon%27s%2Bchoice%2Caps%2C316&sr=1-2&th=1'
url="https://www.cdkeys.com/playstation-network-psn/1-year-playstation-plus-membership-ps3-ps4-ps-vita-digital-code"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response=requests.get(url,headers=headers)
print(response.text)
soup = BeautifulSoup(response.text, "lxml")
# print(soup)

# Target the specific class
# target_text=soup.find(class_="product-usps-text").text
target_text=''

#Insert record to database
# conn = psycopg2.connect(database=os.getenv("DATABASE"),
#                         user = os.getenv("USER"), 
#                         password = os.getenv("PASSWORD"),
#                         host =os.getenv("HOST"), 
#                         port = os.getenv("PORT"))

# cursor=conn.cursor()

if target_text =="Currently Out Of Stock":
    date_time=datetime.datetime.now()
    # #INSERT THE FAILED TRANSACTION
    # try:
    #     cursor.execute('INSERT INTO check_item.all_transactions ("Status","Date") VALUES (%s,%s)',('UNAVAILABLE',date_time))
    #     conn.commit()
    # except Exception as e:
    #     # print(f"Exception:{e}")
    #     pass

else:
    date_time=datetime.datetime.now()
    # #INSERT THE FAILED TRANSACTION
    # try:
    #     cursor.execute('INSERT INTO check_item.all_transactions ("Status","Date") VALUES (%s,%s)',('AVAILABLE',date_time))
    #     conn.commit()
    # except Exception as e:
    #     print(f"Exception:{e}")

    #SEND EMAIL
    # receiver_emails=os.getenv("RECEIVER_EMAIL")
    # send_email("Item back in stock",f"The item is back in stock.Kindly checkout {url}",receiver_emails)

    # #SEND SMS
    # sendSms()
    


