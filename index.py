from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
from sendemail import send_email
import psycopg2
import datetime



# Load environment variables from .env file
load_dotenv()


# Access the variables
url = os.getenv("TARGET_URL")
response=requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# Target the specidic class
target_text=soup.find(class_="product-usps-text").text

#Insert record to database
conn = psycopg2.connect(database=os.getenv("DATABASE"),
                        user = os.getenv("USER"), 
                        password = os.getenv("PASSWORD"),
                        host =os.getenv("HOST"), 
                        port = os.getenv("PORT"))

cursor=conn.cursor()

if target_text =="Currently Out Of Stock":
    date_time=datetime.datetime.now()
    #INSERT THE FAILED TRANSACTION
    try:
        cursor.execute('INSERT INTO check_item.all_transactions ("Status","Date") VALUES (%s,%s)',('UNAVAILABLE',date_time))
        conn.commit()
    except Exception as e:
        # print(f"Exception:{e}")
        pass

else:

    date_time=datetime.datetime.now()
    #INSERT THE FAILED TRANSACTION
    try:
        cursor.execute('INSERT INTO check_item.all_transactions ("Status","Date") VALUES (%s,%s)',('AVAILABLE',date_time))
        conn.commit()
    except Exception as e:
        print(f"Exception:{e}")

    #SEND EMAIL
    receiver_emails=os.getenv("RECEIVER_EMAIL")
    send_email("Item back in stock",f"The item is back in stock.Kindly checkout {url}",receiver_emails)
    # print('In stock')


